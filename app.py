import json
from os import system
from validators import ProjectInputValidator
from rich.console import Console
from rich.table import Table
from storage import save_projects, load_projects, get_next_id
from domain import (
    add_project,
    search_by_deadline,
    search_by_id,
    search_by_priority,
    search_by_title,
    edit_project,
    delete_project,
)

# ---------Creating Objects ---------
console = Console()

projects = load_projects()
state = {
    "projects": projects,
    "next_project_id": get_next_id(projects),
    "RUNNING": True
    }

def list_projects(projects=None):
    table = Table(title="Project Management Software")
    if projects is None:
        projects = state["projects"]

    if not projects:
        print("No projects found.")
        return
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Details", justify="right", style="green")
    table.add_column("Deadline", justify="right", style="green")
    table.add_column("Priority", justify='right', style="red")
    for p in projects:
        priority = (p.get("priority") or "").lower()
        if priority == "low":
            color = "green"
        elif priority == "medium":
            color = "yellow"
        else:
            color = "red"
        table.add_row(str(p.get("id")), p.get("title", ""), p.get("details", ""), p.get("deadline", ""), f"[bold {color}]{p.get('priority', '')}[/]")
    console.print(table)
def search_ui():
    search_choices = ['Search by ID', "Search by title", 'Search by deadline', 'Search by priority']

    for i, choice in enumerate(search_choices, start=1):
        print(f'{i}, {choice}')
    search_map = {
                "1": search_by_id,
                "2": search_by_title,
                "3": search_by_deadline,
                "4": search_by_priority
                }
    user_input_choice = input(">>>")
    if user_input_choice in search_map:
        query = input('Enter search keyword: \n >>>')
        results = search_map[user_input_choice](state['projects'], query)
        list_projects(results)

    else:
        print("Please choose one of the available options")
def get_input():
    menu_number = ['1', '2', '3', '4', '5', '6']
    choices = ['Add Project', 'List Projects', 'Edit Projects', 'Remove Projects','Search','Quit']
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")
    user_choice = input(">>> ")

    if user_choice not in menu_number:
         print("Please choose one of the available options")

    elif user_choice == "1":
        pv = ProjectInputValidator()
        title = pv.validate_title()
        details = input("Project details: ")
        deadline = pv.validate_deadline()
        priority = pv.validate_priority()

        new_project = add_project(state["next_project_id"], title, details, deadline, priority)

        state["projects"].append(new_project)
        state["next_project_id"] += 1
        save_projects(state["projects"])
        print("✅ Project added successfully!")
    
    elif user_choice == "2":
        list_projects()

    elif user_choice == '3':
        edit_project_id = int(input("Enter the ID number of the project you would like to edit:\n>>> "))

        editable = ['title', 'details', 'deadline', 'priority']
        updates = {}
        for field in editable:
            new_value = input(f"New {field} (leave blank to keep current): ")
            updates[field] = new_value if new_value.strip() != '' else None
            
        state['projects'], ok = edit_project(state['projects'], edit_project_id, updates)

        if ok:
            save_projects(state['projects'])
            print("Project was edited successfully!")
        else:
            print("Project not found.")
    elif user_choice == '4':
         remove_project_id = int(input("Enter the ID number of the project you would like to remove:\n>>> "))
         state['projects'], ok = delete_project(state['projects'], remove_project_id)
         if ok:
            save_projects(state['projects'])
            print("Project was deleted successfully!")
         else:
            print("Project not found.")

        
    
    elif user_choice == "5":
        search_ui()

while state['RUNNING']:
    print("Welcome to the Project Management Software")
    print("Please choose one of the following options: ")
    state['RUNNING'] = get_input()
from datetime import datetime  

def add_project(next_id, title, details, deadline, priority):
    return {
        "id": next_id,
        "title": title,
        "details": details,
        "deadline": deadline,
        "priority": priority,
    }


def edit_project(projects, id, updates):
        for p in projects:                           # iterates over existing projects
            if p.get('id') == id:                    # compare id from user to id from db
                for field, value in updates.items(): # 
                    if value is not None and str(value).strip() != '':
                        p[field] = value
                
                return projects, True
        return projects, False
# ---- Search functions ---- To phase out later ---- #
def search_by_title(projects, keyword):
    results = []
    for p in projects:
        if keyword.lower() in p.get('title', '').lower():
            results.append(p)
    return results 


def search_by_id(projects, keyword):
    results = []
    for p in projects:
        if p.get('id') == int(keyword):
            results.append(p)
    return results


def search_by_priority(projects, keyword):
    results = []
    for p in projects:
        if keyword.lower() in p.get('priority', '').lower():
            results.append(p)
    return results


def search_by_deadline(projects, keyword):
    results = []
    for p in projects:
        if keyword in p.get('deadline', ''):
            results.append(p)
    
    return results

# ---- End of Search functions ---- # To phase out later ---- #

def delete_project(projects, id):
    id_found = False
    for p in projects:
        if p.get('id') == id:
            id_found = True
            projects.remove(p)
            return projects, True
    return projects, False

# ---- New combined search function ---- #
def search_projects(projects, *, query=None, priority=None, due_before=None):
        results = projects
        filtered = []
        if query is not None and str(query).strip() != '':
            for p in results:
                title = p.get('title', '').lower()
                details = p.get('details', '').lower()
                if query.lower() in title or query.lower() in details:
                    filtered.append(p)
            results = filtered
        filtered = []
        if priority is not None and str(priority).strip() != '':
            for p in results:
                if priority.lower() == p.get('priority', '').lower():
                    filtered.append(p)
            results = filtered
        filtered = []
        if due_before is not None and str(due_before).strip() != '':
            try:
                due_before_date = datetime.strptime(due_before, "%d/%m/%Y")
                for p in results:
                    deadline_str = p.get('deadline', '')
                    try:
                        deadline_date = datetime.strptime(deadline_str, "%d/%m/%Y")
                        if deadline_date <= due_before_date:
                            filtered.append(p)
                    except ValueError:
                        continue  # Skip projects with invalid date format
                results = filtered
            except ValueError:
                pass  # If due_before is invalid, skip filtering
        return results
import json


# ----- Loop over existing ID's + increment -------
def get_next_id(projects):
    new_id_list = []
    for p in projects:
        new_id_list.append(p.get('id'))
    if not new_id_list:
        return 1
    else:
        return max(new_id_list) + 1


# ------- Save project to JSON ------
def save_projects(projects):
    with open('database.json', 'w') as write_file:
        json.dump(projects, write_file, indent=2)

# ------- Load data from JSON -------
def load_projects():
    try:
        with open('database.json', 'r') as read_file:
            d = json.load(read_file)
            return d
    except FileNotFoundError:
        print("No Projects Available")
        return []
    except json.decoder.JSONDecodeError:
        print('Database empty or corrupted, starting fresh.')
        return []
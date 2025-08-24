
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

def delete_project(projects, id):
    id_found = False
    for p in projects:
        if p.get('id') == id:
            id_found = True
            projects.remove(p)
            return projects, True
    return projects, False
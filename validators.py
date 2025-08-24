from datetime import datetime


class ProjectInputValidator:
    def __init__(self):
        self.title = ""
        self.priority = ""
        self.deadline = ""
        
    def validate_title(self):
        while True:
            self.title = input("Project name: ")
            if not self.title.strip():
                print("Project name cannot be empty")
            else:
                return self.title
    

    def validate_priority(self):
        while True:
            self.priority = input("Priority: High/Medium/Low \n>>> ").lower()
            accepted_input = ['high', 'medium', 'low']
            if self.priority in accepted_input:
                return self.priority
            else:
                print("Only allowed priorities are High, Medium and Low.")
    
    def validate_deadline(self):
        while True:
            self.deadline = input("Input deadline in format DD/MM/YY")
            try:
                datetime.strptime(self.deadline, "%d/%m/%Y")
                return self.deadline
            except ValueError:
                print('Please enter deadline in the right format.')

    
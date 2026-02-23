import json
import os

FILE_NAME = "issue.json"


def load_issues():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_issues(issues):
    with open(FILE_NAME, "w") as file:
        json.dump(issues, file, indent=4)
      def create_issue():

    issues = load_issues()

    title = input("Title: ")
    description = input("Description: ")
    priority = input("Priority (low/medium/high): ")

    issue = {
        "id": len(issues) + 1,
        "title": title,
        "description": description,
        "priority": priority,
        "status": "open"
    }

    issues.append(issue)

    save_issues(issues)

    print("Issue created!")
def list_issues():

    issues = load_issues()

    if not issues:
        print("No issues found")
        return

    for issue in issues:

        print("\nID:", issue["id"])
        print("Title:", issue["title"])
        print("Priority:", issue["priority"])
        print("Status:", issue["status"])
      while True:

    print("\nISSUE TRACKER")
    print("1 - Create Issue")
    print("2 - List Issues")
    print("3 - Exit")

    choice = input("Choose option: ")

    if choice == "1":
        create_issue()

    elif choice == "2":
        list_issues()

    elif choice == "3":
        break

    else:
        print("Invalid option")
        print(load_issues())
        while True:

    print("\nISSUE TRACKER")
    print("1 - Create Issue")
    print("2 - List Issues")
    print("3 - Exit")

    choice = input("Choose option: ")

    if choice == "1":
        create_issue()

    elif choice == "2":
        list_issues()

    elif choice == "3":
        break

    else:
        print("Invalid option")
        
def close_issue():

    issues = load_issues()

    issue_id = int(input("Enter issue ID to close: "))

    for issue in issues:

        if issue["id"] == issue_id:

            issue["status"] = "closed"

            save_issues(issues)

            print("Issue closed successfully!")

            return

    print("Issue not found.")
while True:

    print("\nISSUE TRACKER")
    print("1 - Create Issue")
    print("2 - List Issues")
    print("3 - Close Issue")
    print("4 - Exit")

    choice = input("Choose option: ")

    if choice == "1":
        create_issue()

    elif choice == "2":
        list_issues()

    elif choice == "3":
        close_issue()

    elif choice == "4":
        break

    else:
        print("Invalid option")

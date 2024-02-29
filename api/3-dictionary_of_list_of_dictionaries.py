import requests
import sys
import json

def get_all_employee_tasks():
    base_url = "https://jsonplaceholder.typicode.com"
    all_tasks = {}

    try:
        for employee_id in range(1, 11):  # Assuming employee IDs range from 1 to 10
            user_url = f"{base_url}/users/{employee_id}"
            todos_url = f"{base_url}/users/{employee_id}/todos"

            user_response = requests.get(user_url)
            todos_response = requests.get(todos_url)

            user_data = user_response.json()
            todos_data = todos_response.json()

            tasks = []
            for task in todos_data:
                tasks.append({
                    "username": user_data["name"],
                    "task": task["title"],
                    "completed": task["completed"]
                })

            all_tasks[employee_id] = tasks

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    return all_tasks

if name == "__main__":
    all_employee_tasks = get_all_employee_tasks()

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(all_employee_tasks, outfile, indent=4)
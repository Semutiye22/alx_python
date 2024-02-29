import requests
import json
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data["name"]
        tasks = [{"task": task["title"], "completed": task["completed"], "username": employee_name} for task in todos_data]

        print(f"Employee {employee_name} tasks:")
        print(tasks)

        export_to_json(employee_id, tasks)

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def export_to_json(employee_id, tasks):
    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump({employee_id: tasks}, file, indent=4)

    print(f"Data exported to {filename}")

if name == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
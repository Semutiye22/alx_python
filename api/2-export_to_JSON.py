import json
import requests
import sys

def export_to_json(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    username = employee_data['username']

    # Get employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todo_data = response.json()

    # Format data as required
    formatted_data = {str(employee_id): []}
    for task in todo_data:
        formatted_task = {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        formatted_data[str(employee_id)].append(formatted_task)

    # Write data to JSON file
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump(formatted_data, file)

if name == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
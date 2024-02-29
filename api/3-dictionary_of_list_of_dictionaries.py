'''importing libraries'''
"""importing libraries"""
# iimporting libraries
import json
import requests
import sys

def get_all_employees_todo_progress():
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"

    try:
        users_response = requests.get(users_url)
        users_data = users_response.json()

        all_employees_tasks = {}

        for user in users_data:
            employee_id = user["id"]
            todos_url = f"{base_url}/users/{employee_id}/todos"
            todos_response = requests.get(todos_url)
            todos_data = todos_response.json()

            tasks = [
                {
                    "username": user["username"],
                    "task": task["title"],
                    "completed": task["completed"]
                }
                for task in todos_data
            ]

            all_employees_tasks[employee_id] = tasks

        # Write the dictionary to a JSON file
        filename = "todo_all_employees.json"
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(all_employees_tasks, json_file, ensure_ascii=False, indent=4)

        print(f"Data exported to {filename}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_all_employees_todo_progress()
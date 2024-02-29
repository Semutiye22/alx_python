'''importing libraries'''
"""importing libraries"""
# iimporting libraries

import json
import requests
import sys


# defining our first function
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
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task["completed"])

        # Create a dictionary to store the tasks
        tasks_dict = {
            "USER_ID": [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": user_data["username"]
                }
                for task in todos_data if task["completed"]
            ]
        }

        # Write the dictionary to a JSON file
        filename = f"{employee_id}.json"
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(tasks_dict, json_file, ensure_ascii=False, indent=4)

        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}).")
        print(f"Data exported to {filename}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
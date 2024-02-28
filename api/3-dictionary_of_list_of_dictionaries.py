import json
import requests

def fetch_tasks():
    base_url = "https://jsonplaceholder.typicode.com"
    users_response = requests.get(f"{base_url}/users")
    if users_response.status_code != 200:
        print("Failed to fetch users. Please try again later.")
        return None

    users_data = users_response.json()
    tasks_by_user = {}

    for user in users_data:
        user_id = user["id"]
        username = user["username"]
        tasks_response = requests.get(f"{base_url}/todos?userId={user_id}")
        if tasks_response.status_code == 200:
            tasks_data = tasks_response.json()
            tasks = [{"task": task["title"], "completed": task["completed"], "username": username} for task in tasks_data]
            tasks_by_user[user_id] = tasks
        else:
            print(f"Failed to fetch tasks for user {user_id} ({username})")

    return tasks_by_user

def export_to_json(data):
    try:
        with open("todo_all_employees.json", "w") as f:
            json.dump(data, f, indent=4)
        print("Data exported to todo_all_employees.json successfully.")
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")

if name == "__main__":
    tasks = fetch_tasks()
    if tasks:
        export_to_json(tasks)
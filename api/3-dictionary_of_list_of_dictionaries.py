import json
import requests
import sys

if name == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    tasks_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    user_response = requests.get(f"{base_url}/users/{employee_id}")

    if tasks_response.status_code != 200 or user_response.status_code != 200:
        print("Failed to fetch data. Please try again later.")
        sys.exit(1)

    tasks_data = tasks_response.json()
    user_data = user_response.json()

    user_id = user_data["id"]
    username = user_data["username"]

    tasks = [{"task": task["title"], "completed": task["completed"], "username": username} for task in tasks_data]

    try:
        with open(f"{user_id}.json", "w") as f:
            json.dump({user_id: tasks}, f)
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")
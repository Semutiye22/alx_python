import csv
import sys

# Sample data representing tasks assigned to users
tasks_data = {
    1: [
        {"user_id": 1, "username": "Leanne Graham", "completed": False, "title": "delectus aut autem"},
        {"user_id": 1, "username": "Leanne Graham", "completed": False, "title": "quis ut nam facilis et officia qui"},
        {"user_id": 1, "username": "Leanne Graham", "completed": True, "title": "fugiat veniam minus"},
        {"user_id": 1, "username": "Leanne Graham", "completed": False, "title": "et porro tempora"},
        {"user_id": 1, "username": "Leanne Graham", "completed": False, "title": "laboriosam mollitia et enim quasi adipisci quia provident illum"},
        {"user_id": 1, "username": "Leanne Graham", "completed": False, "title": "qui ullam ratione quibusdam voluptatem quia omnis"},
        {"user_id": 1, "username": "Leanne Graham", "completed": True, "title": "illo expedita consequatur quia in"},
        {"user_id": 1, "username": "Leanne Graham", "completed": False, "title": "quo adipisci enim quam ut ab"},
        {"user_id": 1, "username": "Leanne Graham", "completed": False, "title": "molestiae perspiciatis ipsa"},
        {"user_id": 1, "username": "Leanne Graham", "completed": True, "title": "illo est ratione doloremque quia maiores aut"}
    ],
    2: [
        {"user_id": 2, "username": "Ervin Howell", "completed": False, "title": "delectus aut autem"},
        {"user_id": 2, "username": "Ervin Howell", "completed": True, "title": "quis ut nam facilis et officia qui"},
        {"user_id": 2, "username": "Ervin Howell", "completed": False, "title": "fugiat veniam minus"},
        {"user_id": 2, "username": "Ervin Howell", "completed": True, "title": "et porro tempora"},
        {"user_id": 2, "username": "Ervin Howell", "completed": False, "title": "laboriosam mollitia et enim quasi adipisci quia provident illum"},
        {"user_id": 2, "username": "Ervin Howell", "completed": True, "title": "qui ullam ratione quibusdam voluptatem quia omnis"},
        {"user_id": 2, "username": "Ervin Howell", "completed": True, "title": "illo expedita consequatur quia in"},
        {"user_id": 2, "username": "Ervin Howell", "completed": False, "title": "quo adipisci enim quam ut ab"},
        {"user_id": 2, "username": "Ervin Howell", "completed": False, "title": "molestiae perspiciatis ipsa"},
        {"user_id": 2, "username": "Ervin Howell", "completed": True, "title": "illo est ratione doloremque quia maiores aut"}
    ]
}

def export_to_csv(user_id):
    # Define file name based on user ID
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks_data.get(user_id, []):
            writer.writerow({
                'USER_ID': task['user_id'],
                'USERNAME': task['username'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })

if name == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py USER_ID")
        sys.exit(1)
    
    user_id = int(sys.argv[1])
    export_to_csv(user_id)
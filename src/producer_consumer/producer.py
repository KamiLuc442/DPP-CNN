import sys
import os

FILENAME = "tasks.txt"


try:
    new_tasks_count = int(sys.argv[1])
except ValueError:
    sys.exit(1)

if not os.path.exists(FILENAME):
    open(FILENAME, "w").close()

with open(FILENAME, "r", encoding="utf-8") as file:
    lines = file.readlines()

current_count = len(lines)

with open(FILENAME, "a", encoding="utf-8") as file:
    for i in range(1, new_tasks_count + 1):
        task_id = current_count + i
        task_name = f"task_{task_id}"
        status = "pending"
        file.write(f"{task_id},{task_name},{status}\n")
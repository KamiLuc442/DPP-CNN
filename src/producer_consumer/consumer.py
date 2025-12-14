import time
import os
import tempfile

FILENAME = "tasks.txt"
CHECK_INTERVAL = 5
TASK_DURATION = 30

def consume_task():
    if not os.path.exists(FILENAME):
        return

    task_to_process = None

    with open(FILENAME, "r", encoding="utf-8") as src, \
         tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:

        for line in src:
            task_id, name, status = line.strip().split(",")

            if status == "pending" and task_to_process is None:
                task_to_process = (task_id, name)
                tmp.write(f"{task_id},{name},in_progress\n")
            else:
                tmp.write(line)

    if task_to_process is None:
        os.remove(tmp.name)
        return

    os.replace(tmp.name, FILENAME)

    task_id, name = task_to_process
    print(f"[{os.getpid()}] Taks started: {task_id}: {name}")

    time.sleep(TASK_DURATION)

    with open(FILENAME, "r", encoding="utf-8") as src, \
         tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:

        for line in src:
            tid, tname, status = line.strip().split(",")

            if tid == task_id and status == "in_progress":
                tmp.write(f"{tid},{tname},done\n")
            else:
                tmp.write(line)

    os.replace(tmp.name, FILENAME)
    print(f"[{os.getpid()}] Task done: {task_id}")

if __name__ == "__main__":
    print(f"Consumer uruchomiony (PID={os.getpid()})")

    while True:
        consume_task()
        time.sleep(CHECK_INTERVAL)

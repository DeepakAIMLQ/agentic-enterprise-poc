FAILED_TASKS = []

def add_failed_task(task, reason):
    FAILED_TASKS.append({
        "task": task,
        "reason": reason
    })
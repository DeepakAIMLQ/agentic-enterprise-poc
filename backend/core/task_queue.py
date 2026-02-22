TASK_QUEUE = []

def add_task(task):
    TASK_QUEUE.append(task)

def get_next_task(agent_name):
    for task in TASK_QUEUE:
        if task.status == "PENDING" and (task.assigned_agent in [None, agent_name]):
            task.status = "IN_PROGRESS"
            task.assigned_agent = agent_name
            return task
    return None

def complete_task(task_id):
    for task in TASK_QUEUE:
        if task.id == task_id:
            task.status = "DONE"
            return task
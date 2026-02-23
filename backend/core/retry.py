import time

def retry_with_backoff(fn, task):
    delay = 2 ** task.retries  # 1s, 2s, 4s

    try:
        return fn(task)
    except Exception as e:
        task.retries += 1

        if task.retries >= task.max_retries:
            raise e

        time.sleep(delay)
        return retry_with_backoff(fn, task)
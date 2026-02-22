PROJECT_MEMORY = {}

def write(key, value):
    PROJECT_MEMORY[key] = value

def read(key):
    return PROJECT_MEMORY.get(key)

def read_all():
    return PROJECT_MEMORY
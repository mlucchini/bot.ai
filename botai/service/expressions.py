from botai.db.in_memory import InMemoryDb


def get():
    return InMemoryDb.instance().expressions

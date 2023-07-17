import random
def do_or_empty(f, *args, **kwargs):
    return '' if random.choice([True, False]) else f(*args, **kwargs)
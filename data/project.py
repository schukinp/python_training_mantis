from model.project import Project
import random
import string

def random_name():
    size = 5
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def random_description():
    size = 5
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


testdata = [Project(name=random_name(), description=random_description())]




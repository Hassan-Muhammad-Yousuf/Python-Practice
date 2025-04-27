import random

class smallNumberException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        print("Error Class")

try:
    r = random.random()
    print(r)
    if r < 0.1:
        raise smallNumberException(" Number is Small")
    else:
        print("program work's")

except smallNumberException as e:
    print("Error: ", e)
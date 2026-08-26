from typing import List

def read_integers() -> List[int]:
    ints = input()
    ints_list = ints.split(",")

    return [int(i) for i in ints_list]

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

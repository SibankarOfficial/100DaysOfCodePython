import random 
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for i in a_list:
        new_item = i * 2
        new_item += random.randint(1,3)
        new_item = maths.add(new_item, i)
    b_list.append(new_item)
    print(b_list)

mutate([1,4,7,9])
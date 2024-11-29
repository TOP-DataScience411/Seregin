import random

def tree_generator():
    num = random.randrange(4) 
    tree = []
    zero = []
    at_list_one_not_empty = False
    for char in range(num):

        if random.choice([True, False]):
            if random.choice([True, False]):
                tree.append('leaf') 
            else: tree.append(zero)
        else:
            tree.append(tree_generator())

    for i in range(len(tree)):
        at_list_one_not_empty = at_list_one_not_empty or bool(tree[i-1])
        
    if not at_list_one_not_empty:
        tree.append('leaf')

    return tree


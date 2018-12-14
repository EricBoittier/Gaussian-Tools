from pymol import cmd, stored
import os
import os
def add_states():
    '''
    DESCRIPTION

    Brief description what this function does goes here
    '''
    #
    # Your code goes here
    #
    todo = os.listdir("/Users/ericboittier/Desktop/out")
    count = 0
    values = {}
    for x in todo:
        if x.__contains__(".xyz") and x.__contains__("_extract_"):
            print(x.split("_")[3].split(".")[0])
            values[int(x.split("_")[3].split(".")[0])] = x


    todo = values.keys()
    todo = list(todo)
    todo.sort()

    print(todo)

    for y in todo:
        print(y)
        cmd.create("every_state.xyz", values[y][:-4], 0, count)
        count += 1

    cmd.save("every_state.xyz")



cmd.extend("add_states", add_states)
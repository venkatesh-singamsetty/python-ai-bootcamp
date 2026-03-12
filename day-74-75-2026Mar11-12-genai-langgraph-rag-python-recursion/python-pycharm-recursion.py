# Pycharm
# import sys
# print(sys.setrecursionlimit(150)

import sys
sys.setrecursionlimit(150)
print(sys.getrecursionlimit())

i = 0

def wish():
    global  i
    i += 1
    print('hello', i)
    wish()
wish()

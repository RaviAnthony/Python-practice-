import sys

def fact():
    """ factorial"""
    print sys.path
    factorial=0
    for i in range(30):
        factorial +=i
        print factorial,


if __name__ == '__main__':
    fact()
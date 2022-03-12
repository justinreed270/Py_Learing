# How to change a global variable in a fn.

_x = "hi"

def local_x():
    _x="This var is set to this fn only."
    print(_x)

def set_x():
    global _x
    _x ="Now this var is set to global.\nYou must bring the x variable " \
       "into this function with:\n'global <var>'"
    print(_x)
    x = "Here ye!"

def get_x():
    print(_x)

def separator():
    print("++++++++")

def main():
    local_x()
    separator()
    set_x()
    separator()
    get_x()
    separator()
    local_x()
    separator()
    get_x()

if __name__ == '__main__':
    main()

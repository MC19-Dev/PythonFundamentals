from mypackage.my_first_module import my_func as my_module_func, my_var as my_module_var
from mypackage.my_second_module import *

def main():
    print(my_module_var)
    my_module_func()

if __name__ == '__main__':
    main()
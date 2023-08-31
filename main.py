# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


def f1(func):
    def wrapper(*args, **kwargs):
        print("Hello")
        val=func(*args, **kwargs)
        print("Stop")
        return val
    return wrapper

@f1
def f(a,b=9):
    return a+b

print(f(5,6))
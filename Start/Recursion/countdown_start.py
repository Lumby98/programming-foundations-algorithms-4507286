# Example file for Programming Foundations: Algorithms by Joe Marini
# use recursion to implement a countdown counter


def countdown(x):
    if x == 0:
        print("done")
    else:
        print(x, "...")
        countdown(x-1)
        print("hey")

countdown(5)

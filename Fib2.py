import io
#print fibbonacci series for n numbers

def main():
    n = input("enter the number")
    print(fib(9))


def fib(n):
    if n <= 0:
        print("incorrect number")
        return 0
    elif n==0:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1),fib(n-2)




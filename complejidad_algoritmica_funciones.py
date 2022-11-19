import time
import math as ma


def lineal(n):
    return 1

def logaritmo(n):
    return ma.log10(n)

def o(n):
    return n

def nlog(n):
    return n*ma.log10(n)

def square(n):
    return n**2

def exp(n):
    return 2**n


def run():
    comienzo = time.time()
    print(exp(14284))
    final = time.time()
    print(final - comienzo)


if __name__ == '__main__':
    run()
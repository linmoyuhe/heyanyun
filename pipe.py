#!/usr/bin/env python3
from multiprocessing import Process, Pipe

coon1, coon2 = Pipe()

def f1():
    coon1.send('Hello shiyanlou')


def f2():
    data = coon2.recv()
    print(data)


def main():
    Process(target = f1).start()
    Process(target = f2).start()


if __name__ == '__main__':
   main()

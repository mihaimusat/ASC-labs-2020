"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""

import sys
import random
import threading
import time

def usage(argv):
    print("Usage: " + argv[0] + " <number of threads>")

def my_function(nr):
    print("I'm Thread-", threading.current_thread(), "and I received the number", nr)

def main():
    if len(sys.argv) < 2:
        usage(sys.argv)
        exit(0)

    random.seed(time.time())

    num_threads = int(sys.argv[1])
    thread_list = [None] * num_threads

    for i in range(num_threads):
        thread_list[i] = threading.Thread(target=my_function, args=(random.randint(0, 100), ))
        thread_list[i].start()
        #thread_list.append(thread_list[i])

    for i in range(len(thread_list)):
        thread_list[i].join()

if __name__ == "__main__":
    main()

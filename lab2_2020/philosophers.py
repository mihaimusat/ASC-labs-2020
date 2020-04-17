from threading import Thread, Lock
import time
import random
import sys

class Philosopher(Thread):
    def __init__(self, id, left_fork, right_fork):
        Thread.__init__(self)
        self.id = id
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            self.left_fork.acquire(True) #blocking lock

            time.sleep(random.uniform(0, 0.1))
            locked = self.right_fork.acquire(False) #non-blocking lock
            #daca am si left si right blocate -> quit
            if locked:
                break

            self.left_fork.release()

            self.left_fork, self.right_fork = self.right_fork, self.left_fork

        print("Philosopher %d is eating" % self.id)

        self.left_fork.release()
        self.right_fork.release()

def usage(argv):
    print("Usage: " + argv[0] + " <number of philosophers>")

def main():
    if len(sys.argv) < 2:
        usage(sys.argv)
        exit(0)

    forks = []
    nr_philosophers = int(sys.argv[1])
    philosophers = [None] * nr_philosophers

    for i in range(nr_philosophers):
        forks.append(Lock())

    for i in range(nr_philosophers ):
        philosophers[i] = Philosopher(i, forks[i - 1], forks[i])
        philosophers[i].start()

    for i in range(nr_philosophers ):
        philosophers[i].join()

if __name__ == "__main__":
    main()
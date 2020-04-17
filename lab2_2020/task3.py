"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""

from threading import Semaphore, Lock, Thread
import random
import sys
import time

class Coffee:
    """ Base class """
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_name(self):
        """ Returns the coffee name """
        return self.name

    def get_size(self):
        """ Returns the coffee size """
        return self.size

class Espresso(Coffee):
    """ Espresso implementation """
    def __init__(self, size):
        Coffee.__init__(self, "espresso", size)

    def get_message(self):
        """ Output message """
        return "nice {} {}".format(self.get_size(), self.get_name())

class Americano(Coffee):
    """ Americano implementation """
    def __init__(self, size):
        Coffee.__init__(self, "americano", size)

    def get_message(self):
        """ Output message """
        return "strong {} {}".format(self.get_size(), self.get_name())

class Cappuccino(Coffee):
    """ Cappuccino implementation """
    def __init__(self, size):
        Coffee.__init__(self, "cappuccino", size)

    def get_message(self):
        """ Output message """
        return "italian {} {}".format(self.get_size(), self.get_name())

class Distribuitor:
    """Buffer implementation"""
    def __init__(self, b_size):
        self.b_size = b_size
        self.buffer = [None] * b_size
        self.sem_cons = Semaphore(value=0)
        self.sem_prod = Semaphore(value=b_size)
        self.mutex_cons = Lock()
        self.mutex_prod = Lock()
        self.id = 0

    def put(self, value):
        self.sem_prod.acquire()

        self.mutex_prod.acquire()
        self.id = (self.id + 1) % self.b_size
        self.buffer[self.id] = value
        self.mutex_prod.release()

        self.sem_cons.release()

    def get(self):
        self.sem_cons.acquire()
        value = None

        self.mutex_cons.acquire()
        value = self.buffer[self.id]
        self.id = self.id - 1
        if(self.id < 0):
            self.id = self.b_size - 1
        self.mutex_cons.release()

        self.sem_prod.release()

        return value

class CoffeeFactory(Thread):
    "Producer implementation"
    def __init__(self, id, buffer, sizes, types):
        Thread.__init__(self)
        self.id = id
        self.buffer = buffer
        self.sizes = sizes
        self.types = types

    def run(self):
        while(True):
            coffee_type = random.choice(self.types)
            coffee_size = random.choice(self.sizes)

            coffee = coffee_type(coffee_size)

            print("Factory %d produced a %s" % (self.id, coffee.get_message()))

            self.buffer.put(coffee)

class User(Thread):
    """Consumer implementation"""
    def __init__(self, id, buffer):
        Thread.__init__(self)
        self.id = id
        self.buffer = buffer

    def run(self):
        while True:
            coffee = self.buffer.get()
            print("Consumer %d consumed %s" % (self.id, coffee.get_message()))

def usage(argv):
    print("Usage: " + argv[0] + " <buffer size>" + " <number of producers>" + " <number of consumers>")

def main():
    if len(sys.argv) < 4:
        usage(sys.argv)
        exit(0)

    random.seed(time.time())

    sizes = ["small", "medium", "large"]
    types = [Espresso, Americano, Cappuccino]

    capacity = int(sys.argv[1])
    nr_producers = int(sys.argv[2])
    nr_consumers = int(sys.argv[3])

    buffer = Distribuitor(capacity)
    producers = [None] * nr_producers
    consumers = [None] * nr_consumers

    for i in range(nr_producers):
        producers[i] = CoffeeFactory(i, buffer, sizes, types)
        producers[i].start()

    for i in range(nr_consumers):
        consumers[i] = User(i, buffer)
        consumers[i].start()

    for i in range(len(producers) + len(consumers)):
        producers[i].join()
        consumers[i].join()

if __name__ == '__main__':
    main()

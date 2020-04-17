from threading import enumerate, Event, Thread, Condition

class Master(Thread):
    def __init__(self, max_work, element):
        Thread.__init__(self, name = "Master")
        self.max_work = max_work
        self.element = element
    
    def set_worker(self, worker):
        self.worker = worker
    
    def run(self):
        for i in range(self.max_work):
            # generate work
            self.element.acquire()
            self.work = i
            # notify worker
            self.element.notify()
            # get result
            self.element.wait()
            if self.get_work() + 1 != self.worker.get_result():
                print ("oops")
            print ("%d -> %d" % (self.work, self.worker.get_result()))
            self.element.release()
    
    def get_work(self):
        return self.work

class Worker(Thread):
    def __init__(self, terminate, element):
        Thread.__init__(self, name = "Worker")
        self.terminate = terminate
        self.element = element

    def set_master(self, master):
        self.master = master
    
    def run(self):
        while(True):
            # wait work
            self.element.acquire()
            self.element.wait()
            if(terminate.is_set()): break
            # generate result
            self.result = self.master.get_work() + 1
            # notify master

            self.element.notify()

            self.element.release()
    
    def get_result(self):
        return self.result

if __name__ ==  "__main__":
    # create shared objects
    terminate = Event()
    element = Condition()

    # start worker and master
    w = Worker(terminate, element)
    m = Master(10, element)

    w.set_master(m)
    m.set_worker(w)
    w.start()
    m.start()

    # wait for master
    m.join()

    # wait for worker
    terminate.set()
    element.acquire()
    element.notify()
    element.release()
    w.join()

    # print running threads for verification
    print(enumerate())


from concurrent.futures import ThreadPoolExecutor
import random

def thread_function(index, sample, seq):
    if(seq in "".join(sample[index])):
        print("Am gasit secventa in sample-ul %d" % index)

def main():
    list = []
    for i in range(100):
        list.append([])
        for j in range(10000):
            list[i].append(random.choice('ACGT'))

    subset = "ACGTAC"

    with ThreadPoolExecutor(max_workers=30) as executor:
        for i in range(100):
            executor.submit(thread_function, i, list, subset)

if __name__ == '__main__':
    main()
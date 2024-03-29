# from multiprocessing import Pool, cpu_count
# import time

# start = time.perf_counter()

# def factorize_single(number):
#     return [i for i in range(1, number + 1) if number % i == 0]

# def factorize(*numbers):
#     with Pool(cpu_count()) as pool:
#         result = pool.map(factorize_single, numbers)
#         return result

# finish = time.perf_counter()

# print(f"Running time for 'Pool-multiprocessing' is {round(finish-start, 2)} second(s)")

"""-------------------------------------------"""
from threading import Thread
import time

start = time.perf_counter()

def factorize_single(number):
    return [i for i in range(1, number + 1) if number % i == 0]

class FactorizeThread(Thread):
    def __init__(self, number, result_list):
        super().__init__()
        self.number = number
        self.result_list = result_list

    def run(self):
        self.result_list.extend(factorize_single(self.number))

def factorize(*numbers):
    result = []
    threads = []

    for item in numbers:
        result_list = []
        th = FactorizeThread(item, result_list)
        th.start()
        threads.append((th, result_list))

    for thread, result_list in threads:
        thread.join()
        result.append(result_list)

    return result

finish = time.perf_counter()


print(f"Running time for 'Threads' is {round(finish-start, 2)} second(s)")


a, b, c, d = factorize(128, 255, 99999, 10651060)

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
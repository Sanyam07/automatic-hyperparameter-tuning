# coding=utf8
# author: thomas young
# date: 2017.3.19

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


def return_future_result(message):
    # use time.sleep to simulate the io-busy task
    # time.sleep(2)

    # simulate cpu-busy task
    res = 0.0
    for i in range(10000000):
        res += i

    return message

if __name__ == "__main__":

    # in the init stage, assure n_worker > 1.5x n_executor

    # pool = ProcessPoolExecutor(max_workers=4)
    pool = ThreadPoolExecutor(max_workers=4)
    futures = []
    start_time = time.time()

    # cold start
    for i in range(8):
        futures.append(pool.submit(return_future_result, ("world: %d" % i, 22)))

    count = 8
    while len(futures) > 0 and count < 50:
        if len(futures) <= 6:
            futures.append(pool.submit(return_future_result, ("world: %d" % count, 22)))
            count += 1

        for f in futures:
            if f.done():
                print f.result()
                futures.remove(f)
                # update model and compute the next hyper-parameter.
                # add new evaluation into list futures.

        time.sleep(1e-1)

    # compute the cost of time.
    print "it costs: %f" % (time.time() - start_time)

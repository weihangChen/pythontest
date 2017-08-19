import unittest
import multiprocessing
class PowerOf2Test(unittest.TestCase):
    def worker():
        print("Worker")
        return

    def test_multi(self):
        jobs = []
        for i in range(5):
            p = multiprocessing.Process(target=worker)
            jobs.append(p)
            p.start()




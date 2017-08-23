import unittest
import time
from multiprocessing.pool import Pool

#method needs to be located at top level, else it is not pickable
#https://stackoverflow.com/questions/8804830/python-multiprocessing-pickling-error
def foo(word, number):
    print (word * number)
    #r[(word,number)] = number
    return number

def worker(i):
    time.sleep(i)
    return i

#http://songhuiming.github.io/pages/2016/06/18/python-multiprocessing-and-threads-01/
class MTest(unittest.TestCase):
    
    def test_multiprocess1(self):
        

        words = ['hello', 'world', 'test', 'word', 'another test']
        numbers = [1,2,3,4,5]
        pool = Pool(processes = 5)
        results = []
        for i in range(0, len(words)):
            results.append(pool.apply_async(foo, args=(words[i], numbers[i])))

        pool.close()
        pool.join()
        results = [r.get() for r in results]
        print(results)
    
    
    def test_multiprocess2(self):
        
        pool = Pool()
        result = pool.map_async(worker, range(15))
        while not result.ready():
            print("num left: {}".format(result._number_left))
            time.sleep(1)
        real_result = result.get()
        pool.close()
        pool.join()
    

       
        



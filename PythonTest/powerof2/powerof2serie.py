class PowerOf2Serie:
    def __init__(self):
        pass

    #for [1,2] return [1,2],[1,-2],[-1,2],[-1,-2]
    def PowerOf2Series(self, result, nr):
        length = len(result)
        if len(result) == 0:
            result.append([nr])
            result.append([-nr])
            return
        clone = []
        for x in range(0, length):
            list_item = result[x]
            clone.append(list(list_item))

        for x in range(0, length):
            list_item = result[x]
            list_item.append(nr)

        for x in range(0, length):
            list_item = clone[x]
            list_item.append(-nr)

        for x in range(0, len(clone)):
            result.append(clone[x])

import unittest
class PowerOf2Test(unittest.TestCase):
    def test_powerof2(self):
        service = PowerOf2Serie()
        nrs = [1,2,3]
        result = []
        for x in range(0,3):
            service.PowerOf2Series(result, nrs[x])
        answer = "[[1, 2, 3], [-1, 2, 3], [1, -2, 3], [-1, -2, 3], [1, 2, -3], [-1, 2, -3], [1, -2, -3], [-1, -2, -3]]"
        self.assertTrue(result[0] == [1, 2, 3])
        self.assertTrue(result[1] == [-1, 2, 3])
        self.assertTrue(result[2] == [1, -2, 3])
        self.assertTrue(result[3] == [-1, -2, 3])
        self.assertTrue(result[4] == [1, 2, -3])
        self.assertTrue(result[5] == [-1, 2, -3])
        self.assertTrue(result[6] == [1, -2, -3])
        self.assertTrue(result[7] == [-1, -2, -3])




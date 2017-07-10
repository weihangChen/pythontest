#for [1,2] return [1,2],[1,-2],[-1,2],[-1,-2]
def PowerOf2Series(result, nr):
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

nrs = [1,2,3]
result = []
for x in range(0,3):
    PowerOf2Series(result, nrs[x])
print(result)
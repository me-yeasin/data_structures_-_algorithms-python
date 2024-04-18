from functools import reduce


test = reduce(lambda x,y : x + y, [1,3,5,8])

print(test)
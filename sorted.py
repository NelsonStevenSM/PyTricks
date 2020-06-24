xs = {'a': 4, 'b':3, 'c':2, 'd':1}
print(xs.items())
sorvalues = sorted(xs.items(), key = lambda x : x[1])
print(sorvalues)

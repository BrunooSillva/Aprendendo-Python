import copy

d1 = {
    'c1' : 1, 
    'c2' : 2,
    'list' : [0,1,2],
}

d2 = copy.deepcopy(d1)

d2['c2'] = 3
d2['list'][2] = 5

print(d1)
print(d2)
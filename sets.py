myset = set(['a', 'b', 'c'])
print(myset)
myset.add(1)
print(myset)
setdua = set(['4','p',','])
setdua.update(myset)
print(setdua)
set3 = setdua.difference(myset)
print(set3)
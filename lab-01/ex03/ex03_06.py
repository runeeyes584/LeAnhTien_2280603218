def delElement(dictionay, key):
    if key in dictionay:
        del dictionay[key]
        return True
    else:
        return False
myDict = {'a': 1, 'b': 2, 'c': 3}
keyToDel = 'b'
result = delElement(myDict, keyToDel)
if result:
    print("Phan tu da duoc xoa tu Dictionary", myDict)
else:
    print("Khong tim thay phan tu can xoa")
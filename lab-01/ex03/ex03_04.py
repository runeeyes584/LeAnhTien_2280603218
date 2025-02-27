def accessElement(tupleData):
    firstElement = tupleData[0]
    lastElement = tupleData[-1]
    return firstElement, lastElement
inputTuple = eval(input("Nhap tuple: "))
first, last = accessElement(inputTuple)
print("Phan tu dau tien cua tuple la:", first)
print("Phan tu cuoi cung cua tuple la:", last)
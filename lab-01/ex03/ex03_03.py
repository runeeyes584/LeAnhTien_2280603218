def TupleList(lst):
    return tuple(lst)
inputList = input("Nhap danh sach cac so nguyen cach nhau boi dau phay: ")
numbers = list(map(int, inputList.split(',')))
result = TupleList(numbers)
print("List:", numbers)
print("Tuple tu danh sach la:", result)
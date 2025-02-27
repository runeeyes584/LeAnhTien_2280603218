def reverseList(lst):
    return lst[::-1]
inpuList = input("Nhap danh sach cac so nguyen cach nhau boi dau phay: ")
numbers = list(map(int, inpuList.split(',')))
result = reverseList(numbers)
print("Danh sach sau khi dao nguoc la:", result)

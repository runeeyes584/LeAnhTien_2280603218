def evenNumSum(lst):
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
    return sum
inpuList = input("Nhap danh sach cac so nguyen cach nhau boi dau phay: ")
numbers = list(map(int, inpuList.split(',')))
result = evenNumSum(numbers)
print("Tong cac so chan trong danh sach la:", result)
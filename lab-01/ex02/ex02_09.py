def primeNumbers(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhap so can kiem tra: "))
if primeNumbers(number):
    print("La so nguyen to")
else:
    print("Khong phai so nguyen to")
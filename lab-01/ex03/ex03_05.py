def countApperances(lst):
    countDict = {}
    for item in lst:
        if item in countDict:
            countDict[item] += 1
        else:
            countDict[item] = 1
    return countDict
inputString = input("Nhap danh sach cac tu cach nhau boi dau cach: ")
wordList = inputString.split()
result = countApperances(wordList)
print("So lan xuat hien cua cac tu trong danh sach la:", result)
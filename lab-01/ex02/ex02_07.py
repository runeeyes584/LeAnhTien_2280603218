print("Nhap cac dong vao, ket thuc bang 'done'.")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCac dong da nhap khi chuyen thanh chu in hoa:")
for line in lines:
    print(line.upper())
sogiolam = float(input("Nhap so gio lam moi tuan: "))
luonggio = float(input("Nhap thu la tren moi gio lam tieu chuan: "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam - giotieuchuan)
thuclinh = giotieuchuan * luonggio + luonggio * giovuotchuan * 1.5 
print("Luong thuc linh la: ", thuclinh)
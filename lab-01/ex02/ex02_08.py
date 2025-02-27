def chia_het_cho_5(sonhiphan):
    sothapphan = int(sonhiphan, 2)
    if sothapphan % 5 == 0:
        return True
    else:
        return False
chuoi_so_nhi_phan = input("Nhap so nhi phan (phan tach boi dau phay): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')
so_chi_het_cho_5 = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

if len(so_chi_het_cho_5) > 0:
    ketqua = ', '.join(so_chi_het_cho_5)
    print("Cac so nhi phan sau chia het cho 5:", ketqua)
else: 
    print("Khong co so nao chia het cho 5 trong chuoi da nhap")
def chia_5 (nhi_phan): 
    thap_phan = int(nhi_phan, 2)
    if thap_phan % 5 == 0: 
        return True
    else:
        return False

chuoi_nhi_phan = input("Nhập chuỗi số nhị phân: ")
nhi_phan_list = chuoi_nhi_phan.split(',')
chia_het_5 = [so for so in nhi_phan_list if chia_5(so)]

if len(chia_het_5) > 0:
    result = ','.join(chia_het_5)
    print("Số nhị phân chia hết cho 5: ", result)
else: 
    print("Không có con số nhị phân nào chia hết cho 5")
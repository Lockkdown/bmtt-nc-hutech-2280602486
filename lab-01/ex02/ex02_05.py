#So gio * Muc luong(20.000)
#Gio lam them = Gio tang ca - Gio tieu chuan -> Gio lam them * Luong gio * 1.5 

Gio_tieu_chuan = 44

Luong_theo_gio = float(input("Nhập lương mỗi giờ: "))
So_gio_lam_viec = float(input("Nhập số giờ làm mỗi tuần: "))

if So_gio_lam_viec <= Gio_tieu_chuan: 
    Tong_luong = Luong_theo_gio * So_gio_lam_viec
else:
    Gio_lam_them = So_gio_lam_viec - Gio_tieu_chuan
    Tong_luong = (Gio_tieu_chuan * Luong_theo_gio) + (Gio_lam_them * Luong_theo_gio * 1.5)
 
print("Tổng lương thu nhập: ", Tong_luong, "VND")
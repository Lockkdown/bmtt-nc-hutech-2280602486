from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1 == 1): 
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("*********************************MENU*********************************")
    print("** 1. Thêm sinh viên. **")
    print("** 2. Cập nhập thông tin sinh viên bởi ID. **")
    print("** 3. Xoá sinh viên bởi ID **")
    print("** 4. Tìm kiếm sinh viên theo tên. **")
    print("** 5. Sắp xếp sinh viên theo điểm TB. **")
    print("** 6. Sắp xếp sinh viên theo tên chuyên ngành. **")
    print("** 7. Hiển thị danh sách sinh viên. **")
    print("** 0. Thoát. **")
    print("**********************************************************************")
    
    key = int(input("Nhập: "))
    if (key == 1 ):
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("\nThêm sinh viên thành công.")
    elif (key == 2): 
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhập tt sinh viên")
            print("\nNhập ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nTrống")
    elif (key == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoá sinh viên.")
            print("\nNhập ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nSinh viên có ID = ", ID, "đã bị xoá.")
            else:
                print("\nSinh viên có id = ", ID, "không tồn tại.")
        else: 
            print("\n Trống!")
    elif (key == 4): 
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên.")
            print("\nNhập tên để tìm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else: 
            print("\nTrống")
    elif (key == 5): 
        if(qlsv.soLuongSinhVien() > 0):
            print("\n5. Sắp xếp sinh viên theo điểm trung bình.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else: 
            print("\nTrống")
    elif (key == 6): 
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sắp xếp sinh viên theo tên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else: 
            print("\nTrống")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0): 
            print("\n7. Hiển thị danh sách.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else: 
            print("\nTrống")
    elif (key == 0):
        print("Thoát chương trình.")
        break
    else:
        print("\n Không có chức năng này. Vui lòng chọn phù hợp.")

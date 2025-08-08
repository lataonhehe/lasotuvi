# from lasotuvi.AmDuong import canChiGio

# canGio, chiGio = canChiGio(6, 6)
# print(canGio, chiGio)

# from lasotuvi.AmDuong import ngayThangNam

# # Test chuyển đổi ngày dương sang âm
# ngay_am, thang_am, nam_am, thang_nhuan = ngayThangNam(7, 3, 2003)
# print(f"Ngày {7}/3/2003 dương lịch -> ngày {ngay_am}/{thang_am}/{nam_am} âm lịch")

# # Test thêm một số trường hợp khác
# test_cases = [
#     (15, 8, 2023), 
#     (31, 12, 2023)
# ]

# for ngay, thang, nam in test_cases:
#     ngay_am, thang_am, nam_am, thang_nhuan = ngayThangNam(ngay, thang, nam)
#     print(f"Ngày {ngay}/{thang}/{nam} dương lịch -> ngày {ngay_am}/{thang_am}/{nam_am} âm lịch")


# # Test chuyển đổi ngày tháng năm sang can chi
# from lasotuvi.AmDuong import ngayThangNamCanChi

# # Test một số trường hợp
# test_cases = [
#     (7, 3, 2003),  # Ngày sinh mẫu
#     (15, 8, 2023), # Ngày hiện tại
#     (31, 12, 2023) # Cuối năm
# ]

# print("\nTest chuyển đổi ngày tháng năm sang can chi:")
# for ngay, thang, nam in test_cases:
#     can_ngay, chi_ngay, can_thang, chi_thang, can_nam, chi_nam = ngayThangNamCanChi(ngay, thang, nam)
#     print(f"\nNgày {ngay}/{thang}/{nam}:")
#     print(f"Can ngày: {can_ngay}, Chi ngày: {chi_ngay}")
#     print(f"Can tháng: {can_thang}, Chi tháng: {chi_thang}")  
#     print(f"Can năm: {can_nam}, Chi năm: {chi_nam}")

# Test địa bàn
from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan

print("\nTest địa bàn:")
test_cases = [
    (7, 3, 2003, 6, 1, True, 7),  # Ngày sinh mẫu
    # (15, 8, 2023), # Ngày hiện tại
    # (31, 12, 2023) # Cuối năm
]

for ngay, thang, nam, gio, gioiTinh, duongLich, timeZone in test_cases:
    dia_ban = lapDiaBan(diaBan, ngay, thang, nam, gio, gioiTinh, duongLich, timeZone)
    print(f"\nĐịa bàn cho ngày {ngay}/{thang}/{nam}:")
    print(f"Địa bàn: {dia_ban}")
    print(f"Cung Menh: {dia_ban.cungMenh}")
    print(f"Cung Than: {dia_ban.cungThan}")
    # Print all cung and their properties
    for i in range(1, 13):
        cung = dia_ban.thapNhiCung[i]
        print(f"\nCung {i} ({cung.cungTen}):")
        print(f"Hành: {cung.hanhCung}")
        print(f"Âm dương: {'Âm' if cung.cungAmDuong == -1 else 'Dương'}")
        if hasattr(cung, 'cungChu'):
            print(f"Cung chủ: {cung.cungChu}")
        if hasattr(cung, 'cungDaiHan'):
            print(f"Đại hạn: {cung.cungDaiHan}")
        if hasattr(cung, 'cungTieuHan'):
            print(f"Tiểu hạn: {cung.cungTieuHan}")
        if cung.cungThan:
            print("Cung Thân")
        if hasattr(cung, 'tuanTrung'):
            print("Có Tuần")
        if hasattr(cung, 'trietLo'):
            print("Có Triệt")
        
        # Print all sao in the cung
        # if cung.cungSao:
        #     print("Các sao:")
        #     for sao in cung.cungSao:
        #         print(f"- {sao.get('tenSao', '')}")

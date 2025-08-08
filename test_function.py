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
# from lasotuvi.App import lapDiaBan
# from lasotuvi.DiaBan import diaBan

# print("\nTest địa bàn:")
# test_cases = [
#     (7, 3, 2003, 6, 1, True, 7),  # Ngày sinh mẫu
#     (30, 7, 2005, 21.5, -1, True, 7), # Ngày hiện tại
#     # (31, 12, 2023) # Cuối năm
# ]

# for ngay, thang, nam, gio, gioiTinh, duongLich, timeZone in test_cases:
#     dia_ban = lapDiaBan(diaBan, ngay, thang, nam, gio, gioiTinh, duongLich, timeZone)
#     print(f"\nĐịa bàn cho ngày {ngay}/{thang}/{nam}:")
#     print(f"Địa bàn: {dia_ban}")
#     print(f"Cung Menh: {dia_ban.cungMenh}")
#     print(f"Cung Than: {dia_ban.cungThan}")
#     # Print all cung and their properties
#     for i in range(1, 13):
#         cung = dia_ban.thapNhiCung[i]
#         print(f"\nCung {i} ({cung.cungTen}):")
#         print(f"Hành: {cung.hanhCung}")
#         print(f"Âm dương: {'Âm' if cung.cungAmDuong == -1 else 'Dương'}")
#         if hasattr(cung, 'cungChu'):
#             print(f"Cung chủ: {cung.cungChu}")
#         if hasattr(cung, 'cungDaiHan'):
#             print(f"Đại hạn: {cung.cungDaiHan}")
#         if hasattr(cung, 'cungTieuHan'):
#             print(f"Tiểu hạn: {cung.cungTieuHan}")
#         if cung.cungThan:
#             print("Cung Thân")
#         if hasattr(cung, 'tuanTrung'):
#             print("Có Tuần")
#         if hasattr(cung, 'trietLo'):
#             print("Có Triệt")
        
        # Print all sao in the cung
        # if cung.cungSao:
        #     print("Các sao:")
        #     for sao in cung.cungSao:
        #         print(f"- {sao.get('tenSao', '')}")
# from lasotuvi.App import lapDiaBan, lapThienBan
# from lasotuvi.DiaBan import diaBan
# from lasotuvi.AmDuong import ngayThangNamCanChi
# from lasotuvi.Colors import Colors, print_header, print_section, print_info, print_cung_info, format_star_with_color


# def testHoaTinhLinhTinh(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7):
#     """
#     Test function để kiểm tra an sao Hỏa tinh và Linh tinh
#     """
#     print_header("KIỂM TRA AN SAO HỎA TINH VÀ LINH TINH")
    
#     try:
#         from lasotuvi.AmDuong import timHoaLinh, ngayThangNamCanChi
#         from lasotuvi.DiaBan import diaBan
#         from lasotuvi.App import lapDiaBan
        
#         # Lấy thông tin can chi
#         canNgay, chiNgay, canThang, chiThang, canNam, chiNam = \
#             ngayThangNamCanChi(ngay, thang, nam, duongLich, timeZone)
        
#         # Lấy thông tin âm dương
#         from lasotuvi.AmDuong import thienCan, diaChi
#         amDuongNamSinh = thienCan[canNam]["amDuong"]
        
#         print_section("THÔNG TIN CƠ BẢN", Colors.CYAN)
#         print_info("Ngày sinh", f"{ngay}/{thang}/{nam}")
#         print_info("Giờ sinh", f"{gio} giờ")
#         print_info("Giới tính", 'Nam' if gioiTinh == 1 else 'Nữ')
#         print_info("Can Chi năm", f"{canNam} {chiNam}")
#         print_info("Âm dương năm", 'Dương' if amDuongNamSinh == 1 else 'Âm')
        
#         # Tính toán vị trí Hỏa tinh và Linh tinh
#         viTriHoaTinh, viTriLinhTinh = timHoaLinh(chiNam, gio, gioiTinh, amDuongNamSinh)
        
#         print_section("KẾT QUẢ AN SAO", Colors.GREEN)
#         print_info("Vị trí Hỏa tinh", f"Cung {viTriHoaTinh} ({diaChi[viTriHoaTinh]['tenChi']})")
#         print_info("Vị trí Linh tinh", f"Cung {viTriLinhTinh} ({diaChi[viTriLinhTinh]['tenChi']})")
        
#         # Tạo địa bàn để kiểm tra
#         diaban = lapDiaBan(diaBan, nn=ngay, tt=thang, nnnn=nam, gioSinh=gio, gioiTinh=gioiTinh, duongLich=duongLich, timeZone=timeZone)
        
#         print_section("KIỂM TRA TRÊN ĐỊA BÀN", Colors.YELLOW)
#         tenCung = ["", "Mệnh", "Phụ mẫu", "Phúc đức", "Điền trạch", "Quan lộc", 
#                     "Nô bộc", "Thiên di", "Tật ách", "Tài bạch", "Tử tức", "Phu thê", "Huynh đệ"]
        
#         # Kiểm tra cung Hỏa tinh
#         cungHoaTinh = diaban.thapNhiCung[viTriHoaTinh]
#         hoaTinhFound = False
#         if cungHoaTinh.cungSao:
#             for sao in cungHoaTinh.cungSao:
#                 if isinstance(sao, dict) and sao.get('saoTen') == 'Hỏa tinh':
#                     hoaTinhFound = True
#                     print_info(f"Hỏa tinh tại cung {viTriHoaTinh} ({tenCung[viTriHoaTinh]})", "✓ Tìm thấy")
#                     break
        
#         if not hoaTinhFound:
#             print_info(f"Hỏa tinh tại cung {viTriHoaTinh} ({tenCung[viTriHoaTinh]})", "✗ Không tìm thấy")
        
#         # Kiểm tra cung Linh tinh
#         cungLinhTinh = diaban.thapNhiCung[viTriLinhTinh]
#         linhTinhFound = False
#         if cungLinhTinh.cungSao:
#             for sao in cungLinhTinh.cungSao:
#                 if isinstance(sao, dict) and sao.get('saoTen') == 'Linh tinh':
#                     linhTinhFound = True
#                     print_info(f"Linh tinh tại cung {viTriLinhTinh} ({tenCung[viTriLinhTinh]})", "✓ Tìm thấy")
#                     break
        
#         if not linhTinhFound:
#             print_info(f"Linh tinh tại cung {viTriLinhTinh} ({tenCung[viTriLinhTinh]})", "✗ Không tìm thấy")
        
#         # In chi tiết các sao trong 2 cung này
#         print_section("CHI TIẾT SAO TRONG CUNG HỎA TINH", Colors.RED)
#         if cungHoaTinh.cungSao:
#             for sao in cungHoaTinh.cungSao:
#                 if isinstance(sao, dict):
#                     formatted_star = format_star_with_color(sao)
#                     print_info("Sao", formatted_star)
#         else:
#             print_info("Sao", "Không có sao")
        
#         print_section("CHI TIẾT SAO TRONG CUNG LINH TINH", Colors.MAGENTA)
#         if cungLinhTinh.cungSao:
#             for sao in cungLinhTinh.cungSao:
#                 if isinstance(sao, dict):
#                     formatted_star = format_star_with_color(sao)
#                     print_info("Sao", formatted_star)
#         else:
#             print_info("Sao", "Không có sao")
        
#         print(f"\n{Colors.BOLD}{Colors.GREEN}{'═' * 80}")
#         print(f"{'═' * 20} KẾT THÚC KIỂM TRA HỎA TINH - LINH TINH {'═' * 20}")
#         print(f"{'═' * 80}{Colors.END}")
        
#     except Exception as e:
#         print(f"{Colors.RED}❌ Lỗi khi kiểm tra Hỏa tinh - Linh tinh: {e}{Colors.END}")
#         import traceback
#         traceback.print_exc()


        # Thông tin mẫu
# gio = 6
# ngay = 7
# thang = 3
# nam = 2003
# gioiTinh = 1  # 1 = Nam, -1 = Nữ
# ten = "Nguyễn Văn A"

# testHoaTinhLinhTinh(ngay, thang, nam, gio, gioiTinh, ten)
from lasotuvi.App import lapDiaBan
from lasotuvi.ThienBan import lapThienBan
from lasotuvi.DiaBan import diaBan

def test_thienban():
    test_cases = [
        {
            'ngay': 7,
            'thang': 3,
            'nam': 2003,
            'gio': 6,
            'gioiTinh': 1,
            'ten': "Nguyễn Văn A",
            'duongLich': True,
            'timeZone': 7
        },
        {
            'ngay': 30,
            'thang': 7,
            'nam': 2005,
            'gio': 22,
            'gioiTinh': -1,
            'ten': "Nguyễn Thị B", 
            'duongLich': True,
            'timeZone': 7
        }
    ]

    for test in test_cases:
        try:
            print(f"\nTesting thiên bàn with data: {test}")
            
            # Tạo địa bàn trước để truyền vào thiên bàn
            diaban = lapDiaBan(
                diaBan=diaBan,
                nn=test['ngay'],
                tt=test['thang'],
                nnnn=test['nam'],
                gioSinh=test['gio'],
                gioiTinh=test['gioiTinh'],
                duongLich=test['duongLich'],
                timeZone=test['timeZone']
            )
            
            # Tạo thiên bàn
            thienban = lapThienBan(
                nn=test['ngay'],
                tt=test['thang'],
                nnnn=test['nam'],
                gioSinh=test['gio'],
                gioiTinh=test['gioiTinh'],
                ten=test['ten'],
                diaBan=diaban,
                duongLich=test['duongLich'],
                timeZone=test['timeZone']
            )

            # In tất cả các thuộc tính của thiên bàn
            print("\nChi tiết thiên bàn:")
            print(f"Tên: {thienban.ten}")
            print(f"Giới tính: {thienban.namNu}")
            print(f"Ngày/tháng/năm dương: {thienban.ngayDuong}/{thienban.thangDuong}/{thienban.namDuong}")
            print(f"Ngày/tháng/năm âm: {thienban.ngayAm}/{thienban.thangAm}/{thienban.namAm}")
            print(f"Can ngày: {thienban.canNgayTen}")
            print(f"Chi ngày: {thienban.chiNgayTen}")
            print(f"Can tháng: {thienban.canThangTen}")
            print(f"Chi tháng: {thienban.chiThangTen}")
            print(f"Can năm: {thienban.canNamTen}")
            print(f"Chi năm: {thienban.chiNamTen}")
            print(f"Giờ sinh: {thienban.gioSinh}")
            print(f"Âm dương năm sinh: {thienban.amDuongNamSinh}")
            print(f"Âm dương mệnh: {thienban.amDuongMenh}")
            print(f"Tên cục: {thienban.tenCuc}")
            print(f"Mệnh chủ: {thienban.menhChu}")
            print(f"Thân chủ: {thienban.thanChu}")
            print(f"Bản mệnh: {thienban.banMenh}")
            print(f"Sinh khắc: {thienban.sinhKhac}")
            print("=" * 50)

        except Exception as e:
            print(f"✗ Test failed with error: {str(e)}")
            import traceback
            traceback.print_exc()

test_thienban()


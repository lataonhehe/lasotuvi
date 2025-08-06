from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan
from lasotuvi.ThienBan import lapThienBan
from lasotuvi.AmDuong import diaChi, thienCan

def inLaSoTuViTongHop(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7):
    """
    Tạo và in lá số tử vi tổng hợp với thông tin quan trọng nhất
    """
    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print("║                            LÁ SỐ TỬ VI TỔNG HỢP                           ║")
    print("╚══════════════════════════════════════════════════════════════════════════════╝")
    
    try:
        # Tạo địa bàn và thiên bàn
        diaban = lapDiaBan(diaBan, nn=ngay, tt=thang, nnnn=nam, gioSinh=gio, gioiTinh=gioiTinh, duongLich=duongLich, timeZone=timeZone)
        thienban = lapThienBan(ngay, thang, nam, gio, gioiTinh, ten, diaban, duongLich, timeZone)
        
        # Thông tin cá nhân
        print("\n📋 THÔNG TIN CÁ NHÂN")
        print("─" * 60)
        print(f"   Họ tên: {ten}")
        print(f"   Ngày sinh: {ngay}/{thang}/{nam}")
        print(f"   Giờ sinh: {gio} giờ")
        print(f"   Giới tính: {'Nam' if gioiTinh == 1 else 'Nữ'}")
        print(f"   Can Chi giờ sinh: {thienban.gioSinh}")
        
        # Thông tin can chi
        print("\n📅 THÔNG TIN CAN CHI")
        print("─" * 60)
        print(f"   Can Chi năm: {thienban.canNamTen} {thienban.chiNamTen}")
        print(f"   Can Chi tháng: {thienban.canThangTen} {thienban.chiThangTen}")
        print(f"   Can Chi ngày: {thienban.canNgayTen} {thienban.chiNgayTen}")
        print(f"   Can Chi giờ: {thienban.canGioSinh} {thienban.chiGioSinh['tenChi']}")
        
        # Thông tin mệnh
        print("\n🎯 THÔNG TIN MỆNH")
        print("─" * 60)
        print(f"   Bản mệnh: {thienban.banMenh}")
        print(f"   Mệnh chủ: {thienban.menhChu}")
        print(f"   Thân chủ: {thienban.thanChu}")
        print(f"   Sinh khắc: {thienban.sinhKhac}")
        print(f"   Âm dương mệnh: {thienban.amDuongMenh}")
        
        # Thông tin cục
        print("\n🔢 THÔNG TIN CỤC")
        print("─" * 60)
        print(f"   Hành cục: {thienban.hanhCuc}")
        print(f"   Tên cục: {thienban.tenCuc}")
        
        # Thông tin địa bàn
        print("\n🏠 ĐỊA BÀN (12 CUNG)")
        print("─" * 60)
        print(f"   Cung Mệnh: {diaban.cungMenh}")
        print(f"   Cung Thân: {diaban.cungThan}")
        print(f"   Cung Nô bộc: {diaban.cungNoboc}")
        print(f"   Cung Tật ách: {diaban.cungTatAch}")
        
        # In chi tiết từng cung địa bàn với sao chính
        print("\n📊 CHI TIẾT 12 CUNG ĐỊA BÀN (SAO CHÍNH)")
        print("─" * 100)
        tenCung = ["", "Mệnh", "Phụ mẫu", "Phúc đức", "Điền trạch", "Quan lộc", 
                    "Nô bộc", "Thiên di", "Tật ách", "Tài bạch", "Tử tức", "Phu thê", "Huynh đệ"]
        
        for i in range(1, 13):
            cung = diaban.thapNhiCung[i]
            # Chỉ lấy sao chính (loại 1-6)
            saoChinh = []
            if cung.cungSao:
                for sao in cung.cungSao:
                    try:
                        if isinstance(sao, dict) and 'saoTen' in sao:
                            if sao.get('saoLoai', 0) <= 6:  # Chỉ sao chính
                                saoChinh.append(sao['saoTen'])
                    except:
                        pass
            
            print(f"   Cung {i:2d} ({tenCung[i]:10s}): {cung.cungTen:8s} - Sao chính: {', '.join(saoChinh)}")
        
        # Thông tin đại hạn và tiểu hạn
        print("\n⏰ THÔNG TIN HẠN")
        print("─" * 60)
        for i in range(1, 13):
            cung = diaban.thapNhiCung[i]
            if hasattr(cung, 'cungDaiHan'):
                print(f"   Cung {i} - Đại hạn: {cung.cungDaiHan}")
            if hasattr(cung, 'cungTieuHan'):
                print(f"   Cung {i} - Tiểu hạn: {cung.cungTieuHan}")
        
        print("\n" + "═" * 80)
        print("                           KẾT THÚC LÁ SỐ TỔNG HỢP")
        print("═" * 80)
        
    except Exception as e:
        print(f"❌ Lỗi khi tạo lá số: {e}")
        import traceback
        traceback.print_exc()

def inLaSoTuViNganGon(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7):
    """
    Tạo và in lá số tử vi ngắn gọn với thông tin cơ bản
    """
    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print("║                            LÁ SỐ TỬ VI NGẮN GỌN                           ║")
    print("╚══════════════════════════════════════════════════════════════════════════════╝")
    
    try:
        # Tạo địa bàn và thiên bàn
        diaban = lapDiaBan(diaBan, nn=ngay, tt=thang, nnnn=nam, gioSinh=gio, gioiTinh=gioiTinh, duongLich=duongLich, timeZone=timeZone)
        thienban = lapThienBan(ngay, thang, nam, gio, gioiTinh, ten, diaban, duongLich, timeZone)
        
        # Thông tin cơ bản
        print(f"\n📋 THÔNG TIN: {ten} - {ngay}/{thang}/{nam} - {gio} giờ - {'Nam' if gioiTinh == 1 else 'Nữ'}")
        print(f"🎯 MỆNH: {thienban.banMenh} - {thienban.tenCuc} - {thienban.sinhKhac}")
        print(f"📅 CAN CHI: {thienban.canNamTen} {thienban.chiNamTen} - {thienban.canThangTen} {thienban.chiThangTen} - {thienban.canNgayTen} {thienban.chiNgayTen} - {thienban.gioSinh}")
        
        # 12 cung với sao chính
        print("\n🏠 12 CUNG ĐỊA BÀN:")
        tenCung = ["", "Mệnh", "Phụ mẫu", "Phúc đức", "Điền trạch", "Quan lộc", 
                    "Nô bộc", "Thiên di", "Tật ách", "Tài bạch", "Tử tức", "Phu thê", "Huynh đệ"]
        
        for i in range(1, 13):
            cung = diaban.thapNhiCung[i]
            saoChinh = []
            if cung.cungSao:
                for sao in cung.cungSao:
                    if isinstance(sao, dict) and 'saoTen' in sao:
                        # Chỉ lấy các sao chính (loại 1-6)
                        if sao.get('saoLoai', 0) <= 6:
                            saoChinh.append(sao['saoTen'])
            
            print(f"   Cung {i:2d} ({tenCung[i]:10s}): {cung.cungTen:8s} - Sao chính: {', '.join(saoChinh)}")
        
        print("\n" + "═" * 80)
        print("                           KẾT THÚC LÁ SỐ NGẮN GỌN")
        print("═" * 80)
        
    except Exception as e:
        print(f"❌ Lỗi khi tạo lá số ngắn gọn: {e}")
        import traceback
        traceback.print_exc()

# Thông tin mẫu
gio = 6
ngay = 7
thang = 3
nam = 2003
gioiTinh = 1  # 1 = Nam, -1 = Nữ
ten = "Nguyễn Văn A"

# Tạo lá số tổng hợp
print("=== LÁ SỐ TỬ VI TỔNG HỢP ===")
inLaSoTuViTongHop(ngay, thang, nam, gio, gioiTinh, ten)

print("\n\n" + "="*80 + "\n")

# Tạo lá số ngắn gọn
print("=== LÁ SỐ TỬ VI NGẮN GỌN ===")
inLaSoTuViNganGon(ngay, thang, nam, gio, gioiTinh, ten)

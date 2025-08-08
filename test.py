from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan
from lasotuvi.ThienBan import lapThienBan
from lasotuvi.AmDuong import diaChi, thienCan

# ANSI color codes for better visualization
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def get_ngu_hanh_color(ngu_hanh):
    """Get color based on ngũ hành"""
    ngu_hanh_colors = {
        'K': Colors.YELLOW,  # Kim - Vàng
        'M': Colors.GREEN,    # Mộc - Xanh lá
        'T': Colors.CYAN,     # Thủy - Xanh dương
        'H': Colors.RED,      # Hỏa - Đỏ
        'O': Colors.MAGENTA   # Thổ - Tím
    }
    return ngu_hanh_colors.get(ngu_hanh, Colors.END)

def print_header(title):
    """Print a beautiful header"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}")
    print(f"{'='*20} {title} {'='*20}")
    print(f"{'='*80}{Colors.END}\n")

def print_section(title, color=Colors.BLUE):
    """Print a section header"""
    print(f"\n{color}{Colors.BOLD}📋 {title}{Colors.END}")
    print(f"{color}{'─' * 60}{Colors.END}")

def print_info(label, value, color=Colors.GREEN):
    """Print information with consistent formatting"""
    print(f"   {Colors.BOLD}{label}:{Colors.END} {color}{value}{Colors.END}")

def print_cung_info(cung_num, ten_cung, cung_ten, chinh_tinh, phu_tinh, dac_biet=None):
    """Print cung information with better formatting"""
    # Format palace name with special indicators inline
    palace_display = f"{Colors.CYAN}{ten_cung:10s}{Colors.END}"
    if dac_biet:
        special_indicators = f" [{Colors.RED}{', '.join(dac_biet)}{Colors.END}]"
        palace_display += special_indicators
    
    print(f"   {Colors.YELLOW}Cung {cung_num:2d}{Colors.END} ({palace_display}): {Colors.GREEN}{cung_ten:8s}{Colors.END}")
    if not chinh_tinh:
        chinh_tinh.append("Vô chính diệu")
    print(f"           {Colors.BLUE}Chính tinh:{Colors.END} {', '.join(chinh_tinh)}")
    if phu_tinh:
        print(f"           {Colors.CYAN}Phụ tinh:{Colors.END} {', '.join(phu_tinh)}")

def format_star_with_color(star_info):
    """Format star with ngũ hành color"""
    if isinstance(star_info, dict):
        star_name = star_info.get('saoTen', '')
        star_ngu_hanh = star_info.get('saoNguHanh', '')
        star_dac_tinh = star_info.get('saoDacTinh', '')
        
        color = get_ngu_hanh_color(star_ngu_hanh)
        formatted_name = f"{color}{star_name}{Colors.END}"
        
        if star_dac_tinh:
            formatted_name += f"({star_dac_tinh})"
        
        return formatted_name
    return str(star_info)

def inLaSoTuViTongHop(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7):
    """
    Tạo và in lá số tử vi tổng hợp với thông tin quan trọng nhất
    """
    print_header("LÁ SỐ TỬ VI TỔNG HỢP")
    
    try:
        # Tạo địa bàn và thiên bàn
        diaban = lapDiaBan(diaBan, nn=ngay, tt=thang, nnnn=nam, gioSinh=gio, gioiTinh=gioiTinh, duongLich=duongLich, timeZone=timeZone)
        thienban = lapThienBan(ngay, thang, nam, gio, gioiTinh, ten, diaban, duongLich, timeZone)
        
        # Thông tin cá nhân
        print_section("THÔNG TIN CÁ NHÂN", Colors.CYAN)
        print_info("Họ tên", ten)
        print_info("Ngày sinh", f"{ngay}/{thang}/{nam}")
        print_info("Giờ sinh", f"{gio} giờ")
        print_info("Giới tính", 'Nam' if gioiTinh == 1 else 'Nữ')
        print_info("Can Chi giờ sinh", thienban.gioSinh)
        
        # Thông tin can chi
        print_section("THÔNG TIN CAN CHI", Colors.BLUE)
        print_info("Can Chi năm", f"{thienban.canNamTen} {thienban.chiNamTen}")
        print_info("Can Chi tháng", f"{thienban.canThangTen} {thienban.chiThangTen}")
        print_info("Can Chi ngày", f"{thienban.canNgayTen} {thienban.chiNgayTen}")
        print_info("Can Chi giờ", f"{thienban.canGioSinh['tenCan']} {thienban.chiGioSinh['tenChi']}")
        
        # Thông tin mệnh
        print_section("THÔNG TIN MỆNH", Colors.YELLOW)
        print_info("Bản mệnh", thienban.banMenh)
        print_info("Mệnh chủ", thienban.menhChu)
        print_info("Thân chủ", thienban.thanChu)
        print_info("Sinh khắc", thienban.sinhKhac)
        print_info("Âm dương mệnh", thienban.amDuongMenh)
        
        # Thông tin cục
        print_section("THÔNG TIN CỤC", Colors.GREEN)
        print_info("Hành cục", str(thienban.hanhCuc))
        print_info("Tên cục", thienban.tenCuc)
        
        # In chi tiết từng cung địa bàn với chính tinh và phụ tinh
        print_section("CHI TIẾT 12 CUNG ĐỊA BÀN (CHÍNH TINH & PHỤ TINH)", Colors.RED)
        
        for i in range(1, 13):
            cung = diaban.thapNhiCung[i]
            # Tách chính tinh (saoLoai = 1) và phụ tinh (các sao khác)
            chinhTinh = []
            phuTinh = []
            if cung.cungSao:
                for sao in cung.cungSao:
                    try:
                        if isinstance(sao, dict) and 'saoTen' in sao:
                            # Format star with ngũ hành color
                            formatted_star = format_star_with_color(sao)
                            
                            # Phân loại theo saoLoai
                            if sao.get('saoLoai', 0) == 1:
                                chinhTinh.append(formatted_star)
                            else:
                                phuTinh.append(formatted_star)
                    except:
                        pass
            
            # Thông tin đặc biệt của cung
            dacBiet = []
            if hasattr(cung, 'cungThan') and cung.cungThan:
                dacBiet.append("Thân")
            if hasattr(cung, 'tuanTrung') and cung.tuanTrung:
                dacBiet.append("Tuần")
            if hasattr(cung, 'trietLo') and cung.trietLo:
                dacBiet.append("Triệt")
            
            # In thông tin cung với formatting mới
            print_cung_info(i, cung.tenCungChu, cung.cungTen, chinhTinh, phuTinh, dacBiet)
            
        
        # Thông tin đại hạn và tiểu hạn
        # print_section("THÔNG TIN HẠN", Colors.CYAN)
        # for i in range(1, 13):
        #     cung = diaban.thapNhiCung[i]
        #     if hasattr(cung, 'cungDaiHan'):
        #         print_info(f"Cung {i} - Đại hạn", str(cung.cungDaiHan))
        #     if hasattr(cung, 'cungTieuHan'):
        #         print_info(f"Cung {i} - Tiểu hạn", cung.cungTieuHan)
        
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'═' * 80}")
        print(f"{'═' * 20} KẾT THÚC LÁ SỐ TỔNG HỢP {'═' * 20}")
        print(f"{'═' * 80}{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Lỗi khi tạo lá số: {e}{Colors.END}")
        import traceback
        traceback.print_exc()

def inLaSoTuViNganGon(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7):
    """
    Tạo và in lá số tử vi ngắn gọn với thông tin cơ bản
    """
    print_header("LÁ SỐ TỬ VI NGẮN GỌN")
    
    try:
        # Tạo địa bàn và thiên bàn
        diaban = lapDiaBan(diaBan, nn=ngay, tt=thang, nnnn=nam, gioSinh=gio, gioiTinh=gioiTinh, duongLich=duongLich, timeZone=timeZone)
        thienban = lapThienBan(ngay, thang, nam, gio, gioiTinh, ten, diaban, duongLich, timeZone)
        
        # Thông tin cơ bản
        print_section("THÔNG TIN CƠ BẢN", Colors.CYAN)
        print_info("Thông tin", f"{ten} - {ngay}/{thang}/{nam} - {gio} giờ - {'Nam' if gioiTinh == 1 else 'Nữ'}")
        print_info("Mệnh", f"{thienban.banMenh} - {thienban.tenCuc} - {thienban.sinhKhac}")
        print_info("Can Chi", f"{thienban.canNamTen} {thienban.chiNamTen} - {thienban.canThangTen} {thienban.chiThangTen} - {thienban.canNgayTen} {thienban.chiNgayTen} - {thienban.gioSinh}")
        
        # 12 cung với chính tinh và phụ tinh
        print_section("12 CUNG ĐỊA BÀN", Colors.BLUE)
        
        for i in range(1, 13):
            cung = diaban.thapNhiCung[i]
            chinhTinh = []
            phuTinh = []
            if cung.cungSao:
                for sao in cung.cungSao:
                    if isinstance(sao, dict) and 'saoTen' in sao:
                        # Format star with ngũ hành color
                        formatted_star = format_star_with_color(sao)
                        
                        # Phân loại theo saoLoai
                        if sao.get('saoLoai', 0) == 1:
                            chinhTinh.append(formatted_star)
                        else:
                            phuTinh.append(formatted_star)
            
            print_cung_info(i, cung.getTenCungChu(), cung.cungTen, chinhTinh, phuTinh)
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'═' * 80}")
        print(f"{'═' * 20} KẾT THÚC LÁ SỐ NGẮN GỌN {'═' * 20}")
        print(f"{'═' * 80}{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Lỗi khi tạo lá số ngắn gọn: {e}{Colors.END}")
        import traceback
        traceback.print_exc()

def test_inLaSoTuViNganGon():
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
            print(f"\nTesting with data: {test}")
            inLaSoTuViTongHop(
                test['ngay'],
                test['thang'], 
                test['nam'],
                test['gio'],
                test['gioiTinh'],
                test['ten'],
                test['duongLich'],
                test['timeZone']
            )
            print("✓ Test passed")
        except Exception as e:
            print(f"✗ Test failed: {str(e)}")

def test_palace_names():
    """
    Test function to show palace names in thapNhiCung
    """
    try:
        # Create a test case
        ngay, thang, nam, gio, gioiTinh = 7, 3, 2003, 6, 1
        ten = "Nguyễn Văn A"
        
        # Create diaBan
        diaban = lapDiaBan(diaBan, nn=ngay, tt=thang, nnnn=nam, gioSinh=gio, 
                           gioiTinh=gioiTinh, duongLich=True, timeZone=7)
        
        print_header("THẬP NHỊ CUNG VỚI TÊN CUNG")
        print_section("12 CUNG ĐỊA BÀN", Colors.BLUE)
        
        tenCung = ["", "Mệnh", "Phụ mẫu", "Phúc đức", "Điền trạch", "Quan lộc", 
                    "Nô bộc", "Thiên di", "Tật ách", "Tài bạch", "Tử tức", "Phu thê", "Huynh đệ"]
        
        for i in range(1, 13):
            cung = diaban.thapNhiCung[i]
            palace_name = cung.getTenCungChu()
            print(f"   {Colors.YELLOW}Cung {i:2d}{Colors.END}: {Colors.CYAN}{cung.cungTen:8s}{Colors.END} - {Colors.GREEN}{palace_name}{Colors.END}")
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'═' * 80}")
        print(f"{'═' * 20} KẾT THÚC TEST TÊN CUNG {'═' * 20}")
        print(f"{'═' * 80}{Colors.END}")
        
    except Exception as e:
        print(f"{Colors.RED}❌ Lỗi khi test tên cung: {e}{Colors.END}")
        import traceback
        traceback.print_exc()

test_inLaSoTuViNganGon()
# test_palace_names()
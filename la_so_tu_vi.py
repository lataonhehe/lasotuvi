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

def tao_la_so_tu_vi(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7):
    """
    Tạo và in lá số tử vi tổng hợp với thông tin quan trọng nhất
    
    Args:
        ngay (int): Ngày sinh
        thang (int): Tháng sinh  
        nam (int): Năm sinh
        gio (int): Giờ sinh
        gioiTinh (int): Giới tính (1: Nam, -1: Nữ)
        ten (str): Họ tên
        duongLich (bool): True nếu là dương lịch, False nếu âm lịch
        timeZone (int): Múi giờ
    
    Returns:
        dict: Kết quả lá số tử vi với các thông tin chính
    """
    try:
        # Tạo địa bàn và thiên bàn
        diaban = lapDiaBan(diaBan, nn=ngay, tt=thang, nnnn=nam, gioSinh=gio, gioiTinh=gioiTinh, duongLich=duongLich, timeZone=timeZone)
        thienban = lapThienBan(ngay, thang, nam, gio, gioiTinh, ten, diaban, duongLich, timeZone)
        
        # In header
        # print_header("LÁ SỐ TỬ VI TỔNG HỢP")
        
        # # Thông tin cá nhân
        # print_section("THÔNG TIN CÁ NHÂN", Colors.CYAN)
        # print_info("Họ tên", ten)
        # print_info("Ngày sinh", f"{ngay}/{thang}/{nam}")
        # print_info("Giờ sinh", f"{gio} giờ")
        # print_info("Giới tính", 'Nam' if gioiTinh == 1 else 'Nữ')
        # print_info("Can Chi giờ sinh", thienban.gioSinh)
        
        # # Thông tin can chi
        # print_section("THÔNG TIN CAN CHI", Colors.BLUE)
        # print_info("Can Chi năm", f"{thienban.canNamTen} {thienban.chiNamTen}")
        # print_info("Can Chi tháng", f"{thienban.canThangTen} {thienban.chiThangTen}")
        # print_info("Can Chi ngày", f"{thienban.canNgayTen} {thienban.chiNgayTen}")
        # print_info("Can Chi giờ", f"{thienban.canGioSinh['tenCan']} {thienban.chiGioSinh['tenChi']}")
        
        # # Thông tin mệnh
        # print_section("THÔNG TIN MỆNH", Colors.YELLOW)
        # print_info("Bản mệnh", thienban.banMenh)
        # print_info("Mệnh chủ", thienban.menhChu)
        # print_info("Thân chủ", thienban.thanChu)
        # print_info("Sinh khắc", thienban.sinhKhac)
        # print_info("Âm dương mệnh", thienban.amDuongMenh)
        
        # # Thông tin cục
        # print_section("THÔNG TIN CỤC", Colors.GREEN)
        # print_info("Hành cục", str(thienban.hanhCuc))
        # print_info("Tên cục", thienban.tenCuc)
        
        # # In chi tiết từng cung địa bàn với chính tinh và phụ tinh
        # print_section("CHI TIẾT 12 CUNG ĐỊA BÀN (CHÍNH TINH & PHỤ TINH)", Colors.RED)
        
        # Tạo kết quả trả về
        ket_qua = {
            'thong_tin_ca_nhan': {
                'ho_ten': ten,
                'ngay_sinh': f"{ngay}/{thang}/{nam}",
                'gio_sinh': f"{gio} giờ",
                'gioi_tinh': 'Nam' if gioiTinh == 1 else 'Nữ',
                'can_chi_gio_sinh': thienban.gioSinh
            },
            'can_chi': {
                'can_chi_nam': f"{thienban.canNamTen} {thienban.chiNamTen}",
                'can_chi_thang': f"{thienban.canThangTen} {thienban.chiThangTen}",
                'can_chi_ngay': f"{thienban.canNgayTen} {thienban.chiNgayTen}",
                'can_chi_gio': f"{thienban.canGioSinh['tenCan']} {thienban.chiGioSinh['tenChi']}"
            },
            'menh': {
                'ban_menh': thienban.banMenh,
                'menh_chu': thienban.menhChu,
                'than_chu': thienban.thanChu,
                'sinh_khac': thienban.sinhKhac,
                'am_duong_menh': thienban.amDuongMenh
            },
            'cuc': {
                'hanh_cuc': str(thienban.hanhCuc),
                'ten_cuc': thienban.tenCuc
            },
            'thap_nhi_cung': []
        }
        
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
            
            # # In thông tin cung với formatting mới
            # print_cung_info(i, cung.tenCungChu, cung.cungTen, chinhTinh, phuTinh, dacBiet)
            
            # Thêm vào kết quả
            ket_qua['thap_nhi_cung'].append({
                'cung_so': i,
                'ten_cung': cung.tenCungChu,
                'cung_ten': cung.cungTen,
                'chinh_tinh': chinhTinh,
                'phu_tinh': phuTinh,
                'dac_biet': dacBiet
            })
        
        # print(f"\n{Colors.BOLD}{Colors.GREEN}{'═' * 80}")
        # print(f"{'═' * 20} KẾT THÚC LÁ SỐ TỔNG HỢP {'═' * 20}")
        # print(f"{'═' * 80}{Colors.END}")
        
        return ket_qua
        
    except Exception as e:
        print(f"{Colors.RED}❌ Lỗi khi tạo lá số: {e}{Colors.END}")
        import traceback
        traceback.print_exc()
        return None

def tao_la_so_tu_vi_ngan_gon(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7):
    """
    Tạo và in lá số tử vi ngắn gọn với thông tin cơ bản
    
    Args:
        ngay (int): Ngày sinh
        thang (int): Tháng sinh  
        nam (int): Năm sinh
        gio (int): Giờ sinh
        gioiTinh (int): Giới tính (1: Nam, -1: Nữ)
        ten (str): Họ tên
        duongLich (bool): True nếu là dương lịch, False nếu âm lịch
        timeZone (int): Múi giờ
    
    Returns:
        dict: Kết quả lá số tử vi ngắn gọn
    """
    try:
        # Tạo địa bàn và thiên bàn
        diaban = lapDiaBan(diaBan, nn=ngay, tt=thang, nnnn=nam, gioSinh=gio, gioiTinh=gioiTinh, duongLich=duongLich, timeZone=timeZone)
        thienban = lapThienBan(ngay, thang, nam, gio, gioiTinh, ten, diaban, duongLich, timeZone)
        
        # In header
        print_header("LÁ SỐ TỬ VI NGẮN GỌN")
        
        # Thông tin cơ bản
        print_section("THÔNG TIN CƠ BẢN", Colors.CYAN)
        print_info("Thông tin", f"{ten} - {ngay}/{thang}/{nam} - {gio} giờ - {'Nam' if gioiTinh == 1 else 'Nữ'}")
        print_info("Mệnh", f"{thienban.banMenh} - {thienban.tenCuc} - {thienban.sinhKhac}")
        print_info("Can Chi", f"{thienban.canNamTen} {thienban.chiNamTen} - {thienban.canThangTen} {thienban.chiThangTen} - {thienban.canNgayTen} {thienban.chiNgayTen} - {thienban.gioSinh}")
        
        # Tạo kết quả trả về
        ket_qua = {
            'thong_tin_co_ban': {
                'ho_ten': ten,
                'ngay_sinh': f"{ngay}/{thang}/{nam}",
                'gio_sinh': f"{gio} giờ",
                'gioi_tinh': 'Nam' if gioiTinh == 1 else 'Nữ'
            },
            'menh': {
                'ban_menh': thienban.banMenh,
                'ten_cuc': thienban.tenCuc,
                'sinh_khac': thienban.sinhKhac
            },
            'can_chi': {
                'can_chi_nam': f"{thienban.canNamTen} {thienban.chiNamTen}",
                'can_chi_thang': f"{thienban.canThangTen} {thienban.chiThangTen}",
                'can_chi_ngay': f"{thienban.canNgayTen} {thienban.chiNgayTen}",
                'can_chi_gio': thienban.gioSinh
            },
            'thap_nhi_cung': []
        }
        
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
            
            # Thêm vào kết quả
            ket_qua['thap_nhi_cung'].append({
                'cung_so': i,
                'ten_cung': cung.getTenCungChu(),
                'cung_ten': cung.cungTen,
                'chinh_tinh': chinhTinh,
                'phu_tinh': phuTinh
            })
        
        print(f"\n{Colors.BOLD}{Colors.GREEN}{'═' * 80}")
        print(f"{'═' * 20} KẾT THÚC LÁ SỐ NGẮN GỌN {'═' * 20}")
        print(f"{'═' * 80}{Colors.END}")
        
        return ket_qua
        
    except Exception as e:
        print(f"{Colors.RED}❌ Lỗi khi tạo lá số ngắn gọn: {e}{Colors.END}")
        import traceback
        traceback.print_exc()
        return None

# Ví dụ sử dụng
if __name__ == "__main__":
    # Test case 1
    print("=== TEST CASE 1 ===")
    ket_qua_1 = tao_la_so_tu_vi(
        ngay=7, thang=3, nam=2003, gio=6, 
        gioiTinh=1, ten="Nguyễn Văn A"
    )
    
    print("\n" + "="*50 + "\n")
    
    # Test case 2  
    print("=== TEST CASE 2 ===")
    ket_qua_2 = tao_la_so_tu_vi_ngan_gon(
        ngay=30, thang=7, nam=2005, gio=22,
        gioiTinh=-1, ten="Nguyễn Thị B"
    )

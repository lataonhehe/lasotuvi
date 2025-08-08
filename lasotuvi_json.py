from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import diaBan
from lasotuvi.ThienBan import lapThienBan
from lasotuvi.AmDuong import diaChi, thienCan
import json
from datetime import datetime

def format_star_info(star_info):
    """Format star information for JSON output"""
    if isinstance(star_info, dict):
        return {
            'ten': star_info.get('saoTen', ''),
            'ngu_hanh': star_info.get('saoNguHanh', ''),
            'dac_tinh': star_info.get('saoDacTinh', ''),
            'loai': star_info.get('saoLoai', 0),
            'mo_ta': star_info.get('saoMoTa', ''),
            'hanh_ngu_hanh': {
                'kim': star_info.get('saoNguHanh', '') == 'K',
                'moc': star_info.get('saoNguHanh', '') == 'M',
                'thuy': star_info.get('saoNguHanh', '') == 'T',
                'hoa': star_info.get('saoNguHanh', '') == 'H',
                'tho': star_info.get('saoNguHanh', '') == 'O'
            }
        }
    return str(star_info)

def get_cung_info(cung, cung_ten, cung_so):
    """Get detailed information about a cung"""
    chinh_tinh = []
    phu_tinh = []
    
    if cung.cungSao:
        for sao in cung.cungSao:
            try:
                if isinstance(sao, dict) and 'saoTen' in sao:
                    star_info = format_star_info(sao)
                    
                    # Phân loại theo saoLoai
                    if sao.get('saoLoai', 0) == 1:
                        chinh_tinh.append(star_info)
                    else:
                        phu_tinh.append(star_info)
            except:
                pass
    
    # Thông tin đặc biệt của cung
    dac_biet = []
    if hasattr(cung, 'cungThan') and cung.cungThan:
        dac_biet.append("Thân")
    if hasattr(cung, 'tuanTrung') and cung.tuanTrung:
        dac_biet.append("Tuần")
    if hasattr(cung, 'trietLo') and cung.trietLo:
        dac_biet.append("Triệt")
    
    return {
        'so_cung': cung_so,
        'ten': cung_ten,
        'dia_chi': cung.cungTen,
        'chinh_tinh': chinh_tinh,
        'phu_tinh': phu_tinh,
        'dac_biet': dac_biet,
        'dai_han': getattr(cung, 'cungDaiHan', None),
        'tieu_han': getattr(cung, 'cungTieuHan', None),
        'tong_so_sao': len(chinh_tinh) + len(phu_tinh)
    }

def taoLaSoTuViJSON(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7):
    """
    Tạo lá số tử vi và trả về dạng JSON với cấu trúc được cải thiện
    """
    try:
        # Tạo địa bàn và thiên bàn
        diaban = lapDiaBan(diaBan, nn=ngay, tt=thang, nnnn=nam, gioSinh=gio, gioiTinh=gioiTinh, duongLich=duongLich, timeZone=timeZone)
        thienban = lapThienBan(ngay, thang, nam, gio, gioiTinh, ten, diaban, duongLich, timeZone)
        
        # Tên các cung
        tenCung = ["", "Mệnh", "Phụ mẫu", "Phúc đức", "Điền trạch", "Quan lộc", 
                    "Nô bộc", "Thiên di", "Tật ách", "Tài bạch", "Tử tức", "Phu thê", "Huynh đệ"]
        
        # Thông tin 12 cung
        cung_info = []
        for i in range(1, 13):
            cung = diaban.thapNhiCung[i]
            cung_data = get_cung_info(cung, tenCung[i], i)
            cung_info.append(cung_data)
        
        # Thông tin Tuần và Triệt
        tuan_cung = []
        triet_cung = []
        for i in range(1, 13):
            cung = diaban.thapNhiCung[i]
            if hasattr(cung, 'tuanTrung') and cung.tuanTrung:
                tuan_cung.append({
                    'cung_so': i,
                    'ten_cung': tenCung[i],
                    'dia_chi': cung.cungTen
                })
            if hasattr(cung, 'trietLo') and cung.trietLo:
                triet_cung.append({
                    'cung_so': i,
                    'ten_cung': tenCung[i],
                    'dia_chi': cung.cungTen
                })
        
        # Thống kê sao
        tong_chinh_tinh = sum(len(cung['chinh_tinh']) for cung in cung_info)
        tong_phu_tinh = sum(len(cung['phu_tinh']) for cung in cung_info)
        
        # Cấu trúc JSON được cải thiện
        la_so_json = {
            "metadata": {
                "version": "1.0",
                "created_at": datetime.now().isoformat(),
                "format": "tu_vi_chart",
                "language": "vi"
            },
            "personal_info": {
                "ho_ten": ten,
                "ngay_sinh": {
                    "ngay": ngay,
                    "thang": thang,
                    "nam": nam,
                    "formatted": f"{ngay}/{thang}/{nam}"
                },
                "gio_sinh": {
                    "gio": gio,
                    "formatted": f"{gio} giờ"
                },
                "gioi_tinh": {
                    "code": gioiTinh,
                    "text": 'Nam' if gioiTinh == 1 else 'Nữ'
                },
                "settings": {
                    "duong_lich": duongLich,
                    "time_zone": timeZone
                }
            },
            "astrological_data": {
                "can_chi": {
                    "nam": {
                        "can": thienban.canNamTen,
                        "chi": thienban.chiNamTen,
                        "can_chi": f"{thienban.canNamTen} {thienban.chiNamTen}"
                    },
                    "thang": {
                        "can": thienban.canThangTen,
                        "chi": thienban.chiThangTen,
                        "can_chi": f"{thienban.canThangTen} {thienban.chiThangTen}"
                    },
                    "ngay": {
                        "can": thienban.canNgayTen,
                        "chi": thienban.chiNgayTen,
                        "can_chi": f"{thienban.canNgayTen} {thienban.chiNgayTen}"
                    },
                    "gio": {
                        "can": thienban.canGioSinh,
                        "chi": thienban.chiGioSinh['tenChi'],
                        "can_chi": thienban.gioSinh
                    }
                },
                "menh": {
                    "ban_menh": thienban.banMenh,
                    "menh_chu": thienban.menhChu,
                    "than_chu": thienban.thanChu,
                    "sinh_khac": thienban.sinhKhac,
                    "am_duong_menh": thienban.amDuongMenh
                },
                "cuc": {
                    "hanh_cuc": str(thienban.hanhCuc),
                    "ten_cuc": thienban.tenCuc
                }
            },
            "chart_structure": {
                "dia_ban": {
                    "cung_menh": str(diaban.cungMenh),
                    "cung_than": str(diaban.cungThan),
                    "cung_no_boc": str(diaban.cungNoboc),
                    "cung_tat_ach": str(diaban.cungTatAch)
                },
                "tuan_triet": {
                    "tuan": tuan_cung,
                    "triet": triet_cung,
                    "summary": {
                        "co_tuan": len(tuan_cung) > 0,
                        "co_triet": len(triet_cung) > 0,
                        "tong_tuan": len(tuan_cung),
                        "tong_triet": len(triet_cung)
                    }
                }
            },
            "cung_data": {
                "tong_so_cung": 12,
                "cung_list": cung_info,
                "statistics": {
                    "tong_chinh_tinh": tong_chinh_tinh,
                    "tong_phu_tinh": tong_phu_tinh,
                    "tong_sao": tong_chinh_tinh + tong_phu_tinh,
                    "cung_nhieu_sao_nhat": max(cung_info, key=lambda x: x['tong_so_sao'])['so_cung'],
                    "cung_it_sao_nhat": min(cung_info, key=lambda x: x['tong_so_sao'])['so_cung']
                }
            }
        }
        
        return la_so_json
        
    except Exception as e:
        return {
            "error": {
                "message": str(e),
                "type": "calculation_error"
            },
            "metadata": {
                "version": "1.0",
                "created_at": datetime.now().isoformat(),
                "format": "tu_vi_chart",
                "language": "vi"
            }
        }

def inLaSoTuViJSON(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7, indent=2):
    """
    Tạo và in lá số tử vi dạng JSON
    """
    la_so = taoLaSoTuViJSON(ngay, thang, nam, gio, gioiTinh, ten, duongLich, timeZone)
    print(json.dumps(la_so, ensure_ascii=False, indent=indent))

def luuLaSoTuViJSON(ngay, thang, nam, gio, gioiTinh, ten, duongLich=True, timeZone=7, filename=None):
    """
    Tạo và lưu lá số tử vi dạng JSON vào file
    """
    la_so = taoLaSoTuViJSON(ngay, thang, nam, gio, gioiTinh, ten, duongLich, timeZone)
    
    if filename is None:
        filename = f"la_so_{ten.replace(' ', '_')}_{ngay}_{thang}_{nam}.json"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(la_so, f, ensure_ascii=False, indent=2)
        print(f"Đã lưu lá số vào file: {filename}")
        return filename
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")
        return None

def get_chart_summary(la_so_json):
    """
    Trả về tóm tắt thông tin lá số
    """
    if "error" in la_so_json:
        return {"error": "Không thể tạo tóm tắt do lỗi"}
    
    return {
        "personal": {
            "ten": la_so_json["personal_info"]["ho_ten"],
            "ngay_sinh": la_so_json["personal_info"]["ngay_sinh"]["formatted"],
            "gioi_tinh": la_so_json["personal_info"]["gioi_tinh"]["text"]
        },
        "astrological": {
            "can_chi_nam": la_so_json["astrological_data"]["can_chi"]["nam"]["can_chi"],
            "ban_menh": la_so_json["astrological_data"]["menh"]["ban_menh"],
            "ten_cuc": la_so_json["astrological_data"]["cuc"]["ten_cuc"],
            "sinh_khac": la_so_json["astrological_data"]["menh"]["sinh_khac"]
        },
        "statistics": la_so_json["cung_data"]["statistics"],
        "special_features": la_so_json["chart_structure"]["tuan_triet"]["summary"]
    }

# Thông tin mẫu
if __name__ == "__main__":
    gio = 6
    ngay = 7
    thang = 3
    nam = 2003
    gioiTinh = 1  # 1 = Nam, -1 = Nữ
    ten = "Nguyễn Văn A"
    
    # In lá số dạng JSON
    print("=== LÁ SỐ TỬ VI DẠNG JSON (CẢI THIỆN) ===")
    inLaSoTuViJSON(ngay, thang, nam, gio, gioiTinh, ten)
    
    # Lưu lá số vào file
    print("\n=== LƯU LÁ SỐ VÀO FILE ===")
    luuLaSoTuViJSON(ngay, thang, nam, gio, gioiTinh, ten)

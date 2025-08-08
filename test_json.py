from lasotuvi_json import taoLaSoTuViJSON, inLaSoTuViJSON, luuLaSoTuViJSON, get_chart_summary
import json

# Thông tin mẫu
gio = 6
ngay = 7
thang = 3
nam = 2003
gioiTinh = 1  # 1 = Nam, -1 = Nữ
ten = "Nguyễn Văn A"

print("=== TẠO LÁ SỐ TỬ VI DẠNG JSON (CẢI THIỆN) ===")

# Tạo lá số JSON
la_so = taoLaSoTuViJSON(ngay, thang, nam, gio, gioiTinh, ten)

# In ra metadata
print("📋 METADATA:")
print(json.dumps(la_so["metadata"], ensure_ascii=False, indent=2))

# In ra thông tin cá nhân
print("\n👤 THÔNG TIN CÁ NHÂN:")
print(json.dumps(la_so["personal_info"], ensure_ascii=False, indent=2))

# In ra dữ liệu chiêm tinh
print("\n🔮 DỮ LIỆU CHIÊM TINH:")
print("Can Chi:")
print(json.dumps(la_so["astrological_data"]["can_chi"], ensure_ascii=False, indent=2))

print("\nMệnh:")
print(json.dumps(la_so["astrological_data"]["menh"], ensure_ascii=False, indent=2))

print("\nCục:")
print(json.dumps(la_so["astrological_data"]["cuc"], ensure_ascii=False, indent=2))

# In ra cấu trúc lá số
print("\n🏛️ CẤU TRÚC LÁ SỐ:")
print("Địa bàn:")
print(json.dumps(la_so["chart_structure"]["dia_ban"], ensure_ascii=False, indent=2))

print("\nTuần và Triệt:")
print(json.dumps(la_so["chart_structure"]["tuan_triet"], ensure_ascii=False, indent=2))

# In ra dữ liệu 12 cung
print("\n📊 DỮ LIỆU 12 CUNG:")
print(f"Tổng số cung: {la_so['cung_data']['tong_so_cung']}")
print("Thống kê:")
print(json.dumps(la_so["cung_data"]["statistics"], ensure_ascii=False, indent=2))

# In ra chi tiết cung 1 (Mệnh)
print("\n🎯 CHI TIẾT CUNG 1 (MỆNH):")
cung_1 = la_so["cung_data"]["cung_list"][0]  # Cung 1
print(f"Cung số: {cung_1['so_cung']}")
print(f"Tên: {cung_1['ten']}")
print(f"Địa chi: {cung_1['dia_chi']}")
print(f"Tổng số sao: {cung_1['tong_so_sao']}")

print("\nChính tinh:")
for sao in cung_1['chinh_tinh']:
    print(f"  - {sao['ten']} ({sao['ngu_hanh']}) - {sao['dac_tinh']}")
    print(f"    Ngũ hành: {sao['hanh_ngu_hanh']}")

print("\nPhụ tinh:")
for sao in cung_1['phu_tinh']:
    print(f"  - {sao['ten']} ({sao['ngu_hanh']}) - {sao['dac_tinh']}")

if cung_1['dac_biet']:
    print(f"\nĐặc biệt: {', '.join(cung_1['dac_biet'])}")

# In ra tóm tắt
print("\n📈 TÓM TẮT LÁ SỐ:")
summary = get_chart_summary(la_so)
print(json.dumps(summary, ensure_ascii=False, indent=2))

# Lưu vào file
print("\n💾 LƯU VÀO FILE:")
filename = luuLaSoTuViJSON(ngay, thang, nam, gio, gioiTinh, ten)
print(f"File đã được tạo: {filename}")

# In ra một số thống kê thú vị
print("\n🔍 THỐNG KÊ THÚ VỊ:")
stats = la_so["cung_data"]["statistics"]
print(f"- Tổng chính tinh: {stats['tong_chinh_tinh']}")
print(f"- Tổng phụ tinh: {stats['tong_phu_tinh']}")
print(f"- Tổng sao: {stats['tong_sao']}")
print(f"- Cung nhiều sao nhất: {stats['cung_nhieu_sao_nhat']}")
print(f"- Cung ít sao nhất: {stats['cung_it_sao_nhat']}")

# In ra thông tin Tuần Triệt
tuan_triet = la_so["chart_structure"]["tuan_triet"]["summary"]
print(f"\n- Có Tuần: {tuan_triet['co_tuan']}")
print(f"- Có Triệt: {tuan_triet['co_triet']}")
print(f"- Tổng Tuần: {tuan_triet['tong_tuan']}")
print(f"- Tổng Triệt: {tuan_triet['tong_triet']}")

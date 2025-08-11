import requests
import json

# URL của API
BASE_URL = "http://localhost:8000"

def test_root():
    """Test root endpoint"""
    print("=== TEST ROOT ENDPOINT ===")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    print()

def test_health():
    """Test health check endpoint"""
    print("=== TEST HEALTH CHECK ===")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
    print()

def test_la_so_tu_vi_tong_hop():
    """Test tạo lá số tử vi tổng hợp"""
    print("=== TEST LÁ SỐ TỬ VI TỔNG HỢP ===")
    
    # Dữ liệu test
    data = {
        "ngay": 7,
        "thang": 3,
        "nam": 2003,
        "gio": 6,
        "gioi_tinh": 1,
        "ten": "Nguyễn Văn A",
        "duong_lich": True,
        "time_zone": 7
    }
    
    try:
        response = requests.post(f"{BASE_URL}/la-so-tu-vi/tong-hop", json=data)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Lá số tử vi tổng hợp được tạo thành công!")
            print(f"Thông tin cá nhân: {result['thong_tin_ca_nhan']}")
            print(f"Số cung: {len(result['thap_nhi_cung'])}")
            
            # In chi tiết một số cung
            for cung in result['thap_nhi_cung'][:3]:  # Chỉ in 3 cung đầu
                print(f"Cung {cung['cung_so']}: {cung['ten_cung']} - {cung['cung_ten']}")
                print(f"  Chính tinh: {cung['chinh_tinh']}")
                print(f"  Phụ tinh: {cung['phu_tinh']}")
        else:
            print(f"❌ Lỗi: {response.text}")
            
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    
    print()

def test_la_so_tu_vi_ngan_gon():
    """Test tạo lá số tử vi ngắn gọn"""
    print("=== TEST LÁ SỐ TỬ VI NGẮN GỌN ===")
    
    # Dữ liệu test
    data = {
        "ngay": 30,
        "thang": 7,
        "nam": 2005,
        "gio": 22,
        "gioi_tinh": -1,
        "ten": "Nguyễn Thị B",
        "duong_lich": True,
        "time_zone": 7
    }
    
    try:
        response = requests.post(f"{BASE_URL}/la-so-tu-vi/ngan-gon", json=data)
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Lá số tử vi ngắn gọn được tạo thành công!")
            print(f"Thông tin cơ bản: {result['thong_tin_co_ban']}")
            print(f"Mệnh: {result['menh']}")
            print(f"Số cung: {len(result['thap_nhi_cung'])}")
            
            # In chi tiết một số cung
            for cung in result['thap_nhi_cung'][:3]:  # Chỉ in 3 cung đầu
                print(f"Cung {cung['cung_so']}: {cung['ten_cung']} - {cung['cung_ten']}")
                print(f"  Chính tinh: {cung['chinh_tinh']}")
                print(f"  Phụ tinh: {cung['phu_tinh']}")
        else:
            print(f"❌ Lỗi: {response.text}")
            
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    
    print()

def test_invalid_data():
    """Test với dữ liệu không hợp lệ"""
    print("=== TEST DỮ LIỆU KHÔNG HỢP LỆ ===")
    
    # Test với ngày không hợp lệ
    invalid_data = {
        "ngay": 32,  # Ngày không hợp lệ
        "thang": 3,
        "nam": 2003,
        "gio": 6,
        "gioi_tinh": 1,
        "ten": "Test",
        "duong_lich": True,
        "time_zone": 7
    }
    
    try:
        response = requests.post(f"{BASE_URL}/la-so-tu-vi/tong-hop", json=invalid_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
    except Exception as e:
        print(f"❌ Lỗi kết nối: {e}")
    
    print()

def main():
    """Chạy tất cả các test"""
    print("🚀 BẮT ĐẦU TEST API LÁ SỐ TỬ VI")
    print("=" * 50)
    
    # Test các endpoint cơ bản
    test_root()
    test_health()
    
    # Test tạo lá số tử vi
    test_la_so_tu_vi_tong_hop()
    test_la_so_tu_vi_ngan_gon()
    
    # Test validation
    test_invalid_data()
    
    print("🏁 KẾT THÚC TEST API LÁ SỐ TỬ VI")

if __name__ == "__main__":
    main()

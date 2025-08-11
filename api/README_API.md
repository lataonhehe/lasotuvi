# Lá Số Tử Vi API

FastAPI application để tạo lá số tử vi tổng hợp và ngắn gọn.

## Cấu trúc thư mục

```
api/
├── __init__.py              # Package init
├── api_la_so_tu_vi.py      # FastAPI application
├── run_api.py              # Script chạy server
├── test_api.py             # Test script
├── requirements_api.txt     # Dependencies
└── README_API.md           # Documentation này
```

## Cài đặt

### 1. Cài đặt dependencies

```bash
cd api
pip install -r requirements_api.txt
```

### 2. Chạy server

**Cách 1: Sử dụng script run_api.py**
```bash
cd api
python run_api.py
```

**Cách 2: Chạy trực tiếp**
```bash
cd api
python api_la_so_tu_vi.py
```

**Cách 3: Từ thư mục gốc**
```bash
python api/api_la_so_tu_vi.py
```

Server sẽ chạy tại: `http://localhost:8000`

## API Endpoints

### 1. Root Endpoint
- **URL**: `GET /`
- **Mô tả**: Thông tin cơ bản về API
- **Response**: Thông tin API và danh sách endpoints

### 2. Health Check
- **URL**: `GET /health`
- **Mô tả**: Kiểm tra trạng thái API
- **Response**: Trạng thái hoạt động

### 3. Tạo Lá Số Tử Vi Tổng Hợp
- **URL**: `POST /la-so-tu-vi/tong-hop`
- **Mô tả**: Tạo lá số tử vi với đầy đủ thông tin
- **Request Body**:
```json
{
    "ngay": 7,
    "thang": 3,
    "nam": 2003,
    "gio": 6,
    "gioi_tinh": 1,
    "ten": "Nguyễn Văn A",
    "duong_lich": true,
    "time_zone": 7
}
```

### 4. Tạo Lá Số Tử Vi Ngắn Gọn
- **URL**: `POST /la-so-tu-vi/ngan-gon`
- **Mô tả**: Tạo lá số tử vi với thông tin cơ bản
- **Request Body**: Tương tự như tổng hợp

## Tham số Request

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---------|------|----------|-------|
| ngay | int | ✅ | Ngày sinh (1-31) |
| thang | int | ✅ | Tháng sinh (1-12) |
| nam | int | ✅ | Năm sinh (1900-2100) |
| gio | int | ✅ | Giờ sinh (0-23) |
| gioi_tinh | int | ✅ | Giới tính (1: Nam, -1: Nữ) |
| ten | string | ✅ | Họ tên |
| duong_lich | boolean | ❌ | True nếu dương lịch, False nếu âm lịch (mặc định: True) |
| time_zone | int | ❌ | Múi giờ (-12 đến 14, mặc định: 7) |

## Response Format

### Lá Số Tổng Hợp
```json
{
    "thong_tin_ca_nhan": {
        "ho_ten": "Nguyễn Văn A",
        "ngay_sinh": "7/3/2003",
        "gio_sinh": "6 giờ",
        "gioi_tinh": "Nam",
        "can_chi_gio_sinh": "Giáp Tý"
    },
    "can_chi": {
        "can_chi_nam": "Quý Mùi",
        "can_chi_thang": "Giáp Dần",
        "can_chi_ngay": "Đinh Sửu",
        "can_chi_gio": "Giáp Tý"
    },
    "menh": {
        "ban_menh": "Thủy",
        "menh_chu": "Thủy",
        "than_chu": "Thổ",
        "sinh_khac": "Thủy sinh Mộc",
        "am_duong_menh": "Âm"
    },
    "cuc": {
        "hanh_cuc": "Thủy",
        "ten_cuc": "Thủy Nhị Cục"
    },
    "thap_nhi_cung": [
        {
            "cung_so": 1,
            "ten_cung": "Mệnh",
            "cung_ten": "Tý",
            "chinh_tinh": ["Tử Vi", "Thiên Cơ"],
            "phu_tinh": ["Văn Xương", "Văn Khúc"],
            "dac_biet": ["Thân"]
        }
    ]
}
```

### Lá Số Ngắn Gọn
```json
{
    "thong_tin_co_ban": {
        "ho_ten": "Nguyễn Văn A",
        "ngay_sinh": "7/3/2003",
        "gio_sinh": "6 giờ",
        "gioi_tinh": "Nam"
    },
    "menh": {
        "ban_menh": "Thủy",
        "ten_cuc": "Thủy Nhị Cục",
        "sinh_khac": "Thủy sinh Mộc"
    },
    "can_chi": {
        "can_chi_nam": "Quý Mùi",
        "can_chi_thang": "Giáp Dần",
        "can_chi_ngay": "Đinh Sửu",
        "can_chi_gio": "Giáp Tý"
    },
    "thap_nhi_cung": [...]
}
```

## Sử dụng với cURL

### Tạo lá số tổng hợp
```bash
curl -X POST "http://localhost:8000/la-so-tu-vi/tong-hop" \
     -H "Content-Type: application/json" \
     -d '{
         "ngay": 7,
         "thang": 3,
         "nam": 2003,
         "gio": 6,
         "gioi_tinh": 1,
         "ten": "Nguyễn Văn A",
         "duong_lich": true,
         "time_zone": 7
     }'
```

### Tạo lá số ngắn gọn
```bash
curl -X POST "http://localhost:8000/la-so-tu-vi/ngan-gon" \
     -H "Content-Type: application/json" \
     -d '{
         "ngay": 30,
         "thang": 7,
         "nam": 2005,
         "gio": 22,
         "gioi_tinh": -1,
         "ten": "Nguyễn Thị B",
         "duong_lich": true,
         "time_zone": 7
     }'
```

## Sử dụng với Python

```python
import requests

# Tạo lá số tổng hợp
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

response = requests.post("http://localhost:8000/la-so-tu-vi/tong-hop", json=data)
if response.status_code == 200:
    la_so = response.json()
    print(f"Lá số của {la_so['thong_tin_ca_nhan']['ho_ten']}")
    print(f"Mệnh: {la_so['menh']['ban_menh']}")
```

## Test API

Chạy file test để kiểm tra API:

```bash
cd api
python test_api.py
```

## Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Error Handling

API trả về các mã lỗi HTTP chuẩn:

- `400 Bad Request`: Dữ liệu đầu vào không hợp lệ
- `500 Internal Server Error`: Lỗi server khi tạo lá số

## Validation

API tự động validate các tham số đầu vào:

- Ngày: 1-31
- Tháng: 1-12  
- Năm: 1900-2100
- Giờ: 0-23
- Giới tính: 1 (Nam) hoặc -1 (Nữ)
- Tên: 1-100 ký tự
- Múi giờ: -12 đến 14

## Development

### Cấu trúc project
```
lasotuvi/
├── lasotuvi/              # Core library
├── api/                   # FastAPI application
│   ├── __init__.py
│   ├── api_la_so_tu_vi.py
│   ├── run_api.py
│   ├── test_api.py
│   ├── requirements_api.txt
│   └── README_API.md
├── la_so_tu_vi.py        # Core functions
└── test.py               # Test functions
```

### Chạy từ thư mục gốc
```bash
# Chạy API
python api/api_la_so_tu_vi.py

# Test API
python api/test_api.py

# Chạy core functions
python la_so_tu_vi.py
```

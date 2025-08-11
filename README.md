# La So Tu Vi - Lá Số Tử Vi

Thư viện Python để tạo lá số tử vi tổng hợp và ngắn gọn, bao gồm cả FastAPI application.

## Cấu trúc Project

```
lasotuvi/
├── lasotuvi/              # Core library
│   ├── __init__.py
│   ├── AmDuong.py
│   ├── App.py
│   ├── DiaBan.py
│   ├── Lich_EPHEM.py
│   ├── Lich_HND.py
│   ├── Sao.py
│   └── ThienBan.py
├── api/                   # FastAPI application
│   ├── __init__.py
│   ├── api_la_so_tu_vi.py
│   ├── run_api.py
│   ├── test_api.py
│   ├── requirements_api.txt
│   └── README_API.md
├── tests/                 # Unit tests
├── docs/                  # Documentation
├── la_so_tu_vi.py        # Core functions
├── test.py               # Test functions
├── requirements.txt       # Core dependencies
└── README.md             # This file
```

## Tính năng chính

### 1. Core Library (`lasotuvi/`)
- Tính toán can chi năm, tháng, ngày, giờ
- Xác định bản mệnh, mệnh chủ, thân chủ
- Tính toán thập nhị cung địa bàn
- Phân tích chính tinh và phụ tinh
- Hỗ trợ âm lịch và dương lịch

### 2. Core Functions (`la_so_tu_vi.py`)
- `tao_la_so_tu_vi()`: Tạo lá số tử vi tổng hợp
- `tao_la_so_tu_vi_ngan_gon()`: Tạo lá số tử vi ngắn gọn
- In kết quả với màu sắc và formatting đẹp
- Trả về dictionary với đầy đủ thông tin

### 3. FastAPI Application (`api/`)
- REST API để tạo lá số tử vi
- Validation tự động
- Documentation với Swagger UI
- Error handling chuẩn HTTP
- Health check endpoint

## Cài đặt

### 1. Cài đặt dependencies cơ bản
```bash
pip install -r requirements.txt
```

### 2. Cài đặt dependencies cho API (tùy chọn)
```bash
cd api
pip install -r requirements_api.txt
```

## Sử dụng

### 1. Sử dụng Core Functions

```python
from la_so_tu_vi import tao_la_so_tu_vi, tao_la_so_tu_vi_ngan_gon

# Tạo lá số tổng hợp
ket_qua = tao_la_so_tu_vi(
    ngay=7, thang=3, nam=2003, gio=6,
    gioiTinh=1, ten="Nguyễn Văn A"
)

# Tạo lá số ngắn gọn
ket_qua_ngan_gon = tao_la_so_tu_vi_ngan_gon(
    ngay=30, thang=7, nam=2005, gio=22,
    gioiTinh=-1, ten="Nguyễn Thị B"
)
```

### 2. Sử dụng FastAPI

**Chạy server:**
```bash
# Cách 1: Sử dụng script
cd api
python run_api.py

# Cách 2: Chạy trực tiếp
cd api
python api_la_so_tu_vi.py

# Cách 3: Từ thư mục gốc
python api/api_la_so_tu_vi.py
```

**Truy cập API:**
- Server: http://localhost:8000
- Documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

**Test API:**
```bash
cd api
python test_api.py
```

## API Endpoints

### POST `/la-so-tu-vi/tong-hop`
Tạo lá số tử vi tổng hợp với đầy đủ thông tin.

### POST `/la-so-tu-vi/ngan-gon`
Tạo lá số tử vi ngắn gọn với thông tin cơ bản.

### GET `/health`
Kiểm tra trạng thái API.

### GET `/`
Thông tin cơ bản về API.

## Tham số API

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---------|------|----------|-------|
| ngay | int | ✅ | Ngày sinh (1-31) |
| thang | int | ✅ | Tháng sinh (1-12) |
| nam | int | ✅ | Năm sinh (1900-2100) |
| gio | int | ✅ | Giờ sinh (0-23) |
| gioi_tinh | int | ✅ | Giới tính (1: Nam, -1: Nữ) |
| ten | string | ✅ | Họ tên |
| duong_lich | boolean | ❌ | True nếu dương lịch (mặc định: True) |
| time_zone | int | ❌ | Múi giờ (-12 đến 14, mặc định: 7) |

## Ví dụ sử dụng API

### cURL
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

### Python
```python
import requests

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

## Testing

### Test Core Functions
```bash
python test.py
```

### Test API
```bash
cd api
python test_api.py
```

### Test Unit Tests
```bash
python -m pytest tests/
```

## Documentation

- **API Documentation**: [api/README_API.md](api/README_API.md)
- **Core Library**: [docs/](docs/)
- **Swagger UI**: http://localhost:8000/docs (khi chạy API)

## Tính năng nổi bật

### 1. Core Library
- ✅ Tính toán chính xác can chi
- ✅ Xác định bản mệnh và mệnh chủ
- ✅ Phân tích thập nhị cung
- ✅ Hỗ trợ âm lịch và dương lịch
- ✅ Màu sắc theo ngũ hành

### 2. FastAPI Application
- ✅ REST API chuẩn
- ✅ Validation tự động
- ✅ Documentation tự động
- ✅ Error handling
- ✅ Health check
- ✅ Logging

### 3. Testing
- ✅ Unit tests
- ✅ API tests
- ✅ Integration tests

## License

MIT License - xem file [LICENSE](LICENSE) để biết thêm chi tiết.

## Contributing

1. Fork project
2. Tạo feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## Support

Nếu có vấn đề hoặc câu hỏi, vui lòng tạo issue trên GitHub repository.

# Lasotuvi - Thư viện Tử vi Việt Nam

[![Build Status](https://travis-ci.org/doanguyen/lasotuvi.svg?branch=main)](https://travis-ci.org/doanguyen/lasotuvi)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Lasotuvi** là thư viện Python mã nguồn mở để tính toán tử vi Việt Nam. Thư viện cung cấp các công cụ toàn diện để tạo và phân tích lá số tử vi dựa trên các nguyên tắc tử vi truyền thống Việt Nam.

## 🌟 Tính năng chính

- **✨ Tạo lá số tử vi hoàn chỉnh** - Tạo lá số tử vi Việt Nam đầy đủ với tất cả cung và sao
- **⭐ Tính toán vị trí sao chính xác** - Đặt chính xác tất cả các sao chính và phụ theo thuật toán truyền thống
- **📅 Tích hợp lịch âm dương** - Hỗ trợ cả lịch dương và lịch âm với chuyển đổi tự động
- **🌍 Xử lý múi giờ toàn cầu** - Tính toán múi giờ chính xác để tạo lá số chính xác
- **🔮 Hệ thống sao toàn diện** - Bao gồm tất cả các sao tử vi truyền thống Việt Nam
- **🐍 Triển khai Python hiện đại** - Mã nguồn sạch, được tài liệu hóa tốt, dễ mở rộng
- **🧪 Kiểm thử đầy đủ** - Bộ test toàn diện đảm bảo độ chính xác

## 📦 Cài đặt

### Yêu cầu hệ thống
- Python 3.6 trở lên
- pip package manager

### Cài đặt từ PyPI
```bash
pip install lasotuvi
```

### Cài đặt từ mã nguồn
```bash
git clone https://github.com/doanguyen/lasotuvi.git
cd lasotuvi
pip install -e .
```

### Cài đặt cho phát triển
```bash
git clone https://github.com/doanguyen/lasotuvi.git
cd lasotuvi
python -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc venv\Scripts\activate  # Windows
pip install -e .
pip install -r requirements.txt
pip install pytest black flake8 mypy
```

## 🚀 Hướng dẫn sử dụng

### Ví dụ cơ bản

```python
from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import DiaBan

# Tạo lá số cho người sinh vào:
# Ngày: 15, tháng: 3, năm: 1990
# Giờ: 14:30 (2:30 chiều)
# Giới tính: Nam (1 cho nam, 0 cho nữ)
# Lịch: Dương lịch (True cho dương lịch, False cho âm lịch)
# Múi giờ: UTC+7

diaBan = lapDiaBan(
    DiaBan, 
    nn=15,           # Ngày
    tt=3,            # Tháng  
    nnnn=1990,       # Năm
    gioSinh=14.5,    # Giờ sinh (định dạng 24 giờ)
    gioiTinh=1,      # Giới tính (1=nam, 0=nữ)
    duongLich=True,  # Loại lịch (True=dương lịch, False=âm lịch)
    timeZone=7       # Độ lệch múi giờ
)

# Truy cập thông tin lá số
print(f"Cung Mệnh: {diaBan.cungMenh}")
print(f"Cung Quan: {diaBan.cungQuan}")
print(f"Cung Tài: {diaBan.cungTai}")
print(f"Cung Phụ Mẫu: {diaBan.cungPhuMau}")
print(f"Cung Tử Tức: {diaBan.cungTuTuc}")
```

### Ví dụ nâng cao

```python
# Tạo lá số với lịch âm
diaBanAm = lapDiaBan(
    DiaBan,
    nn=15, tt=3, nnnn=1990,
    gioSinh=14.5, gioiTinh=1,
    duongLich=False,  # Sử dụng âm lịch
    timeZone=7
)

# Xem thông tin chi tiết về các sao
for cung in range(1, 13):
    saoTrongCung = diaBan.getSaoTrongCung(cung)
    if saoTrongCung:
        print(f"Cung {cung}: {saoTrongCung}")
```

## 📚 Tài liệu kỹ thuật

### Các thành phần chính

- **`App.py`** - Logic ứng dụng chính để tạo lá số và đặt sao
- **`DiaBan.py`** - Cấu trúc lá số và tính toán các cung, đại hạn, tiểu hạn
- **`AmDuong.py`** - Tính toán Âm Dương, Ngũ Hành, Can Chi
- **`Sao.py`** - Định nghĩa và đặt tất cả các sao tử vi
- **`ThienBan.py`** - Tính toán thiên bàn và các yếu tố thiên văn
- **`Lich_EPHEM.py`** - Tính toán lịch thiên văn chính xác
- **`Lich_HND.py`** - Chuyển đổi lịch Việt Nam và xử lý ngày tháng

### API chính

#### Tạo lá số
```python
lapDiaBan(diaBan, nn, tt, nnnn, gioSinh, gioiTinh, duongLich, timeZone)
```
Tạo lá số tử vi hoàn chỉnh với tất cả sao và cung.

#### Đặt sao chính
```python
# Đặt sao Tử vi
viTriTuVi = timTuVi(cucSo, nn)
diaBan.nhapSao(viTriTuVi, saoTuVi)

# Đặt sao Liêm Trinh
viTriLiemTrinh = dichCung(viTriTuVi, 4)
diaBan.nhapSao(viTriLiemTrinh, saoLiemTrinh)
```

#### Tính toán đại hạn
```python
# Nhập đại hạn
diaBan = diaBan.nhapDaiHan(cucSo, gioiTinh * amDuongChiNamSinh)

# Nhập tiểu hạn
diaBan = diaBan.nhapTieuHan(khoiHan, gioiTinh, chiNam)
```

## 🧪 Kiểm thử và chất lượng

### Chạy tests
```bash
# Chạy tất cả tests
python -m pytest tests/ -v

# Chạy tests với coverage
python -m pytest tests/ --cov=lasotuvi --cov-report=html

# Chạy tests cụ thể
python -m pytest tests/test_thienban.py -v
```

### Kiểm tra chất lượng code
```bash
# Format code với Black
black lasotuvi/ tests/

# Kiểm tra lỗi với Flake8
flake8 lasotuvi/ tests/

# Type checking với MyPy
mypy lasotuvi/
```

## 📁 Cấu trúc dự án

```
lasotuvi/
├── lasotuvi/           # Gói thư viện chính
│   ├── __init__.py    # Thông tin package
│   ├── App.py         # Logic ứng dụng chính
│   ├── AmDuong.py     # Tính toán Âm Dương
│   ├── DiaBan.py      # Cấu trúc lá số
│   ├── Sao.py         # Định nghĩa sao
│   ├── ThienBan.py    # Thiên bàn
│   ├── Lich_EPHEM.py  # Lịch thiên văn
│   └── Lich_HND.py    # Lịch Việt Nam
├── tests/             # Bộ kiểm thử
│   ├── test_diaban.py
│   ├── test_lich.py
│   └── test_thienban.py
├── docs/              # Tài liệu
│   ├── ANSAO.md
│   └── lich.md
├── requirements.txt    # Dependencies
├── setup.py          # Cấu hình package
├── README.md         # Tài liệu tiếng Anh
└── README_VI.md      # Tài liệu tiếng Việt
```

## 🛠️ Phát triển

### Thiết lập môi trường phát triển

1. **Fork repository**
   ```bash
   # Fork trên GitHub, sau đó clone
   git clone https://github.com/YOUR_USERNAME/lasotuvi.git
   cd lasotuvi
   ```

2. **Thiết lập môi trường**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # hoặc venv\Scripts\activate  # Windows
   pip install -e .
   pip install pytest black flake8 mypy
   ```

3. **Tạo nhánh mới**
   ```bash
   git checkout -b feature/tinh-nang-moi
   ```

4. **Thực hiện thay đổi và commit**
   ```bash
   # Thực hiện thay đổi
   git add .
   git commit -m "Thêm tính năng: mô tả ngắn gọn"
   git push origin feature/tinh-nang-moi
   ```

### Quy tắc phát triển

- **Code style**: Sử dụng Black để format code
- **Type hints**: Thêm type hints cho tất cả functions
- **Documentation**: Viết docstring cho tất cả functions
- **Tests**: Viết tests cho tính năng mới
- **Commit messages**: Sử dụng tiếng Việt hoặc tiếng Anh rõ ràng

### Các lĩnh vực có thể đóng góp

1. **🔧 Cải thiện thuật toán** - Tối ưu hóa tính toán sao
2. **⭐ Thêm sao mới** - Bổ sung các sao chưa có
3. **🌐 Giao diện người dùng** - Tạo CLI hoặc GUI
4. **🔌 API REST** - Tạo web API
5. **📚 Tài liệu** - Cải thiện documentation
6. **🧪 Tests** - Thêm unit tests và integration tests
7. **⚡ Performance** - Tối ưu hóa hiệu suất
8. **🌍 Internationalization** - Hỗ trợ đa ngôn ngữ

## 🔗 Dự án liên quan

- **[lasotuvi-django](https://github.com/doanguyen/lasotuvi-django)** - Ứng dụng web Django frontend cho lasotuvi
- **[lasotuvi-api](https://github.com/doanguyen/lasotuvi-api)** - REST API cho lasotuvi

## 📖 Video hướng dẫn

[![Tutorial](http://i.vimeocdn.com/video/717548888_640.jpg)](https://vimeo.com/283303258 "Tutorial")

## 🤝 Đóng góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng đọc hướng dẫn sau trước khi đóng góp:

### Quy trình đóng góp

1. **Fork repository** và clone về máy
2. **Tạo nhánh mới** cho tính năng/bug fix
3. **Thực hiện thay đổi** và viết tests
4. **Chạy tests** để đảm bảo không có lỗi
5. **Commit** với message rõ ràng
6. **Push** lên nhánh và tạo Pull Request
7. **Mô tả chi tiết** những thay đổi trong PR

### Báo cáo lỗi

Khi báo cáo lỗi, vui lòng cung cấp:
- Phiên bản Python và lasotuvi
- Mô tả lỗi chi tiết
- Code để reproduce lỗi
- Output lỗi (nếu có)

### Đề xuất tính năng

Khi đề xuất tính năng mới:
- Mô tả rõ ràng tính năng mong muốn
- Giải thích lý do tại sao cần tính năng này
- Đề xuất cách implement (nếu có thể)

## 📄 Giấy phép

Dự án này được cấp phép theo MIT License - xem file [LICENSE](LICENSE) để biết chi tiết.

## 👨‍💻 Tác giả

**doanguyen** - [dungnv2410@gmail.com](mailto:dungnv2410@gmail.com)

## 🙏 Lời cảm ơn

- Các bậc thầy và học giả tử vi truyền thống Việt Nam
- Cộng đồng mã nguồn mở vì nguồn cảm hứng và công cụ
- Những người đóng góp và sử dụng dự án lasotuvi
- Tất cả những ai đã ủng hộ và phát triển dự án này

---

**Lưu ý**: Thư viện này dành cho mục đích giáo dục và bảo tồn văn hóa. Tử vi Việt Nam là một thực hành văn hóa truyền thống và nên được tiếp cận với sự tôn trọng đối với ý nghĩa văn hóa của nó. 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
import uvicorn
import sys
import os
import re

# Thêm thư mục cha vào sys.path để import la_so_tu_vi
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from la_so_tu_vi import tao_la_so_tu_vi, tao_la_so_tu_vi_ngan_gon

# Tạo FastAPI app
app = FastAPI(
    title="Lá Số Tử Vi API",
    description="API để tạo lá số tử vi tổng hợp và ngắn gọn",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Pydantic models cho request/response
class LaSoTuViRequest(BaseModel):
    ngay: int = Field(..., ge=1, le=31, description="Ngày sinh (1-31)")
    thang: int = Field(..., ge=1, le=12, description="Tháng sinh (1-12)")
    nam: int = Field(..., ge=1900, le=2100, description="Năm sinh (1900-2100)")
    gio: int = Field(..., ge=0, le=23, description="Giờ sinh (0-23)")
    gioi_tinh: int = Field(..., description="Giới tính (1: Nam, -1: Nữ)")
    ten: str = Field(..., min_length=1, max_length=100, description="Họ tên")
    duong_lich: bool = Field(True, description="True nếu là dương lịch, False nếu âm lịch")
    time_zone: int = Field(7, ge=-12, le=14, description="Múi giờ (-12 đến 14)")

class CungInfo(BaseModel):
    cung_so: int
    ten_cung: str
    cung_ten: str
    chinh_tinh: List[str]
    phu_tinh: List[str]
    dac_biet: Optional[List[str]] = None

class ThongTinCaNhan(BaseModel):
    ho_ten: str
    ngay_sinh: str
    gio_sinh: str
    gioi_tinh: str
    can_chi_gio_sinh: str

class CanChi(BaseModel):
    can_chi_nam: str
    can_chi_thang: str
    can_chi_ngay: str
    can_chi_gio: str

class Menh(BaseModel):
    ban_menh: str
    menh_chu: str
    than_chu: str
    sinh_khac: str
    am_duong_menh: str

class Cuc(BaseModel):
    hanh_cuc: str
    ten_cuc: str

class LaSoTuViResponse(BaseModel):
    thong_tin_ca_nhan: ThongTinCaNhan
    can_chi: CanChi
    menh: Menh
    cuc: Cuc
    thap_nhi_cung: List[CungInfo]

class ThongTinCoBan(BaseModel):
    ho_ten: str
    ngay_sinh: str
    gio_sinh: str
    gioi_tinh: str

class MenhNganGon(BaseModel):
    ban_menh: str
    ten_cuc: str
    sinh_khac: str

class LaSoTuViNganGonResponse(BaseModel):
    thong_tin_co_ban: ThongTinCoBan
    menh: MenhNganGon
    can_chi: CanChi
    thap_nhi_cung: List[CungInfo]

# Utils: strip ANSI color codes from responses
ansi_escape = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

def _strip_ansi(text: str) -> str:
    if not isinstance(text, str):
        return text
    return ansi_escape.sub("", text)

def _clean_data(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: _clean_data(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_clean_data(v) for v in obj]
    if isinstance(obj, str):
        return _strip_ansi(obj)
    return obj

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Lá Số Tử Vi API",
        "version": "1.0.0",
        "endpoints": {
            "tổng hợp": "/la-so-tu-vi/tong-hop",
            "ngắn gọn": "/la-so-tu-vi/ngan-gon",
            "docs": "/docs"
        }
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API đang hoạt động bình thường"}

# Endpoint tạo lá số tử vi tổng hợp
@app.post("/la-so-tu-vi/tong-hop", response_model=LaSoTuViResponse)
async def tao_la_so_tu_vi_tong_hop(request: LaSoTuViRequest):
    """
    Tạo lá số tử vi tổng hợp với đầy đủ thông tin
    
    - **ngay**: Ngày sinh (1-31)
    - **thang**: Tháng sinh (1-12)  
    - **nam**: Năm sinh (1900-2100)
    - **gio**: Giờ sinh (0-23)
    - **gioi_tinh**: Giới tính (1: Nam, -1: Nữ)
    - **ten**: Họ tên
    - **duong_lich**: True nếu là dương lịch, False nếu âm lịch
    - **time_zone**: Múi giờ (-12 đến 14)
    """
    try:
        # Gọi hàm tạo lá số tử vi
        ket_qua = tao_la_so_tu_vi(
            ngay=request.ngay,
            thang=request.thang,
            nam=request.nam,
            gio=request.gio,
            gioiTinh=request.gioi_tinh,
            ten=request.ten,
            duongLich=request.duong_lich,
            timeZone=request.time_zone
        )
        
        if ket_qua is None:
            raise HTTPException(status_code=500, detail="Không thể tạo lá số tử vi")
        
        return _clean_data(ket_qua)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo lá số tử vi: {str(e)}")

# Endpoint tạo lá số tử vi ngắn gọn
@app.post("/la-so-tu-vi/ngan-gon", response_model=LaSoTuViNganGonResponse)
async def tao_la_so_tu_vi_ngan_gon(request: LaSoTuViRequest):
    """
    Tạo lá số tử vi ngắn gọn với thông tin cơ bản
    
    - **ngay**: Ngày sinh (1-31)
    - **thang**: Tháng sinh (1-12)  
    - **nam**: Năm sinh (1900-2100)
    - **gio**: Giờ sinh (0-23)
    - **gioi_tinh**: Giới tính (1: Nam, -1: Nữ)
    - **ten**: Họ tên
    - **duong_lich**: True nếu là dương lịch, False nếu âm lịch
    - **time_zone**: Múi giờ (-12 đến 14)
    """
    try:
        # Gọi hàm tạo lá số tử vi ngắn gọn
        ket_qua = tao_la_so_tu_vi_ngan_gon(
            ngay=request.ngay,
            thang=request.thang,
            nam=request.nam,
            gio=request.gio,
            gioiTinh=request.gioi_tinh,
            ten=request.ten,
            duongLich=request.duong_lich,
            timeZone=request.time_zone
        )
        
        if ket_qua is None:
            raise HTTPException(status_code=500, detail="Không thể tạo lá số tử vi ngắn gọn")
        
        return _clean_data(ket_qua)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi khi tạo lá số tử vi ngắn gọn: {str(e)}")

# Endpoint để test API
@app.get("/test")
async def test_api():
    """
    Test endpoint với dữ liệu mẫu
    """
    test_data = {
        "ngay": 7,
        "thang": 3,
        "nam": 2003,
        "gio": 6,
        "gioi_tinh": 1,
        "ten": "Nguyễn Văn A",
        "duong_lich": True,
        "time_zone": 7
    }
    
    return {
        "message": "Test data mẫu",
        "test_data": test_data,
        "endpoints": {
            "tổng hợp": "POST /la-so-tu-vi/tong-hop",
            "ngắn gọn": "POST /la-so-tu-vi/ngan-gon"
        }
    }

# Error handlers
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {
        "error": True,
        "message": exc.detail,
        "status_code": exc.status_code
    }

@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    return {
        "error": True,
        "message": f"Lỗi không xác định: {str(exc)}",
        "status_code": 500
    }

# Middleware để log requests
@app.middleware("http")
async def log_requests(request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response: {response.status_code}")
    return response

if __name__ == "__main__":
    # Chạy server với uvicorn
    uvicorn.run(
        "api_la_so_tu_vi:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

#!/usr/bin/env python3
"""
Script để chạy FastAPI server cho La So Tu Vi API
"""

import uvicorn
import sys
import os

# Thêm thư mục cha vào sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == "__main__":
    print("🚀 Khởi động La So Tu Vi API Server...")
    print("📍 Server sẽ chạy tại: http://localhost:8000")
    print("📚 Documentation: http://localhost:8000/docs")
    print("🔍 ReDoc: http://localhost:8000/redoc")
    print("=" * 50)
    
    # Chạy server
    uvicorn.run(
        "api_la_so_tu_vi:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

# Lasotuvi - Vietnamese Astrology (Tử vi) Library

[![Build Status](https://travis-ci.org/doanguyen/lasotuvi.svg?branch=master)](https://travis-ci.org/doanguyen/lasotuvi)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)

**Lasotuvi** is an open-source Python library for Vietnamese astrology (Tử vi) calculations. It provides comprehensive tools for creating and analyzing Vietnamese astrological charts based on traditional Vietnamese astrology principles.

## 🌟 Features

- **Complete Tử vi chart generation** - Create full Vietnamese astrological charts
- **Star placement calculations** - Accurate placement of all major and minor stars
- **Lunar calendar integration** - Support for both solar and lunar calendar systems
- **Time zone handling** - Proper time zone calculations for accurate chart generation
- **Comprehensive star system** - Includes all traditional Vietnamese astrological stars
- **Modern Python implementation** - Clean, well-documented codebase

## 📦 Installation

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Install from PyPI
```bash
pip install lasotuvi
```

### Install from source
```bash
git clone https://github.com/doanguyen/lasotuvi.git
cd lasotuvi
pip install -e .
```

## 🚀 Quick Start

```python
from lasotuvi.App import lapDiaBan
from lasotuvi.DiaBan import DiaBan

# Create a chart for a person born on:
# Date: 15th day, 3rd month, 1990
# Time: 14:30 (2:30 PM)
# Gender: Male (1 for male, 0 for female)
# Calendar: Solar calendar (True for solar, False for lunar)
# Timezone: UTC+7

diaBan = lapDiaBan(
    DiaBan, 
    nn=15,           # Day
    tt=3,            # Month  
    nnnn=1990,       # Year
    gioSinh=14.5,    # Birth hour (24-hour format)
    gioiTinh=1,      # Gender (1=male, 0=female)
    duongLich=True,  # Calendar type (True=solar, False=lunar)
    timeZone=7       # Timezone offset
)

# Access chart information
print(f"Life Palace: {diaBan.cungMenh}")
print(f"Career Palace: {diaBan.cungQuan}")
print(f"Wealth Palace: {diaBan.cungTai}")
```

## 📚 Documentation

### Core Components

- **`App.py`** - Main application logic for chart generation
- **`DiaBan.py`** - Chart structure and palace calculations
- **`AmDuong.py`** - Yin-Yang and Five Elements calculations
- **`Sao.py`** - Star placement and interpretation
- **`ThienBan.py`** - Heavenly chart calculations
- **`Lich_EPHEM.py`** - Ephemeris calculations
- **`Lich_HND.py`** - Vietnamese calendar conversions

### Key Functions

#### Chart Generation
```python
lapDiaBan(diaBan, nn, tt, nnnn, gioSinh, gioiTinh, duongLich, timeZone)
```
Generates a complete Tử vi chart with all stars and palaces.

#### Star Placement
```python
# Example: Place Tử vi star
viTriTuVi = timTuVi(cucSo, nn)
diaBan.nhapSao(viTriTuVi, saoTuVi)
```

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
python -m pytest tests/
```

## 📁 Project Structure

```
lasotuvi/
├── lasotuvi/           # Main library package
│   ├── __init__.py
│   ├── App.py         # Main application logic
│   ├── AmDuong.py     # Yin-Yang calculations
│   ├── DiaBan.py      # Chart structure
│   ├── Sao.py         # Star definitions
│   ├── ThienBan.py    # Heavenly chart
│   ├── Lich_EPHEM.py  # Ephemeris
│   └── Lich_HND.py    # Vietnamese calendar
├── tests/             # Test suite
├── docs/              # Documentation
├── requirements.txt    # Dependencies
└── setup.py          # Package configuration
```

## 🔗 Related Projects

- **[lasotuvi-django](https://github.com/doanguyen/lasotuvi-django)** - Django web application frontend for lasotuvi
- **[lasotuvi-api](https://github.com/doanguyen/lasotuvi-api)** - REST API for lasotuvi

## 📖 Tutorial Video

[![Tutorial](http://i.vimeocdn.com/video/717548888_640.jpg)](https://vimeo.com/283303258 "Tutorial")

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**doanguyen** - [dungnv2410@gmail.com](mailto:dungnv2410@gmail.com)

## 🙏 Acknowledgments

- Traditional Vietnamese astrology masters and scholars
- The open-source community for inspiration and tools
- Contributors and users of the lasotuvi project

---

**Note**: This library is for educational and cultural preservation purposes. Vietnamese astrology (Tử vi) is a traditional cultural practice and should be approached with respect for its cultural significance.

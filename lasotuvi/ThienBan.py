# -*- coding: utf-8 -*-
"""
(c) 2016 doanguyen <dungnv2410@gmail.com>.
"""
from lasotuvi.AmDuong import (canChiNgay, canChiGio, diaChi, ngayThangNam, ngayThangNamCanChi,
                     nguHanh, nguHanhNapAm, thienCan, timCuc, sinhKhac)
import time
from lasotuvi.Lich_HND import jdFromDate


class lapThienBan(object):
    def __init__(self, nn, tt, nnnn, gioSinh, gioiTinh, ten, diaBan,
                 duongLich=True, timeZone=7):
        super(lapThienBan, self).__init__()
        self.gioiTinh = 1 if gioiTinh == 1 else -1
        self.namNu = "Nam" if gioiTinh == 1 else "Nữ"

        self.timeZone = timeZone
        self.today = time.strftime("%d/%m/%Y")
        self.ngayDuong, self.thangDuong, self.namDuong, self.ten = \
            nn, tt, nnnn, ten
        if duongLich is True:
            self.ngayAm, self.thangAm, self.namAm, self.thangNhuan = \
                ngayThangNam(self.ngayDuong, self.thangDuong, self.namDuong,
                             True, self.timeZone)
        else:
            self.ngayAm, self.thangAm, self.namAm = self.ngayDuong,\
                self.thangDuong, self.namDuong

        self.canNgay, self.chiNgay, self.canThang, self.chiThang, self.canNam, self.chiNam = \
            ngayThangNamCanChi(self.ngayAm, self.thangAm,
                               self.namAm, False, self.timeZone)

        self.canNgayTen = thienCan[self.canNgay]['tenCan']
        self.chiNgayTen = diaChi[self.chiNgay]['tenChi']
        self.canThangTen = thienCan[self.canThang]['tenCan']
        self.chiThangTen = diaChi[self.chiThang]['tenChi']
        self.canNamTen = thienCan[self.canNam]['tenCan']
        self.chiNamTen = diaChi[self.chiNam]['tenChi']

        
        canGioSinh, chiGioSinh = canChiGio(self.canNgay, gioSinh)
        if canGioSinh == 0:
            canGioSinh = 10
        chiGioSinh = diaChi[chiGioSinh]
        canGioSinh = thienCan[canGioSinh]
        
        self.chiGioSinh = chiGioSinh
        self.canGioSinh = canGioSinh
        self.gioSinh = "{} {}".format(canGioSinh['tenCan'],
                                      chiGioSinh['tenChi'])         

        cungAmDuong = 1 if (diaBan.cungMenh % 2 == 1) else -1
        self.amDuongNamSinh = "Dương" if (self.chiNam % 2 == 1) else "Âm"
        if (cungAmDuong * self.gioiTinh == 1):
            self.amDuongMenh = "Âm dương thuận lý"
        else:
            self.amDuongMenh = "Âm dương nghịch lý"

        cuc = timCuc(diaBan.cungMenh, self.canNam)
        self.hanhCuc = nguHanh(cuc)['id']
        self.tenCuc = nguHanh(cuc)['tenCuc']

        self.menhChu = diaChi[self.chiNam]['menhChu']
        self.thanChu = diaChi[self.chiNam]['thanChu']

        self.menh = nguHanhNapAm(self.chiNam, self.canNam)
        menhId = nguHanh(self.menh)['id']
        menhCuc = sinhKhac(menhId, self.hanhCuc)
        if menhCuc == 1:
            self.sinhKhac = "Bản Mệnh sinh Cục"
        elif menhCuc == -1:
            self.sinhKhac = "Bản Mệnh khắc Cục"
        elif menhCuc == -1j:
            self.sinhKhac = "Cục khắc Bản Mệnh"
        elif menhCuc == 1j:
            self.sinhKhac = "Cục sinh Bản mệnh"
        else:
            self.sinhKhac = "Cục hòa Bản Mệnh"

        self.banMenh = nguHanhNapAm(self.chiNam, self.canNam, True)

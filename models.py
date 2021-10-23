from datetime import datetime

from flask_login import UserMixin
from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer,
                        String, func, or_)
from sqlalchemy.orm import relationship

from __init__ import db

class KhachHang(db.Model):
    __tablename__ = 'KhachHang'
    id = Column(Integer, primary_key=True, autoincrement=True)
    HoTenKH = Column(String(30), nullable=False)
    GioiTinh = Column(String(3), default="Nam")
    NamSinh = Column(Integer, nullable=False)
    SDT = Column(String(10), nullable=False, unique=True)
    CMND = Column(String(7), nullable=False, unique=True)
    HinhAnh = Column(String(100), nullable = True)
    Email = Column(String(100), nullable = False)

    ve = relationship("Ve", backref="khachhang", lazy = True)

    def __str__(self):
        return self.HoTenKH

class SanBay(db.Model):
    __tablename__ = 'SanBay'
    id = Column(Integer, primary_key=True, autoincrement=True)
    TenSB = Column(String(30), default="NoiBai", nullable=False)
    DiaChi = Column(String(100), default="TP. HoChiMinh", nullable=False)

    chuyenbay_di = relationship("ChuyenBay", backref = "sanbay_di", lazy = True, foreign_keys='ChuyenBay.Id_SanBay_Di')
    chuyenbay_den = relationship("ChuyenBay", backref= "sanbay_den", lazy = True, foreign_keys='ChuyenBay.Id_SanBay_Den')
    trunggian = relationship("TrungGianChuyenBay", backref= "sanbay_trunggian", lazy = True)

    def __str__(self):
        return self.TenSB

class MayBay(db.Model):
    __tablename__ = 'MayBay'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Ten = Column(String(30), default = "Boing 737", nullable=False)
    Hang = Column(String(30), default= "VietNamAirLine", nullable=False)
    TinhTrang = Column(Boolean, default=True)

    chuyenbay = relationship("ChuyenBay", backref = "maybay", lazy = True)

    def __str__(self):
        return self.Ten

class ChuyenBay(db.Model):
    __tablename__ = 'ChuyenBay'
    id  = Column(Integer, primary_key=True, autoincrement=True)
    Id_MayBay = Column(Integer, ForeignKey(MayBay.id, ondelete = "CASCADE"), nullable=False)
    Id_SanBay_Di = Column(Integer, ForeignKey(SanBay.id), nullable=False)
    Id_SanBay_Den = Column(Integer, ForeignKey(SanBay.id), nullable=False)
    ThoiGianXuatPhat = Column(DateTime, default = datetime.now())
    ThoiGianBay = Column(Integer, default = 2, nullable=False)
    SoLuongChoNgoi = Column(Integer, default = 30, nullable=False)

    trunggian = relationship("TrungGianChuyenBay", backref="chuyenbay", lazy = True)
    ve = relationship("Ve", backref= "chuyenbay", lazy = True)
    banggia = relationship("BangGiaVe", backref="chuyenbay", lazy = True)


class TrungGianChuyenBay(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    Id_SanBay = Column(Integer, ForeignKey(SanBay.id, ondelete = "CASCADE"), nullable = False)
    Id_ChuyenBay = Column(Integer, ForeignKey(ChuyenBay.id, ondelete = "CASCADE"), nullable=False)
    ThoiGianDung = Column(Integer, default = 0)
    GhiChu = Column(String(100), nullable=True)

class Ve(db.Model):
    __tablename__ = 'Ve'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Id_ChuyenBay = Column(Integer, ForeignKey(ChuyenBay.id, ondelete = "CASCADE"), nullable=False)
    Id_KhachHang = Column(Integer, ForeignKey(KhachHang.id), nullable=False)
    ThoiGianDatVe = Column(DateTime, default = datetime.now(), nullable=False)
    HangVe = Column(String(10), default = "Thuong", nullable=False)

class BangGiaVe(db.Model):
    __tablename__ = 'BangGiaVe'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Id_ChuyenBay = Column(Integer, ForeignKey(ChuyenBay.id, ondelete = "CASCADE"), nullable = False)
    HangVe = Column(String(10), default = "Thuong", nullable=False)
    GiaVe = Column(Float, default = 500000, nullable=False)
    SoGhe = Column(Integer, nullable=True)


class DoanhThuThang(db.Model):
    __tablename__ = 'DoanhThuThang'
    id = Column(Integer, primary_key=True, autoincrement=True)
    TyLe = Column(Float)
    DoanhThu = Column(Float)
    Id_ChuyenBay = Column(Integer, ForeignKey(ChuyenBay.id), nullable=True)
    SoVeBanDuoc = Column(Integer)
    Thang = Column(Integer, default = datetime.now().month)
    Nam = Column(Integer, default = datetime.now().year)

class DoanhThuNam(db.Model):
    __tablename__ = 'DoanhThuNam'
    id = Column(Integer, primary_key=True, autoincrement=True)
    TyLe = Column(Float)
    DoanhThu = Column(Float)
    Nam = Column(Integer, default = datetime.now().year)
    SoChuyenBay = Column(Integer)

class NguoiDung(db.Model, UserMixin):
    __tablename__ = 'NguoiDung'
    id = Column(Integer, primary_key=True, autoincrement=True)
    TenDN = Column(String(10) , nullable=False, unique=True)
    MatKhau = Column(String(100), nullable=False)
    VaiTro = Column(String(1), nullable=False)
    TenNguoiDung = Column(String(30), nullable=False)

    def __str__(self):
        return self.TenDN
# class QuyDinh(db.Model):
#     __tablename__ = 'QuyDinh'
#     TGDatVeTreNhat = Column(Integer)
#     TGHuyVeTreNhat = Column(Integer)
#     SoLuongSanBay = Column(Integer)
#     TGBayToiThieu = Column(Integer)
#     SanBayTGToiDa = Column(Integer)
#     TGDungToiThieu = Column(Integer)
#     TGDungToiDa = Column(Integer)

if __name__ == '__main__':
    db.create_all()

    # user = NguoiDung(TenDN = "admin", MatKhau = "123", VaiTro = "A", TenNguoiDung= "TuanNguyen")
    # db.session.add(user)
    # db.session.commit()

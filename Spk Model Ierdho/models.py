from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class HuaweiPhone(Base):
    __tablename__ = "huaweiphone"

    nama_produk : Mapped[str] = mapped_column(primary_key=True)
    layar : Mapped[str]
    prosesor : Mapped[str]
    ram : Mapped[int]
    penyimpanan : Mapped[int]
    kamera_belakang : Mapped[int]
    kamera_depan : Mapped[int]
    baterai : Mapped[int]
    harga : Mapped[int]

    def __repr__(self) -> str :
        return f"nama_produk={self.nama_produk}, layar={self.layar}, prosesor={self.prosesor}, ram={self.ram}, penyimpanan={self.penyimpanan}, kamera_belakang={self.kamera_belakang}, kamera_depan={self.kamera_depan}, baterai={self.baterai}, harga={self.harga}"


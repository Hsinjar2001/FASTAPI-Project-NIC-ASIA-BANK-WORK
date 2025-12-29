import enum
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum as SQLEnum
from sqlalchemy.sql import func
from database import Base


class StatusEnum(str, enum.Enum):
    completed = "completed"
    pending = "pending"
    cancelled = "cancelled"


class DeviceTypeEnum(str, enum.Enum):
    desktop = "desktop"
    tablet = "tablet"
    phone = "phone"


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    # ✅ Now actually uses the enum
    status = Column(
        SQLEnum(StatusEnum, name="status_enum", create_constraint=True),
        nullable=False,
        default=StatusEnum.pending
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Sales(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    sale_date = Column(DateTime(timezone=True), server_default=func.now())
    # ✅ Now actually uses the enum
    status = Column(
        SQLEnum(StatusEnum, name="sales_status_enum", create_constraint=True),
        nullable=False,
        default=StatusEnum.completed
    )


class Traffic(Base):
    __tablename__ = "traffic"

    id = Column(Integer, primary_key=True, index=True)
    # ✅ Now actually uses the enum
    device_type = Column(
        SQLEnum(DeviceTypeEnum, name="device_type_enum", create_constraint=True),
        nullable=False
    )
    visits = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
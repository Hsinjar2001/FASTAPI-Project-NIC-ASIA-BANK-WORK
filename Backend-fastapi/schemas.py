from pydantic import BaseModel, Field
from typing import Optional


class MetricItem(BaseModel):
    value: str
    change: Optional[str] = None
    changeText: Optional[str] = None
    isPositive: Optional[bool] = None
    progress: Optional[float] = None

    class Config:
        from_attributes = True  # ✅ For SQLAlchemy 2.0 compatibility


class DashboardMetrics(BaseModel):
    budget: MetricItem
    customers: MetricItem
    taskProgress: MetricItem
    profit: MetricItem


class SalesData(BaseModel):
    month: str
    sales: float = Field(..., ge=0)  # ✅ Sales can't be negative

    class Config:
        from_attributes = True


class TrafficData(BaseModel):
    name: str
    value: float = Field(..., ge=0, le=100)  # ✅ Percentage between 0-100

    class Config:
        from_attributes = True
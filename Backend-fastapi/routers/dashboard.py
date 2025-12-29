from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from database import get_db
from models import Budget, Customer, Task, Sales, Traffic, StatusEnum, DeviceTypeEnum
from schemas import DashboardMetrics, SalesData, TrafficData, MetricItem
router = APIRouter(prefix="/api/dashboard", tags=["Dashboard"])


@router.get("/metrics", response_model=DashboardMetrics)
async def get_dashboard_metrics(db: Session = Depends(get_db)):
    """Get all dashboard metrics"""
    try:
        # Budget metrics
        budget_total = db.query(func.sum(Budget.amount)).scalar()
        budget_total = budget_total if budget_total is not None else 24000
        budget_change = 12.0

        # Customer metrics
        customer_count = db.query(func.count(Customer.id)).scalar()
        customer_count = customer_count if customer_count is not None else 1600
        customer_change = -16.0

        # Task progress
        total_tasks = db.query(func.count(Task.id)).scalar() or 0
        # ✅ Now uses enum
        completed_tasks = db.query(func.count(Task.id)).filter(
            Task.status == StatusEnum.completed
        ).scalar() or 0
        task_progress = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 75.5

        # Profit
        # ✅ Now uses enum
        total_profit = db.query(func.sum(Sales.amount)).filter(
            Sales.status == StatusEnum.completed
        ).scalar()
        total_profit = total_profit if total_profit is not None else 15000

        return DashboardMetrics(
            budget=MetricItem(
                value=f"${int(budget_total/1000)}k",
                change=f"+{int(budget_change)}%" if budget_change > 0 else f"{int(budget_change)}%",
                changeText="Since last month",
                isPositive=budget_change > 0
            ),
            customers=MetricItem(
                value=f"{customer_count/1000:.1f}k",
                change=f"+{int(customer_change)}%" if customer_change > 0 else f"{int(customer_change)}%",
                changeText="Since last month",
                isPositive=customer_change > 0
            ),
            taskProgress=MetricItem(
                value=f"{task_progress:.1f}%",
                progress=round(task_progress, 1)
            ),
            profit=MetricItem(
                value=f"${int(total_profit/1000)}k"
            )
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching metrics: {str(e)}")

@router.get("/sales", response_model=list[SalesData])
async def get_sales_data(db: Session = Depends(get_db)):
    """Get monthly sales data"""
    try:
        sales_data = db.query(
            func.to_char(Sales.sale_date, 'Mon').label('month'),
            func.sum(Sales.amount).label('sales')
        ).filter(
            Sales.status == StatusEnum.completed  # ✅ Now uses enum
        ).group_by(
            func.to_char(Sales.sale_date, 'Mon'),
            extract('month', Sales.sale_date)
        ).order_by(
            extract('month', Sales.sale_date)
        ).all()

        if not sales_data:
            # Default data
            return [
                SalesData(month="Jan", sales=15000),
                SalesData(month="Feb", sales=18000),
                SalesData(month="Mar", sales=12000),
                SalesData(month="Apr", sales=14000),
                SalesData(month="May", sales=10000),
                SalesData(month="Jun", sales=16000),
                SalesData(month="Jul", sales=15500),
                SalesData(month="Aug", sales=17000),
                SalesData(month="Sep", sales=19000),
                SalesData(month="Oct", sales=20000),
                SalesData(month="Nov", sales=18500),
                SalesData(month="Dec", sales=21000)
            ]

        return [SalesData(month=row.month, sales=float(row.sales)) for row in sales_data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching sales data: {str(e)}")


@router.get("/traffic", response_model=list[TrafficData])
async def get_traffic_data(db: Session = Depends(get_db)):
    """Get traffic source data"""
    try:
        total_visits = db.query(func.sum(Traffic.visits)).scalar() or 0

        traffic_data = db.query(
            Traffic.device_type,
            func.sum(Traffic.visits).label('visits')
        ).group_by(Traffic.device_type).all()

        if not traffic_data or total_visits == 0:
            return [
                TrafficData(name="Desktop", value=63.0),
                TrafficData(name="Tablet", value=15.0),
                TrafficData(name="Phone", value=23.0)
            ]

        return [
            TrafficData(
                name=row.device_type.value.capitalize(),  # ✅ Access enum value
                value=round((row.visits / total_visits * 100), 1)
            )
            for row in traffic_data
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching traffic data: {str(e)}")
import React from 'react';
import Chart from 'react-apexcharts';
import './SalesChart.css';

const SalesChart = () => {
  const options = {
    chart: {
      type: 'bar',
      height: 350,
      toolbar: {
        show: false
      },
      fontFamily: 'Inter, sans-serif'
    },
    plotOptions: {
      bar: {
        borderRadius: 8,
        columnWidth: '60%',
      }
    },
    dataLabels: {
      enabled: false
    },
    colors: ['#6366f1'],
    grid: {
      borderColor: '#e5e7eb',
      strokeDashArray: 3,
    },
    xaxis: {
      categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      axisBorder: {
        show: false
      },
      axisTicks: {
        show: false
      },
      labels: {
        style: {
          colors: '#6b7280',
          fontSize: '12px'
        }
      }
    },
    yaxis: {
      labels: {
        style: {
          colors: '#6b7280',
          fontSize: '12px'
        },
        formatter: function (value) {
          return value / 1000 + 'K';
        }
      }
    },
    tooltip: {
      theme: 'dark',
      y: {
        formatter: function (value) {
          return '$' + value;
        }
      }
    }
  };

  const series = [{
    name: 'Sales',
    data: [15000, 18000, 12000, 14000, 10000, 16000, 15500, 17000, 19000, 20000, 18500, 21000]
  }];

  return (
    <div className="sales-chart">
      <div className="chart-header">
        <h3>Sales</h3>
        <button className="sync-button">
          <span>🔄</span> Sync
        </button>
      </div>
      <Chart options={options} series={series} type="bar" height={350} />
    </div>
  );
};

export default SalesChart;
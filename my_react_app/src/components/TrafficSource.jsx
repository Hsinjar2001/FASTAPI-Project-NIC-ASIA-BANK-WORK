import React from 'react';
import Chart from 'react-apexcharts';
import './TrafficSource.css';

const TrafficSource = () => {
  const options = {
    chart: {
      type: 'donut',
      fontFamily: 'Inter, sans-serif'
    },
    labels: ['Desktop', 'Tablet', 'Phone'],
    colors: ['#6366f1', '#10b981', '#f59e0b'],
    dataLabels: {
      enabled: false
    },
    legend: {
      show: false
    },
    plotOptions: {
      pie: {
        donut: {
          size: '70%',
          labels: {
            show: false
          }
        }
      }
    },
    stroke: {
      width: 2,
      colors: ['#fff']
    },
    tooltip: {
      theme: 'dark',
      y: {
        formatter: function (value) {
          return value + '%';
        }
      }
    }
  };

  const series = [45, 20, 35];

  return (
    <div className="traffic-source">
      <h3>Traffic Source</h3>
      <Chart options={options} series={series} type="donut" height={250} />
    </div>
  );
};

export default TrafficSource;
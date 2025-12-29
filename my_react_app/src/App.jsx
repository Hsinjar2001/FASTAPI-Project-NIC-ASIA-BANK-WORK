import React, { useState } from 'react';
import './App.css';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import MetricCard from './components/MetricCard';
import SalesChart from './components/SalesChart';
import TrafficSource from './components/TrafficSource';
import DeviceStats from './components/DeviceStats';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <div className="app">
      <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSidebar} />
      <div className="main-content">
        <Header toggleSidebar={toggleSidebar} />
        <div className="dashboard-content">
          <div className="metrics-row">
            <MetricCard 
              title="BUDGET"
              value="$24k"
              change="+12%"
              changeText="Since last month"
              isPositive={true}
              iconColor="#EF4444"
            />
            <MetricCard 
              title="TOTAL CUSTOMERS"
              value="1.6k"
              change="-16%"
              changeText="Since last month"
              isPositive={false}
              iconColor="#10B981"
            />
            <MetricCard 
              title="TASK PROGRESS"
              value="75.5%"
              progress={75.5}
              iconColor="#F59E0B"
            />
            <MetricCard 
              title="TOTAL PROFIT"
              value="$15k"
              iconColor="#6366F1"
            />
          </div>

          <div className="charts-row">
            <SalesChart />
            <div className="right-section">
              <TrafficSource />
              <DeviceStats />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
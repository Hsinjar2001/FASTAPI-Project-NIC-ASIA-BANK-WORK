import React from 'react';
import './DeviceStats.css';

const DeviceStats = () => {
  const devices = [
    { icon: '🖥️', name: 'Desktop', percentage: 63 },
    { icon: '📱', name: 'Tablet', percentage: 15 },
    { icon: '📞', name: 'Phone', percentage: 23 },
  ];

  return (
    <div className="device-stats">
      {devices.map((device, index) => (
        <div key={index} className="device-item">
          <div className="device-icon">{device.icon}</div>
          <div className="device-info">
            <p className="device-name">{device.name}</p>
            <div className="device-bar-container">
              <div 
                className="device-bar" 
                style={{ width: `${device.percentage}%` }}
              ></div>
            </div>
          </div>
          <span className="device-percentage">{device.percentage}%</span>
        </div>
      ))}
    </div>
  );
};

export default DeviceStats;
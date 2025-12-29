import React from 'react';
import './MetricCard.css';

const MetricCard = ({ title, value, change, changeText, isPositive, progress, iconColor }) => {
  return (
    <div className="metric-card">
      <div className="metric-header">
        <div className="metric-info">
          <p className="metric-title">{title}</p>
          <h2 className="metric-value">{value}</h2>
          {change && (
            <div className="metric-change">
              <span className={`change-indicator ${isPositive ? 'positive' : 'negative'}`}>
                {isPositive ? '↑' : '↓'} {change}
              </span>
              <span className="change-text">{changeText}</span>
            </div>
          )}
          {progress !== undefined && (
            <div className="progress-bar-container">
              <div className="progress-bar" style={{ width: `${progress}%` }}></div>
            </div>
          )}
        </div>
        <div className="metric-icon" style={{ backgroundColor: iconColor }}>
          {title.includes('BUDGET') && '💰'}
          {title.includes('CUSTOMERS') && '👥'}
          {title.includes('PROGRESS') && '📋'}
          {title.includes('PROFIT') && '💵'}
        </div>
      </div>
    </div>
  );
};

export default MetricCard;
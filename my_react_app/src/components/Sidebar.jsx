import React from 'react';
import './Sidebar.css';

const Sidebar = ({ isOpen, toggleSidebar }) => {
  const menuItems = [
    { icon: '📊', label: 'Overview', active: true },
    { icon: '👥', label: 'Customers', active: false },
    { icon: '🏢', label: 'Companies', active: false },
    { icon: '👤', label: 'Account', active: false },
    { icon: '⚙️', label: 'Settings', active: false },
    { icon: '🔐', label: 'Login', active: false },
    { icon: '📝', label: 'Register', active: false },
    { icon: '⚠️', label: 'Error', active: false },
  ];

  return (
    <>
      {/* Overlay for mobile */}
      <div 
        className={`sidebar-overlay ${isOpen ? 'active' : ''}`} 
        onClick={toggleSidebar}
      ></div>
      
      <div className={`sidebar ${isOpen ? 'open' : ''}`}>
        <div className="sidebar-header">
          <div className="brand-container">
            <div className="logo">💎</div>
            <div className="brand-info">
              <h3>Devias</h3>
              <p>Production</p>
            </div>
          </div>
          <button className="close-btn" onClick={toggleSidebar}>
            ✕
          </button>
        </div>

        <nav className="sidebar-nav">
          {menuItems.map((item, index) => (
            <div 
              key={index} 
              className={`nav-item ${item.active ? 'active' : ''}`}
            >
              <span className="nav-icon">{item.icon}</span>
              <span className="nav-label">{item.label}</span>
            </div>
          ))}
        </nav>

        <div className="sidebar-footer">
          <p>Need more features?</p>
          <a href="#pro">Check out our Pro solution template.</a>
        </div>
      </div>
    </>
  );
};

export default Sidebar;
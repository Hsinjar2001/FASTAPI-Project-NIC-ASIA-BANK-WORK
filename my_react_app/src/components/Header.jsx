import React from 'react';
import './Header.css';

const Header = ({ toggleSidebar }) => {
  return (
    <header className="header">
      <div className="header-left">
        <button className="hamburger-menu" onClick={toggleSidebar}>
          <span></span>
          <span></span>
          <span></span>
        </button>
        <div className="search-container">
          <span className="search-icon">🔍</span>
          <input type="text" placeholder="Search..." className="search-input" />
        </div>
      </div>
      
      <div className="header-actions">
        <button className="icon-button">
          <span className="icon">👥</span>
        </button>
        <button className="icon-button notification">
          <span className="icon">🔔</span>
          <span className="badge"></span>
        </button>
        <div className="user-avatar">
          <img src="https://i.pravatar.cc/150?img=12" alt="User" />
        </div>
      </div>
    </header>
  );
};

export default Header;
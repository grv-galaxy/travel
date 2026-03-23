<style scoped>
.admin-header {
  background: rgba(12, 12, 12, 0.98);
  backdrop-filter: blur(15px);
  border-bottom: 1px solid rgba(197, 160, 89, 0.15);
  height: 70px;
  position: sticky;
  top: 0;
  z-index: 1000;
  width: 100%;
}

.header-container {
  max-width: 100%;
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 1.5rem;
}

/* Left Section */
.header-left {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.brand-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.brand-logo-img {
  height: 40px;
  width: auto;
  object-fit: contain;
}

.brand-text h1 {
  color: #fff;
  font-size: 1.2rem;
  font-weight: 700;
  margin: 0;
  letter-spacing: 0.5px;
  font-family: 'Playfair Display', serif;
}

.brand-text p {
  color: #c5a059;
  font-size: 0.6rem;
  text-transform: uppercase;
  margin: 0;
  letter-spacing: 2px;
  font-weight: 600;
}

.divider {
  width: 1px;
  height: 24px;
  background: rgba(255, 255, 255, 0.1);
}

.breadcrumbs {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  font-size: 0.8rem;
}

.bc-item { color: #666; transition: 0.3s; }
.bc-item.active { color: #c5a059; font-weight: 600; }
.separator { font-size: 0.6rem; color: #333; }

/* Right Section */
.header-right {
  display: flex;
  align-items: center;
  gap: 1.5rem;
}

.search-bar {
  background: rgba(255, 255, 255, 0.03);
  border-radius: 100px;
  padding: 0.6rem 1.2rem;
  display: flex;
  align-items: center;
  gap: 0.8rem;
  border: 1px solid rgba(255, 255, 255, 0.08);
  width: 280px;
  transition: all 0.3s ease;
}

.search-bar.is-focused {
  background: rgba(197, 160, 89, 0.05);
  border-color: rgba(197, 160, 89, 0.4);
  width: 320px;
}

.search-bar i { color: #555; font-size: 0.9rem; }
.search-bar input {
  background: none;
  border: none;
  color: #fff;
  font-size: 0.85rem;
  width: 100%;
}
.search-bar input:focus { outline: none; }

.action-icons { display: flex; gap: 0.5rem; }

.icon-btn {
  background: rgba(255,255,255,0.03);
  border: none;
  color: #888;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  cursor: pointer;
  position: relative;
  transition: 0.3s;
  display: grid;
  place-items: center;
}

.icon-btn:hover { color: #c5a059; background: rgba(197, 160, 89, 0.1); }

.notification-badge {
  position: absolute;
  top: 10px;
  right: 10px;
  width: 6px;
  height: 6px;
  background: #ff4d4d;
  border-radius: 50%;
  box-shadow: 0 0 10px #ff4d4d;
}

/* Admin Profile */
.admin-profile-wrapper { position: relative; }

.admin-profile {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  cursor: pointer;
  padding: 0.4rem;
  border-radius: 50px;
  transition: 0.3s;
}

.profile-info { text-align: right; }
.admin-name { display: block; color: #fff; font-size: 0.8rem; font-weight: 600; }
.admin-role { color: #c5a059; font-size: 0.65rem; font-weight: 700; text-transform: uppercase; }

.avatar { position: relative; }
.avatar img {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1.5px solid rgba(197, 160, 89, 0.5);
}

.online-status {
  position: absolute;
  bottom: 2px;
  right: 2px;
  width: 10px;
  height: 10px;
  background: #00ff88;
  border: 2px solid #0c0c0c;
  border-radius: 50%;
}

/* Dropdown styling same as desktop */
.profile-dropdown {
  position: absolute;
  top: 120%;
  right: 0;
  background: #161616;
  border: 1px solid rgba(197, 160, 89, 0.2);
  width: 220px;
  border-radius: 12px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.6);
  padding: 0.5rem;
  transform-origin: top right;
}

.dropdown-header {
  padding: 0.8rem 1rem;
  border-bottom: 1px solid rgba(255,255,255,0.05);
  margin-bottom: 0.5rem;
}
.dropdown-header p { font-size: 0.7rem; color: #666; margin: 0; }
.dropdown-header strong { font-size: 0.8rem; color: #c5a059; }

.profile-dropdown a, .logout-btn {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 0.7rem 1rem;
  color: #aaa;
  text-decoration: none;
  font-size: 0.85rem;
  border-radius: 8px;
  transition: 0.2s;
  width: 100%;
  background: none;
  border: none;
  cursor: pointer;
}

.profile-dropdown a:hover { background: rgba(197, 160, 89, 0.1); color: #fff; }
.dropdown-divider { height: 1px; background: rgba(255,255,255,0.05); margin: 0.5rem 0; }
.logout-btn { color: #ff4d4d; }
.logout-btn:hover { background: rgba(255, 77, 77, 0.1); }

.dropdown-slide-enter-active, .dropdown-slide-leave-active {
  transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
}
.dropdown-slide-enter-from, .dropdown-slide-leave-to {
  opacity: 0;
  transform: translateY(-10px) scale(0.95);
}

/* --- SMALL SCREEN OVERRIDES --- */
@media (max-width: 768px) {
  .header-container {
    padding: 0 1rem;
  }
  
  .hide-mobile {
    display: none !important;
  }

  .brand-text h1 {
    font-size: 1.1rem;
  }

  .header-right {
    gap: 0.8rem;
  }

  /* Search bar becomes a circle icon on mobile */
  .search-bar {
    width: 38px;
    height: 38px;
    padding: 0;
    justify-content: center;
    border-radius: 50%;
  }

  .search-bar input {
    display: none;
  }

  /* If clicked/focused on mobile, it can expand or you can trigger a modal */
  .search-bar.is-focused {
    width: 180px;
    border-radius: 100px;
    padding: 0 1rem;
    position: absolute;
    right: 1.5rem;
    background: #1a1a1a;
    z-index: 10;
  }
  
  .search-bar.is-focused input {
    display: block;
  }

  .admin-profile {
    padding: 0;
  }
}
</style>
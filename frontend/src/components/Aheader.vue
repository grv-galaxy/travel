<template>
  <header class="admin-header">
    <div class="header-container">
      
      <div class="header-left">
        <div class="brand-section">
          <img src="../assets/images/LOGO.jpg" alt="Indoria Logo" class="brand-logo-img" />
          <div class="brand-text">
            <h1>Indoria</h1>
            <p>Admin Control</p>
          </div>
        </div>
        
        <div class="divider hide-mobile"></div>

        <nav class="breadcrumbs hide-mobile">
          <span class="bc-item">Dashboard</span>
          <i class="fa-solid fa-chevron-right separator"></i>
          <span class="bc-item active">{{ currentPage }}</span>
        </nav>
      </div>

      <div class="header-right">
        <div class="search-bar" :class="{ 'is-focused': isSearchFocused }">
          <i class="fa-solid fa-magnifying-glass"></i>
          <input 
            type="text" 
            placeholder="Search VIPs, Fleet..." 
            @focus="isSearchFocused = true"
            @blur="isSearchFocused = false"
          />
        </div>

        <!-- <div class="action-icons">
          <button class="icon-btn" title="System Notifications">
            <i class="fa-solid fa-bell"></i>
            <span class="notification-badge"></span>
          </button>
        </div> -->

        <div class="notification-wrapper" ref="notifRef">
          <button class="icon-btn" @click="toggleNotifications" title="System Alerts">
            <i class="fa-solid fa-bell"></i>
            <span v-if="unreadCount > 0" class="notification-badge animate-pulse"></span>
          </button>

          <transition name="dropdown-slide">
            <div v-if="showNotifDropdown" class="notif-dropdown shadow-premium">
              <div class="dropdown-header">
                <span class="text-white font-bold uppercase text-[10px] tracking-widest">Recent Alerts</span>
                <button @click="unreadCount = 0" class="text-[#c5a059] text-[9px] font-bold uppercase">Mark Read</button>
              </div>
              <div class="notif-list">
                <div v-for="n in recentNotifs" :key="n.id" class="notif-item">
                  <div class="n-icon" :class="n.type">
                    <i :class="n.icon"></i>
                  </div>
                  <div class="n-text">
                    <p class="text-white font-bold text-xs">{{ n.title }}</p>
                    <span class="text-slate-500 text-[10px]">{{ n.time }}</span>
                  </div>
                </div>
              </div>
            </div>
          </transition>
        </div>

        <div class="admin-profile-wrapper" ref="dropdownRef">
          <div class="admin-profile" @click="toggleDropdown">
            <div class="profile-info hide-mobile">
              <span class="admin-name">{{ adminData.username }}</span>
              <span class="admin-role">{{ adminData.role }}</span>
            </div>
            <div class="avatar">
              <img :src="`https://ui-avatars.com/api/?name=${adminData.username}&background=c5a059&color=fff`" alt="Admin" />
              <div class="online-status"></div>
            </div>
          </div>
          
          <transition name="dropdown-slide">
            <div v-if="showDropdown" class="profile-dropdown">
              <div class="dropdown-header">
                <p>Logged in as</p>
                <strong>{{adminData.email}}</strong>
              </div>
              <router-link to="/asecurity" @click="showDropdown = false">
                <i class="fa-solid fa-user-shield"></i> Security Settings
              </router-link>
              <router-link to="/asystemlog" @click="showDropdown = false">
                <i class="fa-solid fa-clock-rotate-left"></i> System Logs
              </router-link>
              <div class="dropdown-divider"></div>
              <button @click="triggerLogout" class="logout-btn">
                <i class="fa-solid fa-arrow-right-from-bracket"></i> Sign Out
              </button>
            </div>
          </transition>
        </div>
      </div>
    </div>
    <ConfirmModal
      :show="showLogoutConfirm"
      title="Confirm Logout"
      message="Are you sure you want to logout?"
      @confirm="handleLogout"
      @cancel="showLogoutConfirm = false"
    />
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import Anotification from './Anotification.vue';
import { useRouter } from 'vue-router';
import ConfirmModal from './ConfirmModal.vue';


const router =useRouter();
const props = defineProps({
  currentPage: {
    type: String,
    default: 'Overview'
  }
});

const showDropdown = ref(false);
const showNotifDropdown = ref(false);
const isSearchFocused = ref(false);
const unreadCount = ref(3); // Example unread notifications count
const notifRef = ref(null);
const toastRef = ref(null);
const dropdownRef = ref(null);
const showLogoutConfirm = ref(false);
const recentNotifs = ref([
  { id: 1, title: 'New VIP Booking', time: '2 mins ago', type: 'info', icon: 'fa-solid fa-user-plus' },
  { id: 2, title: 'Fleet Maintenance Due', time: '30 mins ago', type: 'warning', icon: 'fa-solid fa-triangle-exclamation' },
  { id: 3, title: 'Security Alert Resolved', time: '1 hr ago', type: 'success', icon: 'fa-solid fa-shield-check' },
]);

//new admin label
const adminData = ref({
  name: 'Superintendent',
  role: 'SuperAdmin',
  username: 'SuperAdmin'
});

const loadAdminData = () => {
  const rawData = localStorage.getItem('user_data');
  if (rawData) {
    try {
      const parsed = JSON.parse(rawData);
      adminData.value = {
        email: parsed.email || 'admin@indoria.com',
        role: parsed.role || 'Admin',
        username: parsed.username || 'Superintendent'
      };
    } catch (e) {
      console.error("Failed to parse user_data", e);
    }
  }
};
 
const toggleDropdown = () => {
  showDropdown.value = !showDropdown.value;
  showNotifDropdown.value = false;
};

const toggleNotifications = () => {
  showNotifDropdown.value = !showNotifDropdown.value;
  showDropdown.value = false;
};

const handleClickOutside = (event) => {
  if (dropdownRef.value && !dropdownRef.value.contains(event.target)) {
    showDropdown.value = false;
  }
  if (notifRef.value && !notifRef.value.contains(event.target)) {
    showNotifDropdown.value = false;
  }
};

//new logout confirmation
const triggerLogout = () => {
  showDropdown.value = false;
  showLogoutConfirm.value = true;
};

onMounted(() => {
  loadAdminData();
  document.addEventListener('mousedown', handleClickOutside);
  setTimeout(() => {
    toastRef.value?.addNotification({
      source: 'SYSTEM',
      title: 'Session Secured',
      message: 'Admin firewall protocols are now active.',
      type: 'success'
    });
  }, 2000);
});

onUnmounted(() => {
  document.removeEventListener('mousedown', handleClickOutside);
});

const handleLogout = () => {
  localStorage.removeItem('user_token');
  localStorage.removeItem('user_data');
  showLogoutConfirm.value = false;
  router.push('/');
};
</script>

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

/* Added from style 2: Notification Wrapper */
.notification-wrapper { position: relative; }

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

/* Added from style 2: Notification Dropdown */
.notif-dropdown {
  position: absolute;
  top: 130%;
  right: 0;
  width: 320px;
  background: #0c0c0c;
  border: 1px solid #222;
  border-top: 2px solid #c5a059;
  border-radius: 12px;
  z-index: 1001;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
}

.notif-header {
  padding: 1rem;
  border-bottom: 1px solid #1a1a1a;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.notif-item {
  padding: 1rem;
  display: flex;
  gap: 12px;
  border-bottom: 1px solid #111;
  transition: 0.2s;
  cursor: pointer;
}

.notif-item:hover { background: #111; }

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

/* Added from style 2: Avatar Ring */
.avatar-ring {
  padding: 2px;
  border: 1px solid #c5a059;
  border-radius: 50%;
  background: linear-gradient(45deg, #c5a059, #000);
}

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

/* Dropdown styling */
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

/* Animation overrides from style 2 */
.dropdown-slide-enter-active { animation: dropSlide 0.4s cubic-bezier(0.165, 0.84, 0.44, 1); }
.dropdown-slide-leave-active { animation: dropSlide 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) reverse; }

@keyframes dropSlide {
  from { opacity: 0; transform: translateY(-15px) scale(0.98); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

/* --- SMALL SCREEN OVERRIDES --- */
@media (max-width: 1024px) {
  .search-bar { width: 180px; }
}

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
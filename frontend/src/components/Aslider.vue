<template>
  <div class="admin-layout-wrapper">
    
    <aside class="admin-nav">
      <div class="nav-content">
        <div class="nav-links">
          <button 
            v-for="item in primaryLinks" 
            :key="item.id" 
            @click="activeComponent = item.comp"
            :class="['nav-item', { 'active': activeComponent === item.comp }]"
          >
            <i :class="item.icon"></i>
            <span>{{ item.label }}</span>
          </button>

          <button class="nav-item more-trigger hide-desktop" @click="showMore = !showMore">
            <i class="fa-solid" :class="showMore ? 'fa-xmark' : 'fa-ellipsis-h'"></i>
            <span>More</span>
          </button>

          <div class="extended-links" :class="{ 'mobile-visible': showMore }">
            <button 
              v-for="item in extendedLinks" 
              :key="item.id" 
              @click="selectExtended(item.comp)"
              :class="['nav-item', { 'active': activeComponent === item.comp }]"
            >
              <i :class="item.icon"></i>
              <span>{{ item.label }}</span>
            </button>
          </div>
        </div>
      </div>
    </aside>

    <main class="admin-main-content">
      <transition name="fade-slide" mode="out-in">
        <component :is="activeComponent" />
      </transition>
    </main>

    <div v-if="showMore" class="nav-overlay" @click="showMore = false"></div>
  </div>
</template>

<script setup>
import { ref, markRaw } from 'vue';
// Import your pages/components
import AOverview from '../components/Aoverview.vue';
import ATravelers from '../components/Atravel.vue'; // Add these as you create them
import AFleet from '../components/Afleet.vue';
import ADestinations from '../components/Adestinations.vue';
import AConcierge from '../components/Aconcierge.vue';
import AVault from '../components/Avault.vue';
import Apayment from '../components/Apayment.vue';
import Ainquiry from './Ainquiry.vue';

const showMore = ref(false);

// Using markRaw so Vue doesn't make the component instance reactive (performance)
const activeComponent = ref(markRaw(AOverview));

const primaryLinks = [
  { id: 1, label: 'Overview', icon: 'fa-solid fa-chart-pie', comp: markRaw(AOverview) },
  { id: 2, label: 'Travelers', icon: 'fa-solid fa-crown', comp: markRaw(ATravelers) }, 
  { id: 3, label: 'Fleet', icon: 'fa-solid fa-car-side', comp: markRaw(AFleet) }
];

const extendedLinks = [
  { id: 4, label: 'Destinations', icon: 'fa-solid fa-map-location-dot', comp: markRaw(ADestinations) },
  { id: 5, label: 'Concierge', icon: 'fa-solid fa-comments', comp: markRaw(AConcierge) },
  { id: 6, label: 'Vault', icon: 'fa-solid fa-vault', comp: markRaw(AVault) },
  { id: 7, label: 'Payments', icon: 'fa-solid fa-receipt', comp: markRaw(Apayment) },
  { id: 8, label: 'Inquiry', icon: 'fa-solid fa-file-invoice', comp: markRaw(Ainquiry)}
];

const selectExtended = (comp) => {
  activeComponent.value = comp;
  showMore.value = false; // Close mobile drawer after selection
};
</script>

<style scoped>
/* --- DESKTOP: VERTICAL SIDEBAR --- */
.admin-nav {
  width: 260px;
  background: #0c0c0c;
  border-right: 1px solid rgba(197, 160, 89, 0.1);
  height: calc(100vh - 70px);
  position: sticky;
  top: 70px;
  z-index: 99;
}

.nav-links {
  display: flex;
  flex-direction: column;
  padding: 1.5rem 1rem;
  gap: 0.5rem;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.8rem 1.2rem;
  color: #888;
  text-decoration: none;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-size: 0.9rem;
  background: none;
  border: none;
  cursor: pointer;
  width: 100%;
}

.nav-item i {
  width: 20px;
  font-size: 1.1rem;
  text-align: center;
}

.nav-item:hover, .router-link-active {
  background: rgba(197, 160, 89, 0.08);
  color: #c5a059;
}

.router-link-active {
  font-weight: 600;
  border-right: 3px solid #c5a059;
  border-radius: 8px 0 0 8px;
}

/* --- MOBILE: HORIZONTAL BOTTOM BAR --- */
@media (max-width: 768px) {
  .admin-nav {
    width: 100%;
    height: 70px;
    position: fixed;
    bottom: 0;
    top: auto;
    left: 0;
    border-right: none;
    border-top: 1px solid rgba(197, 160, 89, 0.2);
    background: #111;
  }

  .nav-links {
    flex-direction: row;
    padding: 0;
    height: 100%;
    justify-content: space-around;
    align-items: center;
    gap: 0;
  }

  .nav-item {
    flex-direction: column;
    gap: 4px;
    padding: 10px 0;
    font-size: 0.65rem;
    border-radius: 0;
    justify-content: center;
  }

  .nav-item i {
    font-size: 1.2rem;
  }

  .router-link-active {
    border-right: none;
    border-top: 3px solid #c5a059;
  }

  .hide-desktop {
    display: flex;
  }

  /* --- THE "MORE" DRAWER --- */
  .extended-links {
    position: fixed;
    bottom: -100%; /* Hidden initially */
    left: 0;
    width: 100%;
    background: #161616;
    display: grid;
    grid-template-columns: repeat(3, 1/3fr);
    padding: 1.5rem;
    gap: 1rem;
    transition: bottom 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    border-radius: 20px 20px 0 0;
    z-index: 100;
    border-top: 1px solid rgba(197, 160, 89, 0.3);
  }

  .extended-links.mobile-visible {
    bottom: 70px; /* Sits right on top of the bottom bar */
  }

  .nav-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100vh;
    background: rgba(0,0,0,0.7);
    backdrop-filter: blur(4px);
    z-index: 98;
  }
}

@media (min-width: 769px) {
  .hide-desktop {
    display: none;
  }
  .extended-links {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
}

.admin-layout-wrapper {
  display: flex;
  height: calc(100vh - 70px); /* Height after header */
  overflow: hidden;
  background: #080808;
}

.admin-main-content {
  flex: 1; /* This takes up the "Left Out Space" */
  overflow-y: auto;
  padding: 2rem;
  background: #080808;
}

/* --- SIDEBAR STYLES (Desktop) --- */
.admin-nav {
  width: 260px;
  background: #0c0c0c;
  border-right: 1px solid rgba(197, 160, 89, 0.1);
  z-index: 99;
}

.nav-links {
  display: flex;
  flex-direction: column;
  padding: 1.5rem 1rem;
  gap: 0.5rem;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.8rem 1.2rem;
  color: #888;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-size: 0.9rem;
  background: none;
  border: none;
  cursor: pointer;
  width: 100%;
  text-align: left;
}

.nav-item i { width: 20px; font-size: 1.1rem; text-align: center; }
.nav-item:hover, .nav-item.active { background: rgba(197, 160, 89, 0.08); color: #c5a059; }
.nav-item.active { font-weight: 600; border-right: 3px solid #c5a059; border-radius: 8px 0 0 8px; }

/* --- MOBILE STYLES (Bottom Bar) --- */
@media (max-width: 768px) {
  .admin-layout-wrapper { flex-direction: column; }
  
  .admin-nav {
    width: 100%;
    height: 70px;
    position: fixed;
    bottom: 0;
    border-right: none;
    border-top: 1px solid rgba(197, 160, 89, 0.2);
  }

  .nav-links { flex-direction: row; padding: 0; height: 100%; justify-content: space-around; align-items: center; }

  .nav-item {
    flex-direction: column;
    gap: 4px;
    padding: 10px 0;
    font-size: 0.65rem;
    align-items: center;
  }

  .nav-item.active { border-right: none; border-top: 3px solid #c5a059; border-radius: 0; }

  .extended-links {
    position: fixed;
    bottom: -100%;
    left: 0;
    width: 100%;
    background: #121212;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    padding: 1.5rem;
    gap: 1rem;
    transition: bottom 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 20px 20px 0 0;
    border-top: 1px solid rgba(197, 160, 89, 0.3);
  }

  .extended-links.mobile-visible { bottom: 70px; }
  .hide-desktop { display: flex; }
  .admin-main-content { padding: 1rem; padding-bottom: 90px; }
}

@media (min-width: 769px) {
  .hide-desktop { display: none; }
  .extended-links { display: flex; flex-direction: column; gap: 0.5rem; }
}

/* --- ANIMATION --- */
.fade-slide-enter-active, .fade-slide-leave-active { transition: all 0.3s ease; }
.fade-slide-enter-from { opacity: 0; transform: translateX(20px); }
.fade-slide-leave-to { opacity: 0; transform: translateX(-20px); }

.nav-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(4px);
  z-index: 98;
}
</style>
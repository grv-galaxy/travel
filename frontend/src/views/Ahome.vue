<template>
  <div class="admin-layout">
    <Aheader :currentPage="currentActivePage" />
    <Aslider />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import Aheader from '../components/Aheader.vue';
import Aslider from '../components/Aslider.vue';

const route = useRoute();

// Dynamically compute the page title based on the route name for the header breadcrumbs
const currentActivePage = computed(() => {
  return route.name || 'Overview';
});
</script>

<style scoped>
.admin-layout {
  min-height: 100vh;
  background-color: #0c0c0c; /* Deeper black for admin feel */
  display: flex;
  flex-direction: column;
}

.admin-body {
  display: flex;
  flex: 1;
  height: calc(100vh - 70px); /* Subtract header height */
  overflow: hidden;
}

/* Temporary Sidebar Placeholder */
.sidebar-placeholder {
  width: 260px;
  background: #121212;
  border-right: 1px solid rgba(197, 160, 89, 0.1);
  padding: 2rem;
}

.skeleton-nav {
  width: 100%;
  height: 100%;
  background: linear-gradient(180deg, rgba(255,255,255,0.03) 0%, transparent 100%);
  border-radius: 12px;
}

/* Main Content Section */
.admin-content {
  flex: 1;
  overflow-y: auto;
  padding: 2rem;
  background-image: 
    radial-gradient(circle at 50% 50%, rgba(197, 160, 89, 0.02) 0%, transparent 70%);
}

.content-wrapper {
  max-width: 1400px;
  margin: 0 auto;
}

/* Empty State Styling */
.welcome-hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 60vh;
  text-align: center;
  color: #fff;
}

.hero-icon {
  font-size: 4rem;
  color: #c5a059;
  margin-bottom: 1.5rem;
  opacity: 0.8;
}

.welcome-hero h2 {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

.welcome-hero p {
  color: #888;
  max-width: 400px;
}

/* Transitions */
.page-fade-enter-active,
.page-fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.page-fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}

.page-fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

@media (max-width: 768px) {
  .sidebar-placeholder {
    display: none;
  }
}
</style>
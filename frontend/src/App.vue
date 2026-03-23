<!-- <template>
  <RouterView />
</template>

<script setup>
import { RouterView } from 'vue-router'
</script>

<style>
/* Global Reset */
html, body, #app {
  margin: 0;
  padding: 0;
  /* DESKTOP: Matches the deep forest teal in your desktop UI */
  background-color: #1a2421; 
  overflow-x: hidden;
  width: 100%;
  scroll-behavior: smooth;
}

/* SMALL SCREENS (Mobile) */
@media (max-width: 768px) {
  html, body, #app {
    /* MOBILE: Matches the earthy brown in your mobile UI/screenshot */
    background-color: #1e1a15 !important;
    scroll-behavior: smooth;
  }
}
</style> -->






<template>
  <div id="app-container">
    <LoadingOverlay v-if="isLoading" />
    
    <RouterView />
    <Alert ref="alertSystem" />
  </div>
</template>

<script setup>
import { ref, provide } from 'vue'
import { RouterView } from 'vue-router'
import LoadingOverlay from './components/LoadingOverlay.vue'
import Alert from './components/Alert.vue'

// Global loading state
const isLoading = ref(false)
const alertSystem = ref(null)

// We "provide" this so any page (like Login.vue) can turn it on/off
provide('setGlobalLoading', (value) => {
  isLoading.value = value
})

provide('notify', (message, type = 'success', duration = 5000) => {
  if (alertSystem.value) {
    alertSystem.value.add(message, type, duration)
  }
})
</script>

<style>
/* Global Reset */
html, body, #app-container {
  margin: 0;
  padding: 0;
  min-height: 100vh;
  /* DESKTOP BACKGROUND */
  background-color: #1a2421; 
  overflow-x: hidden;
  width: 100%;
  scroll-behavior: smooth;
}

/* SMALL SCREENS (Mobile) */
@media (max-width: 768px) {
  html, body, #app-container {
    /* MOBILE BACKGROUND */
    background-color: #1e1a15 !important;
  }
}

:root {
  --indoria-gold: #f3c969;
  --indoria-dark: #1a150e;
}
</style>
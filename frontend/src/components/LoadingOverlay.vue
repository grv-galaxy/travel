  <template>
    <Transition name="fade">
      <div class="loading-overlay" aria-busy="true" aria-live="polite">
        <div class="loader-content">
          <div class="loader"></div>
          
          <div class="text-wrapper">
            <p class="loading-text">Indoria Journeys</p>
            <span class="sub-text">Preparing your curated experience...</span>
          </div>
        </div>
      </div>
    </Transition>
  </template>

  <style scoped>
  /* 1. LUXURY GLASS OVERLAY */
  .loading-overlay {
    position: fixed;
    inset: 0; /* Shorthand for top/left/right/bottom: 0 */
    width: 100vw;
    height: 100vh;
    /* Dark Deep Forest background with transparency */
    background: rgba(26, 36, 33, 0.85); 
    backdrop-filter: blur(12px) saturate(180%);
    -webkit-backdrop-filter: blur(12px) saturate(180%);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100000; /* Maximum priority */
    pointer-events: all; /* Blocks all clicks during loading */
  }

  .loader-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
  }

  /* 2. CUSTOM THEMED LOADER */
  .loader {
    width: 120px; /* Slightly larger for luxury feel */
    height: 18px;
    margin-bottom: 24px;
    /* Gold/Champagne color for luxury accent */
    --c: #d4af37 92%, #0000; 
    background: 
      radial-gradient(circle closest-side, var(--c)) calc(100%/-4) 0,
      radial-gradient(circle closest-side, var(--c)) calc(100%/4) 0;
    background-size: calc(100%/2) 100%;
    animation: l14 1.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
  }

  @keyframes l14 {
      0%   {background-position: calc(100%/-4) 0, calc(100%/4) 0}
      50%  {background-position: calc(100%/-4) -18px, calc(100%/4) 18px}
      100% {background-position: calc(100%/4) -18px, calc(3*100%/4) 18px}
  }

  /* 3. TYPOGRAPHY */
  .text-wrapper {
    text-align: center;
  }

  .loading-text {
    font-family: 'Playfair Display', serif; /* Use a serif font for luxury */
    color: #f5f5f5;
    font-size: 1.4rem;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin: 0;
    /* Elegant fade pulse */
    animation: textPulse 2s ease-in-out infinite;
  }

  .sub-text {
    display: block;
    font-family: 'Inter', sans-serif;
    color: rgba(245, 245, 245, 0.6);
    font-size: 0.85rem;
    margin-top: 8px;
    letter-spacing: 1px;
  }

  @keyframes textPulse {
    0%, 100% { opacity: 0.8; }
    50% { opacity: 1; text-shadow: 0 0 15px rgba(212, 175, 55, 0.3); }
  }

  /* 4. RESPONSIVE ADJUSTMENTS */
  @media (max-width: 768px) {
    .loading-overlay {
      /* Slightly warmer dark for mobile match */
      background: rgba(30, 26, 21, 0.95); 
    }
    .loading-text {
      font-size: 1.1rem;
      letter-spacing: 2px;
    }
    .loader {
      width: 90px;
    }
  }

  /* 5. TRANSITION */
  .fade-enter-active, .fade-leave-active {
    transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .fade-enter-from, .fade-leave-to {
    opacity: 0;
    transform: scale(1.05); /* Slight zoom out effect on exit */
  }
  </style>

  <script setup>
      defineProps({
          show: {
              type: Boolean,
              default: false
          }
      });
  </script>


<!-- <template>
  <Transition name="fade">
    <div v-if="show" class="loading-overlay" aria-busy="true" aria-live="polite">
      <div class="loader-content">
        <div class="loader"></div>
        
        <div class="text-wrapper">
          <p class="loading-text">Indoria Journeys</p>
          <span class="sub-text">Preparing your curated experience...</span>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
/* 1. LUXURY GLASS OVERLAY */
.loading-overlay {
  position: fixed;
  inset: 0; /* Shorthand for top/left/right/bottom: 0 */
  width: 100vw;
  height: 100vh;
  /* Dark Deep Forest background with transparency */
  background: rgba(26, 36, 33, 0.85); 
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 100000; /* Maximum priority */
  pointer-events: all; /* Blocks all clicks during loading */
}

.loader-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 2rem;
}

/* 2. CUSTOM THEMED LOADER */
.loader {
  width: 120px; /* Slightly larger for luxury feel */
  height: 18px;
  margin-bottom: 24px;
  /* Gold/Champagne color for luxury accent */
  --c: #d4af37 92%, #0000; 
  background: 
    radial-gradient(circle closest-side, var(--c)) calc(100%/-4) 0,
    radial-gradient(circle closest-side, var(--c)) calc(100%/4) 0;
  background-size: calc(100%/2) 100%;
  animation: l14 1.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}

@keyframes l14 {
    0%   {background-position: calc(100%/-4) 0, calc(100%/4) 0}
    50%  {background-position: calc(100%/-4) -18px, calc(100%/4) 18px}
    100% {background-position: calc(100%/4) -18px, calc(3*100%/4) 18px}
}

/* 3. TYPOGRAPHY */
.text-wrapper {
  text-align: center;
}

.loading-text {
  font-family: 'Playfair Display', serif; /* Use a serif font for luxury */
  color: #f5f5f5;
  font-size: 1.4rem;
  font-weight: 600;
  letter-spacing: 3px;
  text-transform: uppercase;
  margin: 0;
  /* Elegant fade pulse */
  animation: textPulse 2s ease-in-out infinite;
}

.sub-text {
  display: block;
  font-family: 'Inter', sans-serif;
  color: rgba(245, 245, 245, 0.6);
  font-size: 0.85rem;
  margin-top: 8px;
  letter-spacing: 1px;
}

@keyframes textPulse {
  0%, 100% { opacity: 0.8; }
  50% { opacity: 1; text-shadow: 0 0 15px rgba(212, 175, 55, 0.3); }
}

/* 4. RESPONSIVE ADJUSTMENTS */
@media (max-width: 768px) {
  .loading-overlay {
    /* Slightly warmer dark for mobile match */
    background: rgba(30, 26, 21, 0.95); 
  }
  .loading-text {
    font-size: 1.1rem;
    letter-spacing: 2px;
  }
  .loader {
    width: 90px;
  }
}

/* 5. TRANSITION */
.fade-enter-active, .fade-leave-active {
  transition: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: scale(1.05); /* Slight zoom out effect on exit */
}
</style>

<script setup>
    defineProps({
        show: {
            type: Boolean,
            default: false
        }
    });
</script> -->
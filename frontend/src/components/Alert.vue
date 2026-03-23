<template>
  <Teleport to="body">
    <TransitionGroup name="alert-list">
      <div 
        v-for="alert in alerts" 
        :key="alert.id"
        class="fixed top-6 right-4 md:right-8 z-[9999] w-[calc(100%-2rem)] max-w-sm"
        :style="{ marginTop: alert.offset + 'px' }"
      >
        <div 
          class="relative overflow-hidden bg-[#1a150e] border border-[#f3c969]/20 rounded-2xl shadow-[0_20px_50px_rgba(0,0,0,0.3)] backdrop-blur-xl p-5 group"
        >
          <div 
            class="absolute bottom-0 left-0 h-[2px] bg-[#f3c969] transition-all linear"
            :style="{ width: alert.progress + '%' }"
          ></div>

          <div class="flex items-start gap-4">
            <div 
              class="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center border border-[#f3c969]/30 shadow-[0_0_15px_rgba(243,201,105,0.1)]"
              :class="alert.type === 'error' ? 'text-red-400 border-red-900/50' : 'text-[#f3c969]'"
            >
              <i :class="getIcon(alert.type)" class="text-lg"></i>
            </div>

            <div class="flex-1 pt-1">
              <h3 class="font-serif text-[13px] font-bold uppercase tracking-[0.2em] mb-1" 
                  :class="alert.type === 'error' ? 'text-red-400' : 'text-[#f3c969]'">
                {{ alert.title || getDefaultTitle(alert.type) }}
              </h3>
              <p class="text-white/80 text-xs font-medium leading-relaxed tracking-tight uppercase">
                {{ alert.message }}
              </p>
            </div>

            <button 
              @click="remove(alert.id)"
              class="flex-shrink-0 text-white/20 hover:text-[#f3c969] transition-colors duration-300"
            >
              <i class="fas fa-times text-xs"></i>
            </button>
          </div>
        </div>
      </div>
    </TransitionGroup>
  </Teleport>
</template>

<script setup>
import { ref } from 'vue';

const alerts = ref([]);
let count = 0;

const getIcon = (type) => {
  if (type === 'success') return 'fas fa-shield-check';
  if (type === 'error') return 'fas fa-exclamation-triangle';
  return 'fas fa-bell';
};

const getDefaultTitle = (type) => {
  if (type === 'success') return 'Vault Verified';
  if (type === 'error') return 'System Alert';
  return 'Notification';
};

const add = (message, type = 'success', duration = 5000) => {
  const id = count++;
  const newAlert = {
    id,
    message,
    type,
    progress: 100,
    offset: alerts.value.length * 90 // Stack alerts vertically
  };
  
  alerts.value.push(newAlert);

  // Animate progress bar
  const start = Date.now();
  const timer = setInterval(() => {
    const elapsed = Date.now() - start;
    newAlert.progress = Math.max(0, 100 - (elapsed / duration) * 100);
    if (newAlert.progress <= 0) clearInterval(timer);
  }, 10);

  // Auto remove
  setTimeout(() => remove(id), duration);
};

const remove = (id) => {
  const index = alerts.value.findIndex(a => a.id === id);
  if (index > -1) {
    alerts.value.splice(index, 1);
    // Recalculate offsets for remaining alerts
    alerts.value.forEach((alert, i) => {
      alert.offset = i * 90;
    });
  }
};

defineExpose({ add });
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

.font-serif { font-family: 'Playfair Display', serif; }

/* Animation: Slide from Right */
.alert-list-enter-active,
.alert-list-leave-active {
  transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
}

.alert-list-enter-from {
  transform: translateX(120%);
  opacity: 0;
}

.alert-list-leave-to {
  transform: scale(0.9);
  opacity: 0;
}

/* Ensure smooth stacking when one is removed */
.alert-list-move {
  transition: transform 0.4s ease;
}
</style>
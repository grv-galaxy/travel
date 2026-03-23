<template>
  <div class="notification-stack">
    <transition-group name="notification-list">
      <div 
        v-for="note in notifications" 
        :key="note.id" 
        class="note-card shadow-premium"
        :class="[note.type.toLowerCase(), { 'is-closing': note.closing }]"
      >
        <div class="scan-line"></div>

        <div class="note-body">
          <div class="icon-section">
            <div class="icon-blob">
              <i :class="getIcon(note.source)"></i>
            </div>
          </div>

          <div class="content-section">
            <div class="flex justify-between items-start">
              <span class="source-tag">{{ note.source }}</span>
              <span class="time-tag">JUST NOW</span>
            </div>
            <h4 class="text-white font-black text-sm uppercase mt-1 tracking-tight">
              {{ note.title }}
            </h4>
            <p class="text-slate-400 text-xs font-medium mt-1 leading-relaxed">
              {{ note.message }}
            </p>
          </div>

          <button class="close-btn" @click="removeNote(note.id)">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <div class="timer-bar" :style="{ transitionDuration: note.duration + 'ms' }"></div>
      </div>
    </transition-group>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const notifications = ref([]);

// Mock data for demo - in production, this would be an Event Bus or Pinia Store
const addNotification = (config) => {
  const id = Date.now();
  const note = {
    id,
    source: config.source || 'SYSTEM',
    title: config.title || 'Security Alert',
    message: config.message || 'Action required immediately.',
    type: config.type || 'info', // info, warning, critical, success
    duration: config.duration || 5000,
    closing: false
  };

  notifications.value.unshift(note);

  // Auto-remove
  setTimeout(() => {
    removeNote(id);
  }, note.duration);
};

const removeNote = (id) => {
  const index = notifications.value.findIndex(n => n.id === id);
  if (index !== -1) {
    notifications.value[index].closing = true;
    setTimeout(() => {
      notifications.value = notifications.value.filter(n => n.id !== id);
    }, 400); // Wait for exit animation
  }
};

const getIcon = (source) => {
  const icons = {
    'FLEET': 'fa-solid fa-car-side',
    'VAULT': 'fa-solid fa-file-shield',
    'PAYMENTS': 'fa-solid fa-credit-card',
    'SECURITY': 'fa-solid fa-user-secret',
    'SYSTEM': 'fa-solid fa-microchip'
  };
  return icons[source] || 'fa-solid fa-bell';
};

// Simulation of incoming data for production preview
onMounted(() => {
  setTimeout(() => {
    addNotification({
      source: 'SECURITY',
      title: 'Unauthorized Access',
      message: 'Blocked breach attempt from IP: 192.168.1.1',
      type: 'critical'
    });
  }, 1500);
});
</script>

<style scoped>
.notification-stack {
  position: fixed;
  top: 30px;
  right: 30px;
  width: 380px;
  z-index: 9999;
  display: flex;
  flex-direction: column;
  gap: 15px;
  pointer-events: none; /* Allows clicking through stack if empty */
}

.note-card {
  pointer-events: auto;
  background: rgba(12, 12, 12, 0.95);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  overflow: hidden;
  position: relative;
  transition: 0.4s cubic-bezier(0.23, 1, 0.32, 1);
}

.note-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(197, 160, 89, 0.05), transparent);
}

/* Source Styling */
.critical { border-left: 4px solid #ff4d4d; }
.warning { border-left: 4px solid #c5a059; }
.success { border-left: 4px solid #00ff88; }
.info { border-left: 4px solid #00d2ff; }

.note-body {
  padding: 1.2rem;
  display: flex;
  gap: 15px;
  position: relative;
  z-index: 1;
}

.icon-blob {
  width: 42px;
  height: 42px;
  background: #1a1a1a;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid rgba(255, 255, 255, 0.05);
}

.icon-blob i {
  font-size: 1.1rem;
  color: #c5a059;
}

.content-section { flex: 1; }

.source-tag {
  font-size: 8px;
  font-weight: 900;
  letter-spacing: 1.5px;
  color: #c5a059;
  text-transform: uppercase;
}

.time-tag {
  font-size: 8px;
  font-weight: 800;
  color: #444;
}

.close-btn {
  background: transparent;
  border: none;
  color: #444;
  cursor: pointer;
  transition: 0.2s;
  height: fit-content;
}

.close-btn:hover { color: white; }

/* Progress Bar */
.timer-bar {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 2px;
  width: 100%;
  background: rgba(197, 160, 89, 0.3);
  animation: timerProgress linear forwards;
}

@keyframes timerProgress {
  from { width: 100%; }
  to { width: 0%; }
}

/* Scan Line Animation */
.scan-line {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: linear-gradient(90deg, transparent, #c5a059, transparent);
  animation: scanTop 3s infinite;
  opacity: 0.3;
}

@keyframes scanTop {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

/* List Transitions */
.notification-list-enter-active {
  animation: slideInRight 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.notification-list-leave-active {
  animation: fadeOutRight 0.4s ease forwards;
}

@keyframes slideInRight {
  from { transform: translateX(100%) scale(0.9); opacity: 0; }
  to { transform: translateX(0) scale(1); opacity: 1; }
}

@keyframes fadeOutRight {
  to { transform: translateX(50px); opacity: 0; }
}

@media (max-width: 480px) {
  .notification-stack {
    top: 20px;
    right: 20px;
    left: 20px;
    width: auto;
  }
}
</style>
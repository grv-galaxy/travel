<template>
  <Transition name="modal-fade">
    <div v-if="show" class="modal-overlay" @click.self="$emit('cancel')">
      <div class="modal-content" role="dialog" aria-modal="true">
        <div class="gold-bar"></div>
        
        <h3 class="modal-title">{{ title }}</h3>
        
        <p class="modal-message">{{ message }}</p>
        
        <div class="modal-actions">
          <button class="btn-secondary" @click="$emit('cancel')" type="button">
            Cancel
          </button>
          <button class="btn-primary" @click="$emit('confirm')" type="button">
            Confirm
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup>
defineProps({
  show: Boolean,
  title: String,
  message: String
});
defineEmits(['confirm', 'cancel']);
</script>

<style scoped>
/* 1. THE OVERLAY: Forces centering and stays above everything */
.modal-overlay {
  position: fixed;
  /* Use inset instead of top/left/right/bottom for modern shorthand */
  inset: 0; 
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.75); /* Darker for better focus */
  backdrop-filter: blur(10px); /* Premium luxury blur */
  -webkit-backdrop-filter: blur(10px);
  display: flex;
  justify-content: center; /* Horizontal center */
  align-items: center;     /* Vertical center */
  z-index: 999999;         /* Highest possible z-index */
  padding: 20px;           /* Prevents edges touching on mobile */
}

/* 2. THE MODAL BOX */
.modal-content {
  background: #1a2421; /* Your Deep Forest Teal */
  border: 1px solid rgba(212, 175, 55, 0.4);
  border-radius: 16px; /* Slightly smoother corners */
  width: 100%;
  max-width: 420px; /* Optimal reading width */
  padding: 40px 30px 30px; /* Extra top padding for gold bar */
  position: relative;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  text-align: center;
  /* Ensure it doesn't get too tall on tiny phones */
  max-height: 90vh;
  overflow-y: auto;
}

.gold-bar {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: linear-gradient(90deg, #d4af37, #f3c969, #d4af37); /* Luxury gradient */
  border-radius: 0 0 8px 8px;
}

.modal-title {
  font-family: 'Playfair Display', Georgia, serif;
  color: #f3c969; /* Lighter gold for readability */
  font-size: 1.75rem;
  margin-bottom: 12px;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.modal-message {
  color: rgba(255, 255, 255, 0.85);
  font-family: 'Inter', system-ui, sans-serif;
  line-height: 1.6;
  font-size: 1rem;
  margin-bottom: 32px;
}

/* 3. BUTTONS */
.modal-actions {
  display: flex;
  gap: 12px;
  justify-content: center;
}

button {
  flex: 1; /* Makes buttons equal width on mobile */
  padding: 14px 20px;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  border: none;
  font-family: 'Inter', sans-serif;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.85rem;
}

.btn-secondary {
  background: rgba(255, 255, 255, 0.05);
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.btn-secondary:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.2);
}

.btn-primary {
  background: #d4af37;
  color: #1a150e;
  box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2);
}

.btn-primary:hover {
  background: #f3c969;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(212, 175, 55, 0.4);
}

/* 4. ANIMATION: Smooth Scale and Fade */
.modal-fade-enter-active {
  transition: all 0.3s ease-out;
}
.modal-fade-leave-active {
  transition: all 0.2s ease-in;
}
.modal-fade-enter-from,
.modal-fade-leave-to {
  opacity: 0;
  transform: scale(0.95);
}

/* 5. MOBILE RESPONSIVENESS */
@media (max-width: 640px) {
  .modal-overlay {
    padding: 15px;
  }
  .modal-content {
    background: #1e1a15; /* Earthy Brown for Mobile */
    padding: 35px 20px 25px;
  }
  .modal-actions {
    flex-direction: column-reverse; /* Stack buttons: Cancel on bottom */
  }
  button {
    width: 100%;
  }
}
</style>
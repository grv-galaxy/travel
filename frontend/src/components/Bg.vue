<template>
  <div class="bg-container">
    <div class="bg-overlay"></div>
    <div class="bottom-gradient"></div>
    <slot />
  </div>
</template>

<style scoped>
/* RESET browser default spacing */
:global(html),
:global(body) {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow-x: hidden;
  /* Match the body to the brown so fast scrolls don't show white */
  background-color: #1e1a15; 
}

.bg-container {
  position: absolute;
  inset: 0;
  z-index: 1;
  width: 100%;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  /* DESKTOP IMAGE */
  background: url('../assets/images/laptop.jpg') center / cover no-repeat;
}

.bg-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.25);
  z-index: 1;
}

/* THE FADE ELEMENT */
.bottom-gradient {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 25vh; /* Slightly taller for a smoother blend */
  z-index: 2;
  /* DESKTOP FADE: Deep Forest Teal */
  background: linear-gradient(to bottom, transparent, #1a2421);
}

/* Phones & small devices */
@media (max-width: 768px) {
  .bg-container {
    /* MOBILE IMAGE (The Fort) */
    background: url('../assets/images/travel.jpg') top / cover no-repeat;
    height: 100vh; 
  }

  .bottom-gradient {
    /* MOBILE FADE: Must match the Brown in About.vue exactly (#1e1a15) */
    background: linear-gradient(
      to bottom,
      transparent 0%,  /* Transparent brown */
      #1e1a15 100%           /* Solid earthy brown */
    ) !important;
    height: 30vh;
    z-index: 3; /* Ensure it stays above the overlay */
  }
}
</style>
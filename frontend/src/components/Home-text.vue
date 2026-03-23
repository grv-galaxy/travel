<template>
  <div class="home-text-wrapper">
    <!-- Heading -->
    <BlurText
      text="Welcome to"
      class-name="hero-heading"
      animate-by="words"
      direction="top"
      :delay="100"
      :step-duration="0.35"
      @animation-complete="handleHeadingComplete"
    />

    <!-- Brand -->
    <h1 class="hero-heading brand-highlight brand-animate">
      Indoria Journeys
    </h1>

    <!-- Subheading -->
    <BlurText
      text="Your Gateway to Explore the Heart of India"
      class-name="hero-subheading"
      animate-by="words"
      direction="top"
      :delay="520"
      :step-duration="0.35"
      @animation-complete="handleSubheadingComplete"
    />
  </div>
</template>

<script setup lang="ts">
import BlurText from '../other/BlurText.vue'

const handleHeadingComplete = () => {
  console.log('Heading animation complete!')
}

const handleSubheadingComplete = () => {
  console.log('Subheading animation complete!')
}
</script>

<style scoped>
/* ================= WRAPPER ================= */
.home-text-wrapper {
  position: absolute;
  inset: 0;
  z-index: 2;

  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-start;

  padding: 0 0 30vh 4vw;

  text-align: left;
  color: #f5e6c8;
}

/* ================= HEADING ================= */
.hero-heading {
  font-family: Georgia, "Times New Roman", serif;
  font-size: 3.4rem;
  font-weight: 700;
  line-height: 1.15;
  max-width: 720px;

  color: #f8efe0;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.55);
}

/* ================= SUBHEADING ================= */
.hero-subheading {
  margin-top: 1rem;
  font-family: "Inter", system-ui, sans-serif;
  font-size: 1.25rem;
  font-weight: 400;
  letter-spacing: 0.5px;
  max-width: 520px;

  color: rgba(248, 239, 224, 0.9);
  text-shadow: 0 2px 12px rgba(0, 0, 0, 0.45);
}

/* ================= BRAND ================= */
.brand-highlight {
  font-weight: 700;
  position: relative;

  background: linear-gradient(
    90deg,
    #f3c969,
    #fff1c1,
    #e8b34b
  );

  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;

  letter-spacing: 0.06em;
}

.brand-highlight::after {
  content: "";
  position: absolute;
  left: 5%;
  bottom: -0.25em;
  width: 90%;
  height: 2px;

  background: linear-gradient(
    90deg,
    transparent,
    rgba(243, 201, 105, 0.85),
    transparent
  );
}

/* ================= BRAND ANIMATION ================= */
.brand-animate {
  opacity: 0;
  transform: translateY(16px);
  animation: brandReveal 0.6s ease-out forwards;
  animation-delay: 0.35s;
}

@keyframes brandReveal {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ================= TABLET ================= */
@media (max-width: 1024px) {
  .home-text-wrapper {
    padding: 0 0 30vh 4vw;
  }

  .hero-heading {
    font-size: 2.6rem;
  }

  .hero-subheading {
    font-size: 1.1rem;
  }
}

/* ================= MOBILE (CENTER → SCROLL UP) ================= */
@media (max-width: 768px) {
  .home-text-wrapper {
    position: absolute;
    top: 50vh;
    left: 50%;
    transform: translate(-50%, -50%);

    width: 90%;
    max-width: 380px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    max-height: 30vh;
    padding: 2rem 1.5rem;

    background: rgba(26, 21, 14, 0.8);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(243, 201, 105, 0.2);
    border-radius: 28px;
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);

    text-align: center;
    z-index: 10;
  }

  .header-group {
    margin-bottom: 1.5rem;
  }

  /* "Welcome to" Styling */
  :deep(.hero-welcome) {
    font-size: 0.9rem !important;
    text-transform: uppercase;
    letter-spacing: 3px;
    color: #f3c969;
    margin-bottom: 0.5rem;
    display: block;
  }

  /* Brand Name Styling */
  .hero-brand {
    font-family: Georgia, serif;
    font-size: 2.25rem;
    line-height: 1.1;
    margin: 0.5rem 0;
    filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.3));
  }

  /* Animated underline adjustment for mobile */
  .brand-highlight::after {
    height: 1px;
    bottom: -5px;
    background: linear-gradient(
      90deg,
      transparent,
      #f3c969,
      transparent
    );
  }

  .mobile-divider {
    width: 40px;
    height: 1px;
    background: rgba(243, 201, 105, 0.3);
    margin-bottom: 1.5rem;
  }

  /* Subheading Styling */
  :deep(.hero-subheading) {
    font-size: 1rem !important;
    text-align: center;
    display: block;
    width: 100%;
    line-height: 1.6;
    max-width: 280px;
    color: rgba(248, 239, 224, 0.85);
    font-weight: 300;
  }
}
</style>

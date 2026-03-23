<template>
  <Header />

  <!-- HERO -->
  <section class="hero">
    <Bg />
    <HomeText />

    <!-- FADE OUT INTO ABOUT -->
    <div class="hero-fade"></div>
  </section>

  <!-- ABOUT SECTION -->
  <About />
  <Destination />
  <Contact />
  <Footer /> 
</template>

<script setup>
import Bg from '../components/Bg.vue'
import Header from '../components/Header.vue'
import HomeText from '../components/Home-text.vue'
import About from '../components/About.vue'
import Destination from '../components/Destination.vue'
import Footer from '../components/Footer.vue'
import Contact from '../components/Contact.vue'
</script>

<style scoped>
/* ================= HERO ================= */
.hero {
  position: relative;
  width: 100%;
  height: 100vh;
  /* Apply a mask to the entire hero section */
  -webkit-mask-image: linear-gradient(to bottom, black 80%, transparent 100%);
  mask-image: linear-gradient(to bottom, black 80%, transparent 100%);
  
  /* Ensure the background of the parent container is the same as About */
  background-color: #1e1a15; 
}

/* ================= HERO FADE ================= */
/* This removes the harsh cut between Hero and About */
.hero-fade {
  position: absolute;
  left: 0;
  bottom: 0;

  width: 100%;
  height: 250px;           /* Desktop fade length */

  background: linear-gradient(
    to bottom,
    rgba(26, 36, 33, 0) 0%,
    rgba(26, 36, 33, 0.7) 50%,
    #1a2421 100%
  );

  pointer-events: none;    /* No interaction issues */
  z-index: 4;              /* Above BG, below text if needed */
}
@media (max-width: 768px) {
  .hero-fade {
    background: linear-gradient(
      to bottom,
      rgba(30, 26, 21,0) 0%, 
      #1e1a15 100%
    ) !important;
    height: 150px;         /* Mobile fade length */
  }
}
</style>

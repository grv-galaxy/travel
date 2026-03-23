<template>
  <section id="about-section" class="about-page">
    <div class="bento-bg"></div>

    <div class="about-container">
      <header class="about-header">
        <h1 class="about-heading">About Indoria Journey</h1>
        <div class="intro-content">
          <p class="about-text">
            Indoria Journey is a travel initiative dedicated to showcasing the rich
            heritage, culture, and hidden stories of India. From ancient forts and
            historic cities to vibrant traditions and local experiences, our goal
            is to help travelers explore India beyond the usual destinations.
          </p>
          <p class="about-text">
            We believe every place has a story to tell. Indoria Journey focuses on
            authentic travel experiences that connect people with history, nature,
            and local communities.
          </p>
          <p class="about-text secondary">
            Through carefully curated guides, visuals, and travel insights, Indoria
            Journey aims to become your trusted companion in discovering the heart
            of India — one journey at a time.
          </p>
        </div>
      </header>

      <div class="about-grid">
        <div class="grid-card">
          <h2 class="card-heading">Our Philosophy</h2>
          <p class="about-text small">
            We believe travel is more than sightseeing. It’s about connecting with
            people, understanding cultures, and preserving the stories of the past.
            Every journey should leave a positive impact.
          </p>
        </div>

        <div class="grid-card">
          <h2 class="card-heading">Our Commitment</h2>
          <p class="about-text small">
            Indoria Journey is committed to responsible and sustainable travel.
            We strive to respect local traditions, reduce environmental impact, and
            support local economies through mindful tourism.
          </p>
        </div>

        <div class="grid-card full-width">
          <h2 class="card-heading">Why Choose Us</h2>
          <p class="about-text small">
            We combine authentic experiences, expert guidance, and carefully
            curated itineraries to ensure your journey is enriching, safe, and
            unforgettable. Whether it’s exploring hidden gems or understanding
            cultural heritage, we make every trip meaningful.
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* ================= PAGE WRAPPER ================= */
.about-page {
  min-height: 100vh;
  padding: 8rem 1.5rem;
  position: relative;
  z-index: 10;
  display: flex;
  justify-content: center;
  overflow-x: hidden;
  background: linear-gradient(180deg, #1a2421 0%, #0d1311 100%);
  color: #f0ede4;
}

.bento-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
  opacity: 0.4;
}

/* ================= CONTENT CONTAINER ================= */
.about-container {
  position: relative;
  z-index: 5;
  max-width: 1000px;
  width: 100%;
}

.about-header {
  text-align: center;
  margin-bottom: 5rem;
}

/* ================= TYPOGRAPHY ================= */
.about-heading {
  font-family: Georgia, "Times New Roman", serif;
  font-size: clamp(2.5rem, 8vw, 4rem);
  font-weight: 700;
  margin-bottom: 2.5rem;
  background: linear-gradient(90deg, #f3c969, #fff1c1, #e8b34b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.about-text {
  font-family: "Inter", system-ui, sans-serif;
  font-size: 1.2rem;
  line-height: 1.8;
  margin-bottom: 1.5rem;
  color: rgba(245, 230, 200, 0.9);
  max-width: 800px;
  margin-inline: auto;
}

.about-text.secondary {
  font-style: italic;
  opacity: 0.8;
}

/* ================= GRID LAYOUT ================= */
.about-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
  margin-top: 4rem;
}

.grid-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(243, 201, 105, 0.1);
  padding: 2.5rem;
  border-radius: 1.5rem;
  backdrop-filter: blur(10px);
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.grid-card:hover {
  transform: translateY(-5px);
  border-color: rgba(243, 201, 105, 0.3);
  background: rgba(255, 255, 255, 0.05);
}

.full-width {
  grid-column: span 2;
}

.card-heading {
  font-family: Georgia, serif;
  font-size: 1.75rem;
  color: #f3c969;
  margin-bottom: 1rem;
}

.about-text.small {
  font-size: 1.05rem;
  line-height: 1.6;
  margin-bottom: 0;
}

/* ================= MOBILE STYLES ================= */
@media (max-width: 768px) {
  .about-page {
    background: linear-gradient(180deg, #1e1a15 0%, #13100d 100%);
    padding: 6rem 1.25rem;
  }

  .about-header {
    margin-bottom: 3rem;
  }

  .about-grid {
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .full-width {
    grid-column: span 1;
  }

  .grid-card {
    padding: 1.5rem;
  }
}
</style>
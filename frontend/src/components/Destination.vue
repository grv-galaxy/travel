<!-- <template>
  <section id="destination-section" class="destinations">
    <div class="container">
      <div class="section-header">
        <p class="brand-gold-text subtitle">Explore the World</p>
        <h1 class="title font-serif">Our Top Destinations</h1>
        <p class="description">
          From serene beaches to majestic mountains, discover the handpicked locations 
          we offer for your next unforgettable journey.
        </p>
      </div>

      <div class="filter-bar">
        <button 
          v-for="cat in categories" 
          :key="cat"
          :class="['filter-btn', { active: activeCategory === cat }]"
          @click="activeCategory = cat"
        >
          {{ cat }}
        </button>
      </div>

      <div class="destination-grid">
        <TransitionGroup name="grid-fade">
          <div 
            v-for="(place, index) in filteredDestinations" 
            :key="place.id" 
            class="dest-card"
          >
            <div class="image-wrapper">
              <img :src="place.image" :alt="place.name" loading="lazy" />
              <div class="badge">{{ place.category }}</div>
              <div class="overlay">
                <button class="view-btn" @click="openDetails(place.id)">View Details</button>
              </div>
            </div>
            
            <div class="dest-info">
              <div class="price-row">
                <span class="location">
                  <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-width="2"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-width="2"/></svg>
                  {{ place.location }}
                </span>
                <span class="price">From ₹{{ place.price }}</span>
              </div>
              <h3 class="font-serif">{{ place.name }}</h3>
              <p>{{ place.excerpt }}</p>
              
              <div class="card-footer">
                <span class="rating">
                  <span class="stars">★★★★★</span>
                  <span class="review-count">(4.9)</span>
                </span>
              </div>
            </div>
          </div>
        </TransitionGroup>
      </div>
    </div>

    <Transition name="modal-fade">
      <div v-if="selectedTrip" class="details-modal" @click.self="closeDetails">
        <div class="modal-inner">
          <button class="close-modal" @click="closeDetails">
            <i class="fas fa-times"></i>
          </button>

          <div class="modal-hero" :style="{ backgroundImage: `url(${selectedTrip.image})` }">
            <div class="hero-content">
              <div class="badge">{{ selectedTrip.category }}</div>
              <h2 class="font-serif">{{ selectedTrip.name }}</h2>
              <div class="hero-meta">
                <span><i class="fas fa-map-marker-alt"></i> {{ selectedTrip.location }}</span>
                <span><i class="fas fa-tag"></i> Starting from ₹{{ selectedTrip.price }}</span>
              </div>
            </div>
          </div>

          <div class="modal-body">
            <div class="details-grid">
              <div class="description-side">
                <h4 class="brand-gold-text">The Experience</h4>
                <p class="full-description">{{ selectedTrip.description }}</p>
                
                <div class="trip-stats">
                  <div class="stat"><i class="fas fa-sun"></i> {{ selectedTrip.weather }}</div>
                  <div class="stat"><i class="fas fa-thermometer-half"></i> {{ selectedTrip.temp }}°C</div>
                  <div class="stat"><i class="fas fa-users"></i> {{ selectedTrip.activeVips }} VIPs Present</div>
                </div>
              </div>

              <div class="itinerary-side">
                <h4 class="brand-gold-text">Strategic Journey Plan</h4>
                <div class="itinerary-timeline">
                  <div v-for="step in selectedTrip.itinerary" :key="step.day" class="timeline-item">
                    <div class="day-marker">Day {{ step.day }}</div>
                    <div class="step-content">
                      <h5>{{ step.title }}</h5>
                      <p>{{ step.activity }}</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="modal-footer">
            <button class="book-now-btn" @click="scrollToInquiry">Request Personalized Proposal</button>
          </div>
        </div>
      </div>
    </Transition>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

const activeCategory = ref('All');
const categories = ['All', 'Beach', 'Mountain', 'City', 'Cultural'];
const destinations = ref([]);
const selectedTrip = ref(null);
const isLoading = ref(true);

const fetchPublicDestinations = async () => {
  isLoading.value = true;
  try {
    const response = await axios.get('https://travel-xxnc.onrender.com/api/admin/destinations');
    if (response.data.success) {
      destinations.value = response.data.data;
    }
  } catch (error) {
    console.error("Public Feed Error:", error);
  } finally {
    isLoading.value = false;
  }
};

// Fetch specific trip details including itinerary from the new table
const openDetails = async (id) => {
  try {
    const response = await axios.get(`https://travel-xxnc.onrender.com/api/admin/destinations/${id}/details`);
    if (response.data.success) {
      selectedTrip.value = response.data.data;
      document.body.style.overflow = 'hidden'; // Stop scrolling
    }
  } catch (error) {
    console.error("Details Fetch Error:", error);
    alert("Unable to retrieve trip intelligence at this time.");
  }
};

const closeDetails = () => {
  selectedTrip.value = null;
  document.body.style.overflow = 'auto'; // Resume scrolling
};

const scrollToInquiry = () => {
  closeDetails();
  document.getElementById('contact-section').scrollIntoView({ behavior: 'smooth' });
};

const filteredDestinations = computed(() => {
  if (activeCategory.value === 'All') return destinations.value;
  return destinations.value.filter(d => d.category === activeCategory.value);
});

onMounted(fetchPublicDestinations);
</script>



<style scoped>
/* HERITAGE LUXURY THEME */
.destinations {
  padding: 100px 0;
  background-color: #fcf9f4; /* Heritage Cream */
  color: #1a150e; /* Deep Charcoal */
}

.container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 2rem;
}

.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

/* Header Section */
.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.brand-gold-text {
  background: linear-gradient(90deg, #f3c969, #e8b34b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subtitle {
  text-transform: uppercase;
  letter-spacing: 0.3em;
  font-size: 0.75rem;
  font-weight: 800;
  margin-bottom: 1rem;
}

.title {
  font-size: 3.2rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}

.description {
  max-width: 650px;
  margin: 0 auto;
  color: #64748b;
  line-height: 1.8;
  font-size: 1.1rem;
}

/* Filter Bar */
.filter-bar {
  display: flex;
  justify-content: center;
  gap: 1.25rem;
  margin-bottom: 4rem;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 0.75rem 2rem;
  border: 1px solid rgba(243, 201, 105, 0.3);
  background: white;
  border-radius: 50px;
  cursor: pointer;
  font-weight: 700;
  font-size: 0.85rem;
  color: #475569;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

.filter-btn.active, .filter-btn:hover {
  background: #1a150e;
  color: #f3c969;
  border-color: #1a150e;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}

/* Card Grid */
.destination-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 3rem;
}

.dest-card {
  background: white;
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid rgba(243, 201, 105, 0.1);
  transition: all 0.4s ease;
}

.dest-card:hover {
  transform: translateY(-15px);
  box-shadow: 0 30px 60px -15px rgba(26, 21, 14, 0.15);
}

.image-wrapper {
  position: relative;
  height: 280px;
  overflow: hidden;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.8s ease;
}

.dest-card:hover .image-wrapper img {
  transform: scale(1.1);
}

.badge {
  position: absolute;
  top: 1.5rem;
  left: 1.5rem;
  background: #1a150e;
  color: #f3c969;
  padding: 0.5rem 1.25rem;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.overlay {
  position: absolute;
  inset: 0;
  background: rgba(26, 21, 14, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  backdrop-filter: blur(4px);
  transition: 0.4s ease;
}

.image-wrapper:hover .overlay {
  opacity: 1;
}

.view-btn {
  padding: 1rem 2rem;
  background: linear-gradient(90deg, #f3c969, #e8b34b);
  border: none;
  border-radius: 12px;
  font-weight: 800;
  color: #1a150e;
  text-transform: uppercase;
  font-size: 0.8rem;
  cursor: pointer;
  box-shadow: 0 10px 20px rgba(243, 201, 105, 0.3);
}

/* Info Section */
.dest-info {
  padding: 2rem;
}

.price-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.location {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: #e8b34b;
  font-weight: 700;
  font-size: 0.85rem;
}

.icon {
  width: 1rem;
  height: 1rem;
}

.price {
  font-weight: 800;
  color: #1a150e;
  font-size: 1rem;
}

.dest-info h3 {
  font-size: 1.6rem;
  margin-bottom: 1rem;
  color: #1a150e;
}

.dest-info p {
  font-size: 1rem;
  color: #64748b;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.card-footer {
  border-top: 1px solid #f1f5f9;
  padding-top: 1.5rem;
}

.stars {
  color: #f3c969;
  letter-spacing: 2px;
}

.review-count {
  margin-left: 0.5rem;
  font-size: 0.85rem;
  font-weight: 700;
  color: #94a3b8;
}

/* Animations */
.grid-fade-enter-active, .grid-fade-leave-active {
  transition: all 0.5s ease;
}
.grid-fade-enter-from, .grid-fade-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

/* Responsive */
@media (max-width: 1024px) {
  .destination-grid {
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  }
}

@media (max-width: 768px) {
  .title {
    font-size: 2.4rem;
  }
  .container {
    padding: 0 1.5rem;
  }
}






.details-modal {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(12px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-inner {
  background: #0a0a0a;
  width: 100%;
  max-width: 1000px;
  height: 90vh;
  border-radius: 24px;
  overflow-y: auto;
  border: 1px solid rgba(197, 160, 89, 0.2);
  position: relative;
  box-shadow: 0 0 50px rgba(0,0,0,1);
}

.modal-hero {
  height: 400px;
  background-size: cover;
  background-position: center;
  position: relative;
}

.hero-content {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, #0a0a0a 10%, transparent 90%);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 40px;
}

.hero-content h2 {
  font-size: clamp(2rem, 5vw, 3.5rem);
  color: white;
  margin: 10px 0;
}

.hero-meta {
  display: flex;
  gap: 20px;
  color: #c5a059;
  font-weight: 600;
  font-size: 0.9rem;
}

.modal-body {
  padding: 40px;
}

.details-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
}

.itinerary-timeline {
  border-left: 1px solid #c5a059;
  padding-left: 30px;
  margin-top: 20px;
}

.timeline-item {
  position: relative;
  margin-bottom: 30px;
}

.day-marker {
  position: absolute;
  left: -42px;
  background: #c5a059;
  color: black;
  font-size: 0.6rem;
  font-weight: 900;
  padding: 4px 8px;
  border-radius: 4px;
  text-transform: uppercase;
}

.step-content h5 {
  color: #fff;
  margin-bottom: 5px;
}

.step-content p {
  color: #888;
  font-size: 0.9rem;
  line-height: 1.6;
}

.book-now-btn {
  background: #c5a059;
  color: black;
  width: 100%;
  padding: 20px;
  font-weight: 800;
  border-radius: 12px;
  text-transform: uppercase;
  letter-spacing: 2px;
  cursor: pointer;
  transition: 0.3s;
}

.close-modal {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 10;
  background: white;
  color: black;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
}

/* Animations */
.modal-fade-enter-active, .modal-fade-leave-active { transition: opacity 0.4s ease; }
.modal-fade-enter-from, .modal-fade-leave-to { opacity: 0; }

/* Responsive */
@media (max-width: 768px) {
  .details-grid { grid-template-columns: 1fr; }
  .modal-hero { height: 250px; }
}
</style> -->

































<template>
  <section id="destination-section" class="destinations">
    <div class="container">
      <div class="section-header">
        <p class="brand-gold-text subtitle">Explore the World</p>
        <h1 class="title font-serif">Our Top Destinations</h1>
        <p class="description">
          From serene beaches to majestic mountains, discover the handpicked locations 
          we offer for your next unforgettable journey.
        </p>
      </div>

      <div class="filter-bar">
        <button 
          v-for="cat in categories" 
          :key="cat"
          :class="['filter-btn', { active: activeCategory === cat }]"
          @click="activeCategory = cat"
        >
          {{ cat }}
        </button>
      </div>

      <div class="destination-grid">
        <TransitionGroup name="grid-fade">
          <div 
            v-for="(place, index) in filteredDestinations" 
            :key="place.id" 
            class="dest-card"
          >
            <div class="image-wrapper">
              <img :src="place.image" :alt="place.name" loading="lazy" />
              <div class="badge">{{ place.category }}</div>
              <div class="overlay">
                <button class="view-btn" @click="openDetails(place.id)">View Details</button>
              </div>
            </div>
            
            <div class="dest-info">
              <div class="price-row">
                <span class="location">
                  <svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" stroke-width="2"/><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" stroke-width="2"/></svg>
                  {{ place.location }}
                </span>
                <span class="price">From ₹{{ place.price }}</span>
              </div>
              <h3 class="font-serif">{{ place.name }}</h3>
              <p>{{ place.excerpt }}</p>
              
              <div class="card-footer">
                <span class="rating">
                  <span class="stars">★★★★★</span>
                  <span class="review-count">(4.9)</span>
                </span>
              </div>
            </div>
          </div>
        </TransitionGroup>
      </div>
    </div>

    <Transition name="modal-fade">
      <div v-if="isModalOpen" class="details-modal" @click.self="closeDetails">
        <div class="modal-inner">
          <button class="close-modal" @click="closeDetails">
            <i class="fas fa-times"></i>
          </button>

          <div v-if="isModalLoading" class="skeleton-wrapper">
            <div class="skeleton-hero shimmer"></div>
            <div class="modal-body">
              <div class="details-grid">
                <div class="description-side">
                  <div class="skeleton-line shimmer title"></div>
                  <div class="skeleton-line shimmer text"></div>
                  <div class="skeleton-line shimmer text"></div>
                  <div class="skeleton-stats-row">
                    <div class="skeleton-stat shimmer" v-for="n in 3" :key="n"></div>
                  </div>
                </div>
                <div class="itinerary-side">
                  <div class="skeleton-line shimmer title"></div>
                  <div class="skeleton-timeline-box shimmer" v-for="n in 3" :key="n"></div>
                </div>
              </div>
            </div>
          </div>

          <template v-else-if="selectedTrip">
            <div class="modal-hero" :style="{ backgroundImage: `url(${selectedTrip.image})` }">
              <div class="hero-content">
                <div class="badge">{{ selectedTrip.category }}</div>
                <h2 class="font-serif">{{ selectedTrip.name }}</h2>
                <div class="hero-meta">
                  <span><i class="fas fa-map-marker-alt"></i> {{ selectedTrip.location }}</span>
                  <span><i class="fas fa-tag"></i> Starting from ₹{{ selectedTrip.price }}</span>
                </div>
              </div>
            </div>

            <div class="modal-body">
              <div class="details-grid">
                <div class="description-side">
                  <h4 class="brand-gold-text">The Experience</h4>
                  <p class="full-description">{{ selectedTrip.description }}</p>
                  
                  <div class="trip-stats">
                    <div class="stat"><i class="fas fa-sun"></i> {{ selectedTrip.weather }}</div>
                    <div class="stat"><i class="fas fa-thermometer-half"></i> {{ selectedTrip.temp }}°C</div>
                    <div class="stat"><i class="fas fa-users"></i> {{ selectedTrip.activeVips }} VIPs Present</div>
                  </div>
                </div>

                <div class="itinerary-side">
                  <h4 class="brand-gold-text">Strategic Journey Plan</h4>
                  <div class="itinerary-timeline">
                    <div v-for="step in selectedTrip.itinerary" :key="step.day" class="timeline-item">
                      <div class="day-marker">Day {{ step.day }}</div>
                      <div class="step-content">
                        <h5>{{ step.title }}</h5>
                        <p>{{ step.activity }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="modal-footer">
              <button class="book-now-btn" @click="scrollToInquiry">Request Personalized Proposal</button>
            </div>
          </template>
        </div>
      </div>
    </Transition>
  </section>
</template>



<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

// --- State Variables ---
const activeCategory = ref('All');
const categories = ['All', 'Beach', 'Mountain', 'City', 'Cultural'];
const destinations = ref([]); // The main list
const selectedTrip = ref(null); // The specific trip data for the modal

// Loading States
const isLoading = ref(true);       // Loading for the main grid
const isModalOpen = ref(false);    // Controls if the modal is visible
const isModalLoading = ref(false); // Controls the skeleton inside the modal

// --- Actions ---

// Fetch the main grid of destinations
const fetchPublicDestinations = async () => {
  isModalLoading.value = true;
  try {
    const response = await axios.get('https://travel-xxnc.onrender.com/api/admin/destinations');
    if (response.data.success) {
      destinations.value = response.data.data;
    }
  } catch (error) {
    console.error("Public Feed Error:", error);
  } finally {
    isModalLoading.value = false;
  }
};

// Fetch specific trip details with Skeleton Loading
const openDetails = async (id) => {
  // 1. Instantly open the modal and show the skeleton
  isModalOpen.value = true;
  isModalLoading.value = true;
  selectedTrip.value = null; // Clear any old data
  document.body.style.overflow = 'hidden'; // Stop background scrolling

  try {
    // 2. Fetch the detailed intelligence
    const response = await axios.get(`https://travel-xxnc.onrender.com/api/admin/destinations/${id}/details`);
    
    if (response.data.success) {
      // 3. Populate data and hide skeleton
      selectedTrip.value = response.data.data;
    }
  } catch (error) {
    console.error("Details Fetch Error:", error);
    // If it fails, close the modal so the user isn't stuck on a loader
    isModalOpen.value = false;
    alert("Unable to retrieve trip intelligence at this time.");
  } finally {
    // 4. End the loading state
    isModalLoading.value = false;
  }
};

const closeDetails = () => {
  isModalOpen.value = false;
  selectedTrip.value = null;
  isModalLoading.value = false;
  document.body.style.overflow = 'auto'; // Resume scrolling
};

const scrollToInquiry = () => {
  closeDetails();
  // Ensure the element exists before scrolling
  const contactSection = document.getElementById('contact-section');
  if (contactSection) {
    contactSection.scrollIntoView({ behavior: 'smooth' });
  }
};

// --- Computed ---
const filteredDestinations = computed(() => {
  if (activeCategory.value === 'All') return destinations.value;
  return destinations.value.filter(d => d.category === activeCategory.value);
});

onMounted(fetchPublicDestinations);
</script>







<style scoped>
/* HERITAGE LUXURY THEME */
.destinations {
  padding: 100px 0;
  background-color: #fcf9f4; /* Heritage Cream */
  color: #1a150e; /* Deep Charcoal */
}

.container {
  max-width: 1240px;
  margin: 0 auto;
  padding: 0 2rem;
}

.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

/* Header Section */
.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.brand-gold-text {
  background: linear-gradient(90deg, #f3c969, #e8b34b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.subtitle {
  text-transform: uppercase;
  letter-spacing: 0.3em;
  font-size: 0.75rem;
  font-weight: 800;
  margin-bottom: 1rem;
}

.title {
  font-size: 3.2rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}

.description {
  max-width: 650px;
  margin: 0 auto;
  color: #64748b;
  line-height: 1.8;
  font-size: 1.1rem;
}

/* Filter Bar */
.filter-bar {
  display: flex;
  justify-content: center;
  gap: 1.25rem;
  margin-bottom: 4rem;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 0.75rem 2rem;
  border: 1px solid rgba(243, 201, 105, 0.3);
  background: white;
  border-radius: 50px;
  cursor: pointer;
  font-weight: 700;
  font-size: 0.85rem;
  color: #475569;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

.filter-btn.active, .filter-btn:hover {
  background: #1a150e;
  color: #f3c969;
  border-color: #1a150e;
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}

/* Card Grid */
.destination-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 3rem;
}

.dest-card {
  background: white;
  border-radius: 24px;
  overflow: hidden;
  border: 1px solid rgba(243, 201, 105, 0.1);
  transition: all 0.4s ease;
}

.dest-card:hover {
  transform: translateY(-15px);
  box-shadow: 0 30px 60px -15px rgba(26, 21, 14, 0.15);
}

.image-wrapper {
  position: relative;
  height: 280px;
  overflow: hidden;
}

.image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.8s ease;
}

.dest-card:hover .image-wrapper img {
  transform: scale(1.1);
}

.badge {
  position: absolute;
  top: 1.5rem;
  left: 1.5rem;
  background: #1a150e;
  color: #f3c969;
  padding: 0.5rem 1.25rem;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.overlay {
  position: absolute;
  inset: 0;
  background: rgba(26, 21, 14, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  backdrop-filter: blur(4px);
  transition: 0.4s ease;
}

.image-wrapper:hover .overlay {
  opacity: 1;
}

.view-btn {
  padding: 1rem 2rem;
  background: linear-gradient(90deg, #f3c969, #e8b34b);
  border: none;
  border-radius: 12px;
  font-weight: 800;
  color: #1a150e;
  text-transform: uppercase;
  font-size: 0.8rem;
  cursor: pointer;
  box-shadow: 0 10px 20px rgba(243, 201, 105, 0.3);
}

/* Info Section */
.dest-info {
  padding: 2rem;
}

.price-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.location {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: #e8b34b;
  font-weight: 700;
  font-size: 0.85rem;
}

.icon {
  width: 1rem;
  height: 1rem;
}

.price {
  font-weight: 800;
  color: #1a150e;
  font-size: 1rem;
}

.dest-info h3 {
  font-size: 1.6rem;
  margin-bottom: 1rem;
  color: #1a150e;
}

.dest-info p {
  font-size: 1rem;
  color: #64748b;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.card-footer {
  border-top: 1px solid #f1f5f9;
  padding-top: 1.5rem;
}

.stars {
  color: #f3c969;
  letter-spacing: 2px;
}

.review-count {
  margin-left: 0.5rem;
  font-size: 0.85rem;
  font-weight: 700;
  color: #94a3b8;
}

/* Animations */
.grid-fade-enter-active, .grid-fade-leave-active {
  transition: all 0.5s ease;
}
.grid-fade-enter-from, .grid-fade-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

/* Responsive */
@media (max-width: 1024px) {
  .destination-grid {
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  }
}

@media (max-width: 768px) {
  .title {
    font-size: 2.4rem;
  }
  .container {
    padding: 0 1.5rem;
  }
}






.details-modal {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.95);
  backdrop-filter: blur(12px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-inner {
  background: #0a0a0a;
  width: 100%;
  max-width: 1000px;
  height: 90vh;
  border-radius: 24px;
  overflow-y: auto;
  border: 1px solid rgba(197, 160, 89, 0.2);
  position: relative;
  box-shadow: 0 0 50px rgba(0,0,0,1);
}

.modal-hero {
  height: 400px;
  background-size: cover;
  background-position: center;
  position: relative;
}

.hero-content {
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, #0a0a0a 10%, transparent 90%);
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 40px;
}

.hero-content h2 {
  font-size: clamp(2rem, 5vw, 3.5rem);
  color: white;
  margin: 10px 0;
}

.hero-meta {
  display: flex;
  gap: 20px;
  color: #c5a059;
  font-weight: 600;
  font-size: 0.9rem;
}

.modal-body {
  padding: 40px;
}

.details-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 60px;
}

.itinerary-timeline {
  border-left: 1px solid #c5a059;
  padding-left: 30px;
  margin-top: 20px;
}

.timeline-item {
  position: relative;
  margin-bottom: 30px;
}

.day-marker {
  position: absolute;
  left: -42px;
  background: #c5a059;
  color: black;
  font-size: 0.6rem;
  font-weight: 900;
  padding: 4px 8px;
  border-radius: 4px;
  text-transform: uppercase;
}

.step-content h5 {
  color: #fff;
  margin-bottom: 5px;
}

.step-content p {
  color: #888;
  font-size: 0.9rem;
  line-height: 1.6;
}

.book-now-btn {
  background: #c5a059;
  color: black;
  width: 100%;
  padding: 20px;
  font-weight: 800;
  border-radius: 12px;
  text-transform: uppercase;
  letter-spacing: 2px;
  cursor: pointer;
  transition: 0.3s;
}

.close-modal {
  position: absolute;
  top: 20px;
  right: 20px;
  z-index: 10;
  background: white;
  color: black;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
}

/* Animations */
.modal-fade-enter-active, .modal-fade-leave-active { transition: opacity 0.4s ease; }
.modal-fade-enter-from, .modal-fade-leave-to { opacity: 0; }

/* Responsive */
@media (max-width: 768px) {
  .details-grid { grid-template-columns: 1fr; }
  .modal-hero { height: 250px; }
}



/* --- SKELETON LOADING STYLES --- */

/* --- LUXURY PRODUCTION-READY SKELETON --- */

.skeleton-wrapper {
  width: 100%;
  background: #121212; /* Deepest background */
}

.shimmer {
  /* Base color: Soft Charcoal instead of solid black */
  background: #1E1E1E;
  
  /* The "Wave": A blend of light white/silver with a hint of gold */
  background-image: linear-gradient(
    95deg, 
    rgba(255, 255, 255, 0) 0%, 
    rgba(255, 255, 255, 0.03) 30%, 
    rgba(255, 255, 255, 0.08) 50%, 
    rgba(255, 255, 255, 0.03) 70%, 
    rgba(255, 255, 255, 0) 100%
  );
  
  background-size: 200% 100%;
  /* Faster, smoother wave like YouTube/Instagram */
  animation: luxury-wave 1.6s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}

@keyframes luxury-wave {
  0% { background-position: 150% 0; }
  100% { background-position: -150% 0; }
}

/* --- REFINED SHAPES --- */

.skeleton-hero {
  height: 380px;
  width: 100%;
  border-radius: 0 0 30px 30px;
  border-bottom: 1px solid rgba(243, 201, 105, 0.1); /* Very faint gold edge */
}

.skeleton-line {
  background: #1E1E1E;
  border-radius: 12px;
  margin-bottom: 1.2rem;
}

.skeleton-line.title {
  height: 28px;
  width: 45%;
}

.skeleton-line.text {
  height: 12px;
  width: 100%;
  opacity: 0.6; /* Soften the body text placeholders */
}

.skeleton-stat {
  height: 70px;
  flex: 1;
  background: #1E1E1E;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.03);
}

.skeleton-timeline-box {
  height: 90px;
  width: 100%;
  background: #1E1E1E;
  margin-bottom: 1.5rem;
  border-radius: 20px;
}

/* Staggered delay for a more natural "wave" feel across the page */
.skeleton-line:nth-child(2) { animation-delay: 0.1s; }
.skeleton-line:nth-child(3) { animation-delay: 0.2s; }
.skeleton-stat:nth-child(2) { animation-delay: 0.15s; }







/* --- PRODUCTION-READY DESCRIPTION STYLE --- */
.full-description {
  font-size: 1.15rem;
  line-height: 1.9;          /* Increased for luxury readability */
  color: #b0b0b0;           /* Soft silver-grey for dark mode */
  font-weight: 400;
  margin-bottom: 2.5rem;
  white-space: pre-line;    /* Preserves line breaks from your DB */
  text-align: justify;      /* Cleaner editorial look */
  letter-spacing: 0.015em;
  max-width: 100%;
}

/* Responsive adjustment for Mobile */
@media (max-width: 768px) {
  .full-description {
    font-size: 1.05rem;
    line-height: 1.7;
    text-align: left;       /* Better for small screens */
    margin-bottom: 2rem;
  }
}









/* --- MINIMALIST HIGHLIGHTED TRIP STATS --- */
.trip-stats {
  display: flex;
  gap: 25px;
  margin-top: 25px;
  padding: 15px 0;
  border-top: 1px solid rgba(197, 160, 89, 0.1);
  border-bottom: 1px solid rgba(197, 160, 89, 0.1);
}

.stat {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #e0e0e0; /* Much brighter light grey/white */
  font-size: 0.95rem;
  font-weight: 500;
}

/* The Highlight: Gold Icons */
.stat i {
  color: #f3c969; /* Bright Gold */
  font-size: 1rem;
  filter: drop-shadow(0 0 5px rgba(243, 201, 105, 0.2));
}

/* Subtle separator between items */
.stat:not(:last-child)::after {
  content: "";
  height: 15px;
  width: 1px;
  background: rgba(197, 160, 89, 0.3);
  margin-left: 15px;
}

/* Responsive: Stack them neatly on mobile */
@media (max-width: 600px) {
  .trip-stats {
    flex-direction: column;
    gap: 12px;
    border: none;
    background: rgba(255, 255, 255, 0.03);
    padding: 20px;
    border-radius: 12px;
  }
  
  .stat:not(:last-child)::after {
    display: none;
  }
}
</style>
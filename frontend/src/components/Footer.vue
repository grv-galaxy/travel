<template>
  <footer class="footer">
    <div class="footer-container">
      <div class="footer-column bio">
        <div class="logo">
          <span class="logo-icon"></span>
          <span class="logo-text font-serif">INDORIA<span>JOURNEYS</span></span>
        </div>
        <p class="footer-description">
          Crafting unforgettable journeys since 2010. We specialize in bespoke travel experiences that connect you with the heart of every destination.
        </p>
        <div class="social-links">
          <a href="https://www.facebook.com/YourPageName" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
            <i class="fab fa-facebook-f"></i>
          </a>
          <a href="https://www.instagram.com/yourprofile/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
            <i class="fab fa-instagram"></i>
          </a>
          <a href="https://twitter.com/yourhandle" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
            <i class="fab fa-twitter"></i>
          </a>
          <a href="https://www.linkedin.com/company/yourcompany/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
            <i class="fab fa-linkedin-in"></i>
          </a>
        </div>
      </div>

      <div class="footer-column">
        <h3>Quick Links</h3>
        <ul class="footer-links">
          <li><a href="/" @click.prevent="scrollToTop">Home</a></li>
          <li><a href="#about-section">About Us</a></li>
          <li><a href="#destination-section">Destinations</a></li>
          <li><a href="#contact-section">Contact</a></li>
        </ul>
      </div>

      <div class="footer-column">
        <h3>Our Services</h3>
        <ul class="footer-links">
          <li><router-link to="/train-booking">Train Reservations</router-link></li>
          <li><router-link to="/travel-insurance">Travel Insurance</router-link></li>
          <li><router-link to="/custom-itinerary">Custom Itineraries</router-link></li>
          <li><router-link to="/guide">Guided Tours</router-link></li>
        </ul>
      </div>

      <div class="footer-column contact">
        <h3>Get In Touch</h3>
        <p><i class="fas fa-map-marker-alt"></i> 123 Travel Way, West 500<br>New Delhi, IND 110041</p>
        <p><i class="fas fa-phone"></i> +91 8881234567</p>
        <p><i class="fas fa-envelope"></i> contact@indoriajourneys.com</p>
        
        <div class="newsletter">
          <h4>Subscribe to our Newsletter</h4>
          <form @submit.prevent="handleSubscribe">
            <input type="email" placeholder="Your Email" required />
            <button type="submit">Join</button>
          </form>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="bottom-container">
        <p>&copy; 2025 IndoriaJourneys. All rights reserved.</p>
        <div class="legal-links">
          <router-link to="/privacy">Privacy Policy</router-link>
          <span class="divider">|</span>
          <router-link to="/terms">Terms of Service</router-link>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  methods: {
    scrollToTop() {
      window.requestAnimationFrame(() => {
        window.scrollTo({ 
          top: 0,
          left: 0,
          behavior: 'smooth' 
        });
      });
    },
    handleSubscribe() {
      alert("Thank you for subscribing!");
    }
  }
};
</script>

<style scoped>
.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

.footer {
  background-color: #1a150e; /* Updated to brand Charcoal */
  color: #e5e7eb;
  padding-top: 80px;
  font-family: 'Inter', sans-serif;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: grid;
  grid-template-columns: 2fr 1fr 1fr 2fr;
  gap: 40px;
}

/* Bio Section */
.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}
.logo-icon {
  width: 35px;
  height: 35px;
  background: url("../assets/images/LOGO.jpg") center / contain no-repeat;
  filter: brightness(1.1) contrast(1.1); /* Slight polish for the dark bg */
}
.logo-text {
  font-weight: bold;
  font-size: 1.4rem;
  letter-spacing: 1px;
}
.logo-text span {
  color: #f3c969; /* Updated to brand Gold */
}

.footer-description {
  line-height: 1.8;
  font-size: 0.95rem;
  color: #94a3b8; /* Better contrast for dark theme */
  margin-bottom: 25px;
}

/* Social Icons */
.social-links {
  display: flex;
  gap: 15px;
}
.social-links a {
  width: 40px;
  height: 40px;
  background: rgba(243, 201, 105, 0.1); /* Subtle gold tint */
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  color: white;
  transition: 0.3s;
  text-decoration: none;
}
.social-links a:hover {
  background: #f3c969; /* Updated to brand Gold */
  color: #1a150e; /* Text becomes charcoal on hover */
  transform: translateY(-3px);
}

/* Column Headers */
h3 {
  color: white;
  font-size: 1.1rem;
  margin-bottom: 25px;
  font-weight: 600;
  position: relative;
}
h3::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -8px;
  width: 30px;
  height: 2px;
  background: #f3c969; /* Updated to brand Gold */
}

/* Links */
.footer-links {
  list-style: none;
  padding: 0;
}
.footer-links li {
  margin-bottom: 12px;
}
.footer-links a {
  color: #94a3b8;
  text-decoration: none;
  font-size: 0.95rem;
  transition: 0.3s;
}
.footer-links a:hover {
  color: #f3c969; /* Updated to brand Gold */
  padding-left: 5px;
}

/* Newsletter & Contact */
.contact p {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  margin-bottom: 15px;
  color: #94a3b8;
  font-size: 0.95rem;
}
.contact i {
  color: #f3c969; /* Updated to brand Gold */
  margin-top: 4px;
}

.newsletter {
  margin-top: 30px;
}
.newsletter h4 {
  font-size: 0.9rem;
  margin-bottom: 15px;
  color: white;
}
.newsletter form {
  display: flex;
  gap: 0;
}
.newsletter input {
  background: #2b241a; /* Dark warm brown for inputs */
  border: 1px solid rgba(243, 201, 105, 0.2); /* Subtle gold border */
  padding: 10px 15px;
  color: white;
  border-radius: 4px 0 0 4px;
  width: 100%;
}
.newsletter button {
  background: #f3c969; /* Updated to brand Gold */
  color: #1a150e;
  border: none;
  padding: 0 20px;
  border-radius: 0 4px 4px 0;
  font-weight: bold;
  cursor: pointer;
  transition: 0.3s;
}
.newsletter button:hover {
  background: #e8b34b; /* Slightly darker gold on hover */
}

/* Footer Bottom */
.footer-bottom {
  margin-top: 60px;
  border-top: 1px solid rgba(243, 201, 105, 0.1); /* Gold-tinted border */
  padding: 25px 0;
}
.bottom-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.85rem;
  color: #64748b;
}
.legal-links a {
  color: #64748b;
  text-decoration: none;
  transition: 0.3s;
}
.legal-links a:hover {
  color: #f3c969;
}
.divider {
  margin: 0 10px;
  color: rgba(243, 201, 105, 0.2);
}

/* Responsive */
@media (max-width: 1024px) {
  .footer-container {
    grid-template-columns: 1fr 1fr;
    gap: 50px;
  }
}
@media (max-width: 640px) {
  .footer-container {
    grid-template-columns: 1fr;
  }
  .bottom-container {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }
}
</style>
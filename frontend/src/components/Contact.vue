<template>
  <section id="contact-section" class="contact-page">
    <div class="container">
      <div class="contact-wrapper">
        
        <div class="contact-form-container">
          <h2 class="section-title font-serif">Plan Your Dream Trip</h2>
          <p class="description">Fill out the form below and our travel experts will get back to you within 24 hours.</p>

          <form @submit.prevent="handleSubmit" class="contact-form">
            <div class="form-group">
              <input type="text" v-model="form.name" placeholder="Full Name" required />
            </div>

            <div class="form-row">
              <div class="form-group">
                <input type="email" v-model="form.email" placeholder="Email Address" required />
              </div>
              <div class="form-group">
                <input type="tel" v-model="form.phone" placeholder="Phone (e.g. +91 000...)" required />
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <select v-model="form.destination" required>
                  <option value="" disabled selected>Destination of Interest</option>
                  <option value="domestic">Domestic (India)</option>
                  <option value="international">International</option>
                  <option value="adventure">Adventure Tours</option>
                  <option value="honeymoon">Honeymoon Packages</option>
                </select>
              </div>
              <div class="form-group">
                <input type="number" v-model="form.travelers" placeholder="No. of Travelers" min="1" />
              </div>
            </div>

            <div class="form-group">
              <textarea v-model="form.message" rows="4" placeholder="Tell us about your travel plans..."></textarea>
            </div>

            <button type="submit" class="submit-btn" :disabled="isSubmitting">
              {{ isSubmitting ? 'Sending...' : 'Send Inquiry' }}
            </button>
          </form>
        </div>

        <div class="contact-info-container">
          <div class="info-card">
            <h3 class="font-serif brand-gold-text">Contact Information</h3>
            <div class="info-item">
              <i class="fas fa-map-marker-alt"></i>
              <span>New Delhi, India</span>
            </div>
            <div class="info-item">
              <i class="fas fa-envelope"></i>
              <span>thakurgauravkr@gmail.com</span>
            </div>
            <div class="info-item">
              <i class="fas fa-clock"></i>
              <span>Mon–Sat: 10 AM – 7 PM</span>
            </div>

            <hr class="divider" />

            <a :href="'https://wa.me/918595109337'" target="_blank" class="whatsapp-btn">
              <i class="fab fa-whatsapp"></i> Chat on WhatsApp
            </a>

            <div class="social-proof">
              <h4>Follow Our Journey</h4>
              <div class="social-icons">
                <a href="https://www.instagram.com/yourprofile/" target="_blank" rel="noopener noreferrer" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
                <a href="https://www.facebook.com/YourPageName" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook"></i></a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showModal" class="modal-overlay">
      <div class="modal-content">
        <div class="success-icon">✓</div>
        <h2 class="font-serif">Thank You!</h2>
        <p>Your inquiry has been received. The team at <strong>Indoria Travels</strong> will contact you shortly.</p>
        <button class="close-btn" @click="showModal = false">Close</button>
      </div>
    </div>
  </section>
</template>


<script setup>
import { ref } from 'vue';
import axios from 'axios';

const isSubmitting = ref(false);
const showModal = ref(false);

const form = ref({
  name: '',         // Maps to full_name
  email: '',
  phone: '',
  destination: '',  // Maps to destination_type
  travelers: 1,
  message: ''
});

const handleSubmit = async () => {
  isSubmitting.value = true;
  
  try {
    // We map the UI-friendly 'form' keys to the 'Inquiry' model keys
    const payload = {
      full_name: form.value.name,
      email: form.value.email,
      phone: form.value.phone,
      destination_type: form.value.destination,
      travelers: form.value.travelers,
      message: form.value.message
    };

    // API Call to the new backend route
    const response = await axios.post('https://indoria-backend-805083888664.us-central1.run.app//api/inquiries/submit', payload);

    if (response.data.success) {
      showModal.value = true;
      // Reset form on success
      form.value = { name: '', email: '', phone: '', destination: '', travelers: 1, message: '' };
    }
  } catch (error) {
    console.error("Transmission Error:", error);
    alert("The concierge connection is currently interrupted. Please try WhatsApp.");
  } finally {
    isSubmitting.value = false;
  }
};
</script>



<style scoped>
.contact-page {
  padding: 100px 0;
  background-color: #fcf9f4; /* Match heritage cream */
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

.brand-gold-text {
  color: #f3c969;
}

.contact-wrapper {
  display: grid;
  grid-template-columns: 1.5fr 1fr;
  gap: 50px;
  align-items: start;
}

/* Form Styles */
.contact-form-container {
  background: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
  border: 1px solid rgba(243, 201, 105, 0.1);
}

.section-title {
  font-size: 2.2rem;
  margin-bottom: 10px;
  color: #1a150e; /* Charcoal */
}

.description {
  color: #64748b;
  margin-bottom: 20px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.form-group {
  margin-bottom: 20px;
}

input, select, textarea {
  width: 100%;
  padding: 14px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 1rem;
  background: #f8fafc;
}

input:focus, select:focus, textarea:focus {
  outline: none;
  border-color: #f3c969;
}

.submit-btn {
  width: 100%;
  padding: 16px;
  background: #1a150e; /* Charcoal background */
  color: #f3c969; /* Gold text */
  border: none;
  border-radius: 8px;
  font-weight: bold;
  font-size: 1rem;
  cursor: pointer;
  transition: 0.3s;
}

.submit-btn:hover {
  background: #2b241a;
  transform: translateY(-2px);
}

/* Info Side Styles */
.info-card {
  background: #1a150e; /* Matching Dark Charcoal */
  color: white;
  padding: 40px;
  border-radius: 12px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 25px;
}

.info-item i {
  color: #f3c969; /* Brand Gold */
  font-size: 1.2rem;
}

.divider {
  border: 0;
  border-top: 1px solid rgba(243, 201, 105, 0.2);
  margin: 20px 0;
}

.whatsapp-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: #25d366;
  color: white;
  text-decoration: none;
  padding: 15px;
  border-radius: 8px;
  font-weight: bold;
  margin-top: 20px;
}

.social-icons {
  display: flex;
  gap: 15px;
  margin-top: 15px;
}

.social-icons i {
  font-size: 1.5rem;
  color: #f3c969; /* Brand Gold */
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(26, 21, 14, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.modal-content {
  background: white;
  padding: 40px;
  border-radius: 15px;
  text-align: center;
  max-width: 400px;
}

.success-icon {
  width: 60px;
  height: 60px;
  background: #f3c969;
  color: #1a150e;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  margin: 0 auto 20px;
}

.close-btn {
  margin-top: 20px;
  padding: 10px 25px;
  background: #1a150e;
  color: #f3c969;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
}

/* Responsive */
@media (max-width: 992px) {
  .contact-wrapper { grid-template-columns: 1fr; }
}

@media (max-width: 600px) {
  .form-row { grid-template-columns: 1fr; }
}
</style>
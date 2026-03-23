<template>
  <div class="privacy-page">
    <header class="privacy-hero">
      <div class="container">
        <h1 class="font-serif">Privacy Policy</h1>
        <p class="updated">Last Updated: December 24, 2025</p>
        <span class="accent-line"></span>
      </div>
    </header>

    <div class="container main-layout">
      <aside class="policy-nav" aria-label="Privacy navigation">
        <ul>
          <li v-for="link in navLinks" :key="link.id">
            <a
              :href="'#' + link.id"
              @click.prevent="scrollTo(link.id)"
            >
              {{ link.text }}
            </a>
          </li>
        </ul>
      </aside>

      <main class="policy-body">
        <section id="introduction">
          <h2 class="font-serif">1. Introduction</h2>
          <p>
            Welcome to <strong>Indoria Travels</strong>, an India-based travel
            company. We respect your privacy and are committed to protecting
            your personal information in accordance with applicable Indian
            laws and global best practices.
          </p>
        </section>

        <section id="data-collection">
          <h2 class="font-serif">2. Information We Collect</h2>
          <ul>
            <li><strong>Personal Details:</strong> Name, email address, phone number.</li>
            <li><strong>Travel Documents:</strong> Passport or Aadhar details (as required for bookings and hotel check-ins).</li>
            <li><strong>Technical Data:</strong> IP address, device type, browser information, and analytics data.</li>
          </ul>
        </section>

        <section id="usage">
          <h2 class="font-serif">3. How We Use Your Information</h2>
          <div class="usage-grid">
            <div class="usage-item">
              <span class="icon">✈</span>
              <p>Flight & Hotel Bookings</p>
            </div>
            <div class="usage-item">
              <span class="icon">🎧</span>
              <p>Customer Support</p>
            </div>
            <div class="usage-item">
              <span class="icon">🛡</span>
              <p>Security & Fraud Prevention</p>
            </div>
          </div>
        </section>

        <section id="storage">
          <h2 class="font-serif">4. Data Storage & Security</h2>
          <p>
            Your data is securely stored using <strong>Google Cloud Infrastructure</strong>.
            We apply SSL encryption, access controls, and industry-standard
            safeguards to prevent unauthorized access or disclosure.
          </p>
        </section>

        <section id="payments">
          <h2 class="font-serif">5. Payments</h2>
          <p>
            Indoria Travels does not store your credit or debit card information.
            Payments are processed through secure, RBI-compliant payment
            gateways and Google-integrated systems.
          </p>
        </section>

        <section id="sharing">
          <h2 class="font-serif">6. Third-Party Sharing</h2>
          <p>
            We only share your information with verified service providers
            such as airlines, hotels, and transport partners to complete
            your bookings. We never sell your personal data.
          </p>
        </section>

        <section id="contact">
          <h2 class="font-serif">7. Grievance & Contact</h2>
          <div class="contact-box">
            <p><strong>Grievance Officer:</strong> Gaurav Thakur</p>
            <p><strong>Email:</strong> thakurgauravkr@gmail.com</p>
            <p><strong>Jurisdiction:</strong> New Delhi, India</p>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: "PrivacyPolicy",
  data() {
    return {
      navLinks: [
        { id: "introduction", text: "Introduction" },
        { id: "data-collection", text: "Data Collection" },
        { id: "usage", text: "Usage" },
        { id: "storage", text: "Storage & Security" },
        { id: "payments", text: "Payments" },
        { id: "sharing", text: "Data Sharing" },
        { id: "contact", text: "Grievance & Contact" }
      ]
    };
  },
  methods: {
    scrollTo(id) {
      const el = document.getElementById(id);
      if (!el) return;
      window.scrollTo({
        top: el.offsetTop - 110,
        behavior: "smooth"
      });
    }
  }
};
</script>

<style scoped>
/* Base */
.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

.privacy-page {
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  color: #1a150e; /* Charcoal text */
  background: #fcf9f4; /* Heritage Cream background */
  line-height: 1.8;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 1.5rem;
}

/* Hero */
.privacy-hero {
  background: #1a150e; /* Charcoal Hero */
  color: #ffffff;
  padding: 120px 0 70px;
  text-align: center;
}

.privacy-hero h1 {
  font-size: clamp(2.2rem, 4vw, 3rem);
  color: #f3c969; /* Gold Title */
}

.updated {
  opacity: 0.8;
  color: #94a3b8;
}

.accent-line {
  display: block;
  width: 64px;
  height: 4px;
  background: #f3c969; /* Gold accent */
  margin: 24px auto 0;
}

/* Layout */
.main-layout {
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 60px;
  padding: 70px 0 100px;
}

/* Sidebar */
.policy-nav {
  position: sticky;
  top: 120px;
}

.policy-nav ul {
  list-style: none;
  padding-left: 16px;
  border-left: 2px solid rgba(243, 201, 105, 0.2); /* Subtle Gold border */
}

.policy-nav li {
  margin-bottom: 14px;
}

.policy-nav a {
  text-decoration: none;
  color: #64748b;
  font-weight: 500;
  transition: 0.25s;
}

.policy-nav a:hover {
  color: #f3c969; /* Gold hover */
  margin-left: 6px;
}

/* Content */
.policy-body section {
  margin-bottom: 56px;
}

.policy-body h2 {
  font-size: 1.75rem;
  margin-bottom: 16px;
  color: #1a150e; /* Charcoal Header */
}

/* Usage grid */
.usage-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-top: 24px;
}

.usage-item {
  background: #ffffff;
  padding: 24px;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 6px 18px rgba(0,0,0,0.03);
  border: 1px solid rgba(243, 201, 105, 0.1); /* Gold tint border */
}

.icon {
  font-size: 1.6rem;
  display: block;
  margin-bottom: 8px;
  color: #f3c969; /* Gold icons */
}

/* Contact box */
.contact-box {
  background: #ffffff;
  border-left: 4px solid #f3c969; /* Gold accent border */
  padding: 24px;
  box-shadow: 0 6px 18px rgba(0,0,0,0.03);
}

/* Responsive */
@media (max-width: 900px) {
  .main-layout {
    grid-template-columns: 1fr;
  }

  .policy-nav {
    display: none;
  }

  .usage-grid {
    grid-template-columns: 1fr;
  }
}
</style>
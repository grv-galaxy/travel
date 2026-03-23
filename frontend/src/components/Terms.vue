<template>
  <div class="terms-page">
    <header class="terms-hero">
      <div class="container">
        <div class="badge">Legal Center</div>
        <h1 class="font-serif">Terms of Service</h1>
        <p>Your guide to booking with Indoria Journeys. Professional, transparent, and reliable.</p>
        <div class="accent-line"></div>
      </div>
    </header>

    <div class="container">
      <main class="terms-card">
        <div class="update-meta">
          <div class="meta-item">
            <i class="fas fa-calendar-alt"></i>
            <span>Effective: Dec 24, 2025</span>
          </div>
          <div class="meta-item">
            <i class="fas fa-gavel"></i>
            <span>Jurisdiction: New Delhi, India</span>
          </div>
        </div>

        <section v-for="(section, index) in termsContent" :key="index" class="terms-section">
          <div class="section-number">{{ index + 1 }}</div>
          <div class="section-text">
            <h3 class="font-serif">{{ section.title }}</h3>
            <p v-html="section.content"></p>
          </div>
        </section>

        <div class="acceptance-box">
          <i class="fas fa-info-circle"></i>
          <p>By paying the <strong>25% booking deposit</strong>, you automatically agree to these terms and conditions. If you have questions regarding our Credit Note policy, please reach out.</p>
          <div class="contact-links">
            <a href="mailto:thakurgauravkr@gmail.com" class="support-link">Email Support</a>
            <span class="dot">•</span>
            <a href="https://wa.me/918595109337" target="_blank" class="support-link">WhatsApp Support</a>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TermsOfService',
  data() {
    return {
      termsContent: [
        {
          title: "Acceptance of Terms",
          content: "By booking with <strong>Indoria Journeys</strong>, you agree to comply with these terms. These conditions govern the relationship between you and Indoria Journeys, a Delhi-based travel entity. Use of our website or payment of a deposit constitutes your full acceptance."
        },
        {
          title: "Booking & Deposit Policy",
          content: "To confirm any travel package, a <strong>minimum booking deposit of 25%</strong> of the total package cost is required. The balance payment must be cleared as per the timeline discussed during the final itinerary confirmation. Bookings are subject to availability until the initial deposit is received and confirmed."
        },
        {
          title: "Price Fluctuations & Quotes",
          content: "All quotes are based on current rates of exchange, flight seat availability, train berths, and hotel inventory. Prices are subject to change without prior notice due to <strong>fluctuations in seat availability, government policy changes, or fuel hikes</strong>. Indoria Journeys reserves the right to adjust the final price if these external factors change before the final payment."
        },
        {
          title: "Cancellation & Refund Timeline",
          content: "Cancellations made <strong>more than 10 days</strong> before the scheduled departure date will be eligible for a refund, subject to airline/hotel cancellation charges and a non-refundable service fee. Cancellations made within the <strong>10-day window</strong> of departure are strictly non-refundable."
        },
        {
          title: "Force Majeure (Credit Note Policy)",
          content: "In the event of 'Acts of God' (natural disasters, floods, pandemics) or external disruptions (government restrictions, strikes), Indoria Journeys will not be liable for immediate cash refunds. In such cases, we will issue a <strong>Credit Note</strong> for the full value of the refundable amount, valid for future travel with us within 12 months."
        },
        {
          title: "Jurisdiction",
          content: "All legal matters and disputes arising out of these terms and conditions shall be subject to the exclusive jurisdiction of the <strong>Courts of New Delhi, India</strong>."
        }
      ]
    };
  },
  mounted() {
    window.scrollTo(0, 0);
  }
};
</script>

<style scoped>
.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

.terms-page {
  background-color: #fcf9f4; /* Heritage Cream background */
  padding-bottom: 100px;
  min-height: 100vh;
  font-family: 'Inter', sans-serif;
}

/* Hero Section */
.terms-hero {
  background: #1a150e; /* Charcoal Brand background */
  color: white;
  padding: 140px 0 80px;
  text-align: center;
}

.badge {
  background: #f3c969; /* Brand Gold */
  color: #1a150e; /* Charcoal text */
  padding: 6px 16px;
  border-radius: 50px;
  font-size: 0.8rem;
  font-weight: 800;
  display: inline-block;
  margin-bottom: 20px;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.terms-hero h1 {
  font-size: 3.2rem;
  margin-bottom: 15px;
  color: #f3c969; /* Title in Gold */
}

.accent-line {
  width: 50px;
  height: 4px;
  background: #f3c969; /* Gold line */
  margin: 20px auto 0;
}

/* Card Section */
.terms-card {
  max-width: 950px;
  margin: -60px auto 0;
  background: white;
  padding: 60px;
  border-radius: 20px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.05);
  border: 1px solid rgba(243, 201, 105, 0.1);
}

.update-meta {
  display: flex;
  justify-content: space-between;
  border-bottom: 1px solid #f1f5f9;
  padding-bottom: 25px;
  margin-bottom: 45px;
}

.meta-item {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #64748b;
  font-size: 0.95rem;
}

.meta-item i {
  color: #f3c969; /* Icon Gold */
}

/* Content Blocks */
.terms-section {
  display: flex;
  gap: 30px;
  margin-bottom: 45px;
}

.section-number {
  flex-shrink: 0;
  width: 45px;
  height: 45px;
  background: rgba(243, 201, 105, 0.1); /* Subtle gold background */
  color: #1a150e; /* Charcoal number */
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1.2rem;
  border: 1px solid rgba(243, 201, 105, 0.3);
}

.section-text h3 {
  font-size: 1.6rem;
  margin-bottom: 12px;
  color: #1a150e; /* Charcoal headers */
}

.section-text p {
  color: #475569;
  line-height: 1.8;
  font-size: 1.05rem;
}

/* Highlighted Text Logic */
:deep(strong) {
  color: #1a150e;
  background: rgba(243, 201, 105, 0.15); /* Gold highlighting */
  padding: 2px 4px;
  border-radius: 4px;
  font-weight: 600;
}

/* Footer Box */
.acceptance-box {
  margin-top: 60px;
  background: #fcf9f4;
  padding: 40px;
  border-radius: 16px;
  text-align: center;
  border: 1px dashed rgba(243, 201, 105, 0.5); /* Gold dashed border */
}

.acceptance-box i {
  font-size: 2rem;
  color: #f3c969;
  margin-bottom: 15px;
}

.acceptance-box p {
  color: #1a150e;
  font-size: 1.1rem;
  margin-bottom: 20px;
}

.contact-links {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 15px;
}

.support-link {
  color: #f3c969; /* Gold links */
  text-decoration: none;
  font-weight: 700;
  transition: 0.3s;
}

.support-link:hover {
  color: #1a150e;
  text-decoration: underline;
}

.dot {
  color: #cbd5e1;
}

/* Responsive Styles */
@media (max-width: 768px) {
  .terms-hero h1 { font-size: 2.2rem; }
  .terms-card { padding: 30px; margin-top: 0; border-radius: 0; }
  .terms-section { flex-direction: column; gap: 15px; }
  .update-meta { flex-direction: column; gap: 15px; }
  .section-number { width: 40px; height: 40px; }
}
</style>
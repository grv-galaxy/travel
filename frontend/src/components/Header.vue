<template>
  <header class="header">
    <div class="logo">
      <span class="logo-icon"></span>
    </div>

    <div class="logo-spacer"></div>

    <div :class="['menu-wrapper', { 'is-open': isMenuOpen }]">
      <nav class="nav">
        <a href="#" :class="{ active: activeSection === 'home' }" @click.prevent="scrollToTop">
          Home
        </a>

        <a href="#about-section" :class="{ active: activeSection === 'about' }"
          @click.prevent="scrollToSection('about-section')">
          About Us
        </a>

        <a href="#destination-section" :class="{ active: activeSection === 'destination' }"
          @click.prevent="scrollToSection('destination-section')">
          Destinations
        </a>
        <a href="#contact-section" :class="{ active: activeSection === 'contact' }"
          @click.prevent="scrollToSection('contact-section')">
          Contact
        </a>
      </nav>

      <div class="actions">
        <a href="#" class="signup" @click.prevent="openAuth('signup')">Signup</a>
        <button class="login-btn" @click="openAuth('login')">Login</button>
      </div>
    </div>

    <teleport to="body">
      <transition name="fade">
        <div v-if="showAuth" class="modal-overlay" @click.self="closeAuth">
          <div class="modal-container">
            <button class="close-modal" @click="closeAuth">&times;</button>

            <div class="modal-header">
              <h2 v-if="authMode === 'admin'">Staff Concierge</h2>
              <h2 v-else>{{ authMode === 'login' ? 'Welcome Back' : 'Join Indoria Journeys' }}</h2>
              
              <p v-if="authMode === 'admin'">Authorized access only.</p>
              <p v-else>{{ authMode === 'login' ? 'Login to access your bookings' : 'Create an account to start planning' }}</p>
            </div>

            <div v-if="authMode === 'admin'" class="auth-methods">
              <div class="admin-auth-fields">
                <div class="input-wrapper admin-input">
                   <input type="email" v-model="adminEmail" placeholder="Work Email" required>
                </div>
                <div class="input-wrapper admin-input">
                   <input type="password" v-model="adminPassword" placeholder="Password" required>
                </div>
                <button class="btn-primary" @click="handleAdminLogin">
                  Verify Credentials
                </button>
                <button class="back-to-login" @click="authMode = 'login'">
                  ← Back to Client Login
                </button>
              </div>
            </div>

            <div v-else class="auth-methods">
              <button class="method-btn google" @click="handleGoogleAuth">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" alt="Google">
                {{ authMode === 'login' ? 'Login with Google' : 'Sign up with Google' }}
              </button>

              <div class="divider"><span>OR</span></div>

              <div class="phone-auth">
                <div class="input-wrapper">
                  <span class="prefix">+91</span>
                  <input type="tel" v-model="phoneNumber" placeholder="Enter Phone Number" maxlength="10">
                </div>
                <button class="btn-primary" @click="handlePhoneAuth" :disabled="phoneNumber.length < 10">
                  {{ authMode === 'login' ? 'Login via OTP' : 'Sign up via OTP' }}
                </button>
              </div>
            </div>

            <div class="modal-footer">
              <div v-if="authMode === 'login'">
                <p>New here? <span @click="authMode = 'signup'">Create an account</span></p>
                <p class="staff-link" @click="authMode = 'admin'">Staff Access</p>
              </div>
              <div v-else-if="authMode === 'signup'">
                <p>Already have an account? <span @click="authMode = 'login'">Login here</span></p>
              </div>
            </div>
          </div>
        </div>
      </transition>
    </teleport>

    <button class="hamburger" :class="{ active: isMenuOpen }" @click.stop="toggleMenu" aria-label="Toggle Menu">
      <span></span>
      <span></span>
      <span></span>
    </button>
  </header>
</template>

<script>
import router from '../router';

export default {
  inject: ['setGlobalLoading'],
  data() {
    return {
      isMenuOpen: false,
      activeSection: "home", 
      showAuth: false,
      authMode: 'login', // 'login', 'signup', or 'admin'
      phoneNumber: '',
      adminEmail: '',
      adminPassword: '',
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
    closeMenu() {
      this.isMenuOpen = false;
    },
    scrollToTop() {
      this.closeMenu();
      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });
    },
    scrollToSection(id) {
      this.closeMenu();
      const el = document.getElementById(id);
      if (el) {
        el.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    },
    handleScroll() {
      const about = document.getElementById("about-section");
      const destination = document.getElementById("destination-section");
      const scrollPos = window.scrollY + 120;

      if (destination && scrollPos >= destination.offsetTop) {
        this.activeSection = "destination";
      } else if (about && scrollPos >= about.offsetTop) {
        this.activeSection = "about";
      } else {
        this.activeSection = "home";
      }
    },
    handleOutsideClick(e) {
      if (this.isMenuOpen && !this.$el.contains(e.target)) {
        this.isMenuOpen = false;
      }
    },
    handleEsc(e) {
      if (e.key === "Escape") {
        this.isMenuOpen = false;
        if(this.showAuth) this.closeAuth();
      }
    },
    openAuth(mode) {
      this.authMode = mode;
      this.showAuth = true;
      document.body.style.overflow = 'hidden';
    },
    closeAuth() {
      this.showAuth = false;
      document.body.style.overflow = 'auto';
      // Reset admin fields on close
      this.adminEmail = '';
      this.adminPassword = '';
    },
    async handleGoogleAuth() {
      if (!window.google) return alert("Google Sign-In is loading, please try again.");

      //new loading overlay
      this.setGlobalLoading(true);
      
      const client = google.accounts.oauth2.initTokenClient({
        client_id: '749329503754-0iu1rkjrvc8e3k0vtdmsf2i2usi02s3n.apps.googleusercontent.com',
        scope: 'openid email profile',
        ux_mode: 'popup',
        callback: async (response) => {
          if (response.access_token) {
            await this.verifyGoogleToken(response.access_token);
          } else {
            this.setGlobalLoading(false); 
          }
        },
      });
      client.requestAccessToken();
    },
    async verifyGoogleToken(token) {
      try {
        const res = await fetch('https://indoria-backend-805083888664.us-central1.run.app/api/auth/google', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ token }),
        });
        const data = await res.json();
        if (data.success) {
          localStorage.setItem('user_token', data.token); 
          localStorage.setItem('user_data', JSON.stringify(data.user));
          this.closeAuth();
          this.$router.push('/Uhome');
        } else {
          alert('Login failed: ' + data.message);
        }
      } catch (error) {
        console.error('Error verifying Google token:', error);
        alert('An error occurred during Google authentication.');
      } finally {
        this.setGlobalLoading(false); 
      }
    },
    handlePhoneAuth() {
      alert(`OTP sent to +91 ${this.phoneNumber}`);
    },
    async handleAdminLogin() {
      if (!this.adminEmail || !this.adminPassword) {
        return alert("Please enter both email and password");
      }
      this.setGlobalLoading(true);
      try {
        // Fixed typo: locallhost -> localhost
        const response = await fetch('https://indoria-backend-805083888664.us-central1.run.app/api/auth/admin-login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email: this.adminEmail,
            password: this.adminPassword
          })
        });
        const data = await response.json();

        if (data.success) {
          // Store token and admin info
          localStorage.setItem('user_token', data.token);
          localStorage.setItem('user_data', JSON.stringify(data.user));
          this.closeAuth();
          this.$router.push('/Ahome'); // Redirect to Admin Dashboard
        } else {
          alert(data.message || "Invalid Admin Credentials");
        }
      } catch (error) {
        console.error('Error during admin login:', error);
        alert("Server error. Please try again later.");
      } finally {
        this.setGlobalLoading(false);  
    }
  },
  mounted() {
    if (!window.google) {
      const script = document.createElement('script');
      script.src = "https://accounts.google.com/gsi/client";
      script.async = true;
      script.defer = true;
      document.head.appendChild(script);
    }
    window.addEventListener("scroll", this.handleScroll);
    document.addEventListener("click", this.handleOutsideClick);
    window.addEventListener("keydown", this.handleEsc);
  },
  beforeUnmount() {
    window.removeEventListener("scroll", this.handleScroll);
    document.removeEventListener("click", this.handleOutsideClick);
    window.removeEventListener("keydown", this.handleEsc);
  },
}
}
</script>



<style scoped>
/* ================= HEADER (OVER IMAGE) ================= */
.header {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.4rem 3.5rem;
  color: white;
}

/* Subtle readability gradient */
.header::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0));
  z-index: -1;
}

/* ================= LOGO ================= */
.logo {
  display: flex;
  align-items: center;
  z-index: 110;
}

.logo-icon {
  width: 42px;
  height: 42px;
  background: url("../assets/images/LOGO.jpg") center / contain no-repeat;
}

.logo-spacer {
  width: 360px;
  flex-shrink: 0;
}

/* ================= DESKTOP MENU ================= */
.menu-wrapper {
  display: flex;
  align-items: center;
  flex-grow: 1;
  justify-content: space-between;
  margin-left: 4rem;
}

.nav {
  display: flex;
  gap: 3.2rem;
}

.nav a,
.signup {
  font-family: Georgia, serif;
  font-size: 0.95rem;
  font-weight: 600;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.85);
  text-decoration: none;
  transition: 0.25s;
}

.nav a:hover,
.nav a.active,
.signup:hover {
  color: #fbbf24;
}

.actions {
  display: flex;
  align-items: center;
  gap: 1.6rem;
}

.login-btn {
  background: white;
  color: #1f2933;
  border: none;
  padding: 0.6rem 1.8rem;
  border-radius: 999px;
  font-weight: 600;
  cursor: pointer;
}

.login-btn:hover {
  background: #fbbf24;
  transform: translateY(-1px);
}

/* Modal Styles (Production Ready & Responsive) */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1001;
  padding: 20px;
  backdrop-filter: blur(4px);
}

.modal-container {
  background: white;
  width: 100%;
  max-width: 400px;
  padding: 40px;
  border-radius: 20px;
  position: relative;
  text-align: center;
}

.close-modal {
  position: absolute;
  top: 15px;
  right: 20px;
  background: none;
  border: none;
  font-size: 2rem;
  cursor: pointer;
  color: #94a3b8;
}

.modal-header h2 {
  font-family: 'Georgia', serif;
  margin-bottom: 8px;
  font-size: 1.8rem;
}

.modal-header p {
  color: #64748b;
  font-size: 0.9rem;
  margin-bottom: 30px;
}

.auth-methods {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.method-btn {
  width: 100%;
  padding: 12px;
  border-radius: 10px;
  border: 1px solid #e2e8f0;
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s;
}

.method-btn:hover {
  background: #f8fafc;
}

.method-btn img {
  width: 20px;
}

.divider {
  margin: 20px 0;
  position: relative;
  border-top: 1px solid #e2e8f0;
}

.divider span {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  padding: 0 10px;
  font-size: 0.75rem;
  color: #94a3b8;
  font-weight: 700;
}

.input-wrapper {
  display: flex;
  border: 1.5px solid #e2e8f0;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 15px;
}

.prefix {
  background: #f1f5f9;
  padding: 12px;
  font-weight: 700;
  color: #475569;
}

input {
  border: none;
  padding: 12px;
  width: 100%;
  outline: none;
}

.btn-primary {
  width: 100%;
  padding: 14px;
  background: #fbbf24;
  border: none;
  border-radius: 10px;
  font-weight: 800;
  cursor: pointer;
}

.btn-primary:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.modal-footer {
  margin-top: 25px;
  font-size: 0.9rem;
  color: #64748b;
}

.modal-footer span {
  color: #fbbf24;
  font-weight: 700;
  cursor: pointer;
}

/* Transitions */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Responsive adjustments */
@media (max-width: 480px) {
  .modal-container {
    padding: 30px 20px;
  }

  .modal-header h2 {
    font-size: 1.5rem;
  }
}

/* ================= HAMBURGER ================= */
.hamburger {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 120;
  flex-direction: column;
  gap: 6px;
}

.hamburger span {
  width: 30px;
  height: 3px;
  background: #f5e6c8;
  /* warm heritage white */
  border-radius: 2px;
  transition: 0.3s;
}

.hamburger.active span:nth-child(1) {
  transform: translateY(9px) rotate(45deg);
}

.hamburger.active span:nth-child(2) {
  opacity: 0;
}

.hamburger.active span:nth-child(3) {
  transform: translateY(-9px) rotate(-45deg);
}

.admin-theme {
  border: 2px solid #1a150e !important;
  background: #fcf9f4;
}

.admin-input {
  width: 100%;
  padding: 12px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  outline: none;
}

.admin-input:focus {
  border-color: #1a150e;
}

.staff-link {
  margin-top: 15px;
  font-size: 0.75rem;
  color: #94a3b8;
  cursor: pointer;
  text-decoration: underline;
}

.back-link {
  background: none;
  border: none;
  color: #64748b;
  font-size: 0.8rem;
  margin-top: 15px;
  cursor: pointer;
}

.admin-btn {
  background: #1a150e !important; /* Darker, more formal button */
}

/* ================= MOBILE SLIDE MENU ================= */
@media (max-width: 1024px) {
  .hamburger {
    display: flex;
  }

  .menu-wrapper {
    position: fixed;
    top: 0;
    right: 0;
    height: 100vh;
    width: 80%;
    max-width: 360px;
    background: #2b241a;
    backdrop-filter: blur(10px);
    flex-direction: column;
    padding: 100px 2rem 3rem;
    transform: translateX(100%);
    transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 110;
  }

  .menu-wrapper.is-open {
    transform: translateX(0);
  }

  .nav {
    flex-direction: column;
    align-items: flex-start;
    gap: 2rem;
    width: 100%;
  }

  .actions {
    flex-direction: column;
    width: 100%;
    margin-top: 2.5rem;
    padding-top: 2.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }

  .logo-spacer {
    display: none;
  }
}

/* ================= SMALL SCREENS ================= */
@media (max-width: 768px) {
  .header {
    background: transparent;
    /* CRITICAL: removes white strip */
  }

  .header::after {
    background: none !important;
  }
}
</style>
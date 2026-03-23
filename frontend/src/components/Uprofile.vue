<template>
  <div class="min-h-screen bg-[#fcf9f4]">
    <!-- <LoadingOverlay :show="loading || saving" /> -->
    <ConfirmModal
      :show="showLogoutConfirm"
      title="Confirm Sign Out"
      message="Are you sure you want to sign out of your Indoria account?"
      @confirm="confirmLogout"
      @cancel="showLogoutConfirm = false"
    />

    <main v-if="!loading" class="mx-auto max-w-4xl px-4 py-8 sm:px-6 lg:py-12">
      <div class="mb-8 overflow-hidden rounded-2xl bg-white shadow-lg border border-[#f3c969]/20">
        <div class="h-32 bg-[#1a150e] relative">
          <div class="absolute inset-0 bg-gradient-to-r from-[#1a150e] to-[#2b241a]"></div>
        </div>


        <div class="px-6 pb-6">
          <div class="relative -mt-12 flex flex-col items-center sm:flex-row sm:items-end sm:space-x-5">
            <div class="relative">
              <img
                class="h-28 w-28 rounded-2xl border-4 border-white bg-white object-cover shadow-lg ring-1 ring-[#f3c969]/30"
                :src="user.profile_image || `https://ui-avatars.com/api/?name=${user.full_name}&background=1a150e&color=f3c969`"
                alt="Profile" />
            </div>

            <div class="mt-6 text-center sm:mt-0 sm:text-left flex-1">
              <p class="brand-gold-text text-[10px] font-extrabold uppercase tracking-[0.25em]">Authentic Traveler</p>
              <h2 class="text-3xl font-bold text-slate-900 tracking-tight font-serif">
                {{ user.full_name }}
              </h2>
              <p class="text-sm text-slate-500 font-medium italic">
                Verified Resident • <span class="text-[#e8b34b] not-italic font-bold">{{ user.tier }}</span>
              </p>
            </div>

            <div class="mt-4">
              <button @click="saveChanges" :disabled="saving" class="btn-primary">
                {{ saving ? 'Saving...' : 'Save Profile' }}
              </button>
            </div>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 gap-8 md:grid-cols-3">
        <aside class="space-y-1">
          <button class="nav-active w-full flex items-center space-x-3 px-4 py-3 rounded-lg">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" stroke-width="2" />
            </svg>
            <span>Personal Info</span>
          </button>

          <button
            class="dropdown-item w-full flex items-center space-x-3 px-4 py-3 rounded-lg opacity-50 cursor-not-allowed">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"
                stroke-width="2" />
            </svg>
            <span>Payment Methods</span>
          </button>

          <div class="py-4">
            <div class="h-px bg-[#f3c969]/20 w-full"></div>
          </div>

          <button @click="handleLogout"
            class="dropdown-item w-full flex items-center space-x-3 px-4 py-3 rounded-lg text-red-600 hover:bg-red-50">
            <svg class="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"
                stroke-width="2" />
            </svg>
            <span>Sign Out</span>
          </button>
        </aside>

        <div class="md:col-span-2 space-y-6">
          <div class="form-card p-6 bg-white rounded-xl shadow-sm border border-slate-100">
            <h3 class="mb-6 text-xl font-bold text-slate-800 font-serif">Account Details</h3>
            <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
              <div class="input-group">
                <label class="label block text-xs font-bold uppercase text-slate-400 mb-2">Full Name</label>
                <input v-model="user.full_name" type="text"
                  class="input-field w-full p-3 rounded-lg border border-slate-200" />
              </div>
              <div class="input-group">
                <label class="label block text-xs font-bold uppercase text-slate-400 mb-2">Phone Number</label>
                <input v-model="user.phone" type="text"
                  class="input-field w-full p-3 rounded-lg border border-slate-200" placeholder="+91 00000 00000" />
              </div>
              <div class="input-group sm:col-span-2">
                <label class="label block text-xs font-bold uppercase text-slate-400 mb-2">Email (Primary)</label>
                <input v-model="user.email" type="email" disabled
                  class="input-field w-full p-3 rounded-lg border border-slate-200 bg-slate-50 cursor-not-allowed" />
              </div>
            </div>
          </div>

          <div class="form-card p-6 bg-white rounded-xl shadow-sm border border-slate-100">
            <h3 class="mb-6 text-xl font-bold text-slate-800 font-serif">Luxury Preferences</h3>
            <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
              <div class="input-group">
                <label class="label block text-xs font-bold uppercase text-slate-400 mb-2">Cabin Temperature
                  (°C)</label>
                <input v-model="user.preferences.temp" type="number"
                  class="input-field w-full p-3 rounded-lg border border-slate-200" />
              </div>
              <div class="input-group">
                <label class="label block text-xs font-bold uppercase text-slate-400 mb-2">Ambience Mood</label>
                <select v-model="user.preferences.mood"
                  class="input-field w-full p-3 rounded-lg border border-slate-200">
                  <option value="Classical">Classical</option>
                  <option value="Modern">Modern</option>
                  <option value="Zen">Zen</option>
                  <option value="Royal">Royal</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>


<script setup>
import { ref, onMounted, inject } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import LoadingOverlay from './LoadingOverlay.vue'
import ConfirmModal from './ConfirmModal.vue'

const router = useRouter()
const loading = ref(true)
const saving = ref(false)
const setGlobalLoading = inject('setGlobalLoading')
const showLogoutConfirm = ref(false)
const user = ref({
  full_name: '',
  email: '',
  phone: '',
  tier: '',
  profile_image: '',
  preferences: {
    temp: 22,
    mood: 'Classical'
  }
})

// 1. Fetch Profile on Load
const fetchProfile = async () => {
  setGlobalLoading(true)
  loading.value = true
  try {
    const token = localStorage.getItem('user_token')
    const response = await axios.get('https://indoria-backend-805083888664.us-central1.run.app/api/user/profile', {
      headers: { Authorization: `Bearer ${token}` }
    })
    
    if (response.data && response.data.success) {
      user.value = response.data.data
      // Ensure preferences has a default if null in DB
      if (!user.value.preferences) {
        user.value.preferences = { temp: 22, mood: 'Classical' }
      }
    }
  } catch (error) {
    console.error("Profile Fetch Error:", error)
    if (error.response?.status === 401) handleLogout()
  } finally {
    setTimeout(() => {
      setGlobalLoading(false)
      loading.value = false
    }, 800)
  }
}

// 2. Save Changes to Backend
const saveChanges = async () => {
  setGlobalLoading(true)
  saving.value = true
  try {
    const token = localStorage.getItem('user_token')
    const updateData = {
      full_name: user.value.full_name,
      phone: user.value.phone,
      preferences: user.value.preferences,
      profile_image: user.value.profile_image
    }

    const response = await axios.put('https://indoria-backend-805083888664.us-central1.run.app/api/user/profile/update', updateData, {
      headers: { Authorization: `Bearer ${token}` }
    })

    if (response.data.success) {
      alert('Your Luxury Vault has been updated.')
    }
  } catch (error) {
    alert('Failed to update profile. Please try again.')
    console.error(error)
  } finally {
    setTimeout(() => {
      setGlobalLoading(false)
      saving.value = false
    }, 500)
  }
}

const handleLogout = () => {
  showLogoutConfirm.value = true;
}

const confirmLogout = () => {
  localStorage.removeItem('user_token')
  localStorage.removeItem('user_data')
  showLogoutConfirm.value = false
  router.push('/')
}

onMounted(fetchProfile)
</script>



<style scoped>
/* YOUR SPECIFIC STYLES INTEGRATED */
.brand-gold-text {
  background: linear-gradient(90deg, #f3c969, #e8b34b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.dropdown-item {
  display: flex;
  align-items: center;
  padding: 0.75rem 1rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: #475569;
  border-radius: 0.75rem;
  transition: all 0.2s;
  width: 100%;
}

.dropdown-item:hover {
  background-color: #fffbeb;
  color: #e8b34b;
}

.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

/* ADDITIONAL HERITAGE CLASSES */
.btn-primary {
  background: linear-gradient(90deg, #f3c969, #e8b34b);
  color: #1a150e;
  font-weight: 800;
  padding: 0.75rem 1.5rem;
  border-radius: 0.75rem;
  font-size: 0.875rem;
  box-shadow: 0 4px 15px rgba(243, 201, 105, 0.3);
  transition: transform 0.2s;
}

.btn-primary:active { transform: scale(0.95); }

.nav-active {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  background-color: #1a150e;
  color: #f3c969;
  border-radius: 0.75rem;
  font-size: 0.875rem;
  font-weight: 700;
  width: 100%;
}

.form-card {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  border: 1px solid rgba(243, 201, 105, 0.1);
}

.input-field {
  width: 100%;
  border-radius: 0.75rem;
  border: 1px solid #e2e8f0;
  background-color: #f8fafc;
  padding: 0.75rem 1rem;
  font-size: 0.875rem;
  outline: none;
  transition: all 0.2s;
}

.input-field:focus {
  border-color: #f3c969;
  box-shadow: 0 0 0 4px rgba(243, 201, 105, 0.1);
}

.label {
  display: block;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #64748b;
  margin-bottom: 0.5rem;
}

.pref-row {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.75rem;
  border-radius: 0.75rem;
  cursor: pointer;
  transition: background 0.2s;
}

.pref-row:hover { background: #f8fafc; }

.checkbox-custom {
  height: 1.25rem;
  width: 1.25rem;
  border-radius: 0.25rem;
  border-color: #f3c969;
  color: #e8b34b;
}
</style>
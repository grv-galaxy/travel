<!-- <template>
  <header
    class="sticky top-0 z-50 flex h-16 w-full items-center justify-between border-b border-[#f3c969]/10 bg-white/90 backdrop-blur-md px-4 shadow-sm sm:px-8"
  >
    <div class="flex flex-1 items-center gap-4 sm:gap-8">
      <div class="flex shrink-0 items-center gap-3">
        <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#1a150e] shadow-lg">
          <img
            src="../assets/images/LOGO.jpg"
            alt="Indoria Journeys"
            class="h-full w-full rounded-lg object-contain border border-[#f3c969]/20"
          />
        </div>

        <div class="hidden flex-col sm:flex">
          <span class="text-sm font-black uppercase tracking-widest text-[#1a150e] font-serif">
            Indoria
          </span>
          <span class="text-[10px] font-bold uppercase tracking-[0.2em] text-[#f3c969] mt-1">
            Journeys
          </span>
        </div>
      </div>

      <div class="hidden lg:block h-8 w-px bg-slate-200"></div>

      <div class="hidden lg:block">
        <h1 class="text-lg font-bold text-[#1a150e] font-serif">
          Adventure Awaits,
          <span class="text-[#f3c969]">{{ userName }}</span>!
        </h1>
        <p class="text-[11px] text-slate-500 uppercase tracking-wider">
          Heritage Travel & Luxury
        </p>
      </div>
    </div>

    <div class="flex items-center space-x-4">
      <div class="relative">
        <button
          @click.stop="showNotifications = !showNotifications"
          class="rounded-full p-2 text-slate-500 hover:bg-[#fcf9f4]"
        >
          <i class="fas fa-bell text-lg"></i>
        </button>

        <Unotification
          v-if="showNotifications"
          class="absolute right-0 mt-2 w-80 bg-white rounded-2xl shadow-2xl border border-[#f3c969]/10 z-50"
          @close="showNotifications = false"
        />
      </div>

      <div class="h-8 w-px bg-slate-200"></div>

      <div class="relative group" ref="profileRef">
        <button
          @click="toggleProfileMenu"
          class="flex items-center gap-3 rounded-lg p-1 hover:bg-[#fcf9f4] transition"
        >
          <img
            class="h-9 w-9 rounded-full object-cover ring-2 ring-white shadow"
            :src="`https://ui-avatars.com/api/?name=${user.username}&background=1a150e&color=f3c969`"
            :alt="user.username"
          />
          <div class="hidden sm:block text-left">
            <p class="text-sm font-semibold text-[#1a150e] font-serif">{{ user.username }}</p>
            <p class="text-[11px] font-bold text-[#f3c969] uppercase tracking-wider">
              {{ user.tier }}
            </p>
          </div>
        </button>

        <div
          :class="[
            'absolute right-0 mt-2 w-52 rounded-2xl border border-[#f3c969]/10 bg-white shadow-2xl py-2 z-50 transition-all',
            showProfileMenu
              ? 'opacity-100 scale-100 visible'
              : 'opacity-0 scale-95 invisible',
            'lg:group-hover:opacity-100 lg:group-hover:scale-100 lg:group-hover:visible'
          ]"
        >
          <div class="px-4 py-2 border-b border-slate-100 mb-1">
            <p class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">
              Account
            </p>
          </div>

          <router-link
            to="/uprofile"
            class="dropdown-item flex items-center px-4 py-2 text-sm text-slate-700 hover:bg-[#fcf9f4]"
            @click="closeProfileMenu"
          >
            <i class="fas fa-user-circle mr-2 w-5"></i>
            My Profile
          </router-link>

          <router-link
            to="/ubookings"
            class="dropdown-item flex items-center px-4 py-2 text-sm text-slate-700 hover:bg-[#fcf9f4]"
            @click="closeProfileMenu"
          >
            <i class="fas fa-suitcase mr-2 w-5"></i>
            My Bookings
          </router-link>

          <router-link
            to="/usopports"
            class="dropdown-item flex items-center px-4 py-2 text-sm text-slate-700 hover:bg-[#fcf9f4]"
            @click="closeProfileMenu"
          >
            <i class="fas fa-headset mr-2 w-5"></i>
            Support
          </router-link>

          <hr class="my-2 border-slate-100" />

          <button
            @click="handleLogout"
            class="dropdown-item flex items-center w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50"
          >
            <i class="fas fa-sign-out-alt mr-2 w-5"></i>
            Logout
          </button>
        </div>
      </div>
    </div>
  </header>
</template> -->




<template>
  <header
    class="sticky top-0 z-50 flex h-16 w-full items-center justify-between border-b border-[#f3c969]/10 bg-white/90 backdrop-blur-md px-4 shadow-sm sm:px-8"
  >
    <div class="flex flex-1 items-center gap-4 sm:gap-8">
      <div class="flex shrink-0 items-center gap-3">
        <div class="flex h-10 w-10 items-center justify-center rounded-xl bg-[#1a150e] shadow-lg">
          <img
            src="../assets/images/LOGO.jpg"
            alt="Indoria Journeys"
            class="h-full w-full rounded-lg object-contain border border-[#f3c969]/20"
          />
        </div>

        <div class="hidden flex-col sm:flex">
          <span class="text-sm font-black uppercase tracking-widest text-[#1a150e] font-serif">
            Indoria
          </span>
          <span class="text-[10px] font-bold uppercase tracking-[0.2em] text-[#f3c969] mt-1">
            Journeys
          </span>
        </div>
      </div>

      <div class="hidden lg:block h-8 w-px bg-slate-200"></div>

      <div class="hidden lg:block">
        <h1 class="text-lg font-bold text-[#1a150e] font-serif">
          Adventure Awaits,
          <span class="text-[#f3c969]">{{ userName }}</span>!
        </h1>
        <p class="text-[11px] text-slate-500 uppercase tracking-wider">
          Heritage Travel & Luxury
        </p>
      </div>
    </div>

    <div class="flex items-center space-x-4">
      <div class="relative">
        <button
          @click.stop="showNotifications = !showNotifications"
          class="rounded-full p-2 text-slate-500 hover:bg-[#fcf9f4]"
        >
          <i class="fas fa-bell text-lg"></i>
        </button>

        <Unotification
          v-if="showNotifications"
          class="absolute right-0 mt-2 w-80 bg-white rounded-2xl shadow-2xl border border-[#f3c969]/10 z-50"
          @close="showNotifications = false"
        />
      </div>

      <div class="h-8 w-px bg-slate-200"></div>

      <div class="relative group" ref="profileRef">
        <button
          @click="toggleProfileMenu"
          class="flex items-center gap-3 rounded-lg p-1 hover:bg-[#fcf9f4] transition"
        >
          <img
            class="h-9 w-9 rounded-full object-cover ring-2 ring-white shadow"
            :src="`https://ui-avatars.com/api/?name=${user.username}&background=1a150e&color=f3c969`"
            :alt="user.username"
          />
          <div class="hidden sm:block text-left">
            <p class="text-sm font-semibold text-[#1a150e] font-serif">{{ user.username }}</p>
            <p class="text-[11px] font-bold text-[#f3c969] uppercase tracking-wider">
              {{ user.tier }}
            </p>
          </div>
        </button>

        <div
          :class="[
            'absolute right-0 mt-2 w-52 rounded-2xl border border-[#f3c969]/10 bg-white shadow-2xl py-2 z-50 transition-all',
            showProfileMenu
              ? 'opacity-100 scale-100 visible'
              : 'opacity-0 scale-95 invisible',
            'lg:group-hover:opacity-100 lg:group-hover:scale-100 lg:group-hover:visible'
          ]"
        >
          <div class="px-4 py-2 border-b border-slate-100 mb-1">
            <p class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">
              Account
            </p>
          </div>

          <router-link
            to="/uprofile"
            class="dropdown-item flex items-center px-4 py-2 text-sm text-slate-700 hover:bg-[#fcf9f4]"
            @click="closeProfileMenu"
          >
            <i class="fas fa-user-circle mr-2 w-5"></i>
            My Profile
          </router-link>

          <router-link
            to="/ubookings"
            class="dropdown-item flex items-center px-4 py-2 text-sm text-slate-700 hover:bg-[#fcf9f4]"
            @click="closeProfileMenu"
          >
            <i class="fas fa-suitcase mr-2 w-5"></i>
            My Bookings
          </router-link>

          <router-link
            to="/usopports"
            class="dropdown-item flex items-center px-4 py-2 text-sm text-slate-700 hover:bg-[#fcf9f4]"
            @click="closeProfileMenu"
          >
            <i class="fas fa-headset mr-2 w-5"></i>
            Support
          </router-link>

          <hr class="my-2 border-slate-100" />

          <button
            @click="triggerLogout"
            class="dropdown-item flex items-center w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50"
          >
            <i class="fas fa-sign-out-alt mr-2 w-5"></i>
            Logout
          </button>
        </div>
      </div>
    </div>
    <ConfirmModal
      :show="showLogoutConfirm"
      title="Confirm Logout"
      message="Are you sure you want to logout?"
      @confirm="handleLogout"
      @cancel="showLogoutConfirm = false" 
    />
  </header>
</template>






<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useRouter } from 'vue-router'
import Unotification from './Unotification.vue'
import ConfirmModal from './ConfirmModal.vue'

const router = useRouter()
const userName = ref('Traveler')
const user = ref({
  username: 'Guest',
  tier: 'Silver Member'
})

const showNotifications = ref(false)
const showProfileMenu = ref(false)
const showLogoutConfirm = ref(false)
const profileRef = ref(null)

// Load user details from LocalStorage
const loadUserData = () => {
  const storedData = localStorage.getItem('user_data')
  if (storedData) {
    try {
      const parsed = JSON.parse(storedData)
      // Note: Use 'username' or 'full_name' depending on your Flask response key
      user.value.username = parsed.username || 'Traveler'
      user.value.tier = parsed.tier || "Silver Member"
      
      // Extract the first name for the "Adventure Awaits" greeting
      userName.value = user.value.username.split(' ')[0]
    } catch (e) {
      console.error("Failed to parse user data", e)
    }
  }
}

//new functions
const triggerLogout = () => {
  showProfileMenu.value = false
  showLogoutConfirm.value = true
}

const toggleProfileMenu = () => {
  showProfileMenu.value = !showProfileMenu.value
}

const closeProfileMenu = () => {
  showProfileMenu.value = false
}

const handleLogout = () => {
    localStorage.removeItem('user_token')
    localStorage.removeItem('user_data')
    showLogoutConfirm.value = false
    router.push('/')
}

/* CLICK OUTSIDE TO CLOSE */
const handleClickOutside = (e) => {
  if (profileRef.value && !profileRef.value.contains(e.target)) {
    showProfileMenu.value = false
  }
}

onMounted(() => {
  loadUserData() // <--- CRITICAL: Populates the name on load
  document.addEventListener('click', handleClickOutside)
})

onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
.dropdown-item {
  transition: all 0.2s ease;
}
</style>

<style scoped>
.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

.dropdown-item {
  display: flex;
  align-items: center;
  width: 100%;
  padding: 0.625rem 1rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: #334155;
  transition: all 0.2s ease;
}

.dropdown-item:hover {
  background-color: #fcf9f4;
  color: #1a150e;
}
</style>

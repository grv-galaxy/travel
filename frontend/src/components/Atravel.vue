<!-- <template>
  <div class="travelers-page">
    <header class="page-header">
      <div class="search-box">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input type="text" v-model="searchQuery" placeholder="Search VIP Name, Passport, or Tier..." />
      </div>
      <div class="actions">
        <button class="filter-btn"><i class="fa-solid fa-filter"></i> Filters</button>
        <button class="add-btn"><i class="fa-solid fa-plus"></i> Register VIP</button>
      </div>
    </header>

    <div class="status-ribbon">
      <div class="status-item">
        <span class="label">Total VIPs</span>
        <span class="count">{{ stats.total }}</span>
      </div>
      <div class="divider"></div>
      <div class="status-item">
        <span class="label">In Transit</span>
        <span class="count highlight">{{ stats.inTransit }}</span>
      </div>
      <div class="divider"></div>
      <div class="status-item">
        <span class="label">Elite Tier</span>
        <span class="count gold">{{ stats.eliteCount }}</span>
      </div>
    </div>

    <div class="table-container shadow-premium">
      <table class="vip-table">
        <thead>
          <tr>
            <th>Traveler</th>
            <th>Passport/ID</th>
            <th>Membership Tier</th>
            <th>Total Spend</th>
            <th>Last Seen</th>
            <th>Status</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="vip in filteredVIPs" :key="vip.id" class="table-row">
            <td>
              <div class="user-profile">
                <div class="avatar-ring" :class="vip.tier.toLowerCase()">
                  <img :src="vip.avatar" alt="VIP" />
                </div>
                <div class="user-info">
                  <span class="name">{{ vip.name }}</span>
                  <span class="email">{{ vip.email }}</span>
                </div>
              </div>
            </td>
            <td class="id-cell"><code>{{ vip.passport }}</code></td>
            <td>
              <span class="tier-badge" :class="vip.tier.toLowerCase()">
                <i class="fa-solid fa-crown"></i> {{ vip.tier }}
              </span>
            </td>
            <td class="spend-cell">₹{{ vip.spend }}</td>
            <td class="date-cell">{{ vip.lastSeen }}</td>
            <td>
              <div class="status-dot" :class="vip.status.toLowerCase()">
                <span>{{ vip.status }}</span>
              </div>
            </td>
            <td class="action-cell">
              <button class="icon-btn"><i class="fa-solid fa-ellipsis-vertical"></i></button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="mobile-grid">
      <div v-for="vip in filteredVIPs" :key="'mob-' + vip.id" class="vip-mobile-card">
        <div class="card-header">
          <img :src="vip.avatar" alt="" />
          <div class="title">
            <h4>{{ vip.name }}</h4>
            <span class="tier-badge" :class="vip.tier.toLowerCase()">{{ vip.tier }}</span>
          </div>
          <div class="status-dot" :class="vip.status.toLowerCase()"></div>
        </div>
        <div class="card-body">
          <div class="info-row"><span>ID:</span> <strong>{{ vip.passport }}</strong></div>
          <div class="info-row"><span>Spent:</span> <strong>₹{{ vip.spend }}</strong></div>
        </div>
        <button class="card-action">Manage Profile</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';

const searchQuery = ref('');
const vips = ref([]);
const stats = ref({total:0, inTransit:0, eliteCount:0});
const isLoading = ref(false);


const fetchTravelers = async () => {
  isLoading.value = true;
  try{
    const response = await fetch(`https://travel-xxnc.onrender.com//api/admin/travelers?search=${searchQuery.value}`);
    const result = await response.json();

    if (result.success){
      vips.value = result.data;
      stats.value = result.stats;
    }
  } catch (error){
    console.error("Error fetching VIPs:", error);
  } finally{
    isLoading.value = false;
  }
};

//search logic 
let timeout;
watch(searchQuery, () =>{
  clearTimeout(timeout);
  timeout = setTimeout(() => {
    fetchTravelers();
  }, 300);
});

//load data when page first open
onMounted(() =>{
  fetchTravelers();
});

const filteredVIPs = computed(() => vips.value);
</script>

<style scoped>
.travelers-page {
  animation: fadeIn 0.6s ease-out;
  color: #ffffff;
}

/* Header & Search */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  gap: 1rem;
}

.search-box {
  background: #121212;
  border: 1px solid rgba(197, 160, 89, 0.35);
  padding: 0.8rem 1.2rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
  max-width: 500px;
  color: #ffffff;
}

.search-box i {
  color: #cfcfcf;
}

.search-box input {
  background: none;
  border: none;
  color: #ffffff;
  width: 100%;
  outline: none;
}

.search-box input::placeholder {
  color: #b5b5b5;
}

.actions {
  display: flex;
  gap: 1rem;
}

.add-btn {
  background: #c5a059;
  color: #0c0c0c;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 10px;
  font-weight: 700;
  cursor: pointer;
}

.filter-btn {
  background: #1a1a1a;
  color: #ffffff;
  border: 1px solid #333;
  padding: 0.8rem 1.2rem;
  border-radius: 10px;
  cursor: pointer;
}

/* Status Ribbon */
.status-ribbon {
  background: #0c0c0c;
  border: 1px solid rgba(197, 160, 89, 0.15);
  padding: 1.5rem;
  border-radius: 16px;
  display: flex;
  align-items: center;
  gap: 3rem;
  margin-bottom: 2rem;
}

.status-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.status-item .label {
  color: #b0b0b0;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.status-item .count {
  font-size: 1.5rem;
  font-weight: 800;
  color: #ffffff;
}

.count.highlight {
  color: #00d2ff;
}

.count.gold {
  color: #c5a059;
}

.divider {
  width: 1px;
  height: 30px;
  background: rgba(255, 255, 255, 0.15);
}

/* Table Styling */
.table-container {
  background: #0c0c0c;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.vip-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  color: #ffffff;
}

.vip-table th {
  padding: 1.2rem;
  color: #cfcfcf;
  font-size: 0.75rem;
  text-transform: uppercase;
  border-bottom: 1px solid #1a1a1a;
}

.vip-table td {
  padding: 1.2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  table-layout: fixed;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
}

.avatar-ring {
  padding: 2px;
  border-radius: 50%;
  border: 2px solid transparent;
}

.avatar-ring.elite {
  border-color: #c5a059;
}

.avatar-ring.gold {
  border-color: #ffd700;
}

.avatar-ring img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
}

.name {
  display: block;
  font-weight: 600;
  font-size: 0.95rem;
  color: #ffffff;
}

.email {
  font-size: 0.75rem;
  color: #b5b5b5;
}

.id-cell code {
  color: #ffffff;
  background: transparent;
}

.spend-cell,
.date-cell {
  color: #eaeaea;
}

/* Tier Badge */
.tier-badge {
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.7rem;
  font-weight: 800;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.tier-badge.elite {
  background: rgba(197, 160, 89, 0.18);
  color: #c5a059;
  border: 1px solid rgba(197, 160, 89, 0.35);
}

.tier-badge.gold {
  background: rgba(255, 215, 0, 0.15);
  color: #ffd700;
  border: 1px solid rgba(255, 215, 0, 0.3);
}

/* Status */
.status-dot {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.8rem;
  color: #ffffff;
}

.status-dot::before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.status-dot.active::before {
  background: #00ff88;
  box-shadow: 0 0 10px rgba(0, 255, 136, 0.6);
}

.status-dot.transit::before {
  background: #00d2ff;
}

.status-dot.inactive::before {
  background: #ff4d4d;
}

/* Action */
.icon-btn {
  background: transparent;
  border: none;
  color: #ffffff;
  cursor: pointer;
}

/* Responsive */
.mobile-grid {
  display: none;
}

@media (max-width: 1024px) {
  .vip-table th:nth-child(4),
  .vip-table td:nth-child(4) {
    display: none;
  }
}

@media (max-width: 768px) {
  .table-container {
    display: none;
  }

  .mobile-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .vip-mobile-card {
    background: #121212;
    border-radius: 12px;
    padding: 1.2rem;
    border: 1px solid #1a1a1a;
    color: #ffffff;
  }

  .card-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 1rem;
    position: relative;
  }

  .card-header img {
    width: 45px;
    height: 45px;
    border-radius: 50%;
  }

  .card-header .status-dot {
    position: absolute;
    top: 0;
    right: 0;
  }

  .card-body {
    padding: 1rem 0;
    border-top: 1px solid #1a1a1a;
    border-bottom: 1px solid #1a1a1a;
    margin-bottom: 1rem;
  }

  .info-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    margin-bottom: 5px;
    color: #e0e0e0;
  }

  .card-action {
    width: 100%;
    background: #1a1a1a;
    color: #ffffff;
    border: 1px solid #333;
    padding: 10px;
    border-radius: 8px;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

</style> -->














<template>
  <div class="travelers-page">
    <header class="page-header">
      <div class="search-box">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input 
          type="text" 
          v-model="searchQuery" 
          placeholder="Search VIP Name, Passport, or Tier..." 
        />
      </div>
      <div class="actions">
        <button class="filter-btn"><i class="fa-solid fa-filter"></i> Filters</button>
        <button class="add-btn"><i class="fa-solid fa-plus"></i> Register VIP</button>
      </div>
    </header>

    <div class="status-ribbon">
      <div class="status-item">
        <span class="label">Total VIPs</span>
        <span v-if="!isLoading" class="count">{{ stats.total }}</span>
        <div v-else class="skeleton skeleton-text" style="width: 50px; height: 28px; margin-top: 4px;"></div>
      </div>
      <div class="divider"></div>
      <div class="status-item">
        <span class="label">In Transit</span>
        <span v-if="!isLoading" class="count highlight">{{ stats.inTransit }}</span>
        <div v-else class="skeleton skeleton-text" style="width: 50px; height: 28px; margin-top: 4px;"></div>
      </div>
      <div class="divider"></div>
      <div class="status-item">
        <span class="label">Elite Tier</span>
        <span v-if="!isLoading" class="count gold">{{ stats.eliteCount }}</span>
        <div v-else class="skeleton skeleton-text" style="width: 50px; height: 28px; margin-top: 4px;"></div>
      </div>
    </div>

    <div class="table-container shadow-premium">
      <table class="vip-table">
        <thead>
          <tr>
            <th style="width: 30%;">Traveler</th>
            <th style="width: 15%;">Passport/ID</th>
            <th style="width: 15%;">Membership Tier</th>
            <th style="width: 15%;">Total Spend</th>
            <th style="width: 15%;">Last Seen</th>
            <th style="width: 10%;">Status</th>
            <th style="width: 5%;"></th>
          </tr>
        </thead>

        <tbody v-if="isLoading">
          <tr v-for="i in 6" :key="'skel-' + i" class="table-row">
            <td>
              <div class="user-profile">
                <div class="skeleton skeleton-avatar"></div>
                <div class="user-info">
                  <div class="skeleton skeleton-text" style="width: 120px; height: 16px;"></div>
                  <div class="skeleton skeleton-text" style="width: 160px; height: 12px;"></div>
                </div>
              </div>
            </td>
            <td><div class="skeleton skeleton-text" style="width: 80px;"></div></td>
            <td><div class="skeleton skeleton-badge"></div></td>
            <td><div class="skeleton skeleton-text" style="width: 60px;"></div></td>
            <td><div class="skeleton skeleton-text" style="width: 90px;"></div></td>
            <td><div class="skeleton skeleton-text" style="width: 70px;"></div></td>
            <td><div class="skeleton" style="width: 24px; height: 24px; border-radius: 50%;"></div></td>
          </tr>
        </tbody>

        <tbody v-else>
          <tr v-for="vip in filteredVIPs" :key="vip.id" class="table-row">
            <td>
              <div class="user-profile">
                <div class="avatar-ring" :class="vip.tier?.toLowerCase()">
                  <img :src="vip.avatar" alt="VIP" />
                </div>
                <div class="user-info">
                  <span class="name">{{ vip.name }}</span>
                  <span class="email">{{ vip.email }}</span>
                </div>
              </div>
            </td>
            <td class="id-cell"><code>{{ vip.passport }}</code></td>
            <td>
              <span class="tier-badge" :class="vip.tier?.toLowerCase()">
                <i class="fa-solid fa-crown"></i> {{ vip.tier }}
              </span>
            </td>
            <td class="spend-cell">₹{{ vip.spend }}</td>
            <td class="date-cell">{{ vip.lastSeen }}</td>
            <td>
              <div class="status-dot" :class="vip.status?.toLowerCase()">
                <span>{{ vip.status }}</span>
              </div>
            </td>
            <td class="action-cell">
              <button class="icon-btn"><i class="fa-solid fa-ellipsis-vertical"></i></button>
            </td>
          </tr>
          <tr v-if="filteredVIPs.length === 0">
            <td colspan="7" class="empty-state">No VIP travelers found matching your search.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="mobile-grid">
      <template v-if="isLoading">
        <div v-for="i in 4" :key="'mob-skel-' + i" class="vip-mobile-card">
          <div class="card-header">
            <div class="skeleton skeleton-avatar" style="width: 45px; height: 45px;"></div>
            <div class="title">
              <div class="skeleton skeleton-text" style="width: 100px; height: 16px;"></div>
              <div class="skeleton skeleton-badge" style="margin-top: 8px;"></div>
            </div>
          </div>
          <div class="card-body">
            <div class="skeleton skeleton-text" style="width: 100%; height: 12px; margin-bottom: 12px;"></div>
            <div class="skeleton skeleton-text" style="width: 100%; height: 12px;"></div>
          </div>
          <div class="skeleton" style="width: 100%; height: 40px; border-radius: 8px;"></div>
        </div>
      </template>

      <template v-else>
        <div v-for="vip in filteredVIPs" :key="'mob-' + vip.id" class="vip-mobile-card">
          <div class="card-header">
            <img :src="vip.avatar" alt="" />
            <div class="title">
              <h4>{{ vip.name }}</h4>
              <span class="tier-badge" :class="vip.tier?.toLowerCase()">{{ vip.tier }}</span>
            </div>
            <div class="status-dot" :class="vip.status?.toLowerCase()"></div>
          </div>
          <div class="card-body">
            <div class="info-row"><span>ID:</span> <strong>{{ vip.passport }}</strong></div>
            <div class="info-row"><span>Spent:</span> <strong>₹{{ vip.spend }}</strong></div>
          </div>
          <button class="card-action">Manage Profile</button>
        </div>
      </template>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch, onUnmounted } from 'vue';

// --- State Management ---
const searchQuery = ref('');
const vips = ref([]);
const stats = ref({ total: 0, inTransit: 0, eliteCount: 0 });
const isLoading = ref(true); // Start as true for initial load
const hasError = ref(false);

// --- API Logic ---
// We use AbortController to cancel pending requests if a user types fast
let abortController = null;

const fetchTravelers = async () => {
  // Cancel any previous pending request
  if (abortController) abortController.abort();
  abortController = new AbortController();

  isLoading.value = true;
  hasError.value = false;

  try {
    const baseUrl = 'https://travel-xxnc.onrender.com/api/admin/travelers';
    const url = new URL(baseUrl);
    if (searchQuery.value) url.searchParams.append('search', searchQuery.value);

    const response = await fetch(url, {
      signal: abortController.signal,
      headers: {
        'Content-Type': 'application/json',
        // 'Authorization': `Bearer ${localStorage.getItem('admin_token')}` // Uncomment if needed
      }
    });

    if (!response.ok) throw new Error('Network response was not ok');

    const result = await response.json();

    if (result.success) {
      vips.value = result.data || [];
      stats.value = result.stats || { total: 0, inTransit: 0, eliteCount: 0 };
    } else {
      throw new Error(result.message || 'Failed to fetch data');
    }
  } catch (error) {
    if (error.name === 'AbortError') return; // Silent catch for user typing fast
    console.error("VIP Fetch Error:", error);
    hasError.value = true;
  } finally {
    // Artificial 300ms delay ensures the skeleton shimmer doesn't "flash" too quickly
    setTimeout(() => {
      isLoading.value = false;
    }, 300);
  }
};

// --- Search & Reactivity ---
let debounceTimeout;
watch(searchQuery, (newVal) => {
  // Immediate feedback: if user clears search, we might want to show loading instantly
  isLoading.value = true; 
  
  clearTimeout(debounceTimeout);
  debounceTimeout = setTimeout(() => {
    fetchTravelers();
  }, 400); // 400ms is standard for professional search UX
});

// --- Lifecycle ---
onMounted(() => {
  fetchTravelers();
});

// Cleanup to prevent memory leaks
onUnmounted(() => {
  if (debounceTimeout) clearTimeout(debounceTimeout);
  if (abortController) abortController.abort();
});

const filteredVIPs = computed(() => vips.value);
</script>

<style scoped>
.travelers-page {
  animation: fadeIn 0.6s ease-out;
  color: #ffffff;
}

/* Header & Search */
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
  gap: 1rem;
}

.search-box {
  background: #121212;
  border: 1px solid rgba(197, 160, 89, 0.35);
  padding: 0.8rem 1.2rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 1rem;
  flex: 1;
  max-width: 500px;
  color: #ffffff;
}

.search-box i {
  color: #cfcfcf;
}

.search-box input {
  background: none;
  border: none;
  color: #ffffff;
  width: 100%;
  outline: none;
}

.search-box input::placeholder {
  color: #b5b5b5;
}

.actions {
  display: flex;
  gap: 1rem;
}

.add-btn {
  background: #c5a059;
  color: #0c0c0c;
  border: none;
  padding: 0.8rem 1.5rem;
  border-radius: 10px;
  font-weight: 700;
  cursor: pointer;
}

.filter-btn {
  background: #1a1a1a;
  color: #ffffff;
  border: 1px solid #333;
  padding: 0.8rem 1.2rem;
  border-radius: 10px;
  cursor: pointer;
}

/* Status Ribbon */
.status-ribbon {
  background: #0c0c0c;
  border: 1px solid rgba(197, 160, 89, 0.15);
  padding: 1.5rem;
  border-radius: 16px;
  display: flex;
  align-items: center;
  gap: 3rem;
  margin-bottom: 2rem;
}

.status-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.status-item .label {
  color: #b0b0b0;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.status-item .count {
  font-size: 1.5rem;
  font-weight: 800;
  color: #ffffff;
}

.count.highlight {
  color: #00d2ff;
}

.count.gold {
  color: #c5a059;
}

.divider {
  width: 1px;
  height: 30px;
  background: rgba(255, 255, 255, 0.15);
}

/* Table Styling */
.table-container {
  background: #0c0c0c;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.vip-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  color: #ffffff;
}

.vip-table th {
  padding: 1.2rem;
  color: #cfcfcf;
  font-size: 0.75rem;
  text-transform: uppercase;
  border-bottom: 1px solid #1a1a1a;
}

.vip-table td {
  padding: 1.2rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  table-layout: fixed;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 12px;
  min-width: 220px; /* Ensures enough space for avatar + text */
  max-width: 280px;
}

.avatar-ring {
  /* This ensures the ring itself has a physical size */
  width: 46px; 
  height: 46px;
  padding: 2px;
  border-radius: 50%;
  border: 2px solid rgba(255, 255, 255, 0.1); /* Default subtle border */
  
  /* Flex centering ensures the image sits exactly in the middle */
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0; /* Prevents the avatar from squishing on mobile */
  transition: all 0.3s ease;
}

.avatar-ring.elite {
  border-color: #c5a059;
  box-shadow: 0 0 8px rgba(197, 160, 89, 0.2); /* Luxury glow */
}

.avatar-ring.gold {
  border-color: #ffd700;
  box-shadow: 0 0 8px rgba(255, 215, 0, 0.2);
}

.avatar-ring img {
  width: 100%;       /* Fills the 46px minus the padding */
  height: 100%;
  object-fit: cover; /* Important: prevents the face from stretching */
  border-radius: 50%;
  background-color: #1a1a1a; /* Placeholder color if image is transparent */
}

.name {
  display: block;
  font-weight: 600;
  font-size: 0.95rem;
  color: #ffffff;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.email {
  font-size: 0.75rem;
  color: #b5b5b5;
  white-space: nowrap;
  overflow: hidden; 
  text-overflow: ellipsis;
}

.id-cell code {
  background: rgba(255, 255, 255, 0.05);
  padding: 4px 8px;
  border-radius: 4px;
  font-family: 'Courier New', Courier, monospace;
}

.spend-cell,
.date-cell {
  color: #eaeaea;
}

/* Tier Badge */
.tier-badge {
  padding: 4px 10px;
  border-radius: 6px;
  font-size: 0.7rem;
  font-weight: 800;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.tier-badge.elite {
  background: rgba(197, 160, 89, 0.18);
  color: #c5a059;
  border: 1px solid rgba(197, 160, 89, 0.35);
}

.tier-badge.gold {
  background: rgba(255, 215, 0, 0.15);
  color: #ffd700;
  border: 1px solid rgba(255, 215, 0, 0.3);
}

/* Status */
.status-dot {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.8rem;
  color: #ffffff;
}

.status-dot::before {
  content: "";
  width: 8px;
  height: 8px;
  border-radius: 50%;
}

.status-dot.active::before {
  background: #00ff88;
  box-shadow: 0 0 10px rgba(0, 255, 136, 0.6);
}

.status-dot.transit::before {
  background: #00d2ff;
}

.status-dot.inactive::before {
  background: #ff4d4d;
}

/* Action */
.icon-btn {
  background: transparent;
  border: none;
  color: #ffffff;
  cursor: pointer;
}

/* Responsive */
.mobile-grid {
  display: none;
}

@media (max-width: 1024px) {
  .vip-table th:nth-child(4),
  .vip-table td:nth-child(4) {
    display: none;
  }
}

@media (max-width: 768px) {
  .table-container {
    display: none;
  }

  .mobile-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;
  }

  .vip-mobile-card {
    background: #121212;
    border-radius: 12px;
    padding: 1.2rem;
    border: 1px solid #1a1a1a;
    color: #ffffff;
  }

  .card-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 1rem;
    position: relative;
  }

  .card-header img {
    width: 45px;
    height: 45px;
    border-radius: 50%;
  }

  .card-header .status-dot {
    position: absolute;
    top: 0;
    right: 0;
  }

  .card-body {
    padding: 1rem 0;
    border-top: 1px solid #1a1a1a;
    border-bottom: 1px solid #1a1a1a;
    margin-bottom: 1rem;
  }

  .info-row {
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    margin-bottom: 5px;
    color: #e0e0e0;
  }

  .card-action {
    width: 100%;
    background: #1a1a1a;
    color: #ffffff;
    border: 1px solid #333;
    padding: 10px;
    border-radius: 8px;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}


/* Skeleton Base & Shimmer Effect */
.skeleton {
  background: #1a1a1a; /* Matches your card background */
  background-image: linear-gradient(
    90deg, 
    #1a1a1a 0px, 
    #252525 40px, 
    #1a1a1a 80px
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite linear;
  border-radius: 4px;
  display: inline-block;
}

@keyframes shimmer {
  0% { background-position: -100% 0; }
  100% { background-position: 100% 0; }
}



/* Skeleton Shapes */
.skeleton-text {
  height: 14px;
  width: 100%;
  margin-bottom: 0.5rem;
}

.skeleton-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  flex-shrink: 0;
}

.skeleton-badge {
  width: 80px;
  height: 24px;
  border-radius: 6px;
}


/* Fix for Layout Stability */
.vip-table {
  table-layout: fixed; /* Prevents column widths from changing when data arrives */
}

.empty-state {
  text-align: center;
  padding: 3rem !important;
  color: #666;
  font-style: italic;
}

</style>
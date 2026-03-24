<template>
  <div class="inquiry-dashboard">
    <header class="dashboard-header">
      <div class="header-content">
        <h2 class="text-white font-bold text-3xl uppercase tracking-tighter">Client Inquiries</h2>
        <div class="flex items-center gap-3 mt-1">
          <span class="pulse-icon"></span>
          <p class="text-[#c5a059] text-[10px] font-black uppercase tracking-[0.3em]">Live Lead Feed</p>
        </div>
      </div>
      <div class="header-actions">
        <div class="search-pill">
          <i class="fas fa-search text-[#c5a059]"></i>
          <input type="text" v-model="searchQuery" placeholder="Search Inquiries..." />
        </div>
        <button @click="refreshInquiries" class="refresh-btn">
          <i class="fas fa-sync-alt mr-2" :class="{ 'fa-spin': isLoading }"></i> Refresh
        </button>
      </div>
    </header>

    <div class="inquiry-filters">
      <button 
        v-for="s in statusFilters" :key="s"
        :class="['filter-btn', { 'active': activeStatusFilter === s }]"
        @click="activeStatusFilter = s"
      >
        {{ s }} ({{ getStatusCount(s) }})
      </button>
    </div>

    <div v-if="isLoading" class="loading-state">
      <div v-for="n in 5" :key="n" class="skeleton-inquiry-card">
        <div class="skeleton-header"></div>
        <div class="skeleton-body-row"></div>
        <div class="skeleton-body-row w-3/4"></div>
        <div class="skeleton-footer"></div>
      </div>
    </div>

    <div v-else-if="filteredInquiries.length === 0" class="empty-state">
      <i class="fas fa-inbox text-5xl mb-4 text-slate-700"></i>
      <p class="uppercase font-black text-xs tracking-widest text-slate-500">No Inquiries Found</p>
      <button v-if="searchQuery || activeStatusFilter !== 'All'" @click="resetFilters" class="text-[#c5a059] text-[10px] font-bold mt-2 underline">Clear Filters</button>
    </div>

    <div v-else class="inquiry-grid">
      <TransitionGroup name="inquiry-list">
        <div 
          v-for="inquiry in filteredInquiries" 
          :key="inquiry.id" 
          class="inquiry-card"
          :class="`status-${inquiry.status.toLowerCase().replace(' ', '-')}`"
        >
          <div class="card-header">
            <h3 class="client-name">{{ inquiry.name }}</h3>
            <span class="status-badge" :class="`status-${inquiry.status.toLowerCase().replace(' ', '-')}`">
              {{ inquiry.status }}
            </span>
          </div>
          
          <div class="card-body">
            <p class="detail-item"><i class="fas fa-envelope icon-gold"></i> {{ inquiry.email }}</p>
            <p class="detail-item"><i class="fas fa-phone-alt icon-gold"></i> {{ inquiry.phone }}</p>
            <p class="detail-item"><i class="fas fa-map-marker-alt icon-gold"></i> Destination: {{ inquiry.destination }}</p>
            <p class="detail-item"><i class="fas fa-users icon-gold"></i> Travelers: {{ inquiry.travelers }}</p>
            <p class="message-text"><i class="fas fa-comment-dots icon-gold"></i> {{ inquiry.message || 'No specific message.' }}</p>
          </div>

          <div class="card-footer">
            <span class="date-time">Inquired: {{ formatDateTime(inquiry.date) }}</span>
            <div class="action-buttons">
              <button @click="updateInquiryStatus(inquiry.id, 'Contacted')" 
                      :disabled="inquiry.status === 'Contacted'"
                      class="action-btn contact-btn">
                <i class="fas fa-user-check mr-1"></i> Contacted
              </button>
              <button @click="updateInquiryStatus(inquiry.id, 'Converted')" 
                      :disabled="inquiry.status === 'Converted'"
                      class="action-btn convert-btn">
                <i class="fas fa-check-double mr-1"></i> Convert
              </button>
              <button @click="updateInquiryStatus(inquiry.id, 'Ignored')" 
                      :disabled="inquiry.status === 'Ignored'"
                      class="action-btn ignore-btn">
                <i class="fas fa-times-circle mr-1"></i> Ignore
              </button>
            </div>
          </div>
        </div>
      </TransitionGroup>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

const inquiries = ref([]);
const isLoading = ref(true);
const searchQuery = ref('');
const activeStatusFilter = ref('All');
const statusFilters = ['All', 'New', 'In-Progress', 'Converted', 'Ignored']; // Matches your ENUM

// --- Fetch Data ---
const fetchInquiries = async () => {
  isLoading.value = true;
  try {
    const response = await axios.get('https://travel-xxnc.onrender.com//api/inquiries/list'); // Your new backend route
    if (response.data.success) {
      inquiries.value = response.data.data;
    }
  } catch (error) {
    console.error("Failed to fetch inquiries:", error);
    alert("Concierge system offline. Cannot retrieve inquiries.");
  } finally {
    isLoading.value = false;
  }
};

const refreshInquiries = () => {
  fetchInquiries();
};

// --- Update Inquiry Status (for the admin to manage) ---
const updateInquiryStatus = async (id, newStatus) => {
  if (!confirm(`Change status of inquiry ${id.substring(0, 4)}... to "${newStatus}"?`)) return;

  try {
    // You'll need a new backend endpoint for this: /inquiries/<id>/status
    const response = await axios.put(`https://travel-xxnc.onrender.com//api/inquiries/${id}/status`, { status: newStatus });
    if (response.data.success) {
      // Update the local data without re-fetching everything
      const index = inquiries.value.findIndex(i => i.id === id);
      if (index !== -1) {
        inquiries.value[index].status = newStatus;
      }
      alert(`Inquiry ${id.substring(0, 4)}... status updated to ${newStatus}.`);
    }
  } catch (error) {
    console.error("Failed to update status:", error);
    alert("Failed to update inquiry status.");
  }
};

// --- Computed Properties for Filtering & Search ---
const filteredInquiries = computed(() => {
  let filtered = inquiries.value;

  // Filter by status
  if (activeStatusFilter.value !== 'All') {
    filtered = filtered.filter(i => i.status === activeStatusFilter.value);
  }

  // Filter by search query
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    filtered = filtered.filter(i =>
      i.name.toLowerCase().includes(query) ||
      i.email.toLowerCase().includes(query) ||
      i.destination.toLowerCase().includes(query) ||
      i.message.toLowerCase().includes(query)
    );
  }
  return filtered;
});

const getStatusCount = (status) => {
  if (status === 'All') return inquiries.value.length;
  return inquiries.value.filter(i => i.status === status).length;
};

// --- UI Helpers ---
const formatDateTime = (isoString) => {
  if (!isoString) return 'N/A';
  const options = { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' };
  return new Date(isoString).toLocaleDateString('en-US', options);
};

const resetFilters = () => {
  searchQuery.value = '';
  activeStatusFilter.value = 'All';
};

// --- Lifecycle Hook ---
onMounted(fetchInquiries);
</script>

<style scoped>
/* --- Base Layout & Fonts --- */
.inquiry-dashboard {
  padding: clamp(1rem, 5vw, 2.5rem);
  max-width: 1600px;
  margin: 0 auto;
  min-height: 100vh;
  /*---background-color: #050505;*/
  color: #e0e0e0;
}

/* --- Dashboard Header --- */
.dashboard-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: clamp(2rem, 8vh, 4rem);
  gap: 2rem;
  flex-wrap: wrap; /* Allows header items to wrap on smaller screens */
}

.header-content { flex: 1; min-width: 250px; }
.header-actions { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }

.pulse-icon {
  width: 8px; height: 8px;
  background: #00ff88; /* Green for "live feed" */
  border-radius: 50%;
  box-shadow: 0 0 10px #00ff88;
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.8); }
  100% { opacity: 1; transform: scale(1); }
}

.search-pill {
  background: rgba(17, 17, 17, 0.8); backdrop-filter: blur(10px);
  border: 1px solid rgba(197, 160, 89, 0.15); border-radius: 12px;
  padding: 0.8rem 1.2rem; display: flex; align-items: center; gap: 12px;
  min-width: 280px; max-width: 400px; /* Constrain search width */
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
.search-pill:focus-within {
  border-color: #c5a059;
  box-shadow: 0 0 25px rgba(197, 160, 89, 0.1);
  min-width: 320px; /* Slight expansion on focus */
}
.search-pill input { background: transparent; border: none; color: white; outline: none; font-size: 0.9rem; font-weight: 500; width: 100%; }
.search-pill input::placeholder { color: #888; }

.refresh-btn {
  background: #222; border: 1px solid #444; color: #eee;
  padding: 0.8rem 1.5rem; border-radius: 12px;
  font-weight: 700; font-size: 0.8rem;
  cursor: pointer; transition: all 0.3s ease;
  display: flex; align-items: center; justify-content: center;
}
.refresh-btn:hover { background: #333; border-color: #c5a059; color: #c5a059; }

/* --- Inquiry Filters --- */
.inquiry-filters {
  display: flex;
  gap: 12px;
  margin-bottom: 30px;
  flex-wrap: wrap;
  justify-content: flex-start;
}
.filter-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: #aaa;
  padding: 8px 18px;
  border-radius: 8px;
  font-size: 0.75rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  white-space: nowrap; /* Prevent breaking status text */
}
.filter-btn:hover, .filter-btn.active {
  background: #c5a059;
  color: #000;
  border-color: #c5a059;
  box-shadow: 0 0 15px rgba(197, 160, 89, 0.2);
}

/* --- Inquiry Grid & Cards --- */
.inquiry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 2rem;
}

.inquiry-card {
  background: #0f0f0f;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.inquiry-card:hover {
  transform: translateY(-5px);
  border-color: rgba(197, 160, 89, 0.3);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}
.client-name {
  font-size: 1.4rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: -0.5px;
}
.status-badge {
  padding: 5px 12px;
  border-radius: 8px;
  font-size: 0.7rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  white-space: nowrap;
}
/* Status specific colors */
.status-new { background-color: #ef4444; color: #fff; } /* Red */
.status-in-progress { background-color: #f59e0b; color: #000; } /* Orange */
.status-converted { background-color: #10b981; color: #fff; } /* Green */
.status-ignored { background-color: #6b7280; color: #fff; } /* Gray */

.card-body {
  flex-grow: 1;
  margin-bottom: 1.5rem;
}
.detail-item {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  color: #bbb;
  margin-bottom: 8px;
}
.icon-gold { color: #c5a059; }
.message-text {
  font-size: 0.9rem;
  color: #aaa;
  line-height: 1.5;
  margin-top: 15px;
  background-color: rgba(255, 255, 255, 0.03);
  border-left: 3px solid #c5a059;
  padding: 12px 15px;
  border-radius: 8px;
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.card-footer {
  display: flex;
  flex-direction: column; /* Stack buttons on mobile */
  gap: 10px;
  padding-top: 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.05);
}
.date-time {
  font-size: 0.75rem;
  color: #888;
  text-align: right;
  margin-bottom: 10px; /* Space between date and buttons */
}
.action-buttons {
  display: flex;
  gap: 8px;
  flex-wrap: wrap; /* Allow buttons to wrap */
}
.action-btn {
  flex: 1; /* Distribute space evenly */
  padding: 10px 15px;
  border-radius: 8px;
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
}
.action-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  filter: grayscale(1);
}
.contact-btn { background-color: #2e7d32; color: white; } /* Dark Green */
.contact-btn:hover:not(:disabled) { background-color: #4caf50; }
.convert-btn { background-color: #c5a059; color: black; } /* Brand Gold */
.convert-btn:hover:not(:disabled) { background-color: #e0b86a; }
.ignore-btn { background-color: #424242; color: white; } /* Dark Gray */
.ignore-btn:hover:not(:disabled) { background-color: #616161; }

/* --- Loading State (Skeleton Loaders) --- */
.loading-state {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 2rem;
}
.skeleton-inquiry-card {
  background: #0f0f0f;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.03);
  padding: 1.5rem;
  overflow: hidden;
  pointer-events: none;
  animation: shimmer 1.8s infinite;
}
.skeleton-header { height: 25px; width: 70%; background: #1a1a1a; margin-bottom: 1rem; border-radius: 4px; }
.skeleton-body-row { height: 15px; background: #1a1a1a; margin-bottom: 10px; border-radius: 4px; }
.skeleton-footer { height: 40px; background: #1a1a1a; margin-top: 1.5rem; border-radius: 8px; }

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

/* --- Empty State --- */
.empty-state {
  grid-column: 1 / -1; /* Span full width in grid */
  padding: 80px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.02);
  border-radius: 20px;
  border: 1px dashed rgba(255, 255, 255, 0.05);
  margin-top: 30px;
}

/* --- Transition Group for Filtering --- */
.inquiry-list-move, /* apply transition to moving elements */
.inquiry-list-enter-active,
.inquiry-list-leave-active {
  transition: all 0.5s ease;
}

.inquiry-list-enter-from,
.inquiry-list-leave-to {
  opacity: 0;
  transform: scale(0.9);
}

/* ensure leaving items are taken out of layout flow so that moving
   animations can be calculated correctly. */
.inquiry-list-leave-active {
  position: absolute;
}


/* --- Responsive Adjustments --- */
@media (max-width: 1024px) {
  .inquiry-grid { grid-template-columns: repeat(2, 1fr); }
  .dashboard-header { flex-direction: column; align-items: flex-start; }
  .header-actions { width: 100%; justify-content: flex-start; }
  .search-pill { width: 100%; max-width: none; }
  .search-pill:focus-within { min-width: unset; }
  .inquiry-filters { justify-content: flex-start; }
}

@media (max-width: 768px) {
  .inquiry-dashboard { padding: 1.5rem; }
  .inquiry-grid { grid-template-columns: 1fr; }
  .dashboard-header { margin-bottom: 2rem; }
  .client-name { font-size: 1.2rem; }
  .action-buttons { flex-direction: column; }
  .action-btn { flex: none; width: 100%; }
  .date-time { text-align: left; margin-bottom: 15px; }
}
</style>
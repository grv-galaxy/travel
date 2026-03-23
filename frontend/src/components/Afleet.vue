<!-- <template>
  <div class="fleet-page">
    <header class="page-header">
      <div class="header-title">
        <h2 class="text-white font-bold text-2xl uppercase tracking-tighter">Fleet Command</h2>
        <p class="text-[#c5a059] text-[10px] font-bold tracking-[0.3em]">Asset Intelligence & Deployment</p>
      </div>
      <div class="actions">
        <button @click="showModal = true" class="add-asset-btn">
          <i class="fa-solid fa-plus"></i> Add Asset
        </button>
      </div>
    </header>

    <div class="fleet-grid">
      <div v-for="asset in fleet" :key="asset.id" class="asset-card shadow-premium group">
        <div class="asset-image relative overflow-hidden">
          <img :src="asset.image" :alt="asset.name" />
          <div class="asset-tag" :class="asset.status.toLowerCase()">{{ asset.status }}</div>
          
          <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-4">
            <button @click="decommissionAsset(asset.id)" class="bg-red-600/20 hover:bg-red-600 text-red-500 hover:text-white p-3 rounded-full transition-all border border-red-600/30">
              <i class="fa-solid fa-trash-can"></i>
            </button>
          </div>
        </div>
        
        <div class="asset-details">
          <div class="flex justify-between items-start mb-4">
            <div>
              <h3 class="text-white font-bold text-lg">{{ asset.name }}</h3>
              <p class="text-slate-400 text-xs font-medium">{{ asset.type }} • {{ asset.license }}</p>
            </div>
            <div class="health-gauge">
              <span class="text-[10px] text-slate-500 font-bold block text-right">Fuel</span>
              <div class="fuel-bar"><div class="fuel-inner" :style="{ width: asset.fuel + '%' }"></div></div>
            </div>
          </div>

          <div class="stats-row border-t border-white/5 pt-4">
            <div class="stat">
              <span class="label">Current VIP</span>
              <span class="value text-white font-bold">{{ asset.currentVip || 'Available' }}</span>
            </div>
            <div class="stat">
              <span class="label">ETA</span>
              <span class="value text-[#c5a059] font-bold">{{ asset.eta || 'N/A' }}</span>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row gap-2 mt-4">
            <button @click="updateAssetStatus(asset)" 
                    class="track-btn status-toggle-btn flex-1"
                    :class="{ 'is-maintenance': asset.status === 'Maintenance' }">
              <i class="fa-solid" :class="asset.status === 'Available' ? 'fa-wrench' : 'fa-check-circle'"></i> 
              <span class="btn-text">
                {{ asset.status === 'Available' ? 'Maintenance' : 'Ready for Duty' }}
              </span>
            </button>
            
            <button class="track-btn location-btn sm:w-12 flex items-center justify-center" title="Live Tracking">
              <i class="fa-solid fa-location-crosshairs"></i>
              <span class="sm:hidden ml-2">Track Asset</span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
       <div class="modal-content animate-slide-up">
        <div class="modal-header">
          <div>
            <h3 class="text-white font-bold text-lg uppercase tracking-wider">Register Asset</h3>
            <p class="text-[#c5a059] text-[9px] font-bold uppercase tracking-[0.2em]">Add to Command Inventory</p>
          </div>
          <button @click="showModal = false" class="close-btn">&times;</button>
        </div>

        <form @submit.prevent="submitAsset" class="modal-body">
          <div class="upload-zone" :class="{ 'has-preview': previewUrl }" @click="fileInput.click()">
            <input type="file" ref="fileInput" class="hidden" accept="image/*" @change="handleFileChange" />
            <div v-if="!previewUrl" class="upload-placeholder">
              <i class="fa-solid fa-camera-retro text-2xl text-[#c5a059] mb-2"></i>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-400">Upload Asset Visual</p>
            </div>
            <img v-else :src="previewUrl" class="upload-preview" />
            <div v-if="previewUrl" class="upload-overlay">Change Image</div>
          </div>

          <div class="form-group">
            <label>Asset Identity</label>
            <input v-model="newAsset.name" type="text" placeholder="e.g. Rolls-Royce Phantom" required />
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="form-group">
              <label>Registry / License</label>
              <input v-model="newAsset.license" type="text" placeholder="VIP-001" required />
            </div>
            <div class="form-group">
              <label>Asset Class</label>
              <select v-model="newAsset.type">
                <option value="Luxury Sedan">Luxury Sedan</option>
                <option value="Luxury SUV">Luxury SUV</option>
                <option value="Private Jet">Private Jet</option>
                <option value="Helicopter">Helicopter</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label>Initial Fuel / Power (%)</label>
            <input v-model.number="newAsset.fuel" type="range" min="0" max="100" class="fuel-slider" />
            <span class="text-right text-[10px] text-[#c5a059] font-bold">{{ newAsset.fuel }}% Charged</span>
          </div>

          <button type="submit" class="submit-btn" :disabled="isSyncing">
            <span v-if="!isSyncing">Authorize Asset Deployment</span>
            <span v-else class="flex items-center justify-center gap-2">
              <i class="fa-solid fa-circle-notch fa-spin"></i> Syncing with Cloud...
            </span>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const API_BASE = 'https://indoria-backend-805083888664.us-central1.run.app/api/admin/fleet/assets';

// --- State Management ---
const fleet = ref([]);
const showModal = ref(false);
const isSyncing = ref(false);
const previewUrl = ref(null);
const selectedFile = ref(null);
const fileInput = ref(null);

const newAsset = ref({
  name: '', license: '', type: 'Luxury Sedan', fuel: 100, status: 'Available'
});

// --- Logic ---

const fetchFleet = async () => {
  try {
    const response = await axios.get(API_BASE);
    if (response.data.success) fleet.value = response.data.data;
  } catch (error) {
    console.error("Fetch Error:", error);
  }
};

// DELETE FEATURE
const decommissionAsset = async (id) => {
  if (!confirm("Are you sure you want to decommission this asset? This action is irreversible.")) return;
  
  try {
    const response = await axios.delete(`${API_BASE}/${id}`);
    if (response.data.success) {
      fleet.value = fleet.value.filter(asset => asset.id !== id);
    }
  } catch (error) {
    alert("Failed to decommission asset.");
  }
};

// UPDATE (MODIFY) FEATURE
const updateAssetStatus = async (asset) => {
  const newStatus = asset.status === 'Available' ? 'Maintenance' : 'Available';
  
  try {
    const response = await axios.patch(`${API_BASE}/${asset.id}`, {
      status: newStatus
    });
    if (response.data.success) {
      asset.status = newStatus; // Local reactive update
    }
  } catch (error) {
    alert("Failed to update status.");
  }
};

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (!file) return;
  selectedFile.value = file;
  previewUrl.value = URL.createObjectURL(file);
};

const submitAsset = async () => {
  if (!selectedFile.value) return alert("Image required.");
  isSyncing.value = true;
  try {
    const formData = new FormData();
    formData.append('image', selectedFile.value);
    formData.append('name', newAsset.value.name);
    formData.append('license', newAsset.value.license);
    formData.append('type', newAsset.value.type);
    formData.append('fuel', newAsset.value.fuel);
    formData.append('status', newAsset.value.status);

    const response = await axios.post('https://indoria-backend-805083888664.us-central1.run.app/api/admin/fleet/add-asset', formData);
    if (response.data.success) {
      fleet.value.unshift(response.data.asset);
      resetForm();
      showModal.value = false;
    }
  } catch (error) {
    console.error(error);
  } finally {
    isSyncing.value = false;
  }
};

const resetForm = () => {
  newAsset.value = { name: '', license: '', type: 'Luxury Sedan', fuel: 100, status: 'Available' };
  previewUrl.value = null;
  selectedFile.value = null;
  if (fileInput.value) fileInput.value.value = "";
};

onMounted(fetchFleet);
</script>


<style scoped>
/* --- Existing Fleet Page Styles --- */
.fleet-page { animation: fadeIn 0.8s ease; }

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2.5rem;
}

.add-asset-btn {
  background: #c5a059;
  color: black;
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  font-weight: 800;
  border: none;
  cursor: pointer;
  text-transform: uppercase;
  font-size: 0.7rem;
  letter-spacing: 1px;
  transition: all 0.3s ease;
}

.add-asset-btn:hover {
  background: #d4b47a;
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(197, 160, 89, 0.4);
}

.fleet-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
}

.asset-card {
  background: #111;
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  overflow: hidden;
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.asset-card:hover { 
  transform: translateY(-5px); 
  border-color: rgba(197, 160, 89, 0.3); 
}

.asset-image {
  height: 180px;
  position: relative;
}

.asset-image img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.8); }

.asset-tag {
  position: absolute;
  top: 15px;
  right: 15px;
  padding: 5px 12px;
  border-radius: 50px;
  font-size: 10px;
  font-weight: 900;
  text-transform: uppercase;
}

.asset-tag.available { background: #00ff88; color: black; }
.asset-tag.in-transit { background: #00d2ff; color: black; }
.asset-tag.maintenance { background: #ff4d4d; color: white; }

.asset-details { padding: 1.5rem; }

.fuel-bar {
  width: 60px;
  height: 4px;
  background: #222;
  border-radius: 10px;
  margin-top: 4px;
}

.fuel-inner {
  height: 100%;
  background: #c5a059;
  border-radius: 10px;
  box-shadow: 0 0 10px #c5a059;
}

.stats-row { display: flex; justify-content: space-between; margin-bottom: 1.5rem; }
.stat { display: flex; flex-direction: column; gap: 4px; }
.stat .label { color: #555; font-size: 10px; font-weight: 800; text-transform: uppercase; }
.stat .value { font-size: 0.9rem; color: white; }

.track-btn {
  width: 100%;
  padding: 12px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
  font-weight: 800;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-radius: 10px;
  cursor: pointer;
  transition: 0.3s;
}

.track-btn:hover { background: white; color: black; }

/* --- New Modal & Form Styles --- */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

.modal-content {
  background: #0f0f0f;
  width: 100%;
  max-width: 450px;
  border-radius: 24px;
  border: 1px solid rgba(197, 160, 89, 0.2);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.modal-header {
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close-btn {
  color: #555;
  font-size: 1.5rem;
  background: none;
  border: none;
  cursor: pointer;
  transition: 0.3s;
}

.close-btn:hover { color: white; }

.modal-body { padding: 1.5rem; display: flex; flex-direction: column; gap: 1.25rem; }

.upload-zone {
  height: 140px;
  background: rgba(255, 255, 255, 0.03);
  border: 2px dashed rgba(197, 160, 89, 0.2);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: 0.3s;
}

.upload-zone:hover { border-color: #c5a059; background: rgba(197, 160, 89, 0.05); }

.upload-preview { width: 100%; height: 100%; object-fit: cover; }

.upload-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  color: white;
  font-size: 10px;
  text-transform: uppercase;
  font-weight: bold;
  transition: 0.3s;
}

.upload-zone:hover .upload-overlay { opacity: 1; }

.form-group { display: flex; flex-direction: column; gap: 0.5rem; }

.form-group label {
  font-size: 9px;
  text-transform: uppercase;
  color: #c5a059;
  font-weight: 800;
  letter-spacing: 1px;
}

.form-group input, .form-group select {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.8rem;
  border-radius: 10px;
  color: white;
  font-size: 13px;
  transition: 0.3s;
}

.form-group input:focus, .form-group select:focus { 
  border-color: #c5a059; 
  outline: none; 
  background: rgba(255, 255, 255, 0.08); 
}

.submit-btn {
  margin-top: 1rem;
  background: #c5a059;
  color: black;
  padding: 1rem;
  border-radius: 12px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  font-size: 11px;
  border: none;
  cursor: pointer;
  transition: 0.3s;
}

.submit-btn:hover:not(:disabled) { background: #d4b47a; transform: scale(1.02); }
.submit-btn:disabled { opacity: 0.5; cursor: not-allowed; }

.fuel-slider {
  accent-color: #c5a059;
  height: 4px;
  cursor: pointer;
}

.animate-slide-up { animation: slideUp 0.4s ease-out; }

@keyframes slideUp {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

/* --- Maintenance & Location Section --- */

/* Base button refinement */
.track-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 42px;
  white-space: nowrap;
}

/* Status Toggle Specifics */
.status-toggle-btn {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.status-toggle-btn.is-maintenance {
  border-color: rgba(255, 77, 77, 0.4);
  color: #ff4d4d;
  background: rgba(255, 77, 77, 0.05);
}

.status-toggle-btn.is-maintenance:hover {
  background: #ff4d4d;
  color: white;
  border-color: #ff4d4d;
}

/* Location Button Specifics */
.location-btn {
  background: rgba(197, 160, 89, 0.1);
  border-color: rgba(197, 160, 89, 0.2);
  color: #c5a059;
}

.location-btn:hover {
  background: #c5a059;
  color: black;
  border-color: #c5a059;
}

/* Maintenance Tag Animation */
.asset-tag.maintenance {
  background: #ff4d4d;
  color: white;
  box-shadow: 0 0 10px rgba(255, 77, 77, 0.5);
  animation: pulse-red 2s infinite;
}

@keyframes pulse-red {
  0% { box-shadow: 0 0 0 0 rgba(255, 77, 77, 0.7); }
  70% { box-shadow: 0 0 0 8px rgba(255, 77, 77, 0); }
  100% { box-shadow: 0 0 0 0 rgba(255, 77, 77, 0); }
}

/* --- Responsive Layout Adjustments --- */
@media (max-width: 640px) {
  .fleet-grid {
    grid-template-columns: 1fr; /* Single column on mobile */
    gap: 1.5rem;
  }
  
  .asset-card {
    border-radius: 16px;
  }
  
  .asset-image {
    height: 220px; /* Taller images on mobile for impact */
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1.5rem;
  }

  .add-asset-btn {
    width: 100%;
    text-align: center;
  }
}

/* Tablet optimization */
@media (min-width: 641px) and (max-width: 1024px) {
  .fleet-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

</style> -->
























<template>
  <div class="fleet-page">
    <header class="page-header">
      <div class="header-title">
        <h2 class="text-white font-bold text-2xl uppercase tracking-tighter">Fleet Command</h2>
        <p class="text-[#c5a059] text-[10px] font-bold tracking-[0.3em]">Asset Intelligence & Deployment</p>
      </div>
      <div class="actions">
        <button @click="showModal = true" class="add-asset-btn">
          <i class="fa-solid fa-plus"></i> Add Asset
        </button>
      </div>
    </header>

    <div class="fleet-grid">
      <template v-if="isLoading">
        <div v-for="i in 6" :key="'skeleton-' + i" class="asset-card skeleton-card">
          <div class="asset-image skeleton shimmer"></div>
          <div class="asset-details">
            <div class="flex justify-between items-start mb-4">
              <div class="w-2/3">
                <div class="skeleton skeleton-title shimmer mb-2"></div>
                <div class="skeleton skeleton-subtitle shimmer"></div>
              </div>
              <div class="w-1/4">
                <div class="skeleton skeleton-small shimmer mb-1"></div>
                <div class="skeleton skeleton-bar shimmer"></div>
              </div>
            </div>
            <div class="stats-row border-t border-white/5 pt-4">
              <div class="stat">
                <div class="skeleton skeleton-label shimmer mb-1"></div>
                <div class="skeleton skeleton-value shimmer"></div>
              </div>
              <div class="stat">
                <div class="skeleton skeleton-label shimmer mb-1"></div>
                <div class="skeleton skeleton-value shimmer"></div>
              </div>
            </div>
            <div class="flex gap-2 mt-4">
              <div class="skeleton skeleton-btn shimmer flex-1"></div>
              <div class="skeleton skeleton-btn shimmer w-12"></div>
            </div>
          </div>
        </div>
      </template>

      <template v-else>
      <div v-for="asset in fleet" :key="asset.id" class="asset-card shadow-premium group">
        <div class="asset-image relative overflow-hidden">
          <img :src="asset.image" :alt="asset.name" />
          <div class="asset-tag" :class="asset.status.toLowerCase()">{{ asset.status }}</div>
          
          <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center gap-4">
            <button @click="decommissionAsset(asset.id)" class="bg-red-600/20 hover:bg-red-600 text-red-500 hover:text-white p-3 rounded-full transition-all border border-red-600/30">
              <i class="fa-solid fa-trash-can"></i>
            </button>
          </div>
        </div>
        
        <div class="asset-details">
          <div class="flex justify-between items-start mb-4">
            <div>
              <h3 class="text-white font-bold text-lg">{{ asset.name }}</h3>
              <p class="text-slate-400 text-xs font-medium">{{ asset.type }} • {{ asset.license }}</p>
            </div>
            <div class="health-gauge">
              <span class="text-[10px] text-slate-500 font-bold block text-right">Fuel</span>
              <div class="fuel-bar"><div class="fuel-inner" :style="{ width: asset.fuel + '%' }"></div></div>
            </div>
          </div>

          <div class="stats-row border-t border-white/5 pt-4">
            <div class="stat">
              <span class="label">Current VIP</span>
              <span class="value text-white font-bold">{{ asset.currentVip || 'Available' }}</span>
            </div>
            <div class="stat">
              <span class="label">ETA</span>
              <span class="value text-[#c5a059] font-bold">{{ asset.eta || 'N/A' }}</span>
            </div>
          </div>

          <div class="flex flex-col sm:flex-row gap-2 mt-4">
            <button @click="updateAssetStatus(asset)" 
                    class="track-btn status-toggle-btn flex-1"
                    :class="{ 'is-maintenance': asset.status === 'Maintenance' }">
              <i class="fa-solid" :class="asset.status === 'Available' ? 'fa-wrench' : 'fa-check-circle'"></i> 
              <span class="btn-text">
                {{ asset.status === 'Available' ? 'Maintenance' : 'Ready for Duty' }}
              </span>
            </button>
            
            <button class="track-btn location-btn sm:w-12 flex items-center justify-center" title="Live Tracking">
              <i class="fa-solid fa-location-crosshairs"></i>
              <span class="sm:hidden ml-2">Track Asset</span>
            </button>
          </div>
        </div>
      </div>
      </template>
    </div>

    <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
       <div class="modal-content animate-slide-up">
        <div class="modal-header">
          <div>
            <h3 class="text-white font-bold text-lg uppercase tracking-wider">Register Asset</h3>
            <p class="text-[#c5a059] text-[9px] font-bold uppercase tracking-[0.2em]">Add to Command Inventory</p>
          </div>
          <button @click="showModal = false" class="close-btn">&times;</button>
        </div>

        <form @submit.prevent="submitAsset" class="modal-body">
          <div class="upload-zone" :class="{ 'has-preview': previewUrl }" @click="fileInput.click()">
            <input type="file" ref="fileInput" class="hidden" accept="image/*" @change="handleFileChange" />
            <div v-if="!previewUrl" class="upload-placeholder">
              <i class="fa-solid fa-camera-retro text-2xl text-[#c5a059] mb-2"></i>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-400">Upload Asset Visual</p>
            </div>
            <img v-else :src="previewUrl" class="upload-preview" />
            <div v-if="previewUrl" class="upload-overlay">Change Image</div>
          </div>

          <div class="form-group">
            <label>Asset Identity</label>
            <input v-model="newAsset.name" type="text" placeholder="e.g. Rolls-Royce Phantom" required />
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="form-group">
              <label>Registry / License</label>
              <input v-model="newAsset.license" type="text" placeholder="VIP-001" required />
            </div>
            <div class="form-group">
              <label>Asset Class</label>
              <select v-model="newAsset.type">
                <option value="Luxury Sedan">Luxury Sedan</option>
                <option value="Luxury SUV">Luxury SUV</option>
                <option value="Private Jet">Private Jet</option>
                <option value="Helicopter">Helicopter</option>
              </select>
            </div>
          </div>

          <div class="form-group">
            <label>Initial Fuel / Power (%)</label>
            <input v-model.number="newAsset.fuel" type="range" min="0" max="100" class="fuel-slider" />
            <span class="text-right text-[10px] text-[#c5a059] font-bold">{{ newAsset.fuel }}% Charged</span>
          </div>

          <button type="submit" class="submit-btn" :disabled="isSyncing">
            <span v-if="!isSyncing">Authorize Asset Deployment</span>
            <span v-else class="flex items-center justify-center gap-2">
              <i class="fa-solid fa-circle-notch fa-spin"></i> Syncing with Cloud...
            </span>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const API_BASE = 'https://indoria-backend-805083888664.us-central1.run.app/api/admin/fleet/assets';

// --- State Management ---
const fleet = ref([]);
const showModal = ref(false);
const isSyncing = ref(false);
const isLoading = ref(true);
const previewUrl = ref(null);
const selectedFile = ref(null);
const fileInput = ref(null);

const newAsset = ref({
  name: '', license: '', type: 'Luxury Sedan', fuel: 100, status: 'Available'
});

// --- Logic ---

const fetchFleet = async () => {
  isLoading.value = true;
  try {
    const response = await axios.get(API_BASE);
    if (response.data.success) fleet.value = response.data.data;
  } catch (error) {
    console.error("Fetch Error:", error);
  } finally {
    setTimeout(() => {  
      isLoading.value = false;
    }, 600); // Simulated delay for better UX
  }
};

// DELETE FEATURE
const decommissionAsset = async (id) => {
  if (!confirm("Are you sure you want to decommission this asset? This action is irreversible.")) return;
  
  try {
    const response = await axios.delete(`${API_BASE}/${id}`);
    if (response.data.success) {
      fleet.value = fleet.value.filter(asset => asset.id !== id);
    }
  } catch (error) {
    alert("Failed to decommission asset.");
  }
};

// UPDATE (MODIFY) FEATURE
const updateAssetStatus = async (asset) => {
  const newStatus = asset.status === 'Available' ? 'Maintenance' : 'Available';
  
  try {
    const response = await axios.patch(`${API_BASE}/${asset.id}`, {
      status: newStatus
    });
    if (response.data.success) {
      asset.status = newStatus; // Local reactive update
    }
  } catch (error) {
    alert("Failed to update status.");
  }
};

const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (!file) return;
  selectedFile.value = file;
  previewUrl.value = URL.createObjectURL(file);
};

const submitAsset = async () => {
  if (!selectedFile.value) return alert("Image required.");
  isSyncing.value = true;
  try {
    const formData = new FormData();
    formData.append('image', selectedFile.value);
    formData.append('name', newAsset.value.name);
    formData.append('license', newAsset.value.license);
    formData.append('type', newAsset.value.type);
    formData.append('fuel', newAsset.value.fuel);
    formData.append('status', newAsset.value.status);

    const response = await axios.post('https://indoria-backend-805083888664.us-central1.run.app/api/admin/fleet/add-asset', formData);
    if (response.data.success) {
      fleet.value.unshift(response.data.asset);
      resetForm();
      showModal.value = false;
    }
  } catch (error) {
    console.error(error);
  } finally {
    isSyncing.value = false;
  }
};

const resetForm = () => {
  newAsset.value = { name: '', license: '', type: 'Luxury Sedan', fuel: 100, status: 'Available' };
  previewUrl.value = null;
  selectedFile.value = null;
  if (fileInput.value) fileInput.value.value = "";
};

onMounted(fetchFleet);
</script>


<style scoped>
/* --- Existing Fleet Page Styles --- */
.fleet-page { animation: fadeIn 0.8s ease; }

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2.5rem;
}

.add-asset-btn {
  background: #c5a059;
  color: black;
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  font-weight: 800;
  border: none;
  cursor: pointer;
  text-transform: uppercase;
  font-size: 0.7rem;
  letter-spacing: 1px;
  transition: all 0.3s ease;
}

.add-asset-btn:hover {
  background: #d4b47a;
  transform: scale(1.05);
  box-shadow: 0 0 15px rgba(197, 160, 89, 0.4);
}

.fleet-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 2rem;
}

.asset-card {
  background: #111;
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.05);
  overflow: hidden;
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.asset-card:hover { 
  transform: translateY(-5px); 
  border-color: rgba(197, 160, 89, 0.3); 
}

.asset-image {
  height: 180px;
  position: relative;
}

.asset-image img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.8); }

.asset-tag {
  position: absolute;
  top: 15px;
  right: 15px;
  padding: 5px 12px;
  border-radius: 50px;
  font-size: 10px;
  font-weight: 900;
  text-transform: uppercase;
}

.asset-tag.available { background: #00ff88; color: black; }
.asset-tag.in-transit { background: #00d2ff; color: black; }
.asset-tag.maintenance { background: #ff4d4d; color: white; }

.asset-details { padding: 1.5rem; }

.fuel-bar {
  width: 60px;
  height: 4px;
  background: #222;
  border-radius: 10px;
  margin-top: 4px;
}

.fuel-inner {
  height: 100%;
  background: #c5a059;
  border-radius: 10px;
  box-shadow: 0 0 10px #c5a059;
}

.stats-row { display: flex; justify-content: space-between; margin-bottom: 1.5rem; }
.stat { display: flex; flex-direction: column; gap: 4px; }
.stat .label { color: #555; font-size: 10px; font-weight: 800; text-transform: uppercase; }
.stat .value { font-size: 0.9rem; color: white; }

.track-btn {
  width: 100%;
  padding: 12px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
  color: white;
  font-weight: 800;
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 1px;
  border-radius: 10px;
  cursor: pointer;
  transition: 0.3s;
}

.track-btn:hover { background: white; color: black; }

/* --- New Modal & Form Styles --- */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 1rem;
}

.modal-content {
  background: #0f0f0f;
  width: 100%;
  max-width: 450px;
  border-radius: 24px;
  border: 1px solid rgba(197, 160, 89, 0.2);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  overflow: hidden;
}

.modal-header {
  padding: 1.5rem;
  background: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.close-btn {
  color: #555;
  font-size: 1.5rem;
  background: none;
  border: none;
  cursor: pointer;
  transition: 0.3s;
}

.close-btn:hover { color: white; }

.modal-body { padding: 1.5rem; display: flex; flex-direction: column; gap: 1.25rem; }

.upload-zone {
  height: 140px;
  background: rgba(255, 255, 255, 0.03);
  border: 2px dashed rgba(197, 160, 89, 0.2);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: 0.3s;
}

.upload-zone:hover { border-color: #c5a059; background: rgba(197, 160, 89, 0.05); }

.upload-preview { width: 100%; height: 100%; object-fit: cover; }

.upload-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0,0,0,0.6);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  color: white;
  font-size: 10px;
  text-transform: uppercase;
  font-weight: bold;
  transition: 0.3s;
}

.upload-zone:hover .upload-overlay { opacity: 1; }

.form-group { display: flex; flex-direction: column; gap: 0.5rem; }

.form-group label {
  font-size: 9px;
  text-transform: uppercase;
  color: #c5a059;
  font-weight: 800;
  letter-spacing: 1px;
}

.form-group input, .form-group select {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  padding: 0.8rem;
  border-radius: 10px;
  color: white;
  font-size: 13px;
  transition: 0.3s;
}

.form-group input:focus, .form-group select:focus { 
  border-color: #c5a059; 
  outline: none; 
  background: rgba(255, 255, 255, 0.08); 
}

.submit-btn {
  margin-top: 1rem;
  background: #c5a059;
  color: black;
  padding: 1rem;
  border-radius: 12px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  font-size: 11px;
  border: none;
  cursor: pointer;
  transition: 0.3s;
}

.submit-btn:hover:not(:disabled) { background: #d4b47a; transform: scale(1.02); }
.submit-btn:disabled { opacity: 0.5; cursor: not-allowed; }

.fuel-slider {
  accent-color: #c5a059;
  height: 4px;
  cursor: pointer;
}

.animate-slide-up { animation: slideUp 0.4s ease-out; }

@keyframes slideUp {
  from { transform: translateY(20px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

/* --- Maintenance & Location Section --- */

/* Base button refinement */
.track-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 42px;
  white-space: nowrap;
}

/* Status Toggle Specifics */
.status-toggle-btn {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.status-toggle-btn.is-maintenance {
  border-color: rgba(255, 77, 77, 0.4);
  color: #ff4d4d;
  background: rgba(255, 77, 77, 0.05);
}

.status-toggle-btn.is-maintenance:hover {
  background: #ff4d4d;
  color: white;
  border-color: #ff4d4d;
}

/* Location Button Specifics */
.location-btn {
  background: rgba(197, 160, 89, 0.1);
  border-color: rgba(197, 160, 89, 0.2);
  color: #c5a059;
}

.location-btn:hover {
  background: #c5a059;
  color: black;
  border-color: #c5a059;
}

/* Maintenance Tag Animation */
.asset-tag.maintenance {
  background: #ff4d4d;
  color: white;
  box-shadow: 0 0 10px rgba(255, 77, 77, 0.5);
  animation: pulse-red 2s infinite;
}

@keyframes pulse-red {
  0% { box-shadow: 0 0 0 0 rgba(255, 77, 77, 0.7); }
  70% { box-shadow: 0 0 0 8px rgba(255, 77, 77, 0); }
  100% { box-shadow: 0 0 0 0 rgba(255, 77, 77, 0); }
}

/* --- Responsive Layout Adjustments --- */
@media (max-width: 640px) {
  .fleet-grid {
    grid-template-columns: 1fr; /* Single column on mobile */
    gap: 1.5rem;
  }
  
  .asset-card {
    border-radius: 16px;
  }
  
  .asset-image {
    height: 220px; /* Taller images on mobile for impact */
  }

  .page-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 1.5rem;
  }

  .add-asset-btn {
    width: 100%;
    text-align: center;
  }
}

/* Tablet optimization */
@media (min-width: 641px) and (max-width: 1024px) {
  .fleet-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}





/* --- Skeleton Loading System --- */

/* 1. The Shimmer Base */
.skeleton {
  background: #1a1a1a;
  background-image: linear-gradient(
    90deg, 
    rgba(255, 255, 255, 0) 0, 
    rgba(255, 255, 255, 0.05) 50%, 
    rgba(255, 255, 255, 0) 100%
  );
  background-size: 200% 100%;
  border-radius: 4px;
}

/* 2. The Animation Logic */
.shimmer {
  animation: placeholderShimmer 1.5s infinite linear;
}

@keyframes placeholderShimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

/* 3. Skeleton Shapes to match Asset Card UI */
.skeleton-card {
  pointer-events: none; /* Disable interaction while loading */
  border-color: rgba(255, 255, 255, 0.03) !important;
}

.skeleton-title {
  height: 24px;
  width: 80%;
}

.skeleton-subtitle {
  height: 14px;
  width: 50%;
}

.skeleton-label {
  height: 10px;
  width: 40px;
}

.skeleton-value {
  height: 18px;
  width: 100px;
}

.skeleton-small {
  height: 10px;
  width: 30px;
  margin-left: auto; /* Align right like the 'Fuel' label */
}

.skeleton-bar {
  height: 4px;
  width: 60px;
  margin-left: auto;
}

.skeleton-btn {
  height: 42px;
  border-radius: 10px;
}

/* Ensure the image area stays the correct size during load */
.asset-image.skeleton {
  height: 180px;
  width: 100%;
  border-radius: 0;
}

</style>
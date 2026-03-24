<!-- <template>
  <div class="destinations-page">
    <header class="page-header">
      <div class="header-info">
        <h2 class="text-white font-bold text-3xl uppercase tracking-tighter">Global Hotspots</h2>
        <div class="flex items-center gap-3 mt-1">
          <span class="pulse-icon"></span>
          <p class="text-[#c5a059] text-[10px] font-black uppercase tracking-[0.3em]">Live Intelligence Feed</p>
        </div>
      </div>
      <div class="actions">
        <div class="search-pill">
          <i class="fa-solid fa-earth-americas text-[#c5a059]"></i>
          <input type="text" v-model="searchQuery" placeholder="Locate Destination..." />
        </div>
        
        <button @click="openAddModal" class="add-btn">
          <i class="fa-solid fa-plus"></i> New Hotspot
        </button>
      </div>
    </header>

    <div class="destinations-grid">
      <div v-for="loc in filteredDestinations" :key="loc.id" class="location-card">
        <div class="card-media">
          <img :src="loc.image" :alt="loc.name" class="main-img" />
          <div class="overlay-gradient"></div>
          
          <button @click="deleteHotspot(loc.id)" class="absolute top-3 right-3 z-10 text-red-500/50 hover:text-red-500 transition-colors bg-black/40 p-2 rounded-full backdrop-blur-md">
            <i class="fa-solid fa-trash-can text-xs"></i>
          </button>

          <div class="occupancy-tag font-bold">
            <i class="fa-solid fa-user-group text-[10px]"></i> {{ loc.activeVips || 0 }} VIPs
          </div>
          <div class="status-badge" :class="loc.status?.toLowerCase().replace(' ', '-')">
            {{ loc.status }}
          </div>
        </div>

        <div class="card-body">
          <div class="flex justify-between items-start mb-4">
            <div>
              <h3 class="text-white font-bold text-xl tracking-tight">{{ loc.name }}</h3>
              <p class="text-[#c5a059] text-[10px] font-black uppercase tracking-widest">{{ loc.region }} • {{ loc.category }}</p>
            </div>
            <div class="weather-info text-right">
              <span class="text-white font-bold block">{{ loc.temp }}°C</span>
              <span class="text-slate-500 text-[9px] font-bold uppercase">{{ loc.weather }}</span>
            </div>
          </div>

          <div class="capacity-section mb-6">
            <div class="flex justify-between text-[10px] font-bold uppercase mb-2">
              <span class="text-slate-400">Resource Capacity</span>
              <span class="text-white">{{ loc.capacity }}%</span>
            </div>
            <div class="progress-bg">
              <div class="progress-fill" :style="{ width: loc.capacity + '%' }" :class="getCapacityClass(loc.capacity)"></div>
            </div>
          </div>

          <div class="card-footer">
            <button @click="editHotspot(loc)" class="action-btn-main">Modify Protocol</button>
            <div class="text-right">
              <span class="block text-[8px] text-slate-500 uppercase font-black">Base Price</span>
              <span class="text-white font-bold text-sm">₹{{ loc.price }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content animate-slide-up">
        <div class="modal-header">
          <div>
            <h3 class="text-white font-bold text-lg uppercase tracking-wider">
              {{ isEditing ? 'Modify Hotspot' : 'Deploy Hotspot' }}
            </h3>
            <p class="text-[#c5a059] text-[9px] font-bold uppercase tracking-[0.2em]">Intelligence Network Sync</p>
          </div>
          <button @click="closeModal" class="close-btn">&times;</button>
        </div>

        <form @submit.prevent="submitDestination" class="modal-body custom-scrollbar">
          <div class="upload-zone" :class="{ 'has-preview': previewUrl }" @click="fileInput.click()">
            <input type="file" ref="fileInput" class="hidden" accept="image/*" @change="handleFileChange" />
            <div v-if="!previewUrl" class="upload-placeholder text-center">
              <i class="fa-solid fa-map-location-dot text-2xl text-[#c5a059] mb-2"></i>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-400">Upload Visual Asset</p>
            </div>
            <img v-else :src="previewUrl" class="upload-preview" />
          </div>

          <div class="form-group mt-4">
            <label>Location Name</label>
            <input v-model="newDest.name" type="text" placeholder="e.g. Udaipur Palace" required />
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="form-group">
              <label>Region/Country</label>
              <input v-model="newDest.region" type="text" placeholder="e.g. Rajasthan" required />
            </div>
            <div class="form-group">
              <label>Category</label>
              <select v-model="newDest.category">
                <option value="Beach">Beach</option>
                <option value="Mountain">Mountain</option>
                <option value="City">City</option>
                <option value="Cultural">Cultural</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="form-group">
              <label>Starting Price (₹)</label>
              <input v-model.number="newDest.price" type="number" required />
            </div>
            <div class="form-group">
              <label>Live Status</label>
              <select v-model="newDest.status">
                <option value="Optimal">Optimal</option>
                <option value="High Peak">High Peak</option>
                <option value="Restricted">Restricted</option>
              </select>
            </div>
          </div>

          <div class="itinerary-builder-section border-t border-[#c5a059]/20 pt-6 mt-6">
            <div class="flex justify-between items-center mb-4">
              <h4 class="text-[#c5a059] text-[10px] font-black uppercase tracking-widest">Journey Itinerary Builder</h4>
              <button type="button" @click="addItineraryDay" class="add-day-btn">
                <i class="fa-solid fa-plus text-[8px]"></i> Add Day
              </button>
            </div>

            <div class="itinerary-list">
              <div v-for="(step, index) in itinerarySteps" :key="index" class="itinerary-step-card animate-slide-in">
                <div class="flex justify-between items-center mb-3">
                  <span class="day-label">Day {{ index + 1 }}</span>
                  <button type="button" @click="removeItineraryDay(index)" class="text-red-500/50 hover:text-red-500">
                    <i class="fa-solid fa-trash-can text-[10px]"></i>
                  </button>
                </div>
                <input v-model="step.title" type="text" placeholder="Activity Title (e.g. Royal Arrival)" class="mb-2" />
                <textarea v-model="step.activity" placeholder="Describe the day's experience..." rows="2"></textarea>
              </div>
            </div>
          </div>

          <div class="form-group mt-6">
            <label>Short Excerpt (Catchy Summary)</label>
            <input v-model="newDest.excerpt" type="text" placeholder="e.g. Experience the Venice of the East.... " maxlength="150"/>
          </div>

          <div class="form-group mt-6">
            <label>Full Description (Heritage Story)</label>
            <textarea v-model="newDest.description" placeholder="Write the full story..." rows="4"></textarea>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="form-group">
              <label>Temp (°C)</label>
              <input v-model.number="newDest.temp" type="number" />
            </div>
            <div class="form-group">
              <label>Weather</label>
              <input v-model="newDest.weather" type="text" placeholder="e.g. Sunny" />
            </div>
          </div>

          <div class="form-group">
            <label>Resource Capacity ({{ newDest.capacity }}%)</label>
            <input v-model.number="newDest.capacity" type="range" min="0" max="100" class="fuel-slider" />
          </div>

          <button type="submit" class="submit-btn" :disabled="isSyncing">
            <span v-if="!isSyncing">{{ isEditing ? 'Update Records' : 'Authorize Deployment' }}</span>
            <span v-else><i class="fa-solid fa-circle-notch fa-spin"></i> Syncing...</span>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>



<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

// --- State Management ---
const destinations = ref([]);
const searchQuery = ref('');
const showModal = ref(false);
const isSyncing = ref(false);
const isEditing = ref(false);
const currentEditId = ref(null);

// --- Form & Media State ---
const previewUrl = ref(null);
const selectedFile = ref(null);
const fileInput = ref(null);

// --- New Itinerary State ---
const itinerarySteps = ref([]); 

const newDest = ref({
  name: '',
  region: '',
  category: 'Beach',
  price: 0,
  excerpt: '',
  description: '', // Full story
  status: 'Optimal',
  temp: 25,
  weather: 'Clear',
  capacity: 50,
  activeVips: 0
});

// --- Fetch Logic ---
const fetchDestinations = async () => {
  try {
    const response = await axios.get('https://travel-xxnc.onrender.com//api/admin/destinations');
    if (response.data.success) destinations.value = response.data.data;
  } catch (error) {
    console.error("Fetch Error:", error);
  }
};

// --- Itinerary Builder Functions ---
const addItineraryDay = () => {
  itinerarySteps.value.push({
    day_number: itinerarySteps.value.length + 1,
    title: '',
    activity: ''
  });
};

const removeItineraryDay = (index) => {
  itinerarySteps.value.splice(index, 1);
  // Normalize day numbers after deletion
  itinerarySteps.value.forEach((step, i) => {
    step.day_number = i + 1;
  });
};

// --- Modal Controls ---
const openAddModal = () => {
  isEditing.value = false;
  currentEditId.value = null;
  resetForm();
  showModal.value = true;
};

const editHotspot = async (loc) => {
  isEditing.value = true;
  currentEditId.value = loc.id;
  
  // Fill basic fields
  newDest.value = { ...loc };
  previewUrl.value = loc.image;

  // Fetch full details (including itinerary) for this ID
  try {
    const res = await axios.get(`https://travel-xxnc.onrender.com//api/destinations/${loc.id}/details`);
    if (res.data.success) {
      itinerarySteps.value = res.data.data.itinerary || [];
    }
  } catch (err) {
    console.error("Error loading itinerary for edit:", err);
  }
  
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
  resetForm();
};

const resetForm = () => {
  newDest.value = { 
    name: '', region: '', category: 'Beach', price: 0, 
    excerpt: '', description: '', status: 'Optimal', 
    temp: 25, weather: 'Clear', capacity: 50, activeVips: 0 
  };
  itinerarySteps.value = [];
  previewUrl.value = null; 
  selectedFile.value = null;
  if (fileInput.value) fileInput.value.value = "";
};

// --- File Handling ---
const handleFileChange = (e) => {
  const file = e.target.files[0];
  if (!file) return;
  selectedFile.value = file;
  previewUrl.value = URL.createObjectURL(file);
};

// --- Submit Logic (Hotspot + Itinerary) ---
const submitDestination = async () => {
  // Validation: If adding new, require image
  if (!isEditing.value && !selectedFile.value) return alert("Image required for deployment.");
  
  isSyncing.value = true;
  
  try {
    const formData = new FormData();
    
    // Append File if exists
    if (selectedFile.value) formData.append('image', selectedFile.value);
    
    // Append basic fields
    Object.keys(newDest.value).forEach(key => {
      formData.append(key, newDest.value[key]);
    });

    // Append Itinerary as JSON string
    formData.append('itinerary', JSON.stringify(itinerarySteps.value));

    const url = isEditing.value 
      ? `https://travel-xxnc.onrender.com//api/admin/destinations/${currentEditId.value}`
      : 'https://travel-xxnc.onrender.com//api/admin/destinations/add';
    
    const method = isEditing.value ? 'put' : 'post';
    const response = await axios[method](url, formData);

    if (response.data.success) {
      await fetchDestinations();
      closeModal();
    }
  } catch (error) {
    console.error("Sync Error:", error);
    alert("Synchronization with Intelligence Network failed.");
  } finally {
    isSyncing.value = false;
  }
};

const deleteHotspot = async (id) => {
  if (!confirm("Decommission this hotspot from the global map?")) return;
  try {
    const res = await axios.delete(`https://travel-xxnc.onrender.com//api/admin/destinations/${id}`);
    if (res.data.success) {
      destinations.value = destinations.value.filter(d => d.id !== id);
    }
  } catch (error) {
    alert("Delete operation failed.");
  }
};

// --- Computed & Helpers ---
const filteredDestinations = computed(() => {
  return destinations.value.filter(d => 
    d.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    d.region.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const getCapacityClass = (val) => val > 80 ? 'high' : val < 30 ? 'low' : 'med';

onMounted(fetchDestinations);
</script>



<style scoped>
/* --- Global Page & Layout --- */
.destinations-page { 
  animation: fadeIn 0.8s ease; 
  padding: 1rem; 
  max-width: 1400px; 
  margin: 0 auto;
  padding-bottom: 100px; 
}

/* --- Header Section --- */
.page-header { 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
  margin-bottom: 3rem; 
  gap: 1.5rem; 
  flex-wrap: wrap; 
}

.header-info { flex: 1; min-width: 250px; }

.pulse-icon { 
  width: 8px; height: 8px; 
  background: #c5a059; 
  border-radius: 50%; 
  box-shadow: 0 0 10px #c5a059; 
  animation: pulse 2s infinite; 
}

.actions { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }

.search-pill { 
  background: #111; 
  border: 1px solid rgba(197, 160, 89, 0.2); 
  border-radius: 50px; 
  padding: 0.6rem 1.2rem; 
  display: flex; 
  align-items: center; 
  gap: 10px; 
  min-width: 280px; 
  transition: 0.3s;
}

.search-pill:focus-within { border-color: #c5a059; box-shadow: 0 0 15px rgba(197, 160, 89, 0.1); }
.search-pill input { background: transparent; border: none; color: white; outline: none; font-size: 0.8rem; font-weight: 600; width: 100%; }

.add-btn { 
  background: #c5a059; 
  color: black; 
  border: none; 
  padding: 0.8rem 1.5rem; 
  border-radius: 50px; 
  font-weight: 800; 
  font-size: 0.7rem; 
  text-transform: uppercase; 
  cursor: pointer; 
  transition: 0.3s cubic-bezier(0.23, 1, 0.32, 1);
  white-space: nowrap;
}

.add-btn:hover { background: white; transform: scale(1.05); }

/* --- Grid System --- */
.destinations-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); 
  gap: 2rem; 
}

/* --- Destination Cards --- */
.location-card { 
  background: #0c0c0c; 
  border-radius: 20px; 
  overflow: hidden; 
  border: 1px solid rgba(255,255,255,0.05); 
  transition: 0.4s cubic-bezier(0.23, 1, 0.32, 1); 
  display: flex;
  flex-direction: column;
}

.location-card:hover { 
  transform: translateY(-8px); 
  border-color: rgba(197, 160, 89, 0.4); 
  box-shadow: 0 20px 40px rgba(0,0,0,0.6); 
}

.card-media { 
  height: 160px; /* Reduced for density */
  position: relative; 
  overflow: hidden; 
}

.main-img { width: 100%; height: 100%; object-fit: cover; transition: 0.8s; }
.location-card:hover .main-img { scale: 1.1; filter: brightness(0.6); }

.overlay-gradient { 
  position: absolute; 
  inset: 0; 
  background: linear-gradient(to bottom, transparent, rgba(12, 12, 12, 0.95)); 
}

/* Float Tags */
.occupancy-tag { 
  position: absolute; top: 15px; left: 15px; 
  background: rgba(0,0,0,0.7); 
  backdrop-filter: blur(10px); 
  color: white; padding: 5px 12px; 
  border-radius: 50px; font-size: 0.65rem; 
  border: 1px solid rgba(255,255,255,0.1); 
  z-index: 10;
}

.status-badge { 
  position: absolute; bottom: 15px; right: 15px; 
  font-size: 8px; font-weight: 900; 
  text-transform: uppercase; letter-spacing: 1px; 
  padding: 4px 10px; border-radius: 4px; 
  z-index: 10;
}

.status-badge.optimal { background: #00ff88; color: black; }
.status-badge.high { background: #ffd700; color: black; }
.status-badge.restricted { background: #ff4d4d; color: white; }

.card-body { padding: 1.25rem; flex-grow: 1; }

/* Progress Bar */
.capacity-section { margin-bottom: 1.25rem; }
.progress-bg { height: 4px; background: #1a1a1a; border-radius: 10px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 10px; transition: 1.2s ease-in-out; }
.progress-fill.low { background: #00d2ff; }
.progress-fill.med { background: #c5a059; }
.progress-fill.high { background: #ff4d4d; box-shadow: 0 0 10px rgba(255, 77, 77, 0.5); }

/* Footer Buttons */
.card-footer { display: flex; gap: 8px; }
.action-btn-main { 
  flex: 1; background: rgba(255,255,255,0.03); 
  border: 1px solid rgba(255,255,255,0.1); 
  color: white; padding: 10px; border-radius: 10px; 
  font-weight: 800; font-size: 0.7rem; 
  text-transform: uppercase; cursor: pointer; transition: 0.3s; 
}
.action-btn-main:hover { background: white; color: black; }

.action-btn-icon { 
  width: 40px; background: rgba(197, 160, 89, 0.1); 
  border: 1px solid rgba(197, 160, 89, 0.2); 
  color: #c5a059; border-radius: 10px; cursor: pointer; 
  transition: 0.3s;
}
.action-btn-icon:hover { background: #c5a059; color: black; }

/* --- Modal Styles --- */
.modal-overlay {
  position: fixed; 
  inset: 0; 
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(10px); 
  z-index: 1000;
  display: flex; 
  align-items: flex-start; 
  justify-content: center; 
  padding: 2rem 1rem;
  overflow-y: auto;
}

.modal-content {
  background: #0a0a0a; 
  width: 100%; 
  max-width: 450px;
  /* max-height: 90vh;  */
  overflow-y: auto;
  border-radius: 8px; 
  border: 1px solid rgba(197, 160, 89, 0.3);
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
  margin-top: auto;
  margin-bottom: auto;
}

.modal-header {
  padding: 1.5rem 2rem; border-bottom: 1px solid rgba(255,255,255,0.05);
  display: flex; justify-content: space-between; align-items: center;
}

.close-btn { 
  color: #555; background: none; border: none; 
  font-size: 1.5rem; cursor: pointer; transition: 0.3s; 
}
.close-btn:hover { color: #ff4d4d; }

.modal-body { padding: 2rem; display: flex; flex-direction: column; gap: 1.2rem; }

/* Modal Form Elements */
.upload-zone {
  height: 140px; background: #050505; border: 2px dashed rgba(197, 160, 89, 0.2);
  border-radius: 16px; display: flex; align-items: center; justify-content: center;
  cursor: pointer; overflow: hidden; transition: 0.3s;
}
.upload-zone:hover { border-color: #c5a059; background: rgba(197, 160, 89, 0.05); }
.upload-preview { width: 100%; height: 100%; object-fit: cover; }

.form-group label { 
  font-size: 9px; text-transform: uppercase; 
  color: #c5a059; font-weight: 800; letter-spacing: 1.5px; 
  margin-bottom: 5px; display: block;
}

.form-group input, .form-group select {
  background: #111; border: 1px solid rgba(255,255,255,0.1);
  padding: 0.75rem; border-radius: 10px; color: white;
  width: 100%; font-size: 0.85rem;
}

.submit-btn {
  margin-top: 1rem; background: #c5a059; color: black;
  padding: 1rem; border-radius: 12px; font-weight: 900;
  text-transform: uppercase; font-size: 0.75rem; border: none;
  cursor: pointer; transition: 0.3s;
}

.submit-btn:hover:not(:disabled) { background: white; transform: translateY(-3px); }

/* --- Animations --- */
@keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

/* --- Responsive Breakpoints --- */
@media (max-width: 1024px) {
  .destinations-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
  .page-header { flex-direction: column; align-items: flex-start; }
  .actions { width: 100%; }
  .search-pill { flex: 1; }
  .destinations-grid { grid-template-columns: 1fr; }
  .modal-content { border-radius: 0; height: 100%; max-height: 100vh; }
}

/* Delete Button Styling */
.location-card {
  position: relative; /* Ensure the card can hold absolute positioned icons */
}

.card-media .absolute {
  opacity: 0;
  transform: translateY(-5px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.location-card:hover .card-media .absolute {
  opacity: 1;
  transform: translateY(0);
}

/* Manage Button State */
.action-btn-main {
  flex: 1;
  background: rgba(197, 160, 89, 0.1);
  border: 1px solid rgba(197, 160, 89, 0.3);
  color: #c5a059;
  font-size: 10px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 10px;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.action-btn-main:hover {
  background: #c5a059;
  color: #000;
  box-shadow: 0 0 15px rgba(197, 160, 89, 0.4);
}

/* Range Slider Styling (Fuel/Capacity) */
.fuel-slider {
  appearance: none;
  -webkit-appearance: none;
  height: 4px;
  background: #1a1a1a;
  border-radius: 10px;
  accent-color: #c5a059;
  width: 100%;
  outline: none;
}

.fuel-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 15px;
  height: 15px;
  background: #c5a059;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 0 10px rgba(197, 160, 89, 0.5);
  transition: transform 0.2s ease;
}

.fuel-slider::-webkit-slider-thumb:hover {
  transform: scale(1.2);
}

/* Modal Enhancements */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: #0a0a0a;
  border: 1px solid rgba(197, 160, 89, 0.2);
  width: 100%;
  max-width: 450px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

/* Status Colors */
.status-badge.high-peak { background: #ef4444; color: white; }
.status-badge.restricted { background: #f59e0b; color: black; }
.status-badge.optimal { background: #10b981; color: white; }

/* Animation */
.animate-slide-up {
  animation: slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* --- New Content: Short Excerpt Textarea --- */
.modal-body textarea {
  width: 100%;
  background: #111;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  color: white;
  padding: 0.75rem;
  font-size: 0.85rem;
  font-family: inherit;
  resize: none;
  transition: 0.3s;
}

.modal-body textarea:focus {
  outline: none;
  border-color: #c5a059;
  background: rgba(197, 160, 89, 0.05);
}

/* --- New Content: Card Footer Price Display --- */
.card-footer .text-right {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 12px;
  border-left: 1px solid rgba(255, 255, 255, 0.05);
  min-width: 80px;
}

.card-footer .text-right span.block {
  color: #c5a059;
  font-size: 8px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 2px;
}

/* --- Select Input Override --- */
/* To ensure category dropdown matches your existing inputs */
.form-group select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%23c5a059'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M19 9l-7 7-7-7'%3E%3C/path%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 12px;
  padding-right: 40px;
}

.itinerary-builder-section {
  border-top: 1px solid rgba(197, 160, 89, 0.2);
  padding-top: 1.5rem;
  margin-top: 1.5rem;
}

/* Luxury Add Day Button */
.add-day-btn {
  background: rgba(197, 160, 89, 0.1);
  border: 1px solid #c5a059;
  color: #c5a059;
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 9px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  transition: 0.3s;
}

.add-day-btn:hover {
  background: #c5a059;
  color: black;
  box-shadow: 0 0 15px rgba(197, 160, 89, 0.3);
}

/* Individual Day Card in the Form */
.itinerary-step-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
  padding: 1.25rem;
  border-radius: 12px;
  margin-bottom: 1rem;
  position: relative;
  transition: border-color 0.3s ease;
}

.itinerary-step-card:hover {
  border-color: rgba(197, 160, 89, 0.3);
}

/* The "Day X" Badge inside the card */
.day-label {
  background: #c5a059;
  color: black;
  font-size: 9px;
  font-weight: 900;
  padding: 3px 8px;
  border-radius: 4px;
  text-transform: uppercase;
}

/* Scroll Area for Itinerary */
.itinerary-list {
  max-height: 300px;
  overflow-y: auto;
  padding-right: 8px;
  margin-top: 10px;
}

/* Custom Scrollbar for Itinerary List */
.itinerary-list::-webkit-scrollbar {
  width: 4px;
}

.itinerary-list::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.02);
}

.itinerary-list::-webkit-scrollbar-thumb {
  background: #c5a059;
  border-radius: 10px;
}

/* Animation for adding new days */
.animate-slide-in {
  animation: slideIn 0.3s ease-out forwards;
}

@keyframes slideIn {
  from { opacity: 0; transform: translateX(-10px); }
  to { opacity: 1; transform: translateX(0); }
}

/* Ensure Textareas in Itinerary look consistent */
.itinerary-step-card textarea {
  min-height: 60px;
  margin-top: 8px;
}

.itinerary-step-card input {
  font-weight: 700;
  border-bottom: 1px solid rgba(197, 160, 89, 0.2);
}
</style> -->















<template>
  <div class="destinations-page">
    <header class="page-header">
      <div class="header-info">
        <h2 class="text-white font-bold text-3xl uppercase tracking-tighter">Global Hotspots</h2>
        <div class="flex items-center gap-3 mt-1">
          <span class="pulse-icon"></span>
          <p class="text-[#c5a059] text-[10px] font-black uppercase tracking-[0.3em]">Live Intelligence Feed</p>
        </div>
      </div>
      <div class="actions">
        <div class="search-pill">
          <i class="fa-solid fa-earth-americas text-[#c5a059]"></i>
          <input type="text" v-model="searchQuery" placeholder="Locate Destination..." />
        </div>
        
        <button @click="openAddModal" class="add-btn">
          <i class="fa-solid fa-plus"></i> New Hotspot
        </button>
      </div>
    </header>

    <div class="destinations-grid">
      <template v-if="isLoading">
        <div v-for="i in 6" :key="'skel-' + i" class="location-card skeleton-card">
          <div class="card-media skeleton shimmer"></div>
          <div class="card-body">
            <div class="flex justify-between items-start mb-4">
              <div class="w-2/3">
                <div class="skeleton skeleton-title shimmer mb-2"></div>
                <div class="skeleton skeleton-subtitle shimmer"></div>
              </div>
              <div class="w-1/4">
                <div class="skeleton skeleton-weather-top shimmer mb-1"></div>
                <div class="skeleton skeleton-weather-bot shimmer"></div>
              </div>
            </div>
            <div class="capacity-section mb-6">
              <div class="flex justify-between mb-2">
                <div class="skeleton skeleton-label shimmer"></div>
                <div class="skeleton skeleton-label shimmer w-8"></div>
              </div>
              <div class="skeleton skeleton-progress shimmer"></div>
            </div>
            <div class="card-footer">
              <div class="skeleton skeleton-btn shimmer"></div>
              <div class="text-right w-1/4">
                <div class="skeleton skeleton-label shimmer mb-1"></div>
                <div class="skeleton skeleton-price shimmer"></div>
              </div>
            </div>
          </div>
        </div>
      </template>

      <template v-else>
        <div v-for="loc in filteredDestinations" :key="loc.id || loc._id" class="location-card">
          <div class="card-media">
            <img :src="loc.image" :alt="loc.name" class="main-img" />
            <div class="overlay-gradient"></div>
            
            <button @click="deleteHotspot(loc.id || loc._id)" class="absolute top-3 right-3 z-10 text-red-500/50 hover:text-red-500 transition-colors bg-black/40 p-2 rounded-full backdrop-blur-md">
              <i class="fa-solid fa-trash-can text-xs"></i>
            </button>

            <div class="occupancy-tag font-bold">
              <i class="fa-solid fa-user-group text-[10px]"></i> {{ loc.activeVips || 0 }} VIPs
            </div>
            <div class="status-badge" :class="loc.status?.toLowerCase().replace(' ', '-')">
              {{ loc.status }}
            </div>
          </div>

          <div class="card-body">
            <div class="flex justify-between items-start mb-4">
              <div>
                <h3 class="text-white font-bold text-xl tracking-tight">{{ loc.name }}</h3>
                <p class="text-[#c5a059] text-[10px] font-black uppercase tracking-widest">{{ loc.region }} • {{ loc.category }}</p>
              </div>
              <div class="weather-info text-right">
                <span class="text-white font-bold block">{{ loc.temp }}°C</span>
                <span class="text-slate-500 text-[9px] font-bold uppercase">{{ loc.weather }}</span>
              </div>
            </div>

            <div class="capacity-section mb-6">
              <div class="flex justify-between text-[10px] font-bold uppercase mb-2">
                <span class="text-slate-400">Resource Capacity</span>
                <span class="text-white">{{ loc.capacity }}%</span>
              </div>
              <div class="progress-bg">
                <div class="progress-fill" :style="{ width: loc.capacity + '%' }" :class="getCapacityClass(loc.capacity)"></div>
              </div>
            </div>

            <div class="card-footer">
              <button @click="editHotspot(loc)" class="action-btn-main">Modify Protocol</button>
              <div class="text-right">
                <span class="block text-[8px] text-slate-500 uppercase font-black">Base Price</span>
                <span class="text-white font-bold text-sm">₹{{ loc.price }}</span>
              </div>
            </div>
          </div>
        </div>
      </template>
    </div>

    <div v-if="showModal" class="modal-overlay" @click.self="closeModal">
      <div class="modal-content animate-slide-up">
        <div class="modal-header">
          <div>
            <h3 class="text-white font-bold text-lg uppercase tracking-wider">
              {{ isEditing ? 'Modify Hotspot' : 'Deploy Hotspot' }}
            </h3>
            <p class="text-[#c5a059] text-[9px] font-bold uppercase tracking-[0.2em]">Intelligence Network Sync</p>
          </div>
          <button @click="closeModal" class="close-btn">&times;</button>
        </div>

        <form @submit.prevent="submitDestination" class="modal-body custom-scrollbar">
          <div class="upload-zone" :class="{ 'has-preview': previewUrl }" @click="$refs.fileInput.click()">
            <input type="file" ref="fileInput" class="hidden" accept="image/*" @change="handleFileChange" />
            <div v-if="!previewUrl" class="upload-placeholder text-center">
              <i class="fa-solid fa-map-location-dot text-2xl text-[#c5a059] mb-2"></i>
              <p class="text-[10px] font-bold uppercase tracking-widest text-slate-400">Upload Visual Asset</p>
            </div>
            <img v-else :src="previewUrl" class="upload-preview" />
          </div>

          <div class="form-group mt-4">
            <label>Location Name</label>
            <input v-model="newDest.name" type="text" placeholder="e.g. Udaipur Palace" required />
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="form-group">
              <label>Region/Country</label>
              <input v-model="newDest.region" type="text" placeholder="e.g. Rajasthan" required />
            </div>
            <div class="form-group">
              <label>Category</label>
              <select v-model="newDest.category">
                <option value="Beach">Beach</option>
                <option value="Mountain">Mountain</option>
                <option value="City">City</option>
                <option value="Cultural">Cultural</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="form-group">
              <label>Starting Price (₹)</label>
              <input v-model.number="newDest.price" type="number" required />
            </div>
            <div class="form-group">
              <label>Live Status</label>
              <select v-model="newDest.status">
                <option value="Optimal">Optimal</option>
                <option value="High Peak">High Peak</option>
                <option value="Restricted">Restricted</option>
              </select>
            </div>
          </div>

          <div class="itinerary-builder-section border-t border-[#c5a059]/20 pt-6 mt-6">
            <div class="flex justify-between items-center mb-4">
              <h4 class="text-[#c5a059] text-[10px] font-black uppercase tracking-widest">Journey Itinerary Builder</h4>
              <button type="button" @click="addItineraryDay" class="add-day-btn">
                <i class="fa-solid fa-plus text-[8px]"></i> Add Day
              </button>
            </div>

            <div class="itinerary-list">
              <div v-for="(step, index) in itinerarySteps" :key="index" class="itinerary-step-card animate-slide-in">
                <div class="flex justify-between items-center mb-3">
                  <span class="day-label">Day {{ index + 1 }}</span>
                  <button type="button" @click="removeItineraryDay(index)" class="text-red-500/50 hover:text-red-500">
                    <i class="fa-solid fa-trash-can text-[10px]"></i>
                  </button>
                </div>
                <input v-model="step.title" type="text" placeholder="Activity Title" class="mb-2" />
                <textarea v-model="step.activity" placeholder="Describe experience..." rows="2"></textarea>
              </div>
            </div>
          </div>

          <div class="form-group mt-6">
            <label>Short Excerpt</label>
            <input v-model="newDest.excerpt" type="text" placeholder="Catchy summary..." maxlength="150"/>
          </div>

          <div class="form-group mt-6">
            <label>Full Description</label>
            <textarea v-model="newDest.description" placeholder="Heritage story..." rows="4"></textarea>
          </div>

          <div class="grid grid-cols-2 gap-4">
            <div class="form-group">
              <label>Temp (°C)</label>
              <input v-model.number="newDest.temp" type="number" />
            </div>
            <div class="form-group">
              <label>Weather</label>
              <input v-model="newDest.weather" type="text" placeholder="Sunny/Rainy" />
            </div>
          </div>

          <div class="form-group">
            <label>Resource Capacity ({{ newDest.capacity }}%)</label>
            <input v-model.number="newDest.capacity" type="range" min="0" max="100" class="fuel-slider" />
          </div>

          <button type="submit" class="submit-btn" :disabled="isSyncing">
            <span v-if="!isSyncing">{{ isEditing ? 'Update Records' : 'Authorize Deployment' }}</span>
            <span v-else><i class="fa-solid fa-circle-notch fa-spin"></i> Syncing...</span>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';

// --- State Management ---
const destinations = ref([]);
const searchQuery = ref('');
const showModal = ref(false);
const isSyncing = ref(false);
const isEditing = ref(false);
const currentEditId = ref(null);
const isLoading = ref(true);

// --- Form & Media State ---
const previewUrl = ref(null);
const selectedFile = ref(null);
const fileInput = ref(null);

// --- New Itinerary State ---
const itinerarySteps = ref([]); 

const newDest = ref({
  name: '',
  region: '',
  category: 'Beach',
  price: 0,
  excerpt: '',
  description: '', // Full story
  status: 'Optimal',
  temp: 25,
  weather: 'Clear',
  capacity: 50,
  activeVips: 0
});

// --- Fetch Logic ---
const fetchDestinations = async () => {
  isLoading.value = true;
  try {
    const response = await axios.get('https://travel-xxnc.onrender.com//api/admin/destinations');
    if (response.data.success) destinations.value = response.data.data;
  } catch (error) {
    console.error("Fetch Error:", error);
  } finally {
    setTimeout(() => { 
      isLoading.value = false; 
    }, 700); // Simulate loading
  }
};

// --- Itinerary Builder Functions ---
const addItineraryDay = () => {
  itinerarySteps.value.push({
    day_number: itinerarySteps.value.length + 1,
    title: '',
    activity: ''
  });
};

const removeItineraryDay = (index) => {
  itinerarySteps.value.splice(index, 1);
  // Normalize day numbers after deletion
  itinerarySteps.value.forEach((step, i) => {
    step.day_number = i + 1;
  });
};

// --- Modal Controls ---
const openAddModal = () => {
  isEditing.value = false;
  currentEditId.value = null;
  resetForm();
  showModal.value = true;
};

const editHotspot = async (loc) => {
  isEditing.value = true;
  currentEditId.value = loc.id;
  
  // Fill basic fields
  newDest.value = { ...loc };
  previewUrl.value = loc.image;

  // Fetch full details (including itinerary) for this ID
  try {
    const res = await axios.get(`https://travel-xxnc.onrender.com/api/destinations/${loc.id}/details`);
    if (res.data.success) {
      itinerarySteps.value = res.data.data.itinerary || [];
    }
  } catch (err) {
    console.error("Error loading itinerary for edit:", err);
  }
  
  showModal.value = true;
};

const closeModal = () => {
  showModal.value = false;
  resetForm();
};

const resetForm = () => {
  newDest.value = { 
    name: '', region: '', category: 'Beach', price: 0, 
    excerpt: '', description: '', status: 'Optimal', 
    temp: 25, weather: 'Clear', capacity: 50, activeVips: 0 
  };
  itinerarySteps.value = [];
  previewUrl.value = null; 
  selectedFile.value = null;
  if (fileInput.value) fileInput.value.value = "";
};

// --- File Handling ---
const handleFileChange = (e) => {
  const file = e.target.files[0];
  if (!file) return;
  selectedFile.value = file;
  previewUrl.value = URL.createObjectURL(file);
};

// --- Submit Logic (Hotspot + Itinerary) ---
const submitDestination = async () => {
  // Validation: If adding new, require image
  if (!isEditing.value && !selectedFile.value) return alert("Image required for deployment.");
  isSyncing.value = true;

  try {
    const formData = new FormData();
    // Append File if exists
    if (selectedFile.value) formData.append('image', selectedFile.value);
    // Append basic fields
    Object.keys(newDest.value).forEach(key => {
      formData.append(key, newDest.value[key]);
    });

    // Append Itinerary as JSON string
    formData.append('itinerary', JSON.stringify(itinerarySteps.value));

    const url = isEditing.value 
      ? `https://travel-xxnc.onrender.com/api/admin/destinations/${currentEditId.value}`
      : 'https://travel-xxnc.onrender.com/api/admin/destinations/add';
    
    const method = isEditing.value ? 'put' : 'post';
    const response = await axios[method](url, formData);

    if (response.data.success) {
      const updatedList = await axios.get('https://travel-xxnc.onrender.com/api/admin/destinations');
      destinations.value = updatedList.data.data;
      closeModal();
    }
  } catch (error) {
    console.error("Sync Error:", error);
    alert("Synchronization with Intelligence Network failed.");
  } finally {
    isSyncing.value = false;
  }
};

const deleteHotspot = async (id) => {
  if (!confirm("Decommission this hotspot from the global map?")) return;
  try {
    const res = await axios.delete(`https://travel-xxnc.onrender.com/api/admin/destinations/${id}`);
    if (res.data.success) {
      destinations.value = destinations.value.filter(d => d.id !== id);
    }
  } catch (error) {
    alert("Delete operation failed.");
  }
};

// --- Computed & Helpers ---
const filteredDestinations = computed(() => {
  return destinations.value.filter(d => 
    d.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
    d.region.toLowerCase().includes(searchQuery.value.toLowerCase())
  );
});

const getCapacityClass = (val) => val > 80 ? 'high' : val < 30 ? 'low' : 'med';

onMounted(fetchDestinations);
</script>





<style scoped>
/* --- Global Page & Layout --- */
.destinations-page { 
  animation: fadeIn 0.8s ease; 
  padding: 1rem; 
  max-width: 1400px; 
  margin: 0 auto;
  padding-bottom: 100px; 
}

/* --- Header Section --- */
.page-header { 
  display: flex; 
  justify-content: space-between; 
  align-items: center; 
  margin-bottom: 3rem; 
  gap: 1.5rem; 
  flex-wrap: wrap; 
}

.header-info { flex: 1; min-width: 250px; }

.pulse-icon { 
  width: 8px; height: 8px; 
  background: #c5a059; 
  border-radius: 50%; 
  box-shadow: 0 0 10px #c5a059; 
  animation: pulse 2s infinite; 
}

.actions { display: flex; align-items: center; gap: 1rem; flex-wrap: wrap; }

.search-pill { 
  background: #111; 
  border: 1px solid rgba(197, 160, 89, 0.2); 
  border-radius: 50px; 
  padding: 0.6rem 1.2rem; 
  display: flex; 
  align-items: center; 
  gap: 10px; 
  min-width: 280px; 
  transition: 0.3s;
}

.search-pill:focus-within { border-color: #c5a059; box-shadow: 0 0 15px rgba(197, 160, 89, 0.1); }
.search-pill input { background: transparent; border: none; color: white; outline: none; font-size: 0.8rem; font-weight: 600; width: 100%; }

.add-btn { 
  background: #c5a059; 
  color: black; 
  border: none; 
  padding: 0.8rem 1.5rem; 
  border-radius: 50px; 
  font-weight: 800; 
  font-size: 0.7rem; 
  text-transform: uppercase; 
  cursor: pointer; 
  transition: 0.3s cubic-bezier(0.23, 1, 0.32, 1);
  white-space: nowrap;
}

.add-btn:hover { background: white; transform: scale(1.05); }

/* --- Grid System --- */
.destinations-grid { 
  display: grid; 
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); 
  gap: 2rem; 
}

/* --- Destination Cards --- */
.location-card { 
  background: #0c0c0c; 
  border-radius: 20px; 
  overflow: hidden; 
  border: 1px solid rgba(255,255,255,0.05); 
  transition: 0.4s cubic-bezier(0.23, 1, 0.32, 1); 
  display: flex;
  flex-direction: column;
}

.location-card:hover { 
  transform: translateY(-8px); 
  border-color: rgba(197, 160, 89, 0.4); 
  box-shadow: 0 20px 40px rgba(0,0,0,0.6); 
}

.card-media { 
  height: 160px; /* Reduced for density */
  position: relative; 
  overflow: hidden; 
}

.main-img { width: 100%; height: 100%; object-fit: cover; transition: 0.8s; }
.location-card:hover .main-img { scale: 1.1; filter: brightness(0.6); }

.overlay-gradient { 
  position: absolute; 
  inset: 0; 
  background: linear-gradient(to bottom, transparent, rgba(12, 12, 12, 0.95)); 
}

/* Float Tags */
.occupancy-tag { 
  position: absolute; top: 15px; left: 15px; 
  background: rgba(0,0,0,0.7); 
  backdrop-filter: blur(10px); 
  color: white; padding: 5px 12px; 
  border-radius: 50px; font-size: 0.65rem; 
  border: 1px solid rgba(255,255,255,0.1); 
  z-index: 10;
}

.status-badge { 
  position: absolute; bottom: 15px; right: 15px; 
  font-size: 8px; font-weight: 900; 
  text-transform: uppercase; letter-spacing: 1px; 
  padding: 4px 10px; border-radius: 4px; 
  z-index: 10;
}

.status-badge.optimal { background: #00ff88; color: black; }
.status-badge.high { background: #ffd700; color: black; }
.status-badge.restricted { background: #ff4d4d; color: white; }

.card-body { padding: 1.25rem; flex-grow: 1; }

/* Progress Bar */
.capacity-section { margin-bottom: 1.25rem; }
.progress-bg { height: 4px; background: #1a1a1a; border-radius: 10px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 10px; transition: 1.2s ease-in-out; }
.progress-fill.low { background: #00d2ff; }
.progress-fill.med { background: #c5a059; }
.progress-fill.high { background: #ff4d4d; box-shadow: 0 0 10px rgba(255, 77, 77, 0.5); }

/* Footer Buttons */
.card-footer { display: flex; gap: 8px; }
.action-btn-main { 
  flex: 1; background: rgba(255,255,255,0.03); 
  border: 1px solid rgba(255,255,255,0.1); 
  color: white; padding: 10px; border-radius: 10px; 
  font-weight: 800; font-size: 0.7rem; 
  text-transform: uppercase; cursor: pointer; transition: 0.3s; 
}
.action-btn-main:hover { background: white; color: black; }

.action-btn-icon { 
  width: 40px; background: rgba(197, 160, 89, 0.1); 
  border: 1px solid rgba(197, 160, 89, 0.2); 
  color: #c5a059; border-radius: 10px; cursor: pointer; 
  transition: 0.3s;
}
.action-btn-icon:hover { background: #c5a059; color: black; }

/* --- Modal Styles --- */
.modal-overlay {
  position: fixed; 
  inset: 0; 
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(10px); 
  z-index: 1000;
  display: flex; 
  align-items: flex-start; 
  justify-content: center; 
  padding: 2rem 1rem;
  overflow-y: auto;
}

.modal-content {
  background: #0a0a0a; 
  width: 100%; 
  max-width: 450px;
  /* max-height: 90vh;  */
  overflow-y: auto;
  border-radius: 8px; 
  border: 1px solid rgba(197, 160, 89, 0.3);
  box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
  margin-top: auto;
  margin-bottom: auto;
}

.modal-header {
  padding: 1.5rem 2rem; border-bottom: 1px solid rgba(255,255,255,0.05);
  display: flex; justify-content: space-between; align-items: center;
}

.close-btn { 
  color: #555; background: none; border: none; 
  font-size: 1.5rem; cursor: pointer; transition: 0.3s; 
}
.close-btn:hover { color: #ff4d4d; }

.modal-body { padding: 2rem; display: flex; flex-direction: column; gap: 1.2rem; }

/* Modal Form Elements */
.upload-zone {
  height: 140px; background: #050505; border: 2px dashed rgba(197, 160, 89, 0.2);
  border-radius: 16px; display: flex; align-items: center; justify-content: center;
  cursor: pointer; overflow: hidden; transition: 0.3s;
}
.upload-zone:hover { border-color: #c5a059; background: rgba(197, 160, 89, 0.05); }
.upload-preview { width: 100%; height: 100%; object-fit: cover; }

.form-group label { 
  font-size: 9px; text-transform: uppercase; 
  color: #c5a059; font-weight: 800; letter-spacing: 1.5px; 
  margin-bottom: 5px; display: block;
}

.form-group input, .form-group select {
  background: #111; border: 1px solid rgba(255,255,255,0.1);
  padding: 0.75rem; border-radius: 10px; color: white;
  width: 100%; font-size: 0.85rem;
}

.submit-btn {
  margin-top: 1rem; background: #c5a059; color: black;
  padding: 1rem; border-radius: 12px; font-weight: 900;
  text-transform: uppercase; font-size: 0.75rem; border: none;
  cursor: pointer; transition: 0.3s;
}

.submit-btn:hover:not(:disabled) { background: white; transform: translateY(-3px); }

/* --- Animations --- */
@keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }

/* --- Responsive Breakpoints --- */
@media (max-width: 1024px) {
  .destinations-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 768px) {
  .page-header { flex-direction: column; align-items: flex-start; }
  .actions { width: 100%; }
  .search-pill { flex: 1; }
  .destinations-grid { grid-template-columns: 1fr; }
  .modal-content { border-radius: 0; height: 100%; max-height: 100vh; }
}

/* Delete Button Styling */
.location-card {
  position: relative; /* Ensure the card can hold absolute positioned icons */
}

.card-media .absolute {
  opacity: 0;
  transform: translateY(-5px);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.location-card:hover .card-media .absolute {
  opacity: 1;
  transform: translateY(0);
}

/* Manage Button State */
.action-btn-main {
  flex: 1;
  background: rgba(197, 160, 89, 0.1);
  border: 1px solid rgba(197, 160, 89, 0.3);
  color: #c5a059;
  font-size: 10px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: 10px;
  border-radius: 4px;
  transition: all 0.3s ease;
}

.action-btn-main:hover {
  background: #c5a059;
  color: #000;
  box-shadow: 0 0 15px rgba(197, 160, 89, 0.4);
}

/* Range Slider Styling (Fuel/Capacity) */
.fuel-slider {
  appearance: none;
  -webkit-appearance: none;
  height: 4px;
  background: #1a1a1a;
  border-radius: 10px;
  accent-color: #c5a059;
  width: 100%;
  outline: none;
}

.fuel-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 15px;
  height: 15px;
  background: #c5a059;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 0 10px rgba(197, 160, 89, 0.5);
  transition: transform 0.2s ease;
}

.fuel-slider::-webkit-slider-thumb:hover {
  transform: scale(1.2);
}

/* Modal Enhancements */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: #0a0a0a;
  border: 1px solid rgba(197, 160, 89, 0.2);
  width: 100%;
  max-width: 450px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

/* Status Colors */
.status-badge.high-peak { background: #ef4444; color: white; }
.status-badge.restricted { background: #f59e0b; color: black; }
.status-badge.optimal { background: #10b981; color: white; }

/* Animation */
.animate-slide-up {
  animation: slideUp 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* --- New Content: Short Excerpt Textarea --- */
.modal-body textarea {
  width: 100%;
  background: #111;
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  color: white;
  padding: 0.75rem;
  font-size: 0.85rem;
  font-family: inherit;
  resize: none;
  transition: 0.3s;
}

.modal-body textarea:focus {
  outline: none;
  border-color: #c5a059;
  background: rgba(197, 160, 89, 0.05);
}

/* --- New Content: Card Footer Price Display --- */
.card-footer .text-right {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding-left: 12px;
  border-left: 1px solid rgba(255, 255, 255, 0.05);
  min-width: 80px;
}

.card-footer .text-right span.block {
  color: #c5a059;
  font-size: 8px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 2px;
}

/* --- Select Input Override --- */
/* To ensure category dropdown matches your existing inputs */
.form-group select {
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 24 24' stroke='%23c5a059'%3E%3Cpath stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M19 9l-7 7-7-7'%3E%3C/path%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 12px;
  padding-right: 40px;
}

.itinerary-builder-section {
  border-top: 1px solid rgba(197, 160, 89, 0.2);
  padding-top: 1.5rem;
  margin-top: 1.5rem;
}

/* Luxury Add Day Button */
.add-day-btn {
  background: rgba(197, 160, 89, 0.1);
  border: 1px solid #c5a059;
  color: #c5a059;
  padding: 5px 12px;
  border-radius: 6px;
  font-size: 9px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  transition: 0.3s;
}

.add-day-btn:hover {
  background: #c5a059;
  color: black;
  box-shadow: 0 0 15px rgba(197, 160, 89, 0.3);
}

/* Individual Day Card in the Form */
.itinerary-step-card {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.05);
  padding: 1.25rem;
  border-radius: 12px;
  margin-bottom: 1rem;
  position: relative;
  transition: border-color 0.3s ease;
}

.itinerary-step-card:hover {
  border-color: rgba(197, 160, 89, 0.3);
}

/* The "Day X" Badge inside the card */
.day-label {
  background: #c5a059;
  color: black;
  font-size: 9px;
  font-weight: 900;
  padding: 3px 8px;
  border-radius: 4px;
  text-transform: uppercase;
}

/* Scroll Area for Itinerary */
.itinerary-list {
  max-height: 300px;
  overflow-y: auto;
  padding-right: 8px;
  margin-top: 10px;
}

/* Custom Scrollbar for Itinerary List */
.itinerary-list::-webkit-scrollbar {
  width: 4px;
}

.itinerary-list::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.02);
}

.itinerary-list::-webkit-scrollbar-thumb {
  background: #c5a059;
  border-radius: 10px;
}

/* Animation for adding new days */
.animate-slide-in {
  animation: slideIn 0.3s ease-out forwards;
}

@keyframes slideIn {
  from { opacity: 0; transform: translateX(-10px); }
  to { opacity: 1; transform: translateX(0); }
}

/* Ensure Textareas in Itinerary look consistent */
.itinerary-step-card textarea {
  min-height: 60px;
  margin-top: 8px;
}

.itinerary-step-card input {
  font-weight: 700;
  border-bottom: 1px solid rgba(197, 160, 89, 0.2);
}




/* --- Skeleton Base & Animation --- */
.skeleton {
  background: #111;
  background-image: linear-gradient(
    90deg, 
    rgba(255, 255, 255, 0) 0, 
    rgba(255, 255, 255, 0.05) 50%, 
    rgba(255, 255, 255, 0) 100%
  );
  background-size: 200% 100%;
  border-radius: 4px;
}

.shimmer {
  animation: placeholderShimmer 1.5s infinite linear;
}

@keyframes placeholderShimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

/* --- Destination Specific Skeleton Shapes --- */
.skeleton-card {
  pointer-events: none;
  border-color: rgba(255, 255, 255, 0.03) !important;
}

/* Image Area */
.card-media.skeleton {
  height: 160px;
  width: 100%;
  border-radius: 20px 20px 0 0;
}

/* Typography */
.skeleton-title { height: 24px; width: 85%; }
.skeleton-subtitle { height: 12px; width: 50%; }

/* Weather Info (Right Aligned) */
.skeleton-weather-top { height: 18px; width: 40px; margin-left: auto; }
.skeleton-weather-bot { height: 10px; width: 30px; margin-left: auto; }

/* Capacity Section */
.skeleton-label { height: 10px; width: 60px; }
.skeleton-progress { height: 4px; width: 100%; border-radius: 10px; }

/* Footer Area */
.skeleton-btn { height: 38px; border-radius: 10px; flex: 1; }
.skeleton-price { height: 20px; width: 60px; margin-left: auto; }
</style>
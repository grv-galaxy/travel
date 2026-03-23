<!-- <template>
  <div class="security-page">
    <header class="page-header animate-slide-down">
      <div class="header-content">
        <h2 class="text-white font-black text-3xl uppercase tracking-tighter">Access Control</h2>
        <div class="flex items-center gap-2 mt-1">
          <span class="secure-pulse"></span>
          <p class="text-[#c5a059] text-[10px] font-black uppercase tracking-[0.3em]">System Integrity: Optimal</p>
        </div>
      </div>
      <div class="header-actions">
        <button class="add-admin-btn" @click="showAddModal = true">
          <i class="fa-solid fa-user-shield"></i> Provision New Admin
        </button>
      </div>
    </header>

    <section class="admin-section mb-10">
      <h3 class="text-white font-bold text-sm uppercase tracking-widest mb-4 opacity-50">Authorized Personnel</h3>
      <div class="admin-grid">
        <div v-for="admin in admins" :key="admin.id" class="admin-card animate-stagger" :style="{'--delay': admin.id * 0.1 + 's'}">
          <div class="admin-info">
            <div class="avatar-box">
              <i class="fa-solid fa-user-tie text-xl text-[#c5a059]"></i>
            </div>
            <div>
              <span class="text-white font-bold block">{{ admin.name }}</span>
              <span class="text-slate-500 text-[10px] font-bold uppercase">{{ admin.role }}</span>
            </div>
          </div>
          <div class="admin-meta">
            <div class="meta-item">
              <span class="label">Last Login</span>
              <span class="text-white font-bold text-xs">{{ admin.lastLogin }}</span>
            </div>
          </div>
          <button class="delete-admin-btn" @click="deleteAdmin(admin.id)" v-if="admin.role !== 'Super Admin'">
            <i class="fa-solid fa-trash-can"></i>
          </button>
        </div>
      </div>
    </section>

    <section class="audit-section animate-fade-in">
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-white font-bold text-sm uppercase tracking-widest opacity-50">Live Audit Trail</h3>
        <div class="filter-box">
          <i class="fa-solid fa-filter text-[#c5a059]"></i>
          <input type="text" v-model="auditSearch" placeholder="Search by Action or Admin..." />
        </div>
      </div>

      <div class="audit-container shadow-premium">
        <table class="audit-table">
          <thead>
            <tr>
              <th class="text-white font-bold uppercase">Timestamp</th>
              <th class="text-white font-bold uppercase">Administrator</th>
              <th class="text-white font-bold uppercase">Action / Event</th>
              <th class="text-white font-bold uppercase">Impact Level</th>
              <th class="text-white font-bold uppercase text-right">Reference ID</th>
            </tr>
          </thead>
          <transition-group name="list" tag="tbody">
            <tr v-for="log in filteredLogs" :key="log.id" class="audit-row">
              <td><span class="text-slate-400 font-bold text-xs">{{ log.time }}</span></td>
              <td><span class="text-white font-bold">{{ log.admin }}</span></td>
              <td>
                <div class="action-cell">
                  <i :class="log.icon" class="text-[#c5a059]"></i>
                  <span class="text-slate-300 font-medium">{{ log.action }}</span>
                </div>
              </td>
              <td>
                <span class="impact-tag" :class="log.impact.toLowerCase()">{{ log.impact }}</span>
              </td>
              <td class="text-right">
                <code class="text-slate-500 text-xs">{{ log.ref }}</code>
              </td>
            </tr>
          </transition-group>
        </table>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const auditSearch = ref('');

// Admin Users State
const admins = ref([
  { id: 1, name: 'System Root', role: 'Super Admin', lastLogin: 'Active Now' },
  { id: 2, name: 'Vikram Singh', role: 'Regional Manager', lastLogin: '2h ago' },
  { id: 3, name: 'Sarah Connor', role: 'Security Lead', lastLogin: '5h ago' },
  { id: 4, name: 'Marcus Aurelius', role: 'Fleet Admin', lastLogin: 'Yesterday' },
]);

// Audit Logs State
const logs = ref([
  { id: 1, time: '2025-12-25 14:02', admin: 'Vikram Singh', action: 'Decrypted Passport: SON-992', impact: 'Critical', icon: 'fa-solid fa-unlock', ref: 'VAULT-991' },
  { id: 2, time: '2025-12-25 13:45', admin: 'System Root', action: 'Added New Fleet Asset: Rolls Royce', impact: 'Low', icon: 'fa-solid fa-plus', ref: 'FLEET-772' },
  { id: 3, time: '2025-12-25 12:10', admin: 'Sarah Connor', action: 'Updated Concierge Protocol', impact: 'Medium', icon: 'fa-solid fa-pen-fancy', ref: 'CONC-112' },
  { id: 4, time: '2025-12-25 09:30', admin: 'Marcus Aurelius', action: 'Deleted Expired VIP Record', impact: 'Medium', icon: 'fa-solid fa-user-minus', ref: 'VIP-440' },
]);

const filteredLogs = computed(() => {
  return logs.value.filter(log => 
    log.admin.toLowerCase().includes(auditSearch.value.toLowerCase()) || 
    log.action.toLowerCase().includes(auditSearch.value.toLowerCase())
  );
});

const deleteAdmin = (id) => {
  if (confirm("Revoke all access for this Administrator? This action is logged.")) {
    admins.value = admins.value.filter(a => a.id !== id);
    // Push to log
    logs.value.unshift({
      id: Date.now(),
      time: 'Just Now',
      admin: 'System Root',
      action: 'Revoked Admin Access',
      impact: 'Critical',
      icon: 'fa-solid fa-user-slash',
      ref: `AUTH-${id}`
    });
  }
};
</script>

<style scoped>
.security-page { animation: fadeIn 0.8s ease; padding-bottom: 50px; }

/* Header */
.page-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 3rem; }
.secure-pulse { width: 8px; height: 8px; background: #00ff88; border-radius: 50%; box-shadow: 0 0 10px #00ff88; animation: pulse 2s infinite; }

.add-admin-btn { background: #c5a059; color: black; border: none; padding: 12px 24px; border-radius: 8px; font-weight: 800; font-size: 11px; text-transform: uppercase; cursor: pointer; }

/* Admin Grid */
.admin-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; }
.admin-card { background: #0c0c0c; border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 1.5rem; position: relative; transition: 0.3s; }
.admin-card:hover { border-color: #c5a059; }

.admin-info { display: flex; align-items: center; gap: 12px; margin-bottom: 1.5rem; }
.avatar-box { width: 45px; height: 45px; background: #151515; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: 1px solid #222; }

.admin-meta { border-top: 1px solid rgba(255,255,255,0.03); }
.meta-item .label { color: #555; font-size: 9px; font-weight: 900; text-transform: uppercase; display: block; margin-bottom: 4px; }

.delete-admin-btn { position: absolute; top: 15px; right: 15px; background: transparent; border: none; color: #333; cursor: pointer; transition: 0.3s; }
.delete-admin-btn:hover { color: #ff4d4d; }

/* Audit Table */
.filter-box { background: #0c0c0c; border: 1px solid #222; border-radius: 50px; padding: 6px 15px; display: flex; align-items: center; gap: 10px; min-width: 300px; }
.filter-box input { background: transparent; border: none; color: white; font-size: 12px; outline: none; width: 100%; }

.audit-container { background: #0c0c0c; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05); overflow: hidden; }
.audit-table { width: 100%; border-collapse: collapse; }
.audit-table th { background: #111; padding: 1.2rem 1.5rem; text-align: left; font-size: 0.7rem; border-bottom: 1px solid #1a1a1a; }
.audit-table td { padding: 1.2rem 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.02); }

.action-cell { display: flex; align-items: center; gap: 10px; }

.impact-tag { font-size: 9px; font-weight: 900; text-transform: uppercase; padding: 3px 8px; border-radius: 4px; }
.impact-tag.critical { background: rgba(255, 77, 77, 0.1); color: #ff4d4d; border: 1px solid #ff4d4d; }
.impact-tag.medium { background: rgba(197, 160, 89, 0.1); color: #c5a059; }
.impact-tag.low { background: rgba(0, 210, 255, 0.1); color: #00d2ff; }

/* List Transitions */
.list-enter-active, .list-leave-active { transition: all 0.5s ease; }
.list-enter-from { opacity: 0; transform: translateY(-20px); }
.list-leave-to { opacity: 0; transform: scale(0.9); }

@keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

@media (max-width: 1024px) {
  .audit-table th:nth-child(4), .audit-table td:nth-child(4) { display: none; }
}
</style> -->

















<!-- <template>
  <div class="security-page">
    <header class="page-header animate-slide-down">
      <div class="header-content">
        <h2 class="text-white font-black text-3xl uppercase tracking-tighter">Access Control</h2>
        <div class="flex items-center gap-2 mt-1">
          <span class="secure-pulse"></span>
          <p class="text-[#c5a059] text-[10px] font-black uppercase tracking-[0.3em]">System Integrity: Optimal</p>
        </div>
      </div>
      <div class="header-actions">
        <button class="add-admin-btn" @click="showAddModal = true">
          <i class="fa-solid fa-user-shield"></i> Provision New Admin
        </button>
      </div>
    </header>

    <section class="admin-section mb-10">
      <h3 class="text-white font-bold text-sm uppercase tracking-widest mb-4 opacity-50">Authorized Personnel</h3>
      <div class="admin-grid">
        <div v-for="admin in admins" :key="admin.id" class="admin-card animate-stagger">
          <div class="admin-info">
            <div class="avatar-box">
              <i class="fa-solid fa-user-tie text-xl text-[#c5a059]"></i>
            </div>
            <div>
              <span class="text-white font-bold block">{{ admin.full_name }}</span>
              <span class="text-slate-500 text-[10px] font-bold uppercase">{{ admin.role }}</span>
            </div>
          </div>
          <div class="admin-meta">
            <div class="meta-item">
              <span class="label">Last Login</span>
              <span class="text-white font-bold text-xs">{{ admin.last_login || 'Never' }}</span>
            </div>
          </div>
          <button class="delete-admin-btn" @click="deleteAdmin(admin.id)" v-if="admin.role !== 'SuperAdmin'">
            <i class="fa-solid fa-trash-can"></i>
          </button>
        </div>
      </div>
    </section>

    <section class="audit-section animate-fade-in">
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-white font-bold text-sm uppercase tracking-widest opacity-50">Live Audit Trail</h3>
        <div class="filter-box">
          <i class="fa-solid fa-filter text-[#c5a059]"></i>
          <input type="text" v-model="auditSearch" placeholder="Search by Action or Admin..." />
        </div>
      </div>

      <div class="audit-container shadow-premium">
        <table class="audit-table">
          <thead>
            <tr>
              <th class="text-white font-bold uppercase">Timestamp</th>
              <th class="text-white font-bold uppercase">Administrator</th>
              <th class="text-white font-bold uppercase">Action / Event</th>
              <th class="text-white font-bold uppercase">Impact Level</th>
              <th class="text-white font-bold uppercase text-right">Reference ID</th>
            </tr>
          </thead>
          <transition-group name="list" tag="tbody">
            <tr v-for="log in filteredLogs" :key="log.id" class="audit-row">
              <td><span class="text-slate-400 font-bold text-xs">{{ log.time }}</span></td>
              <td><span class="text-white font-bold">{{ log.admin }}</span></td>
              <td>
                <div class="action-cell">
                  <i :class="log.icon" class="text-[#c5a059]"></i>
                  <span class="text-slate-300 font-medium">{{ log.action }}</span>
                </div>
              </td>
              <td>
                <span class="impact-tag" :class="log.impact.toLowerCase()">{{ log.impact }}</span>
              </td>
              <td class="text-right">
                <code class="text-slate-500 text-xs">{{ log.ref }}</code>
              </td>
            </tr>
          </transition-group>
        </table>
      </div>
    </section>

    <transition name="modal-fade">
      <div v-if="showAddModal" class="modal-overlay" @click.self="showAddModal = false">
        <div class="provision-modal animate-reveal">
          <div class="modal-header">
            <i class="fa-solid fa-shield-halved text-[#c5a059] text-2xl"></i>
            <div>
              <h3 class="text-white font-black uppercase tracking-widest">Provision Admin</h3>
              <p class="text-slate-500 text-[9px] font-bold uppercase tracking-tighter">Granting System Access Privileges</p>
            </div>
          </div>

          <form @submit.prevent="provisionAdmin" class="modal-form">
            <div class="input-group">
              <label>Full Name</label>
              <input type="text" v-model="newAdmin.full_name" placeholder="Ex: Vikram Singh" required />
            </div>

            <div class="input-group">
              <label>Secure Email</label>
              <input type="email" v-model="newAdmin.email" placeholder="admin@indoria.com" required />
            </div>

            <div class="input-group">
              <label>Temporary Password</label>
              <input type="password" v-model="newAdmin.password" placeholder="••••••••" required />
            </div>

            <div class="input-group">
              <label>Access Role</label>
              <select v-model="newAdmin.role" required>
                <option value="Support">Support</option>
                <option value="Manager">Manager</option>
                <option value="SuperAdmin">SuperAdmin</option>
              </select>
            </div>

            <div class="modal-actions">
              <button type="button" @click="showAddModal = false" class="cancel-btn">Abort</button>
              <button type="submit" class="confirm-btn" :disabled="isSubmitting">
                <span v-if="!isSubmitting">Authorize Access</span>
                <i v-else class="fas fa-circle-notch fa-spin"></i>
              </button>
            </div>
          </form>
        </div>
      </div>
    </transition>
  </div>
</template>


<script setup>
import { ref, computed, onMounted } from 'vue';

// --- CONFIGURATION ---
const API_BASE_URL = 'https://indoria-backend-805083888664.us-central1.run.app/api/admin';

// --- STATE MANAGEMENT ---
const showAddModal = ref(false);
const isSubmitting = ref(false);
const auditSearch = ref('');
const admins = ref([]);
const logs = ref([]);

// Form State for New Admin
const newAdmin = ref({
  full_name: '',
  email: '',
  password: '',
  role: 'Support'
});

// --- AUTHENTICATED USER DATA ---
const getCurrentAdmin = () => {
  const rawData = localStorage.getItem('user_data');
  try {
    return JSON.parse(rawData) || {};
  } catch (e) {
    return {};
  }
};

// --- API ACTIONS ---

// 1. Fetch all admins from backend
const fetchAdmins = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/admins`, {
      method: 'GET',
      headers: { 
        'Authorization': `Bearer ${localStorage.getItem('user_token')}` 
      }
    });
    
    if (!response.ok) throw new Error('Failed to fetch');
    
    // Corrected: native fetch needs .json()
    const data = await response.json();
    admins.value = data;
  } catch (error) {
    console.error("Connectivity Error:", error);
  }
};

// 2. Provision New Admin
const provisionAdmin = async () => {
  if (isSubmitting.value) return;
  isSubmitting.value = true;
  
  const currentAdmin = getCurrentAdmin();

  try {
    const response = await fetch(`${API_BASE_URL}/admins/provision`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('user_token')}`
      },
      body: JSON.stringify(newAdmin.value)
    });

    const result = await response.json();

    if (response.ok) {
      // Update local UI list
      admins.value.unshift(result);
      
      addAuditLog('Provisioned New Admin', 'Medium', 'fa-solid fa-user-plus', result.id);
      
      // UI Reset
      showAddModal.value = false;
      newAdmin.value = { full_name: '', email: '', password: '', role: 'Support' };
      alert("Administrator Access Granted.");
    } else {
      alert(result.message || "Authorization Denied");
    }
  } catch (error) {
    alert("Network Error: Could not reach Security Server");
  } finally {
    isSubmitting.value = false;
  }
};

// 3. Delete Admin (Revoke Access)
const deleteAdmin = async (id) => {
  if (!confirm("Permanently revoke administrative access for this user?")) return;

  try {
    const response = await fetch(`${API_BASE_URL}/admins/${id}`, { 
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${localStorage.getItem('user_token')}` }
    });

    if (response.ok) {
      admins.value = admins.value.filter(a => a.id !== id);
      addAuditLog('Revoked Admin Access', 'Critical', 'fa-solid fa-user-slash', `ID-${id.slice(0,5)}`);
    } else {
      const errorData = await response.json();
      alert(errorData.message || "Action Failed");
    }
  } catch (error) {
    console.error("Delete failed", error);
  }
};

// --- UTILS ---
const addAuditLog = (action, impact, icon, refId) => {
  const currentAdmin = getCurrentAdmin();
  logs.value.unshift({
    id: Date.now(),
    time: new Date().toLocaleString(),
    admin: currentAdmin.full_name || 'System',
    action: action,
    impact: impact,
    icon: icon,
    ref: refId
  });
};

const filteredLogs = computed(() => {
  return logs.value.filter(log => 
    log.admin.toLowerCase().includes(auditSearch.value.toLowerCase()) || 
    log.action.toLowerCase().includes(auditSearch.value.toLowerCase())
  );
});

onMounted(() => {
  fetchAdmins();
  addAuditLog('Security Protocol Initialized', 'Low', 'fa-solid fa-shield-check', 'SYS-INIT');
});
</script> -->

<style scoped>
.security-page { animation: fadeIn 0.8s ease; padding-bottom: 50px; }

/* Header */
.page-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 3rem; }
.secure-pulse { width: 8px; height: 8px; background: #00ff88; border-radius: 50%; box-shadow: 0 0 10px #00ff88; animation: pulse 2s infinite; }

.add-admin-btn { background: #c5a059; color: black; border: none; padding: 12px 24px; border-radius: 8px; font-weight: 800; font-size: 11px; text-transform: uppercase; cursor: pointer; }

/* Admin Grid */
.admin-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; }
.admin-card { background: #0c0c0c; border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 1.5rem; position: relative; transition: 0.3s; }
.admin-card:hover { border-color: #c5a059; }

.admin-info { display: flex; align-items: center; gap: 12px; margin-bottom: 1.5rem; }
.avatar-box { width: 45px; height: 45px; background: #151515; border-radius: 12px; display: flex; align-items: center; justify-content: center; border: 1px solid #222; }

.admin-meta { border-top: 1px solid rgba(255,255,255,0.03); }
.meta-item .label { color: #555; font-size: 9px; font-weight: 900; text-transform: uppercase; display: block; margin-bottom: 4px; }

.delete-admin-btn { position: absolute; top: 15px; right: 15px; background: transparent; border: none; color: #333; cursor: pointer; transition: 0.3s; }
.delete-admin-btn:hover { color: #ff4d4d; }

/* Audit Table */
.filter-box { background: #0c0c0c; border: 1px solid #222; border-radius: 50px; padding: 6px 15px; display: flex; align-items: center; gap: 10px; min-width: 300px; }
.filter-box input { background: transparent; border: none; color: white; font-size: 12px; outline: none; width: 100%; }

.audit-container { background: #0c0c0c; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05); overflow: hidden; }
.audit-table { width: 100%; border-collapse: collapse; }
.audit-table th { background: #111; padding: 1.2rem 1.5rem; text-align: left; font-size: 0.7rem; border-bottom: 1px solid #1a1a1a; }
.audit-table td { padding: 1.2rem 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.02); }

.action-cell { display: flex; align-items: center; gap: 10px; }

.impact-tag { font-size: 9px; font-weight: 900; text-transform: uppercase; padding: 3px 8px; border-radius: 4px; }
.impact-tag.critical { background: rgba(255, 77, 77, 0.1); color: #ff4d4d; border: 1px solid #ff4d4d; }
.impact-tag.medium { background: rgba(197, 160, 89, 0.1); color: #c5a059; }
.impact-tag.low { background: rgba(0, 210, 255, 0.1); color: #00d2ff; }

/* List Transitions */
.list-enter-active, .list-leave-active { transition: all 0.5s ease; }
.list-enter-from { opacity: 0; transform: translateY(-20px); }
.list-leave-to { opacity: 0; transform: scale(0.9); }

@keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

@media (max-width: 1024px) {
  .audit-table th:nth-child(4), .audit-table td:nth-child(4) { display: none; }
}






/* --- PROVISION MODAL STYLES --- */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  z-index: 2000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.provision-modal {
  background: #0a0a0a;
  width: 100%;
  max-width: 450px;
  border: 1px solid rgba(197, 160, 89, 0.3);
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

.modal-header {
  display: flex;
  align-items: center;
  gap: 15px;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.modal-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input-group label {
  color: #c5a059;
  font-size: 10px;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.1em;
}

.input-group input, 
.input-group select {
  background: #111;
  border: 1px solid #222;
  border-radius: 12px;
  padding: 12px 16px;
  color: white;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.input-group input:focus, 
.input-group select:focus {
  outline: none;
  border-color: #c5a059;
  box-shadow: 0 0 10px rgba(197, 160, 89, 0.1);
}

.modal-actions {
  display: flex;
  gap: 12px;
  margin-top: 1rem;
}

.cancel-btn {
  flex: 1;
  background: transparent;
  border: 1px solid #333;
  color: #777;
  padding: 14px;
  border-radius: 12px;
  font-weight: 800;
  font-size: 11px;
  text-transform: uppercase;
  cursor: pointer;
  transition: 0.3s;
}

.cancel-btn:hover {
  border-color: #555;
  color: white;
}

.confirm-btn {
  flex: 2;
  background: linear-gradient(135deg, #c5a059 0%, #a38241 100%);
  color: black;
  border: none;
  padding: 14px;
  border-radius: 12px;
  font-weight: 800;
  font-size: 11px;
  text-transform: uppercase;
  cursor: pointer;
  transition: 0.3s;
}

.confirm-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 20px rgba(197, 160, 89, 0.2);
}

.confirm-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Animations */
.modal-fade-enter-active, .modal-fade-leave-active { transition: opacity 0.3s ease; }
.modal-fade-enter-from, .modal-fade-leave-to { opacity: 0; }

.animate-reveal {
  animation: modalReveal 0.4s cubic-bezier(0.23, 1, 0.32, 1);
}

@keyframes modalReveal {
  from { opacity: 0; transform: translateY(20px) scale(0.95); }
  to { opacity: 1; transform: translateY(0) scale(1); }
}

/* Responsive Overrides */
@media (max-width: 480px) {
  .provision-modal {
    padding: 1.5rem;
    border-radius: 20px;
  }
  .modal-actions {
    flex-direction: column-reverse;
  }
}






.skeleton-container {
  position: relative;
  overflow: hidden !important;
}

.skeleton-bone {
  background: rgba(255, 255, 255, 0.05); /* Low-key Dark Mode bone */
  border-radius: 4px;
  position: relative;
}

.skeleton-shimmer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.05) 50%,
    rgba(255, 255, 255, 0) 100%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  pointer-events: none;
}

@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}


.admin-card.skeleton-container {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(197, 160, 89, 0.1);
} 


</style>






<template>
  <div class="security-page">
    <header class="page-header animate-slide-down">
      <div class="header-content">
        <h2 class="text-white font-black text-3xl uppercase tracking-tighter">Access Control</h2>
        <div class="flex items-center gap-2 mt-1">
          <span class="secure-pulse"></span>
          <p class="text-[#c5a059] text-[10px] font-black uppercase tracking-[0.3em]">System Integrity: Optimal</p>
        </div>
      </div>
      <div class="header-actions">
        <button class="add-admin-btn" @click="showAddModal = true">
          <i class="fa-solid fa-user-shield"></i> Provision New Admin
        </button>
      </div>
    </header>

    <section class="admin-section mb-10">
      <h3 class="text-white font-bold text-sm uppercase tracking-widest mb-4 opacity-50">Authorized Personnel</h3>
      <div class="admin-grid">
        <template v-if="isLoading">
          <div v-for="n in 3" :key="'skel-admin-' + n" class="admin-card skeleton-container">
            <div class="admin-info">
              <div class="avatar-box skeleton-bone w-12 h-12 rounded-lg"></div>
              <div class="flex-1">
                <div class="skeleton-bone h-4 w-3/4 mb-2"></div>
                <div class="skeleton-bone h-3 w-1/2"></div>
              </div>
            </div>
            <div class="admin-meta mt-4">
              <div class="skeleton-bone h-3 w-full"></div>
            </div>
            <div class="skeleton-shimmer"></div>
          </div>
        </template>

        <template v-else>
        <div v-for="admin in admins" :key="admin.id" class="admin-card animate-stagger">
          <div class="admin-info">
            <div class="avatar-box">
              <i class="fa-solid fa-user-tie text-xl text-[#c5a059]"></i>
            </div>
            <div>
              <span class="text-white font-bold block">{{ admin.full_name }}</span>
              <span class="text-slate-500 text-[10px] font-bold uppercase">{{ admin.role }}</span>
            </div>
          </div>
          <div class="admin-meta">
            <div class="meta-item">
              <span class="label">Last Login</span>
              <span class="text-white font-bold text-xs">{{ admin.last_login || 'Never' }}</span>
            </div>
          </div>
          <button class="delete-admin-btn" @click="deleteAdmin(admin.id)" v-if="admin.role !== 'SuperAdmin'">
            <i class="fa-solid fa-trash-can"></i>
          </button>
        </div>
        </template>
      </div>
    </section>

    <section class="audit-section animate-fade-in">
      <div class="flex justify-between items-center mb-4">
        <h3 class="text-white font-bold text-sm uppercase tracking-widest opacity-50">Live Audit Trail</h3>
        <div class="filter-box">
          <i class="fa-solid fa-filter text-[#c5a059]"></i>
          <input type="text" v-model="auditSearch" placeholder="Search by Action or Admin..." />
        </div>
      </div>

      <div class="audit-container shadow-premium">
        <table class="audit-table">
          <thead>
            <tr>
              <th class="text-white font-bold uppercase">Timestamp</th>
              <th class="text-white font-bold uppercase">Administrator</th>
              <th class="text-white font-bold uppercase">Action / Event</th>
              <th class="text-white font-bold uppercase">Impact Level</th>
              <th class="text-white font-bold uppercase text-right">Reference ID</th>
            </tr>
          </thead>
          <tbody v-if="isLoading">
            <tr v-for="n in 5" :key="'skel-log-' + n" class="audit-row skeleton-shimmer-row">
              <td><div class="skeleton-bone h-3 w-20"></div></td>
              <td><div class="skeleton-bone h-3 w-24"></div></td>
              <td><div class="skeleton-bone h-3 w-40"></div></td>
              <td><div class="skeleton-bone h-5 w-16 rounded-full"></div></td>
              <td class="text-right">
                <div class="skeleton-bone h-3 w-12 ml-auto"></div>
              </td>
              </tr>
          </tbody>
          <transition-group name="list" tag="tbody">
            <tr v-for="log in filteredLogs" :key="log.id" class="audit-row">
              <td><span class="text-slate-400 font-bold text-xs">{{ log.time }}</span></td>
              <td><span class="text-white font-bold">{{ log.admin }}</span></td>
              <td>
                <div class="action-cell">
                  <i :class="log.icon" class="text-[#c5a059]"></i>
                  <span class="text-slate-300 font-medium">{{ log.action }}</span>
                </div>
              </td>
              <td>
                <span class="impact-tag" :class="log.impact.toLowerCase()">{{ log.impact }}</span>
              </td>
              <td class="text-right">
                <code class="text-slate-500 text-xs">{{ log.ref }}</code>
              </td>
            </tr>
          </transition-group>
        </table>
      </div>
    </section>

    <transition name="modal-fade">
      <div v-if="showAddModal" class="modal-overlay" @click.self="showAddModal = false">
        <div class="provision-modal animate-reveal">
          <div class="modal-header">
            <i class="fa-solid fa-shield-halved text-[#c5a059] text-2xl"></i>
            <div>
              <h3 class="text-white font-black uppercase tracking-widest">Provision Admin</h3>
              <p class="text-slate-500 text-[9px] font-bold uppercase tracking-tighter">Granting System Access Privileges</p>
            </div>
          </div>

          <form @submit.prevent="provisionAdmin" class="modal-form">
            <div class="input-group">
              <label>Full Name</label>
              <input type="text" v-model="newAdmin.full_name" placeholder="Ex: Vikram Singh" required />
            </div>

            <div class="input-group">
              <label>Secure Email</label>
              <input type="email" v-model="newAdmin.email" placeholder="admin@indoria.com" required />
            </div>

            <div class="input-group">
              <label>Temporary Password</label>
              <input type="password" v-model="newAdmin.password" placeholder="••••••••" required />
            </div>

            <div class="input-group">
              <label>Access Role</label>
              <select v-model="newAdmin.role" required>
                <option value="Support">Support</option>
                <option value="Manager">Manager</option>
                <option value="SuperAdmin">SuperAdmin</option>
              </select>
            </div>

            <div class="modal-actions">
              <button type="button" @click="showAddModal = false" class="cancel-btn">Abort</button>
              <button type="submit" class="confirm-btn" :disabled="isSubmitting">
                <span v-if="!isSubmitting">Authorize Access</span>
                <i v-else class="fas fa-circle-notch fa-spin"></i>
              </button>
            </div>
          </form>
        </div>
      </div>
    </transition>
  </div>
</template>



<script setup>
import { ref, computed, onMounted, inject } from 'vue';
import axios from 'axios';

// --- GLOBAL INJECTIONS ---
const notify = inject('notify');
const setGlobalLoading = inject('setGlobalLoading');

// --- CONFIGURATION ---
const API_BASE_URL = 'https://indoria-backend-805083888664.us-central1.run.app/api/admin';

// --- STATE MANAGEMENT ---
const isLoading = ref(true); // Controls skeletons
const showAddModal = ref(false);
const isSubmitting = ref(false);
const auditSearch = ref('');
const admins = ref([]);
const logs = ref([]);

// Confirmation Modal State
const showRevokeModal = ref(false);
const adminToRevoke = ref(null);

// Form State for New Admin
const newAdmin = ref({
  full_name: '',
  email: '',
  password: '',
  role: 'Support'
});

// --- AUTH HELPERS ---
const getAuthHeader = () => ({
  headers: { 'Authorization': `Bearer ${localStorage.getItem('user_token')}` }
});

const getCurrentAdmin = () => {
  try {
    return JSON.parse(localStorage.getItem('user_data')) || {};
  } catch (e) {
    return {};
  }
};

// --- API ACTIONS ---

// 1. Fetch Admins with Skeleton Support
const fetchAdmins = async () => {
  isLoading.value = true;
  try {
    const response = await axios.get(`${API_BASE_URL}/admins`, getAuthHeader());
    admins.value = Array.isArray(response.data) ? response.data : [];
  } catch (error) {
    notify("Security Feed Interrupted: Could not load personnel.", "error");
    console.error("Connectivity Error:", error);
  } finally {
    // Artificial delay to appreciate the luxury skeleton effect
    setTimeout(() => { isLoading.value = false; }, 800);
  }
};

// 2. Provision New Admin
const provisionAdmin = async () => {
  if (isSubmitting.value) return;
  isSubmitting.value = true;

  try {
    const response = await axios.post(`${API_BASE_URL}/admins/provision`, newAdmin.value, getAuthHeader());

    if (response.data) {
      admins.value.unshift(response.data);
      addAuditLog('Provisioned New Admin', 'Medium', 'fa-solid fa-user-plus', response.data.id);
      
      showAddModal.value = false;
      newAdmin.value = { full_name: '', email: '', password: '', role: 'Support' };
      notify("Administrator Access Granted.", "success");
    }
  } catch (error) {
    const msg = error.response?.data?.message || "Authorization Denied by Security Server";
    notify(msg, "error");
  } finally {
    isSubmitting.value = true;
    // Small delay before enabling button again
    setTimeout(() => { isSubmitting.value = false; }, 500);
  }
};

// 3. Custom Revoke Confirmation Logic
const triggerRevoke = (admin) => {
  adminToRevoke.value = admin;
  showRevokeModal.value = true;
};

const confirmRevoke = async () => {
  const admin = adminToRevoke.value;
  if (!admin) return;

  showRevokeModal.value = false;
  setGlobalLoading(true);

  try {
    await axios.delete(`${API_BASE_URL}/admins/${admin.id}`, getAuthHeader());
    admins.value = admins.value.filter(a => a.id !== admin.id);
    addAuditLog('Revoked Admin Access', 'Critical', 'fa-solid fa-user-slash', `ID-${admin.id.slice(0,5)}`);
    notify(`${admin.full_name}'s access has been purged.`, "success");
  } catch (error) {
    notify("Revocation failed. System integrity protected.", "error");
  } finally {
    setGlobalLoading(false);
    adminToRevoke.value = null;
  }
};

// --- AUDIT SYSTEM ---
const addAuditLog = (action, impact, icon, refId) => {
  const currentAdmin = getCurrentAdmin();
  logs.value.unshift({
    id: Date.now(),
    time: new Date().toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
    admin: currentAdmin.full_name || 'System',
    action: action,
    impact: impact,
    icon: icon,
    ref: refId
  });
};

const filteredLogs = computed(() => {
  if (!auditSearch.value) return logs.value;
  const s = auditSearch.value.toLowerCase();
  return logs.value.filter(log => 
    log.admin.toLowerCase().includes(s) || 
    log.action.toLowerCase().includes(s) ||
    log.ref.toString().toLowerCase().includes(s)
  );
});

// --- INITIALIZATION ---
onMounted(() => {
  fetchAdmins();
  addAuditLog('Security Protocol Initialized', 'Low', 'fa-solid fa-shield-check', 'SYS-INIT');
});
</script>
<template>
  <div class="vault-page">
    <header class="page-header">
      <div class="security-meta">
        <h2 class="text-white font-black text-3xl uppercase tracking-tighter">Secure Vault</h2>
        <div class="encryption-status">
          <i class="fa-solid fa-shield-check text-[#00ff88]"></i>
          <span class="text-[#00ff88] text-[10px] font-bold uppercase tracking-[0.2em]">AES-256 Bit Encryption Active</span>
        </div>
      </div>
      <div class="actions">
        <div class="search-vault">
          <i class="fa-solid fa-fingerprint text-[#c5a059]"></i>
          <input type="text" v-model="searchQuery" placeholder="Search Encrypted Files..." />
        </div>
        <button class="upload-btn"><i class="fa-solid fa-cloud-arrow-up"></i> Secure Upload</button>
      </div>
    </header>

    <div class="vault-stats-grid">
      <div class="stat-card">
        <span class="label">Total Assets</span>
        <span class="value text-white font-bold">4,821</span>
      </div>
      <div class="stat-card">
        <span class="label">Last Breach Attempt</span>
        <span class="value text-[#ff4d4d] font-bold">Blocked</span>
      </div>
      <div class="stat-card">
        <span class="label">Storage Used</span>
        <div class="storage-info">
          <span class="text-white font-bold">1.2 TB</span>
          <div class="mini-progress"><div class="fill" style="width: 65%"></div></div>
        </div>
      </div>
    </div>

    <div class="vault-table-container">
      <table class="vault-table">
        <thead>
          <tr>
            <th class="text-white font-bold uppercase">Document Name</th>
            <th class="text-white font-bold uppercase">Owner</th>
            <th class="text-white font-bold uppercase">Classification</th>
            <th class="text-white font-bold uppercase">Expiry</th>
            <th class="text-white font-bold uppercase text-right">Access</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="file in filteredFiles" :key="file.id" class="vault-row">
            <td>
              <div class="file-info">
                <i :class="file.icon" class="text-[#c5a059] text-xl"></i>
                <div>
                  <span class="text-white font-bold block">{{ file.name }}</span>
                  <span class="text-slate-500 text-[10px] uppercase font-bold">{{ file.size }} • {{ file.id }}</span>
                </div>
              </div>
            </td>
            <td>
              <span class="text-slate-300 font-medium">{{ file.owner }}</span>
            </td>
            <td>
              <span class="class-badge" :class="file.class.toLowerCase()">{{ file.class }}</span>
            </td>
            <td>
              <span class="text-white font-bold" :class="{ 'text-red-500': file.isExpiring }">{{ file.expiry }}</span>
            </td>
            <td class="text-right">
              <div class="access-actions">
                <button class="view-btn"><i class="fa-solid fa-eye"></i></button>
                <button class="lock-btn"><i class="fa-solid fa-key"></i></button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="mobile-vault-grid">
      <div v-for="file in filteredFiles" :key="'m-'+file.id" class="m-vault-card">
        <div class="flex justify-between items-start">
          <i :class="file.icon" class="text-[#c5a059] text-2xl"></i>
          <span class="class-badge" :class="file.class.toLowerCase()">{{ file.class }}</span>
        </div>
        <h4 class="text-white font-bold mt-3">{{ file.name }}</h4>
        <p class="text-slate-500 text-xs">{{ file.owner }}</p>
        <div class="mt-4 flex gap-2">
          <button class="mobile-action-btn flex-1">Decrypt</button>
          <button class="mobile-action-btn"><i class="fa-solid fa-share-nodes"></i></button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const searchQuery = ref('');

const files = ref([
  { id: 'DOC-8821', name: 'Global NDA - Singh.pdf', owner: 'Maharaja Vikram', class: 'Top-Secret', size: '2.4MB', expiry: 'Jan 2026', icon: 'fa-solid fa-file-shield', isExpiring: false },
  { id: 'IMG-0092', name: 'Passport_Copy_Main.enc', owner: 'Sonia Malhotra', class: 'Private', size: '1.1MB', expiry: 'Oct 2025', icon: 'fa-solid fa-passport', isExpiring: true },
  { id: 'KEY-7712', name: 'Private_Jet_Manifest.xlsx', owner: 'Fleet Command', class: 'Internal', size: '840KB', expiry: 'N/A', icon: 'fa-solid fa-file-csv', isExpiring: false },
  { id: 'DOC-1102', name: 'Property_Deed_Zurich.pdf', owner: 'Arjan Iyer', class: 'Top-Secret', size: '12MB', expiry: 'Infinite', icon: 'fa-solid fa-file-contract', isExpiring: false },
]);

const filteredFiles = computed(() => {
  return files.value.filter(f => f.name.toLowerCase().includes(searchQuery.value.toLowerCase()) || f.owner.toLowerCase().includes(searchQuery.value.toLowerCase()));
});
</script>

<style scoped>
.vault-page { animation: fadeIn 0.6s ease; padding-bottom: 50px; }

/* Header */
.page-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 3rem; flex-wrap: wrap; gap: 1.5rem; }
.encryption-status { display: flex; align-items: center; gap: 8px; margin-top: 8px; }

.search-vault { background: #0c0c0c; border: 1px solid #222; border-radius: 12px; padding: 0.8rem 1.2rem; display: flex; align-items: center; gap: 12px; min-width: 320px; }
.search-vault input { background: transparent; border: none; color: white; outline: none; width: 100%; font-size: 0.9rem; }
.upload-btn { background: #c5a059; color: black; border: none; padding: 0.8rem 1.8rem; border-radius: 10px; font-weight: 800; text-transform: uppercase; font-size: 0.75rem; cursor: pointer; }

/* Stats Bar */
.vault-stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-bottom: 2.5rem; }
.stat-card { background: #0c0c0c; padding: 1.5rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.03); }
.stat-card .label { color: #555; font-size: 10px; font-weight: 900; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 8px; }
.stat-card .value { font-size: 1.5rem; }
.mini-progress { height: 4px; background: #222; border-radius: 10px; margin-top: 10px; width: 100px; }
.mini-progress .fill { height: 100%; background: #c5a059; box-shadow: 0 0 10px #c5a059; }

/* Table */
.vault-table-container { background: #0c0c0c; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05); overflow: hidden; }
.vault-table { width: 100%; border-collapse: collapse; }
.vault-table th { background: #111; padding: 1.2rem 1.5rem; text-align: left; font-size: 0.65rem; letter-spacing: 1px; border-bottom: 1px solid #1a1a1a; }
.vault-table td { padding: 1.2rem 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.02); }

.file-info { display: flex; align-items: center; gap: 15px; }

.class-badge { padding: 4px 10px; border-radius: 4px; font-size: 9px; font-weight: 900; text-transform: uppercase; letter-spacing: 0.5px; }
.class-badge.top-secret { background: rgba(255, 77, 77, 0.1); color: #ff4d4d; border: 1px solid rgba(255, 77, 77, 0.2); }
.class-badge.private { background: rgba(197, 160, 89, 0.1); color: #c5a059; border: 1px solid rgba(197, 160, 89, 0.2); }
.class-badge.internal { background: rgba(0, 210, 255, 0.1); color: #00d2ff; }

.access-actions { display: flex; gap: 8px; justify-content: flex-end; }
.access-actions button { background: #1a1a1a; border: 1px solid #333; color: white; width: 35px; height: 35px; border-radius: 8px; cursor: pointer; transition: 0.3s; }
.access-actions button:hover { background: #c5a059; color: black; border-color: #c5a059; }

/* Mobile View */
.mobile-vault-grid { display: none; }

@media (max-width: 1024px) {
  .vault-table th:nth-child(2), .vault-table td:nth-child(2) { display: none; }
}

@media (max-width: 768px) {
  .vault-stats-grid { grid-template-columns: 1fr; }
  .vault-table-container { display: none; }
  .mobile-vault-grid { display: grid; gap: 1rem; }
  .m-vault-card { background: #0c0c0c; padding: 1.5rem; border-radius: 16px; border: 1px solid #222; }
  .mobile-action-btn { background: #1a1a1a; border: 1px solid #333; color: white; padding: 10px; border-radius: 8px; font-weight: 800; font-size: 11px; text-transform: uppercase; }
}

@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style>
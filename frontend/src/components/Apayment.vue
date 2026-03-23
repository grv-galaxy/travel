<template>
  <div class="payments-page">
    <header class="page-header animate-slide-down">
      <div class="header-content">
        <h2 class="text-white font-black text-3xl uppercase tracking-tighter">Financial Ledger</h2>
        <div class="flex items-center gap-2 mt-1">
          <span class="live-indicator"></span>
          <p class="text-[#c5a059] text-[10px] font-black uppercase tracking-[0.3em]">Global Transaction Stream</p>
        </div>
      </div>
      <div class="header-actions">
        <button class="export-btn font-bold"><i class="fa-solid fa-file-invoice-dollar"></i> Export Report</button>
      </div>
    </header>

    <div class="revenue-grid">
      <div class="rev-card animate-stagger" style="--delay: 0.1s">
        <span class="label">Net Revenue (MTD)</span>
        <div class="flex items-baseline gap-2">
          <span class="text-white font-bold text-3xl">₹48.2M</span>
          <span class="text-[#00ff88] text-xs font-bold">+12.4%</span>
        </div>
        <div class="mini-chart-bar"><div class="fill" style="width: 70%"></div></div>
      </div>
      <div class="rev-card animate-stagger" style="--delay: 0.2s">
        <span class="label">Pending Settlements</span>
        <span class="text-white font-bold text-3xl">₹2.1M</span>
        <p class="text-slate-500 text-[10px] font-bold mt-2 uppercase">Verified via Blockchain</p>
      </div>
      <div class="rev-card animate-stagger" style="--delay: 0.3s">
        <span class="label">Avg. VIP Spend</span>
        <span class="text-[#c5a059] font-bold text-3xl">₹8.4L</span>
        <div class="mini-chart-bar"><div class="fill gold" style="width: 45%"></div></div>
      </div>
    </div>

    <div class="table-controls animate-fade-in">
      <div class="search-wrap">
        <i class="fa-solid fa-magnifying-glass-dollar text-[#c5a059]"></i>
        <input type="text" v-model="searchQuery" placeholder="Filter by VIP, ID, or Method..." />
      </div>
      <div class="filter-pills">
        <button v-for="f in ['All', 'Completed', 'Processing']" :key="f" class="pill" :class="{active: filterStatus === f}" @click="filterStatus = f">
          {{ f }}
        </button>
      </div>
    </div>

    <div class="ledger-container shadow-premium animate-fade-in">
      <table class="ledger-table">
        <thead>
          <tr>
            <th class="text-white font-bold uppercase">Transaction ID</th>
            <th class="text-white font-bold uppercase">VIP Client</th>
            <th class="text-white font-bold uppercase">Service</th>
            <th class="text-white font-bold uppercase text-right">Amount</th>
            <th class="text-white font-bold uppercase text-center">Status</th>
          </tr>
        </thead>
        <transition-group name="list" tag="tbody">
          <tr v-for="tx in filteredTransactions" :key="tx.id" class="ledger-row">
            <td><code class="text-[#c5a059] font-bold">{{ tx.id }}</code></td>
            <td>
              <div class="client-cell">
                <span class="text-white font-bold block">{{ tx.client }}</span>
                <span class="text-slate-500 text-[10px] font-bold">{{ tx.date }}</span>
              </div>
            </td>
            <td><span class="text-slate-300 font-medium">{{ tx.service }}</span></td>
            <td class="text-right">
              <span class="text-white font-bold text-lg">₹{{ tx.amount }}</span>
            </td>
            <td class="text-center">
              <span class="status-pill" :class="tx.status.toLowerCase()">{{ tx.status }}</span>
            </td>
          </tr>
        </transition-group>
      </table>

      <div v-if="filteredTransactions.length === 0" class="empty-results">
        <i class="fa-solid fa-ban text-2xl mb-2"></i>
        <p class="font-bold text-xs uppercase tracking-widest text-slate-600">No matching records found</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const searchQuery = ref('');
const filterStatus = ref('All');

const transactions = ref([
  { id: 'TXN-99102', client: 'Maharaja Vikram', date: '25 Dec 2025 • 14:20', service: 'Private Jet Charter', amount: '12,50,000', status: 'Completed' },
  { id: 'TXN-99103', client: 'Sonia Malhotra', date: '25 Dec 2025 • 12:15', service: 'Penthouse Booking', amount: '4,20,000', status: 'Processing' },
  { id: 'TXN-99104', client: 'Elena Rodriguez', date: '24 Dec 2025 • 18:40', service: 'Security Detail', amount: '1,80,000', status: 'Completed' },
  { id: 'TXN-99105', client: 'Dr. Arjan Iyer', date: '24 Dec 2025 • 10:30', service: 'Luxury Fleet', amount: '85,000', status: 'Failed' },
  { id: 'TXN-99106', client: 'Maharaja Vikram', date: '23 Dec 2025 • 16:00', service: 'Fine Dining Event', amount: '3,10,000', status: 'Completed' },
]);

const filteredTransactions = computed(() => {
  return transactions.value.filter(tx => {
    const matchesSearch = tx.client.toLowerCase().includes(searchQuery.value.toLowerCase()) || tx.id.toLowerCase().includes(searchQuery.value.toLowerCase());
    const matchesFilter = filterStatus.value === 'All' || tx.status === filterStatus.value;
    return matchesSearch && matchesFilter;
  });
});
</script>

<style scoped>
.payments-page { animation: fadeIn 0.8s ease; padding-bottom: 50px; }

/* Header & Live Indicator */
.page-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 2.5rem; }
.live-indicator { width: 8px; height: 8px; background: #00ff88; border-radius: 50%; box-shadow: 0 0 10px #00ff88; animation: pulse 2s infinite; }

.export-btn { background: #1a1a1a; border: 1px solid #333; color: white; padding: 10px 20px; border-radius: 8px; font-size: 11px; text-transform: uppercase; cursor: pointer; transition: 0.3s; }
.export-btn:hover { background: white; color: black; }

/* Revenue Grid */
.revenue-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-bottom: 3rem; }
.rev-card { background: #0c0c0c; border: 1px solid rgba(255,255,255,0.05); padding: 2rem; border-radius: 20px; position: relative; overflow: hidden; }
.rev-card .label { color: #555; font-size: 10px; font-weight: 900; text-transform: uppercase; letter-spacing: 1.5px; display: block; margin-bottom: 10px; }

.mini-chart-bar { height: 3px; background: #1a1a1a; margin-top: 15px; border-radius: 10px; overflow: hidden; }
.mini-chart-bar .fill { height: 100%; background: #00ff88; box-shadow: 0 0 10px #00ff88; }
.mini-chart-bar .fill.gold { background: #c5a059; box-shadow: 0 0 10px #c5a059; }

/* Controls */
.table-controls { display: flex; justify-content: space-between; margin-bottom: 1.5rem; gap: 1rem; align-items: center; }
.search-wrap { background: #0c0c0c; border: 1px solid #222; border-radius: 12px; padding: 0.8rem 1.2rem; display: flex; align-items: center; gap: 12px; flex: 1; max-width: 400px; }
.search-wrap input { background: transparent; border: none; color: white; outline: none; width: 100%; font-size: 0.9rem; }

.filter-pills { display: flex; gap: 8px; }
.pill { background: #111; border: 1px solid #222; color: #666; padding: 8px 16px; border-radius: 50px; font-size: 11px; font-weight: 800; cursor: pointer; transition: 0.3s; }
.pill.active { background: #c5a059; color: black; border-color: #c5a059; }

/* Ledger Table */
.ledger-container { background: #0c0c0c; border-radius: 20px; border: 1px solid rgba(255,255,255,0.05); overflow: hidden; }
.ledger-table { width: 100%; border-collapse: collapse; }
.ledger-table th { background: #111; padding: 1.2rem 1.5rem; text-align: left; font-size: 0.7rem; border-bottom: 1px solid #1a1a1a; }
.ledger-table td { padding: 1.2rem 1.5rem; border-bottom: 1px solid rgba(255,255,255,0.02); }

.status-pill { padding: 4px 12px; border-radius: 50px; font-size: 9px; font-weight: 900; text-transform: uppercase; }
.status-pill.completed { background: rgba(0, 255, 136, 0.1); color: #00ff88; border: 1px solid rgba(0, 255, 136, 0.2); }
.status-pill.processing { background: rgba(197, 160, 89, 0.1); color: #c5a059; border: 1px solid rgba(197, 160, 89, 0.2); }
.status-pill.failed { background: rgba(255, 77, 77, 0.1); color: #ff4d4d; border: 1px solid rgba(255, 77, 77, 0.2); }

.empty-results { padding: 4rem; text-align: center; color: #333; }

/* Animations */
.animate-stagger { opacity: 0; animation: slideUp 0.5s ease forwards; animation-delay: var(--delay); }
.list-enter-active, .list-leave-active { transition: all 0.4s ease; }
.list-enter-from { opacity: 0; transform: translateY(10px); }
.list-leave-to { opacity: 0; transform: translateY(-10px); }

@keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
@keyframes slideUp { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }

@media (max-width: 1024px) {
  .revenue-grid { grid-template-columns: 1fr; }
  .table-controls { flex-direction: column; align-items: flex-start; }
}
</style>
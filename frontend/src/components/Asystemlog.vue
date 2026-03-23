<template>
  <div class="system-log-page">
    <header class="page-header animate-slide-down">
      <div class="header-info">
        <h2 class="text-white font-black text-3xl uppercase tracking-tighter">System Console</h2>
        <p class="text-slate-500 text-[10px] font-bold uppercase tracking-[0.2em]">Node-Terminal ID: 00-AF-X19</p>
      </div>
      <div class="metrics-bar">
        <div class="metric">
          <span class="m-label">Uptime</span>
          <span class="m-value text-[#00ff88]">99.98%</span>
        </div>
        <div class="metric">
          <span class="m-label">Latency</span>
          <span class="m-value text-[#c5a059]">24ms</span>
        </div>
        <button class="clear-logs" @click="clearLogs">Flush Buffer</button>
      </div>
    </header>

    <div class="performance-grid mb-8">
      <div v-for="stat in systemStats" :key="stat.label" class="stat-box">
        <div class="flex justify-between items-center mb-2">
          <span class="text-[10px] font-black uppercase text-slate-500">{{ stat.label }}</span>
          <span class="text-white font-bold text-xs">{{ stat.value }}%</span>
        </div>
        <div class="usage-bar">
          <div class="usage-fill" :style="{ width: stat.value + '%' }" :class="getUsageColor(stat.value)"></div>
        </div>
      </div>
    </div>

    <div class="console-wrapper shadow-premium animate-fade-in">
      <div class="console-header">
        <div class="dots"><span></span><span></span><span></span></div>
        <div class="title">Mainframe_Output.log</div>
        <div class="status">LIVE FEED</div>
      </div>
      
      <div class="console-body" ref="scrollContainer">
        <transition-group name="log-list">
          <div v-for="log in filteredLogs" :key="log.id" class="log-entry" :class="log.level.toLowerCase()">
            <span class="log-time">[{{ log.time }}]</span>
            <span class="log-level">{{ log.level }}</span>
            <span class="log-source">[{{ log.source }}]</span>
            <span class="log-msg">{{ log.message }}</span>
            <span class="log-latency" v-if="log.latency">{{ log.latency }}ms</span>
          </div>
        </transition-group>
      </div>

      <div class="console-footer">
        <div class="search-box">
          <i class="fa-solid fa-terminal"></i>
          <input v-model="searchTerm" placeholder="grep --search system..." />
        </div>
        <div class="active-tasks">
          <span class="text-[9px] font-bold text-[#c5a059]">ACTIVE WORKERS: 08</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const searchTerm = ref('');
const scrollContainer = ref(null);

const systemStats = ref([
  { label: 'CPU Load', value: 32 },
  { label: 'RAM Usage', value: 58 },
  { label: 'DB I/O', value: 14 },
  { label: 'Network', value: 82 }
]);

const logs = ref([
  { id: 1, time: '15:20:01', level: 'INFO', source: 'AUTH', message: 'User session verified for Maharaja Vikram', latency: 12 },
  { id: 2, time: '15:20:05', level: 'WARN', source: 'FLEET', message: 'GPS ping delayed for Asset VIP-001', latency: 450 },
  { id: 3, time: '15:21:10', level: 'INFO', source: 'DB', message: 'Syncing Global Destinations table...', latency: 89 },
  { id: 4, time: '15:22:00', level: 'ERROR', source: 'PAY', message: 'Handshake failed with Payment Gateway API', latency: 1200 },
  { id: 5, time: '15:22:15', level: 'INFO', source: 'SYS', message: 'Automated backup completed successfully', latency: null },
  { id: 6, time: '15:23:40', level: 'DEBUG', source: 'CACH', message: 'Flushing redundant session tokens', latency: 5 },
]);

const filteredLogs = computed(() => {
  return logs.value.filter(l => 
    l.message.toLowerCase().includes(searchTerm.value.toLowerCase()) || 
    l.source.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});

const getUsageColor = (val) => {
  if (val > 80) return 'bg-red-500';
  if (val > 50) return 'bg-[#c5a059]';
  return 'bg-[#00ff88]';
};

const clearLogs = () => { logs.value = []; };

// Simulate live updates
onMounted(() => {
  setInterval(() => {
    systemStats.value.forEach(s => {
      const change = Math.floor(Math.random() * 5) - 2;
      s.value = Math.max(10, Math.min(95, s.value + change));
    });
  }, 3000);
});
</script>

<style scoped>
.system-log-page { animation: fadeIn 0.5s ease; font-family: 'JetBrains Mono', 'Fira Code', monospace; }

/* Header Metrics */
.page-header { display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 2rem; }
.metrics-bar { display: flex; align-items: center; gap: 2rem; }
.metric { display: flex; flex-direction: column; text-align: right; }
.m-label { font-size: 9px; font-weight: 900; color: #555; text-transform: uppercase; }
.m-value { font-size: 1.2rem; font-weight: 800; }

.clear-logs { background: transparent; border: 1px solid #333; color: #777; padding: 6px 15px; border-radius: 4px; font-size: 10px; font-weight: 800; cursor: pointer; transition: 0.3s; }
.clear-logs:hover { border-color: #ff4d4d; color: #ff4d4d; }

/* Performance Grid */
.performance-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; }
.stat-box { background: #0c0c0c; padding: 1rem; border-radius: 12px; border: 1px solid #1a1a1a; }
.usage-bar { height: 4px; background: #1a1a1a; border-radius: 2px; overflow: hidden; }
.usage-fill { height: 100%; transition: width 1s ease; }

/* Console Aesthetic */
.console-wrapper { background: #080808; border-radius: 12px; border: 1px solid #222; overflow: hidden; display: flex; flex-direction: column; height: 60vh; }

.console-header { background: #111; padding: 0.8rem 1.2rem; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #222; }
.dots { display: flex; gap: 6px; }
.dots span { width: 8px; height: 8px; border-radius: 50%; background: #333; }
.title { font-size: 10px; color: #555; font-weight: bold; letter-spacing: 1px; }
.status { font-size: 8px; color: #00ff88; font-weight: 900; letter-spacing: 2px; }

.console-body { flex: 1; padding: 1.5rem; overflow-y: auto; display: flex; flex-direction: column; gap: 8px; background-image: radial-gradient(circle at 50% 50%, rgba(0, 255, 136, 0.02) 0%, transparent 100%); }

.log-entry { font-size: 12px; display: flex; gap: 12px; white-space: nowrap; border-left: 2px solid transparent; padding-left: 10px; }
.log-time { color: #444; }
.log-level { font-weight: 900; width: 50px; }
.log-source { color: #c5a059; font-weight: bold; }
.log-msg { color: #ccc; white-space: normal; }
.log-latency { color: #555; font-style: italic; }

/* Level Colors */
.info .log-level { color: #00ff88; }
.warn .log-level { color: #ffd700; }
.error { background: rgba(255, 77, 77, 0.05); border-color: #ff4d4d; }
.error .log-level { color: #ff4d4d; }
.debug .log-level { color: #00d2ff; }

.console-footer { background: #111; padding: 0.8rem 1.2rem; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #222; }
.search-box { display: flex; align-items: center; gap: 10px; flex: 1; }
.search-box i { color: #c5a059; font-size: 12px; }
.search-box input { background: transparent; border: none; outline: none; color: #00ff88; font-size: 12px; width: 100%; }

/* Transitions */
.log-list-enter-active { transition: all 0.3s ease-out; }
.log-list-enter-from { opacity: 0; transform: translateX(-10px); }

@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

@media (max-width: 1024px) {
  .performance-grid { grid-template-columns: 1fr 1fr; }
}
</style>
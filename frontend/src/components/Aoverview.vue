<template>
  <div class="overview-container">
    <section class="welcome-banner">
      <div class="text-content">
        <h2>Executive Dashboard</h2>
        <p>Welcome back, Superintendent. Here is the status of the Indoria ecosystem today.</p>
      </div>
      <div class="live-indicator">
        <span class="pulse"></span> Live System Monitoring
      </div>
    </section>

    <div class="stats-grid">
      <div v-for="stat in quickStats" :key="stat.label" class="stat-card">
        <div class="stat-icon" :style="{ color: stat.color, background: stat.bg }">
          <i :class="stat.icon"></i>
        </div>
        <div class="stat-info">
          <h3>{{ stat.value }}</h3>
          <p>{{ stat.label }}</p>
        </div>
        <div class="stat-trend" :class="stat.trendUp ? 'up' : 'down'">
          <i :class="stat.trendUp ? 'fa-solid fa-arrow-up' : 'fa-solid fa-arrow-down'"></i>
          {{ stat.percentage }}%
        </div>
      </div>
    </div>

    <div class="analytics-row">
      <div class="chart-container main-chart">
        <div class="chart-header">
          <h4>Revenue & Bookings Trend</h4>
          <select class="chart-filter">
            <option>Last 7 Days</option>
            <option>Last 30 Days</option>
          </select>
        </div>
        <div class="chart-wrapper">
          <Line :data="revenueData" :options="chartOptions" />
        </div>
      </div>

      <div class="chart-container side-chart">
        <h4>Fleet Mood Monitor</h4>
        <div class="mood-list">
          <div v-for="fleet in fleetStatus" :key="fleet.id" class="mood-item">
            <div class="fleet-info">
              <strong>{{ fleet.car }}</strong>
              <span>VIP: {{ fleet.passenger }}</span>
            </div>
            <div class="mood-status">
              <span class="mood-label" :style="{ color: fleet.moodColor }">{{ fleet.mood }}</span>
              <div class="mood-bar-bg">
                <div class="mood-bar-fill" :style="{ width: fleet.intensity + '%', background: fleet.moodColor }"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="activity-section">
      <h4>Recent VIP Transactions</h4>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>Traveler</th>
              <th>Destination</th>
              <th>Status</th>
              <th>Amount</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="tx in recentTransactions" :key="tx.id">
              <td>
                <div class="user-cell">
                  <img :src="tx.avatar" alt="VIP" />
                  <div>
                    <strong>{{ tx.user }}</strong>
                    <span>{{ tx.tier }}</span>
                  </div>
                </div>
              </td>
              <td>{{ tx.location }}</td>
              <td><span class="status-pill" :class="tx.status.toLowerCase()">{{ tx.status }}</span></td>
              <td>₹{{ tx.amount }}</td>
              <td><button class="view-btn">View Details</button></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { Line } from 'vue-chartjs';
import { 
  Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement 
} from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

// Mock Data for Quick Stats
const quickStats = ref([
  { label: 'Total Revenue', value: '₹12.4M', icon: 'fa-solid fa-indian-rupee-sign', color: '#c5a059', bg: 'rgba(197, 160, 89, 0.1)', trendUp: true, percentage: '12' },
  { label: 'Active VIPs', value: '142', icon: 'fa-solid fa-user-check', color: '#00d2ff', bg: 'rgba(0, 210, 255, 0.1)', trendUp: true, percentage: '5' },
  { label: 'Fleet Online', value: '18/20', icon: 'fa-solid fa-car', color: '#00ff88', bg: 'rgba(0, 255, 136, 0.1)', trendUp: false, percentage: '2' },
  { label: 'Pending Vaults', value: '7', icon: 'fa-solid fa-folder-open', color: '#ff4d4d', bg: 'rgba(255, 77, 77, 0.1)', trendUp: true, percentage: '14' }
]);

// Fleet Data
const fleetStatus = ref([
  { id: 1, car: 'Rolls Royce Ghost', passenger: 'Vikram Singh', mood: 'Calm', intensity: 85, moodColor: '#00d2ff' },
  { id: 2, car: 'Bentley Mulsanne', passenger: 'Ananya Rao', mood: 'Energetic', intensity: 70, moodColor: '#ff9f43' },
  { id: 3, car: 'Mercedes Maybach', passenger: 'Rahul Jain', mood: 'Festive', intensity: 95, moodColor: '#c5a059' }
]);

// Chart Data
const revenueData = {
  labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  datasets: [{
    label: 'Revenue (Lakhs)',
    data: [12, 19, 15, 25, 22, 30, 28],
    borderColor: '#c5a059',
    backgroundColor: 'rgba(197, 160, 89, 0.1)',
    tension: 0.4,
    fill: true
  }]
};

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: { legend: { display: false } },
  scales: {
    y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#666' } },
    x: { grid: { display: false }, ticks: { color: '#666' } }
  }
};

const recentTransactions = ref([
  { id: 1, user: 'Maharaja Vikram', tier: 'Platinum', location: 'Udaipur', status: 'Confirmed', amount: '4,50,000', avatar: 'https://i.pravatar.cc/150?u=1' },
  { id: 2, user: 'Sonia Malhotra', tier: 'Gold', location: 'Jaipur', status: 'Pending', amount: '1,20,000', avatar: 'https://i.pravatar.cc/150?u=2' }
]);
</script>

<style scoped>
.overview-container {
  color: #fff;
  padding-bottom: 100px; /* Space for mobile slider */
}

/* Banner */
.welcome-banner {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.welcome-banner h2 { font-family: 'Playfair Display', serif; font-size: 1.8rem; margin: 0; }
.welcome-banner p { color: #888; margin: 5px 0 0; }

.live-indicator {
  display: flex;
  align-items: center;
  gap: 10px;
  background: rgba(0, 255, 136, 0.05);
  padding: 8px 15px;
  border-radius: 20px;
  color: #00ff88;
  font-size: 0.8rem;
  border: 1px solid rgba(0, 255, 136, 0.2);
}

.pulse {
  width: 8px;
  height: 8px;
  background: #00ff88;
  border-radius: 50%;
  animation: pulse 1.5s infinite;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2.5rem;
}

.stat-card {
  background: #121212;
  border: 1px solid rgba(255,255,255,0.05);
  padding: 1.5rem;
  border-radius: 16px;
  display: flex;
  align-items: center;
  position: relative;
  transition: transform 0.3s ease;
}

.stat-card:hover { transform: translateY(-5px); border-color: rgba(197, 160, 89, 0.3); }

.stat-icon {
  width: 50px;
  height: 50px;
  border-radius: 12px;
  display: grid;
  place-items: center;
  font-size: 1.2rem;
  margin-right: 1rem;
}

.stat-info h3 { font-size: 1.5rem; margin: 0; }
.stat-info p { color: #666; font-size: 0.8rem; margin: 0; }

.stat-trend {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  font-size: 0.75rem;
  font-weight: 700;
}
.stat-trend.up { color: #00ff88; }
.stat-trend.down { color: #ff4d4d; }

/* Analytics Row */
.analytics-row {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
}

.chart-container {
  background: #121212;
  padding: 1.5rem;
  border-radius: 16px;
  border: 1px solid rgba(255,255,255,0.05);
}

.chart-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; }
.chart-wrapper { height: 300px; }

.mood-list { display: flex; flex-direction: column; gap: 1.2rem; margin-top: 1rem; }
.mood-item { background: rgba(255,255,255,0.02); padding: 12px; border-radius: 10px; }
.fleet-info { display: flex; flex-direction: column; margin-bottom: 8px; }
.fleet-info strong { font-size: 0.9rem; }
.fleet-info span { font-size: 0.75rem; color: #666; }

.mood-bar-bg { background: rgba(255,255,255,0.05); height: 6px; border-radius: 10px; overflow: hidden; }
.mood-bar-fill { height: 100%; transition: width 1s ease-in-out; }

/* Table Section */
.activity-section {
  background: #121212;
  padding: 1.5rem;
  border-radius: 16px;
}

table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
th { text-align: left; color: #444; font-size: 0.75rem; text-transform: uppercase; padding: 12px; border-bottom: 1px solid rgba(255,255,255,0.05); }
td { padding: 15px 12px; border-bottom: 1px solid rgba(255,255,255,0.02); font-size: 0.9rem; }

.user-cell { display: flex; align-items: center; gap: 12px; }
.user-cell img { width: 35px; height: 35px; border-radius: 50%; border: 1px solid #c5a059; }
.user-cell span { font-size: 0.7rem; color: #c5a059; display: block; }

.status-pill { padding: 4px 10px; border-radius: 20px; font-size: 0.7rem; font-weight: 700; }
.confirmed { background: rgba(0, 255, 136, 0.1); color: #00ff88; }
.pending { background: rgba(255, 159, 67, 0.1); color: #ff9f43; }

.view-btn { background: none; border: 1px solid #333; color: #888; padding: 5px 12px; border-radius: 6px; cursor: pointer; transition: 0.3s; }
.view-btn:hover { border-color: #c5a059; color: #c5a059; }

@keyframes pulse {
  0% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.5); opacity: 0.4; }
  100% { transform: scale(1); opacity: 1; }
}

@media (max-width: 1024px) {
  .analytics-row { grid-template-columns: 1fr; }
}
</style>
<template>
  <div class="min-h-screen bg-[#fcf9f4]">
    <main class="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
      <div class="mb-8 flex flex-col justify-between gap-4 md:flex-row md:items-end">
        <div>
          <h1 class="text-2xl font-bold text-[#1a150e] font-serif">Booking Analytics</h1>
          <p class="text-slate-500">Track your travel footprint and spending habits.</p>
        </div>
        <div class="flex gap-3">
          <select class="rounded-lg border-slate-200 bg-white text-sm font-medium text-[#1a150e] shadow-sm focus:ring-[#f3c969] focus:border-[#f3c969]">
            <option>Year 2024</option>
            <option>Year 2023</option>
          </select>
          <button class="inline-flex items-center rounded-lg bg-[#1a150e] px-4 py-2 text-sm font-semibold text-[#f3c969] shadow-sm hover:bg-[#2b241a] transition-colors border border-[#f3c969]/20">
            Export Report
          </button>
        </div>
      </div>

      <div class="mb-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <div v-for="stat in stats" :key="stat.label" class="rounded-2xl border border-[#f3c969]/10 bg-white p-6 shadow-sm">
          <div class="flex items-center space-x-4">
            <div class="rounded-xl p-3 bg-[#1a150e] flex items-center justify-center w-12 h-12">
              <i :class="`${stat.icon} text-[#f3c969] text-xl`"></i>
            </div>
            <div>
              <p class="text-sm font-medium text-slate-500">{{ stat.label }}</p>
              <p class="text-2xl font-bold text-[#1a150e]">{{ stat.value }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="mb-8 grid grid-cols-1 gap-8 lg:grid-cols-3">
        <div class="lg:col-span-2 rounded-2xl border border-[#f3c969]/10 bg-white p-6 shadow-sm">
          <h3 class="mb-6 text-lg font-bold text-[#1a150e] font-serif">Spending Trends (USD)</h3>
          <div class="h-64 relative">
            <canvas id="spendingChart"></canvas>
          </div>
        </div>

        <div class="rounded-2xl border border-[#f3c969]/10 bg-white p-6 shadow-sm">
          <h3 class="mb-6 text-lg font-bold text-[#1a150e] font-serif">Top Categories</h3>
          <div class="h-64 relative">
            <canvas id="categoryChart"></canvas>
          </div>
        </div>
      </div>

      <div class="overflow-hidden rounded-2xl border border-[#f3c969]/10 bg-white shadow-sm">
        <div class="border-b border-slate-100 px-6 py-4">
          <h3 class="text-lg font-bold text-[#1a150e] font-serif">Recent Bookings</h3>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left">
            <thead class="bg-[#fcf9f4] text-xs font-semibold uppercase tracking-wider text-[#1a150e]/60">
              <tr>
                <th class="px-6 py-4">Destination</th>
                <th class="px-6 py-4">Date</th>
                <th class="px-6 py-4">Status</th>
                <th class="px-6 py-4">Amount</th>
                <th class="px-6 py-4 text-right">Actions</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-100 text-sm text-slate-600">
              <tr v-for="booking in bookings" :key="booking.id" class="hover:bg-[#fcf9f4]/50 transition-colors">
                <td class="whitespace-nowrap px-6 py-4">
                  <div class="flex items-center space-x-3">
                    <img :src="booking.img" class="h-10 w-10 rounded-lg object-cover border border-[#f3c969]/10" />
                    <span class="font-semibold text-[#1a150e]">{{ booking.place }}</span>
                  </div>
                </td>
                <td class="px-6 py-4">{{ booking.date }}</td>
                <td class="px-6 py-4">
                  <span :class="`rounded-full px-2.5 py-0.5 text-xs font-medium ${booking.statusClass}`">
                    {{ booking.status }}
                  </span>
                </td>
                <td class="px-6 py-4 font-medium text-[#1a150e]">{{ booking.amount }}</td>
                <td class="px-6 py-4 text-right">
                  <button class="text-[#f3c969] hover:text-[#1a150e] font-bold transition-colors">Details</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Chart from 'chart.js/auto'

// Updated stats with FontAwesome icons
const stats = ref([
  { label: 'Total Spent', value: '$12,450', icon: 'fas fa-wallet' },
  { label: 'Trips Completed', value: '14', icon: 'fas fa-route' },
  { label: 'Saved Destinations', value: '28', icon: 'fas fa-heart' },
  { label: 'Reward Points', value: '4,200', icon: 'fas fa-coins' }
])

const bookings = ref([
  { id: 1, place: 'Paris, France', date: 'Dec 12, 2024', amount: '$1,200', status: 'Confirmed', statusClass: 'bg-emerald-50 text-emerald-700', img: 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=100&q=80' },
  { id: 2, place: 'Tokyo, Japan', date: 'Oct 05, 2024', amount: '$2,850', status: 'Completed', statusClass: 'bg-blue-50 text-blue-700', img: 'https://images.unsplash.com/photo-1540959733332-e94e270b4d82?auto=format&fit=crop&w=100&q=80' },
  { id: 3, place: 'Bali, Indonesia', date: 'Aug 22, 2024', amount: '$950', status: 'Cancelled', statusClass: 'bg-red-50 text-red-700', img: 'https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=100&q=80' }
])

onMounted(() => {
  // 1. Line Chart: Spending Trends
  const ctxLine = document.getElementById('spendingChart').getContext('2d');
  new Chart(ctxLine, {
    type: 'line',
    data: {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      datasets: [{
        label: 'Spending',
        data: [1200, 1900, 1500, 2100, 1800, 2400, 3200, 2800, 3500, 4100, 3900, 4500],
        borderColor: '#f3c969', // Brand Gold
        backgroundColor: 'rgba(243, 201, 105, 0.1)', // Gold Glow
        borderWidth: 3,
        tension: 0.4, // Smooth curve
        fill: true,
        pointBackgroundColor: '#1a150e',
        pointBorderColor: '#f3c969',
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        y: { beginAtZero: true, grid: { color: 'rgba(0,0,0,0.05)' } },
        x: { grid: { display: false } }
      }
    }
  });

  // 2. Donut Chart: Category Breakdown
  const ctxDonut = document.getElementById('categoryChart').getContext('2d');
  new Chart(ctxDonut, {
    type: 'doughnut',
    data: {
      labels: ['Hotels', 'Flights', 'Activities', 'Transport'],
      datasets: [{
        data: [45, 25, 20, 10],
        backgroundColor: ['#1a150e', '#f3c969', '#2b241a', '#e2e8f0'],
        hoverOffset: 10,
        borderWidth: 0
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'bottom', labels: { boxWidth: 12, padding: 20 } }
      },
      cutout: '70%'
    }
  });
})
</script>

<style scoped>
/* Ensure icons align correctly if not using a library-specific component */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}
</style>
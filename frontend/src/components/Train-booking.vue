<template>
  <div class="min-h-screen bg-[#fafaf9] pb-12">
    <header class="bg-[#1a150e] text-white pt-24 pb-20 text-center relative overflow-hidden">
      <div class="absolute inset-0 opacity-10">
        <i class="fas fa-train text-[200px] absolute -bottom-10 -right-10 rotate-12"></i>
      </div>
      <div class="relative z-10 container mx-auto px-4">
        <h1 class="font-serif text-4xl md:text-5xl font-bold mb-4 tracking-tight">
          Book <span class="text-[#f3c969]">Train</span> Tickets
        </h1>
        <p class="text-slate-400 font-medium tracking-widest uppercase text-xs">
          Authorized IRCTC Partner • Fast • Secure • Heritage Travel
        </p>
      </div>
    </header>

    <div class="max-w-5xl mx-auto px-4">
      <section class="-mt-12 relative z-20">
        <div class="flex gap-1">
          <button 
            @click="searchMode = 'station'"
            :class="searchMode === 'station' ? 'bg-white text-[#1a150e] border-t-2 border-[#f3c969]' : 'bg-white/60 text-slate-500'"
            class="px-6 py-3 rounded-t-xl font-bold text-sm transition-all flex items-center gap-2 cursor-pointer"
          >
            <i class="fas fa-map-marked-alt"></i> Stations
          </button>
          <button 
            @click="searchMode = 'number'"
            :class="searchMode === 'number' ? 'bg-white text-[#1a150e] border-t-2 border-[#f3c969]' : 'bg-white/60 text-slate-500'"
            class="px-6 py-3 rounded-t-xl font-bold text-sm transition-all flex items-center gap-2 cursor-pointer"
          >
            <i class="fas fa-train"></i> Train No.
          </button>
        </div>

        <div class="bg-white p-6 md:p-8 rounded-b-2xl rounded-tr-2xl shadow-xl shadow-[#1a150e]/5 border border-slate-100">
          <div class="grid grid-cols-1 md:grid-cols-12 gap-6 items-end">
            
            <template v-if="searchMode === 'station'">
              <div class="md:col-span-4 space-y-2">
                <label :class="labelStyle">From</label>
                <div class="relative">
                  <i class="fas fa-map-pin absolute left-4 top-1/2 -translate-y-1/2 text-[#f3c969]"></i>
                  <input type="text" v-model="search.from" placeholder="Source" :class="inputStyle" />
                </div>
              </div>
              
              <div class="md:col-span-1 flex justify-center pb-1">
                <button @click="swapStations" class="h-10 w-10 rounded-full bg-[#fcf9f4] border border-[#f3c969]/20 text-[#f3c969] hover:bg-[#f3c969] hover:text-white transition-all">
                  <i class="fas fa-exchange-alt"></i>
                </button>
              </div>

              <div class="md:col-span-4 space-y-2">
                <label :class="labelStyle">To</label>
                <div class="relative">
                  <i class="fas fa-location-arrow absolute left-4 top-1/2 -translate-y-1/2 text-[#f3c969]"></i>
                  <input type="text" v-model="search.to" placeholder="Destination" :class="inputStyle" />
                </div>
              </div>
            </template>

            <template v-else>
              <div class="md:col-span-9 space-y-2">
                <label :class="labelStyle">Train Name or Number</label>
                <input type="text" v-model="search.trainNo" placeholder="Enter 5 digit number (e.g. 12004)" :class="inputStyle" />
              </div>
            </template>

            <div class="md:col-span-3 space-y-2">
              <label :class="labelStyle">Travel Date</label>
              <input type="date" v-model="search.date" :min="today" :class="inputStyle" />
            </div>

            <div class="md:col-span-12 lg:col-span-12 mt-4">
              <button 
                @click="handleSearch"
                :disabled="loading"
                class="w-full bg-[#1a150e] text-[#f3c969] font-bold py-4 rounded-xl shadow-lg hover:shadow-[#f3c969]/20 transition-all uppercase tracking-widest flex items-center justify-center gap-3 cursor-pointer border border-[#f3c969]/30"
              >
                <i v-if="loading" class="fas fa-spinner animate-spin"></i>
                <span v-else>Search Available Trains</span>
              </button>
            </div>
          </div>
        </div>
      </section>

      <section v-if="hasSearched" class="mt-12 space-y-6">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-[#f3c969]/20 pb-4">
          <h3 class="text-xl font-bold text-[#1a150e] font-serif">
            Available Services for <span class="text-[#f3c969]">{{ search.date }}</span>
          </h3>
          <div class="flex items-center gap-2">
            <span class="text-[10px] font-bold uppercase text-slate-400">Filter By:</span>
            <button class="px-3 py-1 bg-white border border-slate-200 rounded-full text-xs font-bold hover:border-[#f3c969]">Sleeper</button>
            <button class="px-3 py-1 bg-white border border-slate-200 rounded-full text-xs font-bold hover:border-[#f3c969]">AC Classes</button>
          </div>
        </div>

        <div v-for="train in results" :key="train.id" class="bg-white rounded-2xl overflow-hidden border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
          <div class="p-6 flex flex-col md:flex-row justify-between items-center gap-8">
            <div class="text-center md:text-left">
              <span class="text-[#f3c969] font-black text-xs tracking-widest uppercase">#{{ train.no }}</span>
              <h4 class="text-xl font-bold text-[#1a150e] font-serif uppercase tracking-tight">{{ train.name }}</h4>
            </div>

            <div class="flex items-center gap-6 md:gap-12">
              <div class="text-center">
                <span class="block text-2xl font-bold text-[#1a150e]">{{ train.departureTime }}</span>
                <span class="text-xs font-bold text-slate-400 uppercase tracking-tighter">{{ train.from }}</span>
              </div>
              
              <div class="flex flex-col items-center min-w-[100px]">
                <span class="text-[10px] font-bold text-slate-400 mb-1 uppercase">{{ train.duration }}</span>
                <div class="w-full h-[2px] bg-slate-100 relative">
                  <div class="absolute -top-1 right-0 text-[#f3c969] text-[8px]"><i class="fas fa-circle"></i></div>
                  <div class="absolute -top-1 left-0 text-slate-300 text-[8px]"><i class="fas fa-circle"></i></div>
                </div>
              </div>

              <div class="text-center">
                <span class="block text-2xl font-bold text-[#1a150e]">{{ train.arrivalTime }}</span>
                <span class="text-xs font-bold text-slate-400 uppercase tracking-tighter">{{ train.to }}</span>
              </div>
            </div>
          </div>

          <div class="bg-[#fcf9f4]/50 border-t border-slate-50 p-4 flex gap-4 overflow-x-auto">
            <div 
              v-for="cls in train.classes" 
              :key="cls.name" 
              class="min-w-[160px] bg-white border border-slate-200 p-4 rounded-xl hover:border-[#f3c969] transition-all cursor-pointer relative group"
            >
              <div class="flex justify-between items-start mb-3">
                <span class="font-black text-[#1a150e]">{{ cls.name }}</span>
                <span class="text-sm font-bold text-[#f3c969]">₹{{ cls.price }}</span>
              </div>
              <div class="mb-4">
                <p :class="cls.status.includes('WL') ? 'text-red-500' : 'text-emerald-600'" class="text-xs font-bold uppercase tracking-wide">
                  {{ cls.status }}
                </p>
                <p class="text-[10px] text-slate-400 font-medium">{{ cls.seats }} Seats Left</p>
              </div>
              <button 
                @click="handleBooking(train, cls)"
                class="w-full py-2 bg-[#1a150e] text-white text-[10px] font-bold uppercase tracking-widest rounded-lg opacity-0 group-hover:opacity-100 transition-opacity"
              >
                Book
              </button>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

// UI Logic Styles
const labelStyle = "text-[10px] font-black uppercase tracking-widest text-slate-500 ml-1"
const inputStyle = "w-full rounded-xl border border-slate-200 bg-slate-50 py-3 px-4 md:pl-10 text-sm font-bold text-[#1a150e] focus:border-[#f3c969] focus:bg-white focus:outline-none focus:ring-4 focus:ring-[#f3c969]/10 transition-all placeholder:text-slate-300"

const searchMode = ref('station')
const loading = ref(false)
const hasSearched = ref(false)
const today = new Date().toISOString().split('T')[0]

const search = reactive({
  from: '',
  to: '',
  trainNo: '',
  date: ''
})

const results = ref([
  {
    id: 1, no: '12004', name: 'LKO SHTBDI EXP', from: 'NDLS', to: 'LKO',
    departureTime: '06:10', arrivalTime: '12:40', duration: '06h 30m',
    classes: [
      { name: 'CC', price: '1240', status: 'Available', seats: '142' },
      { name: 'EC', price: '2450', status: 'WL-4', seats: '0' }
    ]
  },
  {
    id: 2, no: '12230', name: 'LUCKNOW MAIL', from: 'NDLS', to: 'LKO',
    departureTime: '22:15', arrivalTime: '06:05', duration: '07h 50m',
    classes: [
      { name: 'SL', price: '340', status: 'Available', seats: '24' },
      { name: '3A', price: '950', status: 'RAC-12', seats: '0' },
      { name: '2A', price: '1400', status: 'Available', seats: '04' }
    ]
  }
])

const swapStations = () => {
  const temp = search.from
  search.from = search.to
  search.to = temp
}

const handleSearch = () => {
  loading.value = true
  setTimeout(() => {
    loading.value = false
    hasSearched.value = true
  }, 1200)
}

const handleBooking = (train, cls) => {
  alert(`Initiating luxury booking for ${train.name} - Class ${cls.name}`)
}
</script>

<style scoped>
.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

/* Hide scrollbar for Chrome, Safari and Opera */
.overflow-x-auto::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.overflow-x-auto {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
</style>
<template>
  <div class="min-h-screen bg-[#fafaf9] pb-32 font-sans text-[#1a150e]">
    
    <header class="bg-[#1a150e] text-white pt-24 pb-32 relative overflow-hidden">
      <div class="absolute inset-0 opacity-10 pointer-events-none">
        <i class="fas fa-file-invoice-dollar text-[250px] absolute -bottom-20 -left-20 rotate-12"></i>
      </div>
      
      <div class="max-w-6xl mx-auto px-4 relative z-10">
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-8">
          <div>
            <div class="inline-block bg-[#f3c969] text-[#1a150e] px-3 py-1 rounded-md font-black text-[9px] uppercase tracking-[0.2em] mb-4">
              Financial Records
            </div>
            <h1 class="font-serif text-4xl md:text-5xl font-bold tracking-tight">Payment <span class="text-[#f3c969]">History</span></h1>
            <p class="text-slate-400 mt-4 max-w-md text-sm leading-relaxed">
              Review your global protection investments and download official tax-compliant invoices for your records.
            </p>
          </div>
          
          <div class="flex gap-4 md:gap-8">
            <div class="text-right">
              <span class="block text-[9px] font-black text-slate-500 uppercase tracking-widest mb-1">Total Protected</span>
              <span class="text-2xl font-serif font-bold text-white">₹14,290</span>
            </div>
            <div class="w-px h-10 bg-white/10 self-center"></div>
            <div class="text-right">
              <span class="block text-[9px] font-black text-slate-500 uppercase tracking-widest mb-1">Active Policies</span>
              <span class="text-2xl font-serif font-bold text-[#f3c969]">02</span>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="max-w-6xl mx-auto px-4 -mt-16 relative z-20">
      <div class="bg-white rounded-[2rem] shadow-2xl shadow-[#1a150e]/5 border border-slate-100 overflow-hidden">
        
        <div class="p-6 md:p-8 border-b border-slate-50 flex flex-col md:flex-row justify-between items-center gap-4">
          <h3 class="font-serif text-xl font-bold">Transaction Archive</h3>
          <div class="flex gap-3 w-full md:w-auto">
            <button class="flex-1 md:flex-none px-6 py-2.5 rounded-xl border border-slate-200 text-[10px] font-black uppercase tracking-widest hover:bg-slate-50 transition-all cursor-pointer">
              <i class="fas fa-download mr-2"></i> Export All
            </button>
            <button class="flex-1 md:flex-none px-6 py-2.5 rounded-xl bg-[#1a150e] text-[#f3c969] text-[10px] font-black uppercase tracking-widest transition-all cursor-pointer">
              <i class="fas fa-filter mr-2"></i> Filter
            </button>
          </div>
        </div>

        <div class="overflow-x-auto">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="bg-[#fcf9f4]">
                <th :class="thStyle">Description</th>
                <th :class="thStyle">Date & Time</th>
                <th :class="thStyle">Reference ID</th>
                <th :class="thStyle">Amount</th>
                <th :class="thStyle">Status</th>
                <th :class="thStyle" class="text-right">Invoice</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-slate-50">
              <tr v-for="tx in transactions" :key="tx.id" class="hover:bg-slate-50/50 transition-colors group">
                <td class="p-6">
                  <div class="flex items-center gap-4">
                    <div class="w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-[#1a150e] text-xs">
                      <i :class="tx.icon"></i>
                    </div>
                    <div>
                      <div class="text-sm font-bold text-[#1a150e]">{{ tx.plan }}</div>
                      <div class="text-[10px] text-slate-400 font-medium uppercase tracking-tighter">{{ tx.region }} Coverage</div>
                    </div>
                  </div>
                </td>
                
                <td class="p-6">
                  <div class="text-xs font-bold text-[#1a150e]">{{ tx.date }}</div>
                  <div class="text-[10px] text-slate-400 uppercase font-medium">{{ tx.time }}</div>
                </td>

                <td class="p-6">
                  <span class="font-mono text-[10px] text-slate-500 bg-slate-100 px-2 py-1 rounded">#{{ tx.ref }}</span>
                </td>

                <td class="p-6">
                  <div class="text-sm font-black text-[#1a150e]">₹{{ tx.amount }}</div>
                </td>

                <td class="p-6">
                  <div :class="getStatusClass(tx.status)">
                    <span class="w-1.5 h-1.5 rounded-full mr-2" :class="tx.status === 'Completed' ? 'bg-emerald-500' : 'bg-amber-500'"></span>
                    {{ tx.status }}
                  </div>
                </td>

                <td class="p-6 text-right">
                  <button class="text-slate-300 hover:text-[#1a150e] transition-colors p-2 cursor-pointer">
                    <i class="fas fa-file-pdf text-lg"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="p-6 bg-slate-50/50 flex justify-between items-center">
          <p class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Showing 1-4 of 12 Records</p>
          <div class="flex gap-2">
            <button class="w-8 h-8 flex items-center justify-center rounded-lg border border-slate-200 text-slate-400 hover:bg-white transition-all cursor-pointer"><i class="fas fa-chevron-left text-[10px]"></i></button>
            <button class="w-8 h-8 flex items-center justify-center rounded-lg bg-[#1a150e] text-[#f3c969] text-[10px] font-black">1</button>
            <button class="w-8 h-8 flex items-center justify-center rounded-lg border border-slate-200 text-slate-600 hover:bg-white transition-all cursor-pointer font-bold text-[10px]">2</button>
            <button class="w-8 h-8 flex items-center justify-center rounded-lg border border-slate-200 text-slate-400 hover:bg-white transition-all cursor-pointer"><i class="fas fa-chevron-right text-[10px]"></i></button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const thStyle = "p-6 text-[10px] font-black uppercase tracking-[0.2em] text-slate-400"

const transactions = reactive([
  {
    id: 1,
    plan: 'Premium Plus Portfolio',
    region: 'International',
    date: 'Dec 24, 2025',
    time: '14:32 PM',
    ref: 'IND-9921-001',
    amount: '6,930',
    status: 'Completed',
    icon: 'fas fa-globe-americas'
  },
  {
    id: 2,
    plan: 'Essential Shield',
    region: 'Domestic',
    date: 'Oct 12, 2025',
    time: '09:15 AM',
    ref: 'IND-8842-152',
    amount: '1,490',
    status: 'Completed',
    icon: 'fas fa-shield-alt'
  },
  {
    id: 3,
    plan: 'Premium Plus Portfolio',
    region: 'International',
    date: 'Aug 05, 2025',
    time: '18:45 PM',
    ref: 'IND-7712-990',
    amount: '5,870',
    status: 'Pending',
    icon: 'fas fa-plane-departure'
  }
])

const getStatusClass = (status) => {
  const base = "inline-flex items-center px-3 py-1 rounded-full text-[10px] font-black uppercase tracking-wider "
  return status === 'Completed' 
    ? base + "bg-emerald-50 text-emerald-700 border border-emerald-100 shadow-sm shadow-emerald-100"
    : base + "bg-amber-50 text-amber-700 border border-amber-100 shadow-sm shadow-amber-100"
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

.font-serif {
  font-family: 'Playfair Display', serif;
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
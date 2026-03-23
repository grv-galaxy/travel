<template>
  <div class="space-y-10 animate-reveal pb-20">
    <div class="flex flex-col md:flex-row md:items-end justify-between gap-6">
      <div class="space-y-2">
        <span class="text-[#f3c969] text-[10px] font-black uppercase tracking-[0.4em] block">Reservations</span>
        <h1 class="text-5xl md:text-7xl font-serif italic text-[#1a150e]">
          The Grand <span class="text-[#f3c969]">Express</span>
        </h1>
      </div>
      <div class="flex items-center gap-4 text-[10px] font-black uppercase tracking-widest text-slate-400">
        <i class="fas fa-circle text-[#f3c969] animate-pulse"></i>
        <span>Active Journey: NDLS - BOM</span>
      </div>
    </div>

    <div class="relative group cursor-pointer overflow-hidden rounded-2xl bg-[#1a150e] p-8 md:p-12 text-white shadow-2xl">
      <div class="absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-[#f3c969]/20 to-transparent"></div>
      <div class="absolute bottom-4 right-8 opacity-10 font-serif text-8xl italic select-none">First Class</div>

      <div class="relative z-10 flex flex-col md:flex-row justify-between gap-12">
        <div class="space-y-8 flex-1">
          <div class="flex items-center gap-8">
            <div class="text-center">
              <p class="text-[10px] text-[#f3c969] uppercase tracking-widest mb-1">Origin</p>
              <h4 class="text-3xl font-serif">DEL</h4>
              <p class="text-xs text-slate-400">10:30 AM</p>
            </div>
            
            <div class="flex-1 flex flex-col items-center group">
              <div class="w-full h-px bg-slate-700 relative">
                <div class="absolute inset-0 bg-[#f3c969] w-2/3 shadow-[0_0_10px_#f3c969]"></div>
                <i class="fas fa-train absolute -top-2 left-2/3 -translate-x-1/2 text-[#f3c969] text-xs"></i>
              </div>
              <span class="mt-4 text-[8px] uppercase tracking-[0.5em] text-slate-500">Maharaja Class</span>
            </div>

            <div class="text-center">
              <p class="text-[10px] text-[#f3c969] uppercase tracking-widest mb-1">Destination</p>
              <h4 class="text-3xl font-serif">MUM</h4>
              <p class="text-xs text-slate-400">08:45 PM</p>
            </div>
          </div>

          <div class="grid grid-cols-2 md:grid-cols-4 gap-6 pt-6 border-t border-white/10">
            <div v-for="label in ['Coach A1', 'Seat 12', 'Status: On-Time', 'Gate 04']" :key="label">
               <p class="text-[9px] uppercase tracking-widest text-slate-500">{{ label.split(': ')[0] }}</p>
               <p class="text-xs font-bold">{{ label.split(': ')[1] || label }}</p>
            </div>
          </div>
        </div>

        <div class="flex items-center justify-center">
          <button class="bg-[#f3c969] text-[#1a150e] px-8 py-4 rounded-lg font-black text-[10px] uppercase tracking-[0.2em] hover:bg-white transition-colors duration-500">
            View Digital Pass
          </button>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div v-for="service in services" :key="service.title" 
        class="bg-white border border-slate-100 p-8 hover:border-[#f3c969]/40 transition-all duration-700 group shadow-sm hover:shadow-xl">
        <div class="w-12 h-12 bg-[#fcf9f4] flex items-center justify-center mb-6 group-hover:bg-[#1a150e] transition-colors duration-700">
          <i :class="[service.icon, 'text-[#f3c969]']"></i>
        </div>
        <h5 class="font-serif text-lg font-bold mb-2">{{ service.title }}</h5>
        <p class="text-xs text-slate-500 leading-relaxed mb-6">{{ service.desc }}</p>
        <button class="text-[9px] font-black uppercase tracking-widest text-[#f3c969] border-b border-[#f3c969]/20 pb-1 group-hover:border-[#f3c969] transition-all">
          Manage Service
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const services = [
  { icon: 'fas fa-concierge-bell', title: 'Dining At Seat', desc: 'Pre-order artisanal meals curated by master chefs for your arrival.' },
  { icon: 'fas fa-car-side', title: 'Chauffeur Link', desc: 'Private luxury transport from the platform directly to your residence.' },
  { icon: 'fas fa-suitcase-rolling', title: 'Porter Service', desc: 'Seamless baggage handling from terminal entry to your specific cabin.' }
]
</script>

<style scoped>
.animate-reveal {
  animation: reveal 1s cubic-bezier(0.23, 1, 0.32, 1) forwards;
}

@keyframes reveal {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
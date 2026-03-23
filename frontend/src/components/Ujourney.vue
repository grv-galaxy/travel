<template>
  <div class="min-h-screen bg-[#fafaf9] pb-32 font-sans text-[#1a150e]">
    
    <header class="bg-[#1a150e] text-white pt-24 pb-40 relative overflow-hidden">
      <div class="absolute inset-0 opacity-10 pointer-events-none">
        <svg class="w-full h-full" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
          <path d="M0,500 Q250,400 500,500 T1000,500" stroke="#f3c969" fill="none" stroke-width="0.5" />
          <path d="M0,600 Q250,500 500,600 T1000,600" stroke="#f3c969" fill="none" stroke-width="0.5" />
        </svg>
      </div>

      <div class="max-w-6xl mx-auto px-4 relative z-10">
        <div class="flex flex-col items-center text-center space-y-6">
          <div class="inline-block px-4 py-1 border border-[#f3c969]/30 rounded-full">
            <span class="text-[9px] font-black uppercase tracking-[0.4em] text-[#f3c969]">Active Expedition</span>
          </div>
          <h1 class="font-serif text-5xl md:text-7xl font-bold tracking-tight">The <span class="text-[#f3c969]">Grand</span> Itinerary</h1>
          <p class="text-slate-400 max-w-xl text-sm md:text-base leading-relaxed">
            From the deserts of Rajasthan to the heritage corridors of Jaipur. Your curated sequence of events is synchronized with your Concierge.
          </p>
        </div>
      </div>
    </header>

    <div class="max-w-4xl mx-auto px-4 -mt-24 relative z-20">
      
      <div class="relative">
        <div class="absolute left-0 md:left-1/2 md:-ml-px top-0 bottom-0 w-px bg-gradient-to-b from-[#f3c969] via-slate-200 to-transparent"></div>

        <div class="space-y-24">
          <div v-for="(moment, idx) in itinerary" :key="idx" 
            class="relative flex flex-col md:flex-row items-start"
            :class="idx % 2 === 0 ? 'md:flex-row-reverse' : ''"
          >
            <div class="absolute left-[-8px] md:left-1/2 md:-ml-2 top-0 w-4 h-4 rounded-full bg-[#1a150e] border-2 border-[#f3c969] z-10 shadow-[0_0_10px_#f3c969]"></div>

            <div class="w-full md:w-[45%] pl-8 md:pl-0">
              <div class="group bg-white p-8 rounded-[2.5rem] shadow-xl border border-slate-50 hover:border-[#f3c969]/30 transition-all duration-700">
                <div class="flex items-center justify-between mb-4">
                  <span class="text-[10px] font-black text-[#f3c969] uppercase tracking-widest">{{ moment.time }}</span>
                  <i :class="[moment.icon, 'text-slate-200 group-hover:text-[#1a150e] transition-colors']"></i>
                </div>
                <h3 class="font-serif text-2xl font-bold mb-3">{{ moment.title }}</h3>
                <p class="text-xs text-slate-500 leading-relaxed mb-6">{{ moment.desc }}</p>
                
                <div class="flex items-center gap-3 py-4 border-t border-slate-50">
                   <div class="w-8 h-8 rounded-full bg-slate-50 flex items-center justify-center text-[10px]">
                     <i class="fas fa-map-pin"></i>
                   </div>
                   <span class="text-[9px] font-bold uppercase tracking-tighter text-slate-400">{{ moment.location }}</span>
                </div>
              </div>
            </div>

            <div class="hidden md:block md:w-[45%]"></div>
          </div>
        </div>
      </div>

      <div class="mt-32 text-center">
        <button class="px-12 py-5 bg-[#1a150e] text-[#f3c969] rounded-2xl font-black text-[10px] uppercase tracking-[0.4em] shadow-2xl hover:bg-white hover:text-[#1a150e] transition-all border border-[#1a150e]">
          Download Full PDF Guide
        </button>
      </div>

    </div>
  </div>
</template>

<script setup>
const itinerary = [
  {
    time: '09:00 AM • DEC 24',
    title: 'The Maharaja Express Arrival',
    desc: 'Disembark at platform 1. Your private concierge will be waiting at the carriage door to manage your luggage transfers.',
    location: 'Sawai Madhopur Station',
    icon: 'fas fa-train'
  },
  {
    time: '09:45 AM • DEC 24',
    title: 'Fleet Connection',
    desc: 'Transition to your Mercedes-Maybach S-Class for the heritage drive through the city gates.',
    location: 'Station VIP Gate',
    icon: 'fas fa-car-side'
  },
  {
    time: '11:30 AM • DEC 24',
    title: 'Imperial Haveli Check-in',
    desc: 'A private check-in ceremony followed by a welcome refreshment in the courtyard.',
    location: 'The Imperial Palace',
    icon: 'fas fa-hotel'
  },
  {
    time: '19:00 PM • DEC 24',
    title: 'Dinner Under The Stars',
    desc: 'A curated 7-course Rajasthani thali prepared by Chef Vardhan on the rooftop terrace.',
    location: 'Palace Observatory',
    icon: 'fas fa-utensils'
  }
]
</script>

<style scoped>
.font-serif { font-family: 'Playfair Display', serif; }

/* Custom ease for the hover effect */
.transition-all {
  transition-timing-function: cubic-bezier(0.23, 1, 0.32, 1);
}
</style>
<template>
  <div class="min-h-screen bg-[#fafaf9] pb-32 font-sans text-[#1a150e]">
    
    <header class="bg-[#1a150e] text-white pt-24 pb-32 relative overflow-hidden">
      <div class="absolute inset-0 opacity-10 pointer-events-none">
        <i class="fas fa-car-side text-[250px] absolute -bottom-10 -right-20 rotate-12"></i>
      </div>
      
      <div class="max-w-6xl mx-auto px-4 relative z-10">
        <div class="flex flex-col md:flex-row justify-between items-end gap-8">
          <div class="space-y-4">
            <div class="inline-flex items-center gap-2 bg-[#f3c969]/10 border border-[#f3c969]/30 px-4 py-1.5 rounded-full">
              <span class="text-[9px] font-black uppercase tracking-[0.3em] text-[#f3c969]">Active Logistics</span>
            </div>
            <h1 class="font-serif text-4xl md:text-5xl font-bold tracking-tight">Private <span class="text-[#f3c969]">Fleet</span></h1>
            <p class="text-slate-400 max-w-md text-sm leading-relaxed">
              Your chauffeur-driven experience is being coordinated. Manage your cabin preferences and track your arrival.
            </p>
          </div>

          <div class="bg-white/5 border border-white/10 p-6 rounded-2xl flex items-center gap-6">
            <div class="text-right">
              <span class="block text-[9px] font-black text-slate-500 uppercase tracking-widest">Estimated Arrival</span>
              <span class="text-2xl font-serif font-bold text-[#f3c969]">12 Mins</span>
            </div>
            <div class="w-12 h-12 rounded-full bg-[#f3c969] text-[#1a150e] flex items-center justify-center animate-pulse">
              <i class="fas fa-map-marker-alt"></i>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="max-w-6xl mx-auto px-4 -mt-16 relative z-20">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <div class="lg:col-span-2 space-y-8">
          <div class="bg-white rounded-[2.5rem] p-8 md:p-10 shadow-xl border border-slate-100">
            <div class="flex flex-col md:flex-row gap-10">
              <div class="w-full md:w-1/2 bg-[#fcf9f4] rounded-3xl p-8 flex flex-col items-center justify-center border border-slate-50 relative overflow-hidden group">
                <i class="fas fa-car text-[120px] text-slate-100 absolute transition-transform group-hover:scale-110"></i>
                <div class="relative z-10 text-center">
                  <h4 class="text-[10px] font-black uppercase tracking-[0.4em] text-slate-400 mb-2">Current Vehicle</h4>
                  <p class="font-serif text-2xl font-bold">Mercedes-Maybach S-Class</p>
                  <span class="inline-block mt-4 px-4 py-1 bg-[#1a150e] text-[#f3c969] text-[10px] font-black rounded-full uppercase tracking-widest">
                    DL 01 CAS 0007
                  </span>
                </div>
              </div>

              <div class="w-full md:w-1/2 flex flex-col justify-center space-y-6">
                <div class="flex items-center gap-4">
                  <div class="w-16 h-16 rounded-2xl bg-slate-100 flex items-center justify-center">
                    <i class="fas fa-user-tie text-2xl text-slate-400"></i>
                  </div>
                  <div>
                    <h5 class="text-sm font-black uppercase tracking-widest">Vikram Singh</h5>
                    <p class="text-xs text-slate-400">Executive Chauffeur • 8 Years Exp.</p>
                  </div>
                </div>
                <div class="h-px bg-slate-100 w-full"></div>
                <div class="grid grid-cols-2 gap-4">
                  <button class="flex items-center justify-center gap-2 py-4 bg-slate-50 hover:bg-[#1a150e] hover:text-[#f3c969] transition-all rounded-xl text-[10px] font-black uppercase tracking-widest">
                    <i class="fas fa-phone"></i> Call
                  </button>
                  <button class="flex items-center justify-center gap-2 py-4 bg-slate-50 hover:bg-[#1a150e] hover:text-[#f3c969] transition-all rounded-xl text-[10px] font-black uppercase tracking-widest">
                    <i class="fas fa-comment"></i> Chat
                  </button>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-white rounded-[2.5rem] p-8 md:p-10 shadow-xl border border-slate-100">
            <h3 class="font-serif text-2xl font-bold mb-8">Cabin <span class="text-[#f3c969]">Environment</span></h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-10">
              
              <div class="space-y-4">
                <div class="flex justify-between items-center">
                  <span class="text-[10px] font-black uppercase tracking-widest">Temperature</span>
                  <span class="text-xl font-serif font-bold text-[#f3c969]">{{ cabin.temp }}°C</span>
                </div>
                <input type="range" v-model="cabin.temp" min="16" max="28" class="w-full accent-[#1a150e]">
                <div class="flex justify-between text-[8px] font-bold text-slate-300 uppercase tracking-widest">
                  <span>Arctic</span>
                  <span>Tropical</span>
                </div>
              </div>

              <div class="space-y-4">
                <span class="text-[10px] font-black uppercase tracking-widest block">In-Car Mood</span>
                <div class="flex gap-2">
                  <button 
                    v-for="mood in moods" :key="mood"
                    @click="cabin.mood = mood"
                    :class="[
                      'flex-1 py-3 rounded-xl text-[8px] font-black uppercase tracking-widest transition-all',
                      cabin.mood === mood ? 'bg-[#1a150e] text-[#f3c969] shadow-lg' : 'bg-slate-50 text-slate-400'
                    ]"
                  >
                    {{ mood }}
                  </button>
                </div>
              </div>

            </div>
          </div>
        </div>

        <div class="space-y-6">
          <div class="bg-[#1a150e] rounded-[2.5rem] p-8 text-white shadow-2xl relative overflow-hidden">
            <h3 class="font-serif text-xl font-bold mb-6 text-[#f3c969]">Route Details</h3>
            <div class="space-y-8 relative">
              <div class="absolute left-3 top-2 bottom-2 w-px bg-white/10"></div>
              
              <div class="relative pl-10">
                <div class="absolute left-1.5 top-1.5 w-3 h-3 rounded-full bg-[#f3c969] ring-4 ring-[#f3c969]/20"></div>
                <div class="text-[9px] font-black uppercase text-slate-500 tracking-widest mb-1">Pick-up</div>
                <div class="text-sm font-bold uppercase">Heritage Station • Gate 1</div>
              </div>

              <div class="relative pl-10">
                <div class="absolute left-1.5 top-1.5 w-3 h-3 rounded-full bg-white/20"></div>
                <div class="text-[9px] font-black uppercase text-slate-500 tracking-widest mb-1">Destination</div>
                <div class="text-sm font-bold uppercase tracking-tight">The Imperial Haveli, Jaipur</div>
              </div>
            </div>
            
            <button class="w-full mt-10 py-5 rounded-2xl bg-[#f3c969] text-[#1a150e] font-black text-[10px] uppercase tracking-[0.3em] hover:bg-white transition-all">
              Live Map View
            </button>
          </div>

          <div class="bg-white rounded-[2.5rem] p-8 border border-slate-100 flex items-center justify-between">
            <div>
              <h4 class="text-[10px] font-black uppercase tracking-widest text-slate-400">WiFi Key</h4>
              <p class="text-sm font-bold mt-1">MAYBACH_GUEST</p>
            </div>
            <i class="fas fa-wifi text-[#f3c969]"></i>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue'

const cabin = reactive({
  temp: 21,
  mood: 'Classic'
})

const moods = ['Silent', 'Classic', 'Jazz', 'News']
</script>

<style scoped>
.font-serif { font-family: 'Playfair Display', serif; }

input[type=range] {
    appearance: none;
  -webkit-appearance: none;
  background: transparent;
}

input[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 4px;
  background: #f1f5f9;
  border-radius: 2px;
}

input[type=range]::-webkit-slider-thumb {
  -webkit-appearance: none;
  height: 20px;
  width: 20px;
  border-radius: 50%;
  background: #1a150e;
  border: 4px solid #f3c969;
  margin-top: -8px;
  cursor: pointer;
}
</style>
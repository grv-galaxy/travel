<!-- <template>
  <div class="flex h-screen bg-[#f8f7f4] overflow-hidden font-sans text-[#1a150e] selection:bg-[#f3c969]/30">
    
    <aside 
      :class="[
        'hidden md:flex flex-col bg-[#1a150e] text-white transition-all duration-700 ease-[cubic-bezier(0.23,1,0.32,1)] relative z-50',
        isExpanded ? 'w-80' : 'w-24'
      ]"
      @mousemove="handleTrail"
    >
      <canvas ref="trailCanvas" class="absolute inset-0 pointer-events-none opacity-30"></canvas>

      <div 
        class="absolute right-0 top-0 w-[1px] bg-[#f3c969] transition-all duration-1000 ease-in-out shadow-[0_0_15px_rgba(243,201,105,0.5)]"
        :style="{ height: isExpanded ? '100%' : '0%' }"
      ></div>

      <div class="h-32 flex items-center px-8 overflow-hidden">
        <button @click="toggleSidebar" class="flex items-center gap-6 group cursor-pointer outline-none">
          <div class="relative w-8 h-8 flex-shrink-0">
            <span :class="['absolute inset-0 border border-[#f3c969] transition-transform duration-700', isExpanded ? 'rotate-45 scale-110' : 'rotate-0']"></span>
            <span :class="['absolute inset-2 bg-[#f3c969] transition-all duration-700', isExpanded ? 'scale-0' : 'scale-100']"></span>
          </div>
          <div :class="['transition-all duration-500', isExpanded ? 'opacity-100 translate-x-0' : 'opacity-0 -translate-x-10']">
            <span class="text-[#f3c969] font-black text-[9px] uppercase tracking-[0.5em] block leading-none mb-1">Indoria</span>
            <span class="font-serif text-xl font-bold italic tracking-tight">Concierge</span>
          </div>
        </button>
      </div>

      <nav class="flex-1 px-4 py-6 space-y-2 overflow-hidden">
        <button 
          v-for="(item, index) in navItems" 
          :key="item.id"
          @click="selectItem(item.id)"
          @mouseenter="playHoverHaptic"
          :class="[
            'w-full flex items-center rounded-none transition-all duration-500 group relative py-4 outline-none',
            activeId === item.id ? 'text-[#f3c969]' : 'text-slate-500 hover:text-white'
          ]"
        >
          <div class="w-16 flex justify-center items-center shrink-0">
            <i :class="[item.icon, 'text-sm transition-transform duration-500 group-hover:scale-125']"></i>
          </div>
          <span 
            :class="['text-[10px] font-black uppercase tracking-[0.3em] transition-all duration-500 whitespace-nowrap', isExpanded ? 'opacity-100' : 'opacity-0 pointer-events-none']"
            :style="{ transitionDelay: isExpanded ? (index * 40) + 'ms' : '0ms' }"
          >
            {{ item.label }}
          </span>
          <div v-if="activeId === item.id" class="absolute left-0 w-[2px] h-6 bg-[#f3c969] shadow-[0_0_15px_#f3c969]"></div>
        </button>
      </nav>

      <div class="p-8 border-t border-white/5 overflow-hidden">
        <div class="flex items-center gap-5">
          <div class="w-8 h-8 rounded-full border border-[#f3c969]/30 flex items-center justify-center shrink-0">
            <i class="fas fa-crown text-[10px] text-[#f3c969]"></i>
          </div>
          <p :class="['text-[8px] font-black text-slate-500 uppercase tracking-widest transition-opacity duration-500', isExpanded ? 'opacity-100' : 'opacity-0']">
            Member <br/> <span class="text-white font-bold">VIP Elite</span>
          </p>
        </div>
      </div>
    </aside>

    <main class="flex-1 relative overflow-y-auto pb-32 md:pb-0 scrollbar-hide">
      <header class="sticky top-0 z-20 bg-[#f8f7f4]/90 backdrop-blur-xl px-8 md:px-12 py-8 flex justify-between items-center border-b border-slate-100">
        <div class="space-y-1">
          <span class="text-[#f3c969] text-[9px] font-black uppercase tracking-[0.4em] block">Exclusive Portfolio</span>
          <h3 class="font-serif text-2xl italic font-bold tracking-tight">{{ activeItem.label }}</h3>
        </div>
        <div class="flex items-center gap-6">
          <div class="hidden sm:block h-px w-12 bg-slate-200"></div>
          <div class="w-10 h-10 rounded-full border border-[#f3c969]/30 flex items-center justify-center bg-white shadow-sm">
             <i class="fas fa-fingerprint text-[#f3c969] text-xs"></i>
          </div>
        </div>
      </header>

      <section class="p-8 md:p-16">
        <transition name="page-reveal" mode="out-in">
          <div :key="activeId">
            <component :is="activeItem.component" />
          </div>
        </transition>
      </section>
    </main>

    <nav class="md:hidden fixed bottom-0 left-0 right-0 bg-[#1a150e] border-t border-[#f3c969]/20 z-50 px-4 pt-4 pb-8">
      <div class="flex items-center justify-between gap-2 overflow-x-auto scrollbar-hide">
        <button 
          v-for="item in navItems.slice(0, 3)" 
          :key="item.id"
          @click="selectItem(item.id)"
          :class="activeId === item.id ? 'text-[#f3c969]' : 'text-slate-500'"
          class="flex-1 flex flex-col items-center gap-2 min-w-[80px] outline-none"
        >
          <div :class="activeId === item.id ? 'bg-[#f3c969] text-[#1a150e]' : 'bg-white/5 text-slate-500'" class="w-10 h-10 rounded-xl flex items-center justify-center transition-all">
            <i :class="item.icon" class="text-xs"></i>
          </div>
          <span class="text-[8px] font-black uppercase tracking-widest">{{ item.label }}</span>
        </button>

        <button @click="showMoreMenu = true" class="flex-1 flex flex-col items-center gap-2 min-w-[80px] text-slate-500 outline-none">
          <div class="w-10 h-10 bg-white/5 rounded-xl flex items-center justify-center">
            <i class="fas fa-ellipsis-h text-xs"></i>
          </div>
          <span class="text-[8px] font-black uppercase tracking-widest">More</span>
        </button>
      </div>
    </nav>

    <transition name="drawer">
      <div v-if="showMoreMenu" class="md:hidden fixed inset-0 z-[60] bg-[#1a150e]/98 backdrop-blur-2xl p-12 flex flex-col">
        <div class="flex justify-between items-center mb-16">
          <span class="text-[#f3c969] font-black text-[10px] uppercase tracking-[0.4em]">Directory</span>
          <button @click="showMoreMenu = false" class="text-[#f3c969] text-2xl"><i class="fas fa-times"></i></button>
        </div>
        <div class="grid grid-cols-2 gap-6">
          <button 
            v-for="item in navItems.slice(3)" 
            :key="item.id"
            @click="selectItem(item.id); showMoreMenu = false"
            class="flex flex-col items-start gap-4 p-6 border border-white/5 bg-white/[0.02]"
          >
            <i :class="item.icon" class="text-[#f3c969] text-xl"></i>
            <span class="text-white text-[10px] font-black uppercase tracking-widest text-left">{{ item.label }}</span>
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, markRaw } from 'vue'
import Utrain from '../components/Utrain.vue'
import Uinsurance from './Uinsurance.vue'
import Upayment from './Upayment.vue'
import Uprivilege from './Uprivilege.vue'
import Udocuments from './Udocuments.vue'
import Ufleet from './Ufleet.vue'
import Uconcierge from './Uconcierge.vue'
import Ujourney from './Ujourney.vue'

const isExpanded = ref(false)
const activeId = ref('train')
const showMoreMenu = ref(false)
const trailCanvas = ref(null)

// Audio Engine
let audioCtx = null
const initAudio = () => { if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)() }
const playHaptic = (freq, dur, type) => {
  initAudio(); const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain()
  osc.type = type; osc.frequency.setValueAtTime(freq, audioCtx.currentTime)
  gain.gain.setValueAtTime(0.04, audioCtx.currentTime); gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + dur)
  osc.connect(gain); gain.connect(audioCtx.destination); osc.start(); osc.stop(audioCtx.currentTime + dur)
}
const playHoverHaptic = () => playHaptic(120, 0.1, 'triangle')
const playClickHaptic = () => playHaptic(700, 0.05, 'sine')

// Interaction Handlers
const toggleSidebar = () => { isExpanded.value = !isExpanded.value; playClickHaptic() }
const selectItem = (id) => { activeId.value = id; playClickHaptic() }
const handleTrail = (e) => {
  const canvas = trailCanvas.value; if (!canvas) return
  const ctx = canvas.getContext('2d'); const rect = canvas.getBoundingClientRect()
  const x = e.clientX - rect.left; const y = e.clientY - rect.top
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  const grad = ctx.createRadialGradient(x, y, 0, x, y, 120)
  grad.addColorStop(0, 'rgba(243, 201, 105, 0.12)'); grad.addColorStop(1, 'rgba(243, 201, 105, 0)')
  ctx.fillStyle = grad; ctx.fillRect(0, 0, canvas.width, canvas.height)
}

const navItems = [
  { 
    id: 'train', 
    icon: 'fas fa-train', 
    label: 'Rail Suite', 
    component: markRaw(Utrain) 
  },
  { 
    id: 'insurance', 
    icon: 'fas fa-umbrella', 
    label: 'Insurance', 
    component: markRaw(Uinsurance) 
  },
  { 
    id: 'history', 
    icon: 'fas fa-history', 
    label: 'Payments', 
    component: markRaw(Upayment)
  },
  { 
    id: 'rewards', 
    icon: 'fas fa-crown', 
    label: 'Privileges', 
    component: markRaw(Uprivilege)
  },
  { 
    id: 'visa', 
    icon: 'fas fa-passport', 
    label: 'Documents', 
    component: markRaw(Udocuments) 
    },
    { 
    id: 'fleet', 
    icon: 'fas fa-car-side', 
    label: 'Private Fleet', 
    component: markRaw(Ufleet) 
  },
  { 
    id: 'concierge', 
    icon: 'fas fa-comment-dots', 
    label: 'Live Butler', 
    component: markRaw(Uconcierge) 
  },
  { 
    id: 'itinerary', 
    icon: 'fas fa-map-marked-alt', 
    label: 'The Journey', 
    component: markRaw(Ujourney) 
  }
]

const activeItem = computed(() => navItems.find(i => i.id === activeId.value))

onMounted(() => {
  if (trailCanvas.value) { trailCanvas.value.width = 320; trailCanvas.value.height = window.innerHeight }
})
</script>

<style scoped>
.font-serif { font-family: 'Playfair Display', serif; }

/* Cinematic Transitions */
.page-reveal-enter-active { transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1); }
.page-reveal-enter-from { opacity: 0; transform: translateY(30px); filter: blur(10px); }
.page-reveal-leave-to { opacity: 0; transform: translateY(-20px); filter: blur(5px); }

.drawer-enter-active, .drawer-leave-active { transition: transform 0.8s cubic-bezier(0.19, 1, 0.22, 1); }
.drawer-enter-from, .drawer-leave-to { transform: translateY(100%); }

.scrollbar-hide::-webkit-scrollbar { display: none; }
.scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }

.animate-reveal { animation: reveal 1.2s cubic-bezier(0.23, 1, 0.32, 1) forwards; }
@keyframes reveal { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
</style> -->


















<template>
  <div class="flex h-screen bg-[#f8f7f4] overflow-hidden font-sans text-[#1a150e] selection:bg-[#f3c969]/30">
    
    <aside 
      :class="[
        'hidden md:flex flex-col bg-[#1a150e] text-white transition-all duration-700 ease-[cubic-bezier(0.23,1,0.32,1)] relative z-50',
        isExpanded ? 'w-80' : 'w-24'
      ]"
      @mousemove="handleTrail"
    >
      <canvas ref="trailCanvas" class="absolute inset-0 pointer-events-none opacity-30"></canvas>

      <div 
        class="absolute right-0 top-0 w-[1px] bg-[#f3c969] transition-all duration-1000 ease-in-out shadow-[0_0_15px_rgba(243,201,105,0.5)]"
        :style="{ height: isExpanded ? '100%' : '0%' }"
      ></div>

      <div class="h-32 flex items-center px-8 overflow-hidden">
        <button @click="toggleSidebar" class="flex items-center gap-6 group cursor-pointer outline-none">
          <div class="relative w-8 h-8 flex-shrink-0">
            <span :class="['absolute inset-0 border border-[#f3c969] transition-transform duration-700', isExpanded ? 'rotate-45 scale-110' : 'rotate-0']"></span>
            <span :class="['absolute inset-2 bg-[#f3c969] transition-all duration-700', isExpanded ? 'scale-0' : 'scale-100']"></span>
          </div>
          <div :class="['transition-all duration-500', isExpanded ? 'opacity-100 translate-x-0' : 'opacity-0 -translate-x-10']">
            <span class="text-[#f3c969] font-black text-[9px] uppercase tracking-[0.5em] block leading-none mb-1">Indoria</span>
            <span class="font-serif text-xl font-bold italic tracking-tight">Concierge</span>
          </div>
        </button>
      </div>

      <nav class="flex-1 px-4 py-6 space-y-2 overflow-hidden">
        <button 
          v-for="(item, index) in navItems" 
          :key="item.id"
          @click="selectItem(item.id)"
          @mouseenter="playHoverHaptic"
          :class="[
            'w-full flex items-center rounded-none transition-all duration-500 group relative py-4 outline-none',
            activeId === item.id ? 'text-[#f3c969]' : 'text-slate-500 hover:text-white'
          ]"
        >
          <div class="w-16 flex justify-center items-center shrink-0">
            <i :class="[item.icon, 'text-sm transition-transform duration-500 group-hover:scale-125']"></i>
          </div>
          <span 
            :class="['text-[10px] font-black uppercase tracking-[0.3em] transition-all duration-500 whitespace-nowrap', isExpanded ? 'opacity-100' : 'opacity-0 pointer-events-none']"
            :style="{ transitionDelay: isExpanded ? (index * 40) + 'ms' : '0ms' }"
          >
            {{ item.label }}
          </span>
          <div v-if="activeId === item.id" class="absolute left-0 w-[2px] h-6 bg-[#f3c969] shadow-[0_0_15px_#f3c969]"></div>
        </button>
      </nav>

      <div class="p-8 border-t border-white/5 overflow-hidden">
        <div class="flex items-center gap-5">
          <div class="w-8 h-8 rounded-full border border-[#f3c969]/30 flex items-center justify-center shrink-0">
            <i class="fas fa-crown text-[10px] text-[#f3c969]"></i>
          </div>
          <p :class="['text-[8px] font-black text-slate-500 uppercase tracking-widest transition-opacity duration-500', isExpanded ? 'opacity-100' : 'opacity-0']">
            Member <br/> <span class="text-white font-bold">VIP Elite</span>
          </p>
        </div>
      </div>
    </aside>

    <main class="flex-1 relative overflow-y-auto pb-32 md:pb-0 scrollbar-hide">
      <!-- <header class="sticky top-0 z-20 bg-[#f8f7f4]/90 backdrop-blur-xl px-8 md:px-12 py-8 flex justify-between items-center border-b border-slate-100">
        <div class="space-y-1">
          <span class="text-[#f3c969] text-[9px] font-black uppercase tracking-[0.4em] block">Exclusive Portfolio</span>
          <h3 class="font-serif text-2xl italic font-bold tracking-tight">{{ activeItem.label }}</h3>
        </div>
        <div class="flex items-center gap-6">
          <div class="hidden sm:block h-px w-12 bg-slate-200"></div>
          <div class="w-10 h-10 rounded-full border border-[#f3c969]/30 flex items-center justify-center bg-white shadow-sm">
             <i class="fas fa-fingerprint text-[#f3c969] text-xs"></i>
          </div>
        </div>
      </header> -->

      <section class="p-8 md:p-16">
        <transition name="page-reveal" mode="out-in">
          <div :key="activeId">
            <component :is="activeItem.component" />
          </div>
        </transition>
      </section>
    </main>

    <nav class="md:hidden fixed bottom-0 left-0 right-0 bg-[#1a150e] border-t border-[#f3c969]/20 z-50 px-4 pt-4 pb-8">
      <div class="flex items-center justify-between gap-2 overflow-x-auto scrollbar-hide">
        <button 
          v-for="item in navItems.slice(0, 3)" 
          :key="item.id"
          @click="selectItem(item.id)"
          :class="activeId === item.id ? 'text-[#f3c969]' : 'text-slate-500'"
          class="flex-1 flex flex-col items-center gap-2 min-w-[80px] outline-none"
        >
          <div :class="activeId === item.id ? 'bg-[#f3c969] text-[#1a150e]' : 'bg-white/5 text-slate-500'" class="w-10 h-10 rounded-xl flex items-center justify-center transition-all">
            <i :class="item.icon" class="text-xs"></i>
          </div>
          <span class="text-[8px] font-black uppercase tracking-widest">{{ item.label }}</span>
        </button>

        <button @click="showMoreMenu = true" class="flex-1 flex flex-col items-center gap-2 min-w-[80px] text-slate-500 outline-none">
          <div class="w-10 h-10 bg-white/5 rounded-xl flex items-center justify-center">
            <i class="fas fa-ellipsis-h text-xs"></i>
          </div>
          <span class="text-[8px] font-black uppercase tracking-widest">More</span>
        </button>
      </div>
    </nav>

    <transition name="drawer">
      <div v-if="showMoreMenu" class="md:hidden fixed inset-0 z-[60] bg-[#1a150e]/98 backdrop-blur-2xl p-12 flex flex-col">
        <div class="flex justify-between items-center mb-16">
          <span class="text-[#f3c969] font-black text-[10px] uppercase tracking-[0.4em]">Directory</span>
          <button @click="showMoreMenu = false" class="text-[#f3c969] text-2xl"><i class="fas fa-times"></i></button>
        </div>
        <div class="grid grid-cols-2 gap-6">
          <button 
            v-for="item in navItems.slice(3)" 
            :key="item.id"
            @click="selectItem(item.id); showMoreMenu = false"
            class="flex flex-col items-start gap-4 p-6 border border-white/5 bg-white/[0.02]"
          >
            <i :class="item.icon" class="text-[#f3c969] text-xl"></i>
            <span class="text-white text-[10px] font-black uppercase tracking-widest text-left">{{ item.label }}</span>
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, markRaw } from 'vue'
import Utrain from '../components/Utrain.vue'
import Uinsurance from './Uinsurance.vue'
import Upayment from './Upayment.vue'
import Uprivilege from './Uprivilege.vue'
import Udocuments from './Udocuments.vue'
import Ufleet from './Ufleet.vue'
import Uconcierge from './Uconcierge.vue'
import Ujourney from './Ujourney.vue'

const isExpanded = ref(false)
const activeId = ref('train')
const showMoreMenu = ref(false)
const trailCanvas = ref(null)

// Audio Engine
let audioCtx = null
const initAudio = () => { if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)() }
const playHaptic = (freq, dur, type) => {
  initAudio(); const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain()
  osc.type = type; osc.frequency.setValueAtTime(freq, audioCtx.currentTime)
  gain.gain.setValueAtTime(0.04, audioCtx.currentTime); gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + dur)
  osc.connect(gain); gain.connect(audioCtx.destination); osc.start(); osc.stop(audioCtx.currentTime + dur)
}
const playHoverHaptic = () => playHaptic(120, 0.1, 'triangle')
const playClickHaptic = () => playHaptic(700, 0.05, 'sine')

// Interaction Handlers
const toggleSidebar = () => { isExpanded.value = !isExpanded.value; playClickHaptic() }
const selectItem = (id) => { activeId.value = id; playClickHaptic() }
const handleTrail = (e) => {
  const canvas = trailCanvas.value; if (!canvas) return
  const ctx = canvas.getContext('2d'); const rect = canvas.getBoundingClientRect()
  const x = e.clientX - rect.left; const y = e.clientY - rect.top
  ctx.clearRect(0, 0, canvas.width, canvas.height)
  const grad = ctx.createRadialGradient(x, y, 0, x, y, 120)
  grad.addColorStop(0, 'rgba(243, 201, 105, 0.12)'); grad.addColorStop(1, 'rgba(243, 201, 105, 0)')
  ctx.fillStyle = grad; ctx.fillRect(0, 0, canvas.width, canvas.height)
}

const navItems = [
  { 
    id: 'train', 
    icon: 'fas fa-train', 
    label: 'Rail Suite', 
    component: markRaw(Utrain) 
  },
  { 
    id: 'insurance', 
    icon: 'fas fa-umbrella', 
    label: 'Insurance', 
    component: markRaw(Uinsurance) 
  },
  { 
    id: 'history', 
    icon: 'fas fa-history', 
    label: 'Payments', 
    component: markRaw(Upayment)
  },
  { 
    id: 'rewards', 
    icon: 'fas fa-crown', 
    label: 'Privileges', 
    component: markRaw(Uprivilege)
  },
  { 
    id: 'visa', 
    icon: 'fas fa-passport', 
    label: 'Documents', 
    component: markRaw(Udocuments) 
    },
    { 
    id: 'fleet', 
    icon: 'fas fa-car-side', 
    label: 'Private Fleet', 
    component: markRaw(Ufleet) 
  },
  { 
    id: 'concierge', 
    icon: 'fas fa-comment-dots', 
    label: 'Live Butler', 
    component: markRaw(Uconcierge) 
  },
  { 
    id: 'itinerary', 
    icon: 'fas fa-map-marked-alt', 
    label: 'The Journey', 
    component: markRaw(Ujourney) 
  }
]

const activeItem = computed(() => navItems.find(i => i.id === activeId.value))

onMounted(() => {
  if (trailCanvas.value) { trailCanvas.value.width = 320; trailCanvas.value.height = window.innerHeight }
})
</script>

<style scoped>
.font-serif { font-family: 'Playfair Display', serif; }

/* Cinematic Transitions */
.page-reveal-enter-active { transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1); }
.page-reveal-enter-from { opacity: 0; transform: translateY(30px); filter: blur(10px); }
.page-reveal-leave-to { opacity: 0; transform: translateY(-20px); filter: blur(5px); }

.drawer-enter-active, .drawer-leave-active { transition: transform 0.8s cubic-bezier(0.19, 1, 0.22, 1); }
.drawer-enter-from, .drawer-leave-to { transform: translateY(100%); }

.scrollbar-hide::-webkit-scrollbar { display: none; }
.scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }

.animate-reveal { animation: reveal 1.2s cubic-bezier(0.23, 1, 0.32, 1) forwards; }
@keyframes reveal { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
</style>
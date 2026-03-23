<template>
  <div class="min-h-screen bg-[#f8f7f4] pb-32 font-sans text-[#1a150e]">
    <header class="bg-[#1a150e] text-white pt-40 pb-32 text-center relative overflow-hidden border-b border-[#f3c969]/20">
      <div class="absolute inset-0 opacity-10 pointer-events-none">
        <svg class="absolute top-0 left-0 w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="none">
          <pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse">
            <path d="M 10 0 L 0 0 0 10" fill="none" stroke="#f3c969" stroke-width="0.1"/>
          </pattern>
          <rect width="100" height="100" fill="url(#grid)" />
        </svg>
      </div>
      
      <div class="relative z-10 container mx-auto px-4">
        <div class="flex items-center justify-center gap-4 mb-8">
          <div class="h-px w-12 bg-[#f3c969]/50"></div>
          <span class="text-[#f3c969] font-black text-[11px] uppercase tracking-[0.4em]">The Art of Travel</span>
          <div class="h-px w-12 bg-[#f3c969]/50"></div>
        </div>
        
        <h1 class="font-serif text-5xl md:text-7xl font-bold mb-8 tracking-tight leading-tight">
          Curate Your <span class="italic text-[#f3c969]">Private</span> Escape
        </h1>
        <p class="text-slate-400 font-medium max-w-xl mx-auto text-lg leading-relaxed italic">
          "Expertly crafted itineraries for the discerning voyager."
        </p>
      </div>
    </header>

    <div class="max-w-5xl mx-auto px-4">
      <section class="-mt-16 relative z-20 mb-20">
        <div class="flex justify-center items-center gap-0 md:gap-4">
          <div v-for="n in 3" :key="n" class="flex items-center group">
            <div class="flex flex-col items-center gap-3">
              <div 
                :class="currentStep >= n ? 'bg-[#f3c969] text-[#1a150e] shadow-[0_0_20px_rgba(243,201,105,0.4)]' : 'bg-[#1a150e] text-slate-500 border border-slate-700'"
                class="w-12 h-12 rounded-full flex items-center justify-center font-serif italic text-lg transition-all duration-700"
              >
                {{ n }}
              </div>
              <span :class="currentStep >= n ? 'text-[#1a150e] font-bold opacity-100' : 'text-slate-400 opacity-50'" class="text-[9px] uppercase tracking-[0.2em] transition-all">
                {{ stepLabels[n-1] }}
              </span>
            </div>
            <div v-if="n < 3" :class="currentStep > n ? 'bg-[#f3c969]' : 'bg-slate-200'" class="w-12 md:w-24 h-[1px] mx-4 mt-[-20px] transition-all duration-1000"></div>
          </div>
        </div>
      </section>

      <main class="bg-white rounded-none md:rounded-lg p-10 md:p-20 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.1)] border-t-[6px] border-[#1a150e] relative overflow-hidden">
        <div class="absolute top-0 right-0 w-32 h-32 opacity-5 pointer-events-none">
          <i class="fas fa-feather-alt text-8xl rotate-45"></i>
        </div>

        <form @submit.prevent="nextStep">
          <div v-if="currentStep === 1" class="space-y-12 animate-in">
            <div class="text-center space-y-2">
              <h3 class="font-serif text-4xl font-bold text-[#1a150e]">The Canvas</h3>
              <p class="text-slate-400 text-sm italic font-medium">Define the geography of your next adventure</p>
            </div>

            <div class="space-y-4">
              <label :class="labelStyle">Dream Destination</label>
              <input type="text" v-model="form.destination" placeholder="Where does your heart lead?" :class="inputStyle" />
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
              <div class="space-y-4">
                <label :class="labelStyle">Departure Window</label>
                <input type="date" v-model="form.startDate" :min="today" :class="inputStyle" />
              </div>
              <div class="space-y-4">
                <label :class="labelStyle">Length of Stay</label>
                <div class="flex items-center border-b border-slate-200 focus-within:border-[#f3c969] transition-all">
                  <input type="number" v-model="form.duration" class="w-full py-4 bg-transparent font-serif text-xl outline-none" />
                  <span class="text-slate-400 text-xs uppercase tracking-widest font-bold">Days</span>
                </div>
              </div>
            </div>
          </div>

          <div v-if="currentStep === 2" class="space-y-12 animate-in">
            <div class="text-center space-y-2">
              <h3 class="font-serif text-4xl font-bold text-[#1a150e]">The Signature</h3>
              <p class="text-slate-400 text-sm italic font-medium">Tailoring the pace and texture of your journey</p>
            </div>

            <div class="space-y-6">
              <label :class="labelStyle">Curation Style</label>
              <div class="grid grid-cols-2 md:grid-cols-5 gap-3">
                <button 
                  type="button" v-for="style in styles" :key="style" 
                  @click="form.style = style"
                  :class="form.style === style ? 'bg-[#1a150e] text-[#f3c969] border-[#1a150e]' : 'bg-transparent text-slate-400 border-slate-200 hover:border-slate-400'"
                  class="py-4 border text-[10px] font-black uppercase tracking-widest transition-all"
                >
                  {{ style }}
                </button>
              </div>
            </div>

            <div class="space-y-10 pt-6">
              <div class="flex justify-between items-end">
                <label :class="labelStyle">Estimated Investment</label>
                <span class="font-serif text-2xl text-[#1a150e]">₹{{ Number(form.budget).toLocaleString() }}</span>
              </div>
              <input type="range" v-model="form.budget" min="20000" max="1000000" step="10000" class="luxe-slider" />
              <div class="flex justify-between text-[10px] text-slate-300 font-bold uppercase tracking-widest">
                <span>Standard</span>
                <span>Ultra-Luxury</span>
              </div>
            </div>
          </div>

          <div v-if="currentStep === 3" class="space-y-12 animate-in">
             <div class="text-center space-y-2">
              <h3 class="font-serif text-4xl font-bold text-[#1a150e]">The Hand-off</h3>
              <p class="text-slate-400 text-sm italic font-medium">Finalize your bespoke request with our curators</p>
            </div>

            <div class="space-y-4">
              <label :class="labelStyle">Special Requests & Nuances</label>
              <textarea v-model="form.notes" rows="3" placeholder="Dietary preferences, accessibility, or milestone celebrations..." :class="inputStyle"></textarea>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
              <div class="space-y-4">
                <label :class="labelStyle">Legal Name</label>
                <input type="text" v-model="form.userName" :class="inputStyle" />
              </div>
              <div class="space-y-4">
                <label :class="labelStyle">Private Contact (WhatsApp)</label>
                <input type="tel" v-model="form.phone" :class="inputStyle" />
              </div>
            </div>
          </div>

          <div class="flex flex-col md:flex-row items-center justify-between gap-8 mt-16 pt-10 border-t border-slate-100">
            <button 
              v-if="currentStep > 1" 
              type="button" 
              @click="currentStep--" 
              class="text-slate-400 hover:text-[#1a150e] font-black text-xs uppercase tracking-[0.3em] transition-all cursor-pointer"
            >
              ← Previous
            </button>
            <div v-else></div>

            <button 
              type="submit" 
              class="group relative overflow-hidden bg-[#1a150e] text-[#f3c969] px-16 py-6 font-black text-xs uppercase tracking-[0.3em] transition-all hover:pr-20"
            >
              <span class="relative z-10">{{ currentStep === 3 ? 'Finalize Portfolio' : 'Next Chapter' }}</span>
              <i class="fas fa-arrow-right absolute right-6 top-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 transition-all"></i>
            </button>
          </div>
        </form>
      </main>

      <section class="flex flex-col md:flex-row justify-between gap-12 mt-24 px-10">
        <div v-for="trust in trustItems" :key="trust.label" class="flex items-start gap-6 group">
          <i :class="trust.icon" class="text-2xl text-[#f3c969]/40 group-hover:text-[#f3c969] transition-colors"></i>
          <div>
            <h5 class="font-black text-[10px] uppercase tracking-[0.2em] mb-1">{{ trust.label }}</h5>
            <p class="text-slate-400 text-xs leading-relaxed">Dedicated human expertise for every detail.</p>
          </div>
        </div>
      </section>
    </div>

    <Transition name="fade">
      <div v-if="showSuccess" class="fixed inset-0 z-[100] flex items-center justify-center bg-[#1a150e]/98 backdrop-blur-xl">
        <div class="text-center space-y-8 p-6 max-w-xl">
          <div class="inline-block relative">
            <div class="absolute inset-0 bg-[#f3c969] blur-2xl opacity-20 animate-pulse"></div>
            <i class="fas fa-envelope-open-text text-6xl text-[#f3c969] relative"></i>
          </div>
          <h2 class="font-serif text-5xl text-white">The Journey Begins</h2>
          <p class="text-slate-400 text-lg italic leading-relaxed">
            "We have received your request. A personal travel designer will contact you within the next 24 hours to present a vision of your journey."
          </p>
          <div class="h-px w-24 bg-[#f3c969] mx-auto opacity-30"></div>
          <button @click="showSuccess = false" class="text-[#f3c969] font-black text-[10px] uppercase tracking-[0.5em] hover:tracking-[0.6em] transition-all">
            Return to Gallery
          </button>
        </div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const labelStyle = "block text-[10px] font-black uppercase tracking-[0.3em] text-[#1a150e]/50 ml-1"
const inputStyle = "w-full py-4 bg-transparent border-b border-slate-200 font-serif text-xl text-[#1a150e] placeholder:text-slate-200 focus:border-[#f3c969] focus:outline-none transition-all duration-500"

const currentStep = ref(1)
const showSuccess = ref(false)
const today = new Date().toISOString().split('T')[0]
const stepLabels = ['Vision', 'Vibe', 'Contact']
const styles = ['Relaxed', 'Adventure', 'Heritage', 'Romance', 'Family']

const trustItems = [
  { icon: 'fas fa-shield-alt', label: 'Private Curation' },
  { icon: 'fas fa-gem', label: 'Bespoke Assets' },
  { icon: 'fas fa-concierge-bell', label: 'Elite Support' }
]

const form = reactive({
  destination: '',
  startDate: '',
  duration: 7,
  style: 'Heritage',
  hotelType: 'Boutique / Heritage',
  budget: 150000,
  notes: '',
  userName: '',
  phone: ''
})

const nextStep = () => {
  if (currentStep.value < 3) {
    currentStep.value++
    window.scrollTo({ top: 0, behavior: 'smooth' })
  } else {
    showSuccess.value = true
  }
}
</script>

<style scoped>
.font-serif {
  font-family: 'Playfair Display', Georgia, serif;
}

.luxe-slider {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 100%;
  height: 2px;
  background: #f1f5f9;
  outline: none;
}

.luxe-slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  width: 20px;
  height: 20px;
  background: #1a150e;
  border: 2px solid #f3c969;
  cursor: pointer;
  border-radius: 50%;
  transition: all 0.3s;
}

.luxe-slider::-webkit-slider-thumb:hover {
  transform: scale(1.2);
  box-shadow: 0 0 15px rgba(243,201,105,0.4);
}

.animate-in {
  animation: luxeFadeUp 1s cubic-bezier(0.19, 1, 0.22, 1) forwards;
}

@keyframes luxeFadeUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.fade-enter-active, .fade-leave-active { transition: all 0.8s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; transform: scale(1.05); }
</style>
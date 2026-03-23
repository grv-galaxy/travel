<template>
  <div class="min-h-screen bg-[#fafaf9] pb-32 font-sans text-[#1a150e]">
    
    <div :class="[
      'py-3 px-6 text-center transition-all duration-700',
      hasActiveInsurance ? 'bg-emerald-50 text-emerald-700' : 'bg-[#f3c969]/10 text-[#1a150e]'
    ]">
      <div class="max-w-6xl mx-auto flex items-center justify-center gap-3">
        <i :class="hasActiveInsurance ? 'fas fa-shield-check' : 'fas fa-exclamation-circle'"></i>
        <span class="text-[10px] font-black uppercase tracking-[0.2em]">
          {{ hasActiveInsurance ? 'You are currently protected under Premium Plus' : 'No active insurance found for your current itinerary' }}
        </span>
        <button v-if="!hasActiveInsurance" @click="scrollToPlans" class="ml-4 text-[10px] font-black uppercase border-b border-[#1a150e]">Secure Protection Now</button>
      </div>
    </div>

    <header class="bg-[#1a150e] text-white pt-24 pb-20 text-center relative overflow-hidden">
      <div class="absolute inset-0 opacity-5 pointer-events-none">
        <i class="fas fa-umbrella text-[300px] absolute -top-10 -right-10 rotate-12"></i>
      </div>

      <div class="relative z-10 container mx-auto px-4">
        <div class="inline-block border border-[#f3c969]/30 text-[#f3c969] px-4 py-1.5 rounded-full font-black text-[9px] uppercase tracking-[0.3em] mb-6">
          Global Indemnity
        </div>
        <h1 class="font-serif text-4xl md:text-6xl font-bold mb-6 tracking-tight">
          Travel Safe, Travel <span class="text-[#f3c969]">Smart</span>
        </h1>
        <p class="text-slate-400 font-medium max-w-2xl mx-auto text-base md:text-lg">
          Bespoke coverage for medical emergencies, heritage protection, and journey interruptions.
        </p>
      </div>
    </header>

    <div class="max-w-6xl mx-auto px-4">
      <section class="-mt-12 relative z-20 mb-24">
        <div class="bg-white p-8 md:p-10 rounded-3xl shadow-2xl shadow-[#1a150e]/5 border border-slate-100">
          <div class="flex items-center gap-4 mb-8">
             <div class="w-10 h-10 rounded-full bg-[#fcf9f4] flex items-center justify-center text-[#f3c969]">
               <i class="fas fa-calculator"></i>
             </div>
             <h3 class="font-serif text-2xl font-bold">Premium Estimator</h3>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-4 gap-8 items-end">
            <div class="space-y-3">
              <label :class="labelStyle">Region</label>
              <select v-model="quote.type" :class="inputStyle">
                <option value="domestic">Domestic (India)</option>
                <option value="international">International</option>
              </select>
            </div>
            <div class="space-y-3">
              <label :class="labelStyle">Travelers</label>
              <input type="number" v-model="quote.members" min="1" max="10" :class="inputStyle">
            </div>
            <div class="space-y-3">
              <label :class="labelStyle">Duration (Days)</label>
              <input type="number" v-model="quote.days" min="1" :class="inputStyle">
            </div>
            <div class="bg-[#fcf9f4] p-5 rounded-2xl border border-[#f3c969]/10 text-center">
              <span class="block text-[9px] font-black text-slate-400 uppercase tracking-widest mb-1">Total Premium</span>
              <span class="text-3xl font-black text-[#1a150e]">₹{{ calculatedPrice }}<span class="text-sm text-[#f3c969] ml-1">*</span></span>
            </div>
          </div>
        </div>
      </section>

      <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-12 mb-32">
        <div v-for="benefit in benefits" :key="benefit.title" class="group">
          <div class="w-14 h-14 bg-[#1a150e] text-[#f3c969] rounded-2xl flex items-center justify-center mb-6 text-xl shadow-lg group-hover:scale-110 transition-transform duration-500">
            <i :class="benefit.icon"></i>
          </div>
          <h4 class="font-serif text-lg font-bold mb-3">{{ benefit.title }}</h4>
          <p class="text-xs text-slate-500 leading-relaxed">{{ benefit.desc }}</p>
        </div>
      </section>

      <section id="plans" class="mb-32">
        <div class="text-center mb-16">
          <span class="text-[#f3c969] text-[10px] font-black uppercase tracking-[0.4em]">Comparison</span>
          <h2 class="font-serif text-4xl font-bold mt-2">Coverage Portfolios</h2>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-10 max-w-4xl mx-auto">
          <div class="bg-white p-10 rounded-[2rem] border border-slate-200 flex flex-col hover:shadow-xl transition-all duration-500">
            <div class="mb-8">
              <h3 class="font-serif text-xl font-bold text-slate-400 uppercase tracking-widest mb-4">Essential</h3>
              <div class="text-5xl font-black text-[#1a150e]">₹49<span class="text-base text-slate-400 font-medium ml-1">/day</span></div>
            </div>
            <ul class="space-y-5 mb-12 flex-grow">
              <li v-for="f in features.essential" :key="f" class="flex items-center gap-4 text-xs font-bold text-slate-600">
                <i class="fas fa-check text-emerald-500"></i> {{ f }}
              </li>
              <li v-for="f in features.excluded" :key="f" class="flex items-center gap-4 text-xs font-bold text-slate-300 line-through">
                <i class="fas fa-times"></i> {{ f }}
              </li>
            </ul>
            <button @click="purchase('Essential')" class="w-full py-5 rounded-xl border-2 border-slate-100 font-black text-[10px] uppercase tracking-[0.2em] hover:bg-[#1a150e] hover:text-white transition-all cursor-pointer">
              Purchase Essential
            </button>
          </div>

          <div class="bg-[#1a150e] p-10 rounded-[2rem] border-2 border-[#f3c969] shadow-2xl relative flex flex-col md:scale-105">
            <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#f3c969] text-[#1a150e] px-6 py-1.5 rounded-full font-black text-[9px] uppercase tracking-widest">
              Most Selected
            </div>
            <div class="mb-8">
              <h3 class="font-serif text-xl font-bold text-[#f3c969] uppercase tracking-widest mb-4">Premium Plus</h3>
              <div class="text-5xl font-black text-white">₹99<span class="text-base text-slate-500 font-medium ml-1">/day</span></div>
            </div>
            <ul class="space-y-5 mb-12 flex-grow text-slate-300">
              <li v-for="f in [...features.essential, ...features.excluded]" :key="f" class="flex items-center gap-4 text-xs font-bold">
                <i class="fas fa-check text-[#f3c969]"></i> {{ f }}
              </li>
            </ul>
            <button @click="purchase('Premium Plus')" class="w-full py-5 rounded-xl bg-[#f3c969] text-[#1a150e] font-black text-[10px] uppercase tracking-[0.2em] shadow-lg shadow-[#f3c969]/20 hover:bg-white transition-all cursor-pointer">
              Purchase Premium
            </button>
          </div>
        </div>
      </section>

      <section class="bg-white rounded-[2.5rem] p-8 md:p-16 border border-slate-100 shadow-sm flex flex-col lg:flex-row items-center justify-between gap-12">
        <div class="max-w-md text-center lg:text-left">
          <h2 class="font-serif text-3xl font-bold mb-6">Need Assistance?</h2>
          <p class="text-slate-500 text-sm leading-relaxed mb-8">Our luxury concierge team is available 24/7 to handle your claims and emergency travel requirements.</p>
          <div class="flex flex-wrap justify-center lg:justify-start gap-6">
            <div class="flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              <span class="text-[10px] font-black uppercase tracking-widest">Claims Live</span>
            </div>
            <div class="flex items-center gap-2">
              <span class="w-2 h-2 rounded-full bg-[#f3c969]"></span>
              <span class="text-[10px] font-black uppercase tracking-widest">24/7 Concierge</span>
            </div>
          </div>
        </div>
        <div class="flex flex-col items-center">
           <a href="tel:1800-INDORIA" class="bg-[#1a150e] text-[#f3c969] px-10 py-6 rounded-2xl font-black text-xl md:text-2xl shadow-xl hover:-translate-y-1 transition-transform no-underline">
              1800-INDORIA
           </a>
           <p class="mt-4 text-[9px] font-black text-slate-400 uppercase tracking-[0.3em]">International Helpline</p>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { reactive, computed, ref } from 'vue'

// UI Styles
const labelStyle = "block text-[9px] font-black uppercase tracking-[0.2em] text-slate-500 ml-1"
const inputStyle = "w-full p-4 rounded-xl border border-slate-100 bg-slate-50 text-sm font-bold text-[#1a150e] focus:border-[#f3c969] focus:bg-white focus:outline-none transition-all outline-none"

// State
const hasActiveInsurance = ref(false) // Toggle this to see 'Active' state
const quote = reactive({ type: 'domestic', members: 1, days: 7 })

const benefits = [
  { icon: 'fas fa-hospital-user', title: 'Global Medical', desc: 'Direct settlement with 10,000+ elite hospitals across the globe.' },
  { icon: 'fas fa-suitcase-rolling', title: 'Baggage Care', desc: 'Concierge-led support for lost, damaged, or delayed belongings.' },
  { icon: 'fas fa-calendar-times', title: 'Trip Interrupt', desc: 'Full refunds for non-refundable heritage hotel and rail bookings.' },
  { icon: 'fas fa-concierge-bell', title: '24/7 Priority', desc: 'Access to a dedicated emergency concierge for immediate help.' }
]

const features = {
  essential: ['Medical Cover (Up to 5L)', 'Baggage Loss (Up to 20k)', 'Accidental Cover'],
  excluded: ['100% Trip Cancellation', 'Flight Delay Indemnity', 'Adventure Sports Cover']
}

// Logic
const calculatedPrice = computed(() => {
  const base = quote.type === 'domestic' ? 49 : 199
  return base * quote.members * quote.days
})

const scrollToPlans = () => {
  document.getElementById('plans')?.scrollIntoView({ behavior: 'smooth' })
}

const purchase = (plan) => {
  alert(`Initializing secure payment for ${plan} Portfolio...`)
  // Link to your payment gateway here
}
</script>

<style scoped>
.font-serif { font-family: 'Playfair Display', serif; }

select {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%23f3c969' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M6 8l4 4 4-4'/%3e%3c/svg%3e");
  background-position: right 1rem center;
  background-repeat: no-repeat;
  background-size: 1.2em 1.2em;
  appearance: none;
}
</style>
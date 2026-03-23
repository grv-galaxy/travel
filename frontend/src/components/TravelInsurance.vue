<template>
  <div class="min-h-screen bg-[#fafaf9] pb-20 font-sans text-[#1a150e]">
    <header class="bg-[#1a150e] text-white pt-32 pb-24 text-center relative overflow-hidden">
      <div class="absolute inset-0 opacity-10">
        <i class="fas fa-shield-alt text-[250px] absolute -top-10 -left-10 rotate-12"></i>
      </div>
      <div class="relative z-10 container mx-auto px-4">
        <div class="inline-block bg-[#f3c969] text-[#1a150e] px-4 py-1.5 rounded-full font-black text-[10px] uppercase tracking-[0.2em] mb-6 shadow-lg shadow-[#f3c969]/20">
          Peace of Mind
        </div>
        <h1 class="font-serif text-4xl md:text-6xl font-bold mb-6 tracking-tight">
          Travel Safe, Travel <span class="text-[#f3c969]">Smart</span>
        </h1>
        <p class="text-slate-400 font-medium max-w-2xl mx-auto text-lg">
          Bespoke coverage for medical emergencies, heritage protection, and journey interruptions.
        </p>
      </div>
    </header>

    <div class="max-w-6xl mx-auto px-4">
      <section class="-mt-16 relative z-20 mb-20">
        <div class="bg-white p-8 md:p-10 rounded-3xl shadow-2xl shadow-[#1a150e]/5 border border-slate-100">
          <h3 class="font-serif text-2xl font-bold mb-8 flex items-center gap-3">
             <i class="fas fa-calculator text-[#f3c969]"></i> Instant Premium Quote
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-4 gap-8 items-end">
            <div class="space-y-3">
              <label :class="labelStyle">Region</label>
              <select v-model="quote.type" :class="inputStyle" class="appearance-none cursor-pointer">
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
            <div class="bg-[#fcf9f4] p-4 rounded-2xl border border-[#f3c969]/10 text-center">
              <span class="block text-[10px] font-bold text-slate-400 uppercase tracking-widest mb-1">Estimated Premium</span>
              <span class="text-3xl font-black text-[#1a150e]">₹{{ calculatedPrice }}<span class="text-sm text-[#f3c969] ml-1">*</span></span>
            </div>
          </div>
          <div class="mt-8 flex flex-col md:flex-row justify-between items-center gap-4">
            <p class="text-[11px] text-slate-400 italic leading-relaxed max-w-lg">
              *Calculated premium is based on standard age groups and heritage destination safety ratings. Final pricing may vary upon document verification.
            </p>
            <button @click="scrollToPlans" class="w-full md:w-auto px-10 py-4 bg-[#1a150e] text-[#f3c969] font-black rounded-xl uppercase tracking-widest text-xs hover:shadow-xl hover:shadow-[#f3c969]/10 transition-all cursor-pointer border border-[#f3c969]/30">
              Select Your Plan
            </button>
          </div>
        </div>
      </section>

      <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-10 mb-24">
        <div v-for="benefit in benefits" :key="benefit.title" class="text-center group">
          <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center mx-auto mb-6 text-2xl text-[#f3c969] shadow-sm border border-slate-100 group-hover:bg-[#f3c969] group-hover:text-white transition-all duration-500">
            <i :class="benefit.icon"></i>
          </div>
          <h4 class="font-serif text-lg font-bold mb-3 text-[#1a150e]">{{ benefit.title }}</h4>
          <p class="text-sm text-slate-500 leading-relaxed px-4">{{ benefit.desc }}</p>
        </div>
      </section>

      <section id="plans" class="mb-24">
        <h2 class="text-center font-serif text-4xl font-bold mb-16">Exclusive Coverage <span class="text-[#f3c969]">Portfolios</span></h2>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-10 max-w-4xl mx-auto">
          <div class="bg-white p-10 rounded-3xl border border-slate-200 shadow-sm flex flex-col hover:border-[#f3c969]/30 transition-all">
            <div class="mb-8">
              <h3 class="font-serif text-2xl font-bold mb-2">Essential</h3>
              <div class="text-4xl font-black text-[#1a150e]">₹49<span class="text-sm text-slate-400 font-medium ml-1">/day</span></div>
            </div>
            <ul class="space-y-4 mb-10 flex-grow">
              <li class="flex items-center gap-3 text-sm font-medium"><i class="fas fa-check-circle text-emerald-500"></i> Medical Cover (Up to 5L)</li>
              <li class="flex items-center gap-3 text-sm font-medium"><i class="fas fa-check-circle text-emerald-500"></i> Lost Baggage (Up to 20k)</li>
              <li class="flex items-center gap-3 text-sm font-medium"><i class="fas fa-check-circle text-emerald-500"></i> Accidental Cover</li>
              <li class="flex items-center gap-3 text-sm font-medium text-slate-300 line-through"><i class="fas fa-times-circle"></i> Trip Cancellation</li>
              <li class="flex items-center gap-3 text-sm font-medium text-slate-300 line-through"><i class="fas fa-times-circle"></i> Adventure Sports</li>
            </ul>
            <button class="w-full py-4 rounded-xl border-2 border-slate-100 font-black text-xs uppercase tracking-widest text-slate-400 hover:border-[#1a150e] hover:text-[#1a150e] transition-all cursor-pointer">Initialize Essential</button>
          </div>

          <div class="bg-[#1a150e] p-10 rounded-3xl border-2 border-[#f3c969] shadow-2xl shadow-[#f3c969]/10 relative flex flex-col transform md:scale-105">
            <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#f3c969] text-[#1a150e] px-6 py-1 rounded-full font-black text-[10px] uppercase tracking-widest">
              Most Selected
            </div>
            <div class="mb-8">
              <h3 class="font-serif text-2xl font-bold mb-2 text-white">Premium Plus</h3>
              <div class="text-4xl font-black text-[#f3c969]">₹99<span class="text-sm text-slate-400 font-medium ml-1">/day</span></div>
            </div>
            <ul class="space-y-4 mb-10 flex-grow text-slate-300">
              <li class="flex items-center gap-3 text-sm font-medium"><i class="fas fa-check-circle text-[#f3c969]"></i> Medical Cover (Up to 25L)</li>
              <li class="flex items-center gap-3 text-sm font-medium"><i class="fas fa-check-circle text-[#f3c969]"></i> Global Baggage Support</li>
              <li class="flex items-center gap-3 text-sm font-medium"><i class="fas fa-check-circle text-[#f3c969]"></i> 100% Cancellation Refund</li>
              <li class="flex items-center gap-3 text-sm font-medium"><i class="fas fa-check-circle text-[#f3c969]"></i> Flight Delay Indemnity</li>
              <li class="flex items-center gap-3 text-sm font-medium"><i class="fas fa-check-circle text-[#f3c969]"></i> Adventure Sports Cover</li>
            </ul>
            <button class="w-full py-4 rounded-xl bg-[#f3c969] text-[#1a150e] font-black text-xs uppercase tracking-widest shadow-lg shadow-[#f3c969]/20 transition-all cursor-pointer">Initialize Premium</button>
          </div>
        </div>
      </section>

      <section class="bg-[#1a150e] rounded-[40px] overflow-hidden relative border border-[#f3c969]/20 shadow-2xl">
        <div class="absolute right-0 bottom-0 opacity-10 pointer-events-none">
          <i class="fas fa-file-invoice-dollar text-[300px] text-[#f3c969]"></i>
        </div>
        <div class="p-10 md:p-16 flex flex-col lg:flex-row justify-between items-center gap-12 relative z-10">
          <div class="max-w-xl text-center lg:text-left">
            <h2 class="font-serif text-3xl md:text-4xl font-bold text-white mb-6">Seamless <span class="text-[#f3c969]">3-Step</span> Settlement</h2>
            <p class="text-slate-400 mb-10 text-lg">Involved in an emergency? Our dedicated concierge team ensures your claim is prioritized and settled within record time.</p>
            <div class="flex flex-col sm:flex-row gap-8 justify-center lg:justify-start">
              <div v-for="(step, idx) in ['Notify Us', 'Upload Bills', 'Get Settled']" :key="step" class="flex items-center gap-3">
                <span class="w-8 h-8 rounded-full bg-[#f3c969]/20 border border-[#f3c969]/50 text-[#f3c969] flex items-center justify-center font-black text-xs">{{ idx + 1 }}</span>
                <span class="text-white font-bold text-sm tracking-wide">{{ step }}</span>
              </div>
            </div>
          </div>
          <div class="text-center">
            <p class="text-[10px] font-black uppercase text-[#f3c969] tracking-[0.3em] mb-4">Emergency Assistance</p>
            <a href="tel:1800-123-4567" class="inline-flex items-center gap-4 bg-[#f3c969] text-[#1a150e] px-10 py-6 rounded-2xl font-black text-2xl shadow-xl shadow-[#f3c969]/20 hover:-translate-y-1 transition-transform no-underline">
              <i class="fas fa-phone-alt text-lg"></i> 1800-INDORIA
            </a>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { reactive, computed } from 'vue'

const labelStyle = "block text-[10px] font-black uppercase tracking-[0.2em] text-slate-500 ml-1"
const inputStyle = "w-full p-4 rounded-xl border border-slate-200 bg-slate-50 text-sm font-bold text-[#1a150e] focus:border-[#f3c969] focus:bg-white focus:outline-none focus:ring-4 focus:ring-[#f3c969]/10 transition-all outline-none"

const quote = reactive({ type: 'domestic', members: 1, days: 7 })

const benefits = [
  { icon: 'fas fa-hospital-user', title: 'Cashless Medical', desc: 'Direct settlement with 10,000+ elite hospitals worldwide.' },
  { icon: 'fas fa-suitcase-rolling', title: 'Baggage Protection', desc: 'Financial indemnity for lost or delayed personal belongings.' },
  { icon: 'fas fa-calendar-times', title: 'Trip Interruption', desc: 'Full refunds for non-refundable flight and luxury hotel bookings.' },
  { icon: 'fas fa-clock', title: 'Concierge Help', desc: 'A dedicated 24/7 global helpline for all travel emergencies.' }
]

const calculatedPrice = computed(() => {
  const base = quote.type === 'domestic' ? 49 : 199
  return base * quote.members * quote.days
})

const scrollToPlans = () => {
  document.getElementById('plans').scrollIntoView({ behavior: 'smooth' })
}
</script>

<style scoped>
.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

/* Custom Select Dropdown Styling */
select {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%23f3c969' stroke-linecap='round' stroke-linejoin='round' stroke-width='2' d='M6 8l4 4 4-4'/%3e%3c/svg%3e");
  background-position: right 1rem center;
  background-repeat: no-repeat;
  background-size: 1.5em 1.5em;
}
</style>
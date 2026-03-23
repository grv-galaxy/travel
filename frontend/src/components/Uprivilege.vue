<template>
  <div class="min-h-screen bg-[#fafaf9] pb-32 font-sans text-[#1a150e]">
    
    <header class="bg-[#1a150e] text-white pt-24 pb-40 relative overflow-hidden">
      <div class="absolute inset-0 opacity-20 pointer-events-none">
        <div class="absolute top-10 left-1/4 w-1 h-1 bg-[#f3c969] rounded-full animate-pulse"></div>
        <div class="absolute top-40 right-1/3 w-2 h-2 bg-[#f3c969] rounded-full animate-ping"></div>
        <div class="absolute bottom-20 left-10 w-1 h-1 bg-[#f3c969] rounded-full animate-pulse"></div>
      </div>

      <div class="max-w-6xl mx-auto px-4 relative z-10 text-center">
        <div class="inline-flex items-center gap-3 border border-[#f3c969]/30 px-6 py-2 rounded-full mb-8">
          <i class="fas fa-crown text-[#f3c969] text-xs"></i>
          <span class="text-[10px] font-black uppercase tracking-[0.4em] text-[#f3c969]">VIP Elite Status</span>
        </div>
        <h1 class="font-serif text-5xl md:text-7xl font-bold mb-6 italic tracking-tight">
          Beyond <span class="text-[#f3c969]">First Class</span>
        </h1>
        <p class="text-slate-400 font-medium max-w-2xl mx-auto text-base md:text-xl leading-relaxed">
          Unlock a world of curated heritage experiences and private terminal access designed exclusively for Indoria Journeys members.
        </p>
      </div>
    </header>

    <div class="max-w-6xl mx-auto px-4">
      
      <section class="-mt-24 mb-24 relative z-20">
        <div class="bg-gradient-to-br from-[#1a150e] to-[#2a241a] rounded-[2.5rem] p-1 shadow-2xl shadow-black/20">
          <div class="bg-[#1a150e]/50 backdrop-blur-xl rounded-[2.4rem] p-8 md:p-12 flex flex-col md:flex-row items-center justify-between gap-12 border border-white/5">
            
            <div class="space-y-6 text-center md:text-left">
              <div>
                <p class="text-[10px] font-black uppercase tracking-[0.3em] text-[#f3c969] mb-2">Current Tier</p>
                <h2 class="text-4xl font-serif font-bold text-white">Gold Maharaja</h2>
              </div>
              <div class="flex items-center justify-center md:justify-start gap-4">
                <div class="h-1.5 w-48 bg-white/10 rounded-full overflow-hidden">
                  <div class="h-full bg-[#f3c969] shadow-[0_0_10px_#f3c969]" style="width: 75%"></div>
                </div>
                <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">750 / 1000 Points</span>
              </div>
              <p class="text-xs text-slate-400 max-w-sm">You are 250 points away from unlocking <span class="text-white font-bold">Platinum Imperial</span> status.</p>
            </div>

            <div class="grid grid-cols-2 gap-4 w-full md:w-auto">
              <div class="bg-white/5 border border-white/10 p-6 rounded-2xl text-center">
                <i class="fas fa-gem text-[#f3c969] mb-3 block text-xl"></i>
                <span class="text-[10px] font-black uppercase text-white tracking-widest">Lounge Pass</span>
                <p class="text-[9px] text-slate-500 uppercase mt-1">Unlimited</p>
              </div>
              <div class="bg-white/5 border border-white/10 p-6 rounded-2xl text-center">
                <i class="fas fa-concierge-bell text-[#f3c969] mb-3 block text-xl"></i>
                <span class="text-[10px] font-black uppercase text-white tracking-widest">Butler Desk</span>
                <p class="text-[9px] text-slate-500 uppercase mt-1">24/7 Access</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="mb-32">
        <div class="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6">
          <div class="space-y-2">
            <span class="text-[#f3c969] text-[10px] font-black uppercase tracking-[0.4em] block">Your Benefits</span>
            <h3 class="font-serif text-4xl font-bold italic">Curated <span class="text-[#f3c969]">Privileges</span></h3>
          </div>
          <button class="text-[10px] font-black uppercase tracking-widest text-slate-400 border-b border-slate-200 pb-1 hover:text-[#1a150e] transition-colors">View All Benefits</button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div v-for="priv in privileges" :key="priv.title" class="group relative overflow-hidden bg-white rounded-3xl border border-slate-100 shadow-sm hover:shadow-2xl transition-all duration-700 p-10">
            <div class="absolute top-0 right-0 p-8 text-[#f3c969]/10 group-hover:text-[#f3c969]/20 transition-colors">
              <i :class="[priv.icon, 'text-6xl']"></i>
            </div>
            <div class="relative z-10">
              <div class="w-12 h-12 bg-[#fcf9f4] flex items-center justify-center rounded-xl mb-8 group-hover:bg-[#1a150e] group-hover:text-[#f3c969] transition-all duration-500">
                <i :class="priv.icon"></i>
              </div>
              <h4 class="font-serif text-xl font-bold mb-4">{{ priv.title }}</h4>
              <p class="text-xs text-slate-500 leading-relaxed mb-8">{{ priv.desc }}</p>
              <button class="w-full py-4 rounded-xl border border-slate-100 text-[10px] font-black uppercase tracking-widest group-hover:bg-[#f3c969] group-hover:text-[#1a150e] group-hover:border-[#f3c969] transition-all duration-500">
                Claim Benefit
              </button>
            </div>
          </div>
        </div>
      </section>

      <section class="bg-[#1a150e] rounded-[3rem] overflow-hidden flex flex-col lg:flex-row relative">
        <div class="lg:w-1/2 h-80 lg:h-auto overflow-hidden">
          <img src="https://images.unsplash.com/photo-1544161515-4ad6ce6ca85d?auto=format&fit=crop&q=80&w=800" alt="Spa Experience" class="w-full h-full object-cover opacity-80 group-hover:scale-110 transition-transform duration-1000">
        </div>
        <div class="lg:w-1/2 p-10 md:p-16 flex flex-col justify-center">
          <div class="inline-block text-[#f3c969] text-[9px] font-black uppercase tracking-[0.4em] mb-4">Limited Edition</div>
          <h2 class="font-serif text-3xl md:text-4xl font-bold text-white mb-6">The Royal <span class="text-[#f3c969]">Haveli</span> Retreat</h2>
          <p class="text-slate-400 text-sm leading-relaxed mb-10">Experience a private dinner for two under the stars at an 18th-century Rajput palace, exclusively available to Maharaja Tier members this month.</p>
          <div class="flex gap-4">
            <button class="px-8 py-4 bg-[#f3c969] text-[#1a150e] font-black text-[10px] uppercase tracking-widest rounded-xl hover:bg-white transition-colors">Book Invitation</button>
            <button class="px-8 py-4 border border-white/20 text-white font-black text-[10px] uppercase tracking-widest rounded-xl hover:bg-white/5 transition-colors">Details</button>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
const privileges = [
  {
    icon: 'fas fa-shuttle-van',
    title: 'Tarmac Pick-up',
    desc: 'Skip the crowds. A private chauffeur will collect you directly from the rail platform or aircraft stairs.'
  },
  {
    icon: 'fas fa-wine-glass-alt',
    title: 'Heritage Lounge',
    desc: 'Unlimited access to our partner lounges worldwide, featuring locally curated fine dining and spa services.'
  },
  {
    icon: 'fas fa-user-shield',
    title: 'Personal Host',
    desc: 'A dedicated concierge is assigned to your itinerary 48 hours before departure to handle all micro-needs.'
  }
]
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

.font-serif {
  font-family: 'Playfair Display', serif;
}

/* Luxury Glow Effect */
.shadow-2xl {
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
}

@keyframes ping {
  75%, 100% {
    transform: scale(2);
    opacity: 0;
  }
}
</style>
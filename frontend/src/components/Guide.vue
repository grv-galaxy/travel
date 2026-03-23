<template>
  <div class="min-h-screen bg-[#f8f7f4] pb-32 font-sans text-[#1a150e]">
    <header class="bg-[#1a150e] text-white pt-40 pb-32 text-center relative overflow-hidden border-b border-[#f3c969]/20">
      <div class="absolute inset-0 opacity-10 pointer-events-none">
        <svg class="w-full h-full" viewBox="0 0 100 100" preserveAspectRatio="none">
          <pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse">
            <path d="M 10 0 L 0 0 0 10" fill="none" stroke="#f3c969" stroke-width="0.1"/>
          </pattern>
          <rect width="100" height="100" fill="url(#grid)" />
        </svg>
      </div>
      
      <div class="relative z-10 container mx-auto px-4">
        <div class="flex items-center justify-center gap-4 mb-8">
          <div class="h-px w-12 bg-[#f3c969]/50"></div>
          <span class="text-[#f3c969] font-black text-[11px] uppercase tracking-[0.4em]">The Dual Perspective</span>
          <div class="h-px w-12 bg-[#f3c969]/50"></div>
        </div>
        <h1 class="font-serif text-5xl md:text-7xl font-bold mb-8 tracking-tight">
          Explore with <span class="italic text-[#f3c969]">Intelligence</span>
        </h1>
        <p class="text-slate-400 font-medium max-w-xl mx-auto text-lg leading-relaxed italic opacity-80">
          "Choose between the ancient wisdom of local historians or the digital precision of BuddyAi."
        </p>
      </div>
    </header>

    <div class="max-w-6xl mx-auto px-4">
      <section class="-mt-16 relative z-20 mb-32">
        <div class="bg-[#0c0a09] border border-[#f3c969]/20 shadow-[0_40px_100px_-20px_rgba(0,0,0,0.4)] flex flex-col lg:flex-row overflow-hidden">
          
          <div class="flex-1 p-10 md:p-20 space-y-10 relative">
            <div class="absolute top-0 left-0 w-24 h-1 bg-[#f3c969]"></div>
            
            <div class="space-y-4">
              <span class="text-[#f3c969] font-black text-[10px] uppercase tracking-[0.3em]">Augmented Reality Companion</span>
              <h2 class="font-serif text-5xl text-white font-bold tracking-tight">Meet <span class="italic">BuddyAi</span></h2>
              <p class="text-slate-400 text-lg leading-relaxed italic">
                A 24/7 personal travel curator in your pocket. Point, scan, and let the walls of Delhi speak to you.
              </p>
            </div>

            <ul class="space-y-6">
              <li v-for="feature in aiFeatures" :key="feature.title" class="flex gap-6 group">
                <div class="w-10 h-10 shrink-0 border border-[#f3c969]/30 flex items-center justify-center text-[#f3c969] group-hover:bg-[#f3c969] group-hover:text-[#1a150e] transition-all">
                  <i :class="feature.icon" class="text-sm"></i>
                </div>
                <div>
                  <h4 class="text-white font-bold text-xs uppercase tracking-widest mb-1">{{ feature.title }}</h4>
                  <p class="text-slate-500 text-xs leading-relaxed max-w-xs">{{ feature.desc }}</p>
                </div>
              </li>
            </ul>

            <div class="flex flex-col sm:flex-row items-center gap-10 pt-10 border-t border-white/5">
              <div class="flex items-baseline gap-2">
                <span class="text-white text-4xl font-serif">₹199</span>
                <span class="text-slate-500 text-[10px] font-black uppercase tracking-[0.2em]">/ Journey</span>
              </div>
              <button @click="launchAI" class="group relative overflow-hidden bg-[#f3c969] text-[#1a150e] px-10 py-5 font-black text-[10px] uppercase tracking-[0.3em] transition-all hover:bg-white cursor-pointer">
                Activate Companion
              </button>
            </div>
          </div>

          <div class="flex-1 bg-[#1a150e] flex items-center justify-center p-12 border-l border-white/5">
            <div class="relative group">
              <div class="absolute inset-0 bg-[#f3c969] blur-[80px] opacity-10 group-hover:opacity-20 transition-opacity"></div>
              
              <div class="w-[280px] h-[580px] border-[6px] border-[#332b21] rounded-[45px] bg-black relative overflow-hidden shadow-2xl">
                <div class="h-full w-full bg-cover bg-center transition-transform duration-[3s] group-hover:scale-110" 
                     style="background-image: url('https://images.unsplash.com/photo-1548013146-72479768bbaa?auto=format&fit=crop&q=80&w=1000')">
                  
                  <div class="absolute inset-0 bg-black/30 flex flex-col items-center justify-center">
                    <div class="w-40 h-40 border border-[#f3c969]/50 rounded-full animate-pulse flex items-center justify-center">
                      <div class="bg-[#f3c969] text-[#1a150e] px-4 py-2 text-[9px] font-black uppercase tracking-widest shadow-xl">
                        India Gate • 1921
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section class="space-y-20">
        <div class="text-center space-y-4">
          <div class="h-px w-24 bg-[#f3c969] mx-auto opacity-30"></div>
          <h2 class="font-serif text-4xl md:text-5xl font-bold text-[#1a150e]">Verified Local <span class="italic">Historians</span></h2>
          <p class="text-slate-400 font-medium italic text-lg max-w-xl mx-auto opacity-70">
            For those who seek the human touch, the unwritten stories, and the soul of the city.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-12">
          <div v-for="guide in guideOptions" :key="guide.type" class="group bg-white p-12 shadow-[0_20px_60px_-15px_rgba(0,0,0,0.05)] border-t-[4px] border-[#1a150e] hover:border-[#f3c969] transition-all duration-700">
            <div class="mb-10 text-[#f3c969]">
              <i :class="guide.icon" class="text-3xl"></i>
            </div>
            
            <h3 class="font-serif text-2xl font-bold text-[#1a150e] mb-4 tracking-tight">{{ guide.type }}</h3>
            <p class="text-slate-400 text-sm leading-relaxed mb-10 min-h-[60px] italic">{{ guide.description }}</p>
            
            <div class="flex items-center gap-6 border-y border-slate-50 py-6 mb-10">
              <div class="flex flex-col gap-1">
                <span class="text-[9px] font-black text-slate-300 uppercase tracking-widest">Duration</span>
                <span class="text-[10px] font-bold text-[#1a150e]">{{ guide.duration }}</span>
              </div>
              <div class="w-px h-6 bg-slate-100"></div>
              <div class="flex flex-col gap-1">
                <span class="text-[9px] font-black text-slate-300 uppercase tracking-widest">Capacity</span>
                <span class="text-[10px] font-bold text-[#1a150e]">{{ guide.people }} Guests</span>
              </div>
            </div>

            <div class="flex items-center justify-between">
              <div class="flex flex-col">
                <span class="text-[9px] font-black text-slate-300 uppercase tracking-widest">Investment</span>
                <span class="text-2xl font-serif font-bold">₹{{ guide.price }}</span>
              </div>
              <button class="px-8 py-3 bg-[#1a150e] text-[#f3c969] font-black text-[9px] uppercase tracking-widest hover:bg-[#f3c969] hover:text-[#1a150e] transition-all cursor-pointer">
                Reserve
              </button>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
const aiFeatures = [
  { icon: 'fas fa-camera', title: 'Visual Intel', desc: 'Identify ancient structures and artistic motifs instantly through your lens.' },
  { icon: 'fas fa-magic', title: 'AR Paths', desc: 'Floating digital cues guide you through the labyrinth of the Walled City.' },
  { icon: 'fas fa-language', title: 'Live Narrative', desc: 'Real-time translation of heritage plaques and dialectal street signage.' }
]

const guideOptions = [
  {
    type: 'Heritage Expert',
    icon: 'fas fa-landmark',
    description: 'A deep dive into Mughal architecture and the colonial evolution of Old Delhi.',
    duration: '8 Hours',
    people: '4',
    price: '2,500'
  },
  {
    type: 'Culinary Explorer',
    icon: 'fas fa-utensils',
    description: 'Navigate spice markets and hidden street food stalls with a professional gastronome.',
    duration: '5 Hours',
    people: '6',
    price: '1,800'
  },
  {
    type: 'Photo Curator',
    icon: 'fas fa-camera-retro',
    description: 'A visual artist guides you to the most evocative, un-Instagrammed frames of the city.',
    duration: '4 Hours',
    people: '2',
    price: '3,200'
  }
]

const launchAI = () => {
  alert("BuddyAi is calibrating your device's visual sensors. Please ensure you are outdoors for optimal AR performance.");
}
</script>

<style scoped>
.font-serif {
  font-family: 'Playfair Display', Georgia, serif;
}

/* Custom transitions for luxury cards */
.group {
  transition: all 0.5s cubic-bezier(0.19, 1, 0.22, 1);
}

.group:hover {
  transform: translateY(-10px);
}
</style>
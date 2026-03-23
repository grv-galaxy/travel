<template>
  <div class="h-[calc(100vh-140px)] bg-[#fafaf9] font-sans text-[#1a150e] flex flex-col">
    
    <div class="max-w-5xl mx-auto w-full flex-1 flex flex-col md:flex-row gap-8 p-4 md:p-8 overflow-hidden">
      
      <div class="w-full md:w-80 flex flex-col gap-6">
        <div class="bg-[#1a150e] rounded-[2.5rem] p-8 text-white relative overflow-hidden shadow-2xl">
          <div class="relative z-10 flex flex-col items-center text-center">
            <div class="relative mb-6">
              <div class="w-24 h-24 rounded-full border-2 border-[#f3c969] p-1">
                <div class="w-full h-full rounded-full bg-slate-800 flex items-center justify-center overflow-hidden">
                   <i class="fas fa-user-tie text-4xl text-slate-500"></i>
                </div>
              </div>
              <div class="absolute bottom-1 right-1 w-5 h-5 bg-emerald-500 border-4 border-[#1a150e] rounded-full"></div>
            </div>
            
            <h3 class="font-serif text-xl font-bold italic text-[#f3c969]">Arjun Vardhan</h3>
            <p class="text-[9px] font-black uppercase tracking-[0.3em] text-slate-400 mt-2">Lead Personal Butler</p>
            
            <div class="mt-8 pt-8 border-t border-white/10 w-full space-y-4">
              <div class="flex justify-between items-center text-[10px]">
                <span class="text-slate-500 uppercase font-black">Response Time</span>
                <span class="text-[#f3c969]">~2 Mins</span>
              </div>
              <div class="flex justify-between items-center text-[10px]">
                <span class="text-slate-500 uppercase font-black">Languages</span>
                <span class="text-white">EN, HI, FR</span>
              </div>
            </div>
          </div>
        </div>

        <div class="hidden md:grid grid-cols-1 gap-3">
          <button v-for="action in quickActions" :key="action" class="text-left px-6 py-4 bg-white border border-slate-100 rounded-2xl text-[10px] font-black uppercase tracking-widest hover:bg-[#1a150e] hover:text-[#f3c969] transition-all group">
            <i class="fas fa-plus mr-3 opacity-30 group-hover:opacity-100"></i> {{ action }}
          </button>
        </div>
      </div>

      <div class="flex-1 bg-white rounded-[2.5rem] shadow-xl border border-slate-100 flex flex-col overflow-hidden">
        <div class="px-8 py-6 border-b border-slate-50 flex justify-between items-center">
          <div class="flex items-center gap-4">
            <div class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></div>
            <span class="text-[10px] font-black uppercase tracking-[0.2em] text-slate-400">Secure Encrypted Line</span>
          </div>
          <i class="fas fa-ellipsis-h text-slate-300"></i>
        </div>

        <div class="flex-1 overflow-y-auto p-8 space-y-8 scrollbar-hide">
          <div v-for="(msg, idx) in messages" :key="idx" 
            :class="['flex w-full', msg.role === 'user' ? 'justify-end' : 'justify-start']">
            
            <div :class="[
              'max-w-[80%] p-6 rounded-3xl text-sm leading-relaxed shadow-sm',
              msg.role === 'user' 
                ? 'bg-[#1a150e] text-white rounded-tr-none' 
                : 'bg-[#fcf9f4] text-[#1a150e] rounded-tl-none border border-slate-100'
            ]">
              <p class="font-medium">{{ msg.text }}</p>
              <span :class="['text-[8px] uppercase tracking-widest mt-4 block font-black', msg.role === 'user' ? 'text-slate-500' : 'text-[#f3c969]']">
                {{ msg.time }}
              </span>
            </div>
          </div>
        </div>

        <div class="p-6 bg-slate-50/50 border-t border-slate-100">
          <div class="bg-white rounded-2xl border border-slate-200 p-2 flex items-center gap-2 shadow-inner">
            <button class="w-12 h-12 rounded-xl text-slate-300 hover:text-[#1a150e] transition-colors"><i class="fas fa-paperclip"></i></button>
            <input 
              v-model="newMessage" 
              @keyup.enter="sendMessage"
              type="text" 
              placeholder="Request your concierge..." 
              class="flex-1 bg-transparent border-none outline-none px-2 text-sm font-medium"
            >
            <button 
              @click="sendMessage"
              class="w-12 h-12 rounded-xl bg-[#1a150e] text-[#f3c969] shadow-lg shadow-[#1a150e]/20 active:scale-95 transition-all"
            >
              <i class="fas fa-paper-plane"></i>
            </button>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const newMessage = ref('')
const quickActions = ['Champagne Service', 'Late Checkout', 'Baggage Handling', 'Spa Booking']

const messages = ref([
  {
    role: 'concierge',
    text: 'Good evening, Sir. I hope your journey from Udaipur is comfortable. I have pre-chilled the vintage Krug 2008 in your suite as per your preference. Is there anything else you require upon arrival?',
    time: '18:42 PM'
  },
  {
    role: 'user',
    text: 'That is perfect, Arjun. Please ensure the chauffeur is ready at Gate 1. I have an additional suitcase.',
    time: '18:45 PM'
  },
  {
    role: 'concierge',
    text: 'Consider it done. Vikram is already stationed at Gate 1 with the S-Class. He has been notified about the extra luggage.',
    time: '18:46 PM'
  }
])

const sendMessage = () => {
  if (!newMessage.value.trim()) return
  messages.value.push({
    role: 'user',
    text: newMessage.value,
    time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
  })
  newMessage.value = ''
}
</script>

<style scoped>
.font-serif { font-family: 'Playfair Display', serif; }
.scrollbar-hide::-webkit-scrollbar { display: none; }
</style>
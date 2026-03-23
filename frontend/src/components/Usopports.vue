<template>
  <div class="min-h-screen bg-[#fafaf9]">
    <main class="mx-auto max-w-6xl px-4 py-8 sm:px-6 lg:py-16">
      <div class="mb-12 text-center">
        <h1 class="text-3xl font-bold text-[#1a150e] sm:text-5xl font-serif tracking-tight">
          How can we <span class="text-[#f3c969]">assist</span> your journey?
        </h1>
        <p class="mt-4 text-lg text-slate-600 font-medium max-w-2xl mx-auto">
          Our travel curators are available 24/7 to ensure your heritage experience remains seamless.
        </p>
      </div>

      <div class="grid grid-cols-1 gap-8 lg:grid-cols-3">
        <div class="space-y-6">
          <div class="rounded-2xl bg-white p-6 shadow-sm border border-slate-200/60">
            <h3 class="text-lg font-bold text-[#1a150e] mb-6 font-serif border-b border-[#f3c969]/20 pb-2">Direct Concierge</h3>
            <div class="space-y-6">
              <div v-for="method in supportMethods" :key="method.title" class="flex items-start space-x-4 group cursor-pointer">
                <div class="rounded-xl p-3 bg-[#fcf9f4] border border-[#f3c969]/10 text-[#f3c969] group-hover:bg-[#f3c969] group-hover:text-white transition-all duration-300 shadow-sm">
                  <i :class="method.iconClass" class="text-lg"></i>
                </div>
                <div>
                  <p class="text-sm font-bold text-[#1a150e]">{{ method.title }}</p>
                  <p class="text-xs font-medium text-slate-500 mt-0.5">{{ method.desc }}</p>
                </div>
              </div>
            </div>
          </div>

          <div class="rounded-2xl bg-[#1a150e] p-8 text-white shadow-xl shadow-[#1a150e]/10 border border-[#f3c969]/30 relative overflow-hidden group">
            <h3 class="font-bold font-serif text-[#f3c969] text-xl">Priority Hotline</h3>
            <p class="mt-2 text-sm text-slate-300 leading-relaxed">Urgent on-ground assistance?</p>
            <div class="mt-6 flex items-center gap-3">
               <div class="h-10 w-10 rounded-full bg-[#f3c969]/20 flex items-center justify-center">
                  <i class="fas fa-phone-alt text-[#f3c969] animate-pulse"></i>
               </div>
               <p class="text-xl font-bold tracking-wider">+91 (800) INDORIA</p>
            </div>
          </div>
        </div>

        <div class="lg:col-span-2">
          <div class="rounded-2xl bg-white p-8 shadow-sm border border-slate-200/60 relative">
            <div class="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-transparent via-[#f3c969] to-transparent"></div>
            <h3 class="text-2xl font-bold text-[#1a150e] mb-8 font-serif">Inquiry Portfolio</h3>
            
            <form @submit.prevent="submitSupport" class="space-y-6">
              <div class="grid grid-cols-1 gap-6 sm:grid-cols-2">
                <div class="space-y-2">
                  <label class="text-[11px] uppercase tracking-widest font-bold text-slate-500 ml-1">Inquiry Nature</label>
                  <select v-model="form.subject" :class="inputStyles" class="appearance-none">
                    <option value="" disabled>Select a topic</option>
                    <option>Curated Tour Inquiry</option>
                    <option>Existing Booking Modification</option>
                    <option>Bespoke Request</option>
                    <option>Feedback & Praise</option>
                  </select>
                </div>
                <div class="space-y-2">
                  <label class="text-[11px] uppercase tracking-widest font-bold text-slate-500 ml-1">Reference ID</label>
                  <input v-model="form.bookingId" type="text" placeholder="#IND-4492" :class="inputStyles" />
                </div>
                <div class="sm:col-span-2 space-y-2">
                  <label class="text-[11px] uppercase tracking-widest font-bold text-slate-500 ml-1">Your Message</label>
                  <textarea v-model="form.message" rows="5" placeholder="Details..." :class="inputStyles"></textarea>
                </div>
              </div>

              <div class="mt-8">
                <button 
                  type="submit" 
                  :disabled="isSubmitting"
                  class="w-full sm:w-auto inline-flex items-center justify-center rounded-xl bg-[#1a150e] px-10 py-4 text-sm font-bold text-[#f3c969] shadow-lg hover:shadow-[#f3c969]/10 hover:-translate-y-0.5 transition-all disabled:opacity-50 border border-[#f3c969]/40 uppercase tracking-widest cursor-pointer"
                >
                  <span v-if="!isSubmitting">Dispatch Inquiry</span>
                  <span v-else>Processing...</span>
                  <i v-if="!isSubmitting" class="fas fa-paper-plane ml-3 text-xs"></i>
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

// Tailwind v4 workaround: Store common classes in a variable instead of @apply
const inputStyles = "block w-full rounded-xl border border-slate-200 bg-slate-50 py-3 px-4 text-sm text-[#1a150e] font-medium placeholder:text-slate-400 focus:border-[#f3c969] focus:bg-white focus:outline-none focus:ring-4 focus:ring-[#f3c969]/10 transition-all"

const isSubmitting = ref(false)
const form = reactive({ subject: '', bookingId: '', message: '' })

const supportMethods = [
  { title: 'Electronic Mail', desc: 'concierge@indoriajourneys.com', iconClass: 'fas fa-envelope' },
  { title: 'Instant Chat', desc: 'Average response: 2 minutes', iconClass: 'fas fa-comments' },
  { title: 'Travel Dossier', desc: 'Search our travel guides', iconClass: 'fas fa-book-open' }
]

const submitSupport = () => {
  if (!form.subject || !form.message) return alert('Please refine details.')
  isSubmitting.value = true
  setTimeout(() => {
    alert('Inquiry dispatched successfully.')
    isSubmitting.value = false
    form.subject = ''; form.bookingId = ''; form.message = ''
  }, 1500)
}
</script>

<style scoped>
.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

/* For the select arrow only - non-tailwind CSS is fine here */
select {
  background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='none' viewBox='0 0 20 20'%3e%3cpath stroke='%2364748b' stroke-linecap='round' stroke-linejoin='round' stroke-width='1.5' d='M6 8l4 4 4-4'/%3e%3c/svg%3e");
  background-position: right 1rem center;
  background-repeat: no-repeat;
  background-size: 1.5em 1.5em;
}
</style>
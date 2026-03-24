<!-- <template>
  <div class="min-h-screen bg-[#fafaf9] pb-32 font-sans text-[#1a150e]">
    
    <header class="bg-[#1a150e] text-white pt-24 pb-32 relative overflow-hidden">
      <div class="absolute inset-0 opacity-5 pointer-events-none">
        <i class="fas fa-passport text-[280px] absolute -bottom-10 -right-10 -rotate-12"></i>
      </div>
      
      <div class="max-w-6xl mx-auto px-4 relative z-10">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-8">
          <div class="space-y-4">
            <div class="inline-flex items-center gap-2 bg-[#f3c969]/10 border border-[#f3c969]/30 px-4 py-1.5 rounded-full">
              <span class="relative flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#f3c969] opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-[#f3c969]"></span>
              </span>
              <span class="text-[9px] font-black uppercase tracking-[0.3em] text-[#f3c969]">Secure Encrypted Vault</span>
            </div>
            <h1 class="font-serif text-4xl md:text-5xl font-bold tracking-tight">Global <span class="text-[#f3c969]">Credentials</span></h1>
            <p class="text-slate-400 max-w-md text-sm leading-relaxed">
              Access your travel visas, identification, and health permits. Verified by Indoria Concierge for seamless border crossings.
            </p>
          </div>

          <div class="group cursor-pointer">
            <div class="bg-white/5 border border-white/10 p-8 rounded-[2rem] hover:bg-white/10 transition-all duration-500 flex flex-col items-center text-center">
              <div class="w-12 h-12 bg-[#f3c969] text-[#1a150e] rounded-full flex items-center justify-center mb-4 shadow-[0_0_20px_rgba(243,201,105,0.3)]">
                <i class="fas fa-plus transition-transform group-hover:rotate-90"></i>
              </div>
              <span class="text-[10px] font-black uppercase tracking-widest text-white">Upload New</span>
              <p class="text-[9px] text-slate-500 uppercase mt-1 tracking-tighter">Max 10MB (PDF, JPG)</p>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="max-w-6xl mx-auto px-4 -mt-16 relative z-20">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
        
        <div class="lg:col-span-2 space-y-6">
          <div v-for="doc in documents" :key="doc.id" 
            class="bg-white rounded-[2rem] p-6 md:p-8 border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-500 group">
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
              
              <div class="flex items-start gap-6">
                <div class="w-16 h-20 bg-[#fcf9f4] rounded-lg border border-slate-100 flex flex-col items-center justify-center text-slate-400 group-hover:bg-[#1a150e] group-hover:text-[#f3c969] transition-colors duration-500">
                  <i :class="doc.icon" class="text-2xl mb-1"></i>
                  <span class="text-[8px] font-black uppercase tracking-tighter">{{ doc.ext }}</span>
                </div>
                <div>
                  <h4 class="font-serif text-xl font-bold mb-1">{{ doc.name }}</h4>
                  <div class="flex flex-wrap gap-4 items-center">
                    <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Added: {{ doc.date }}</span>
                    <span :class="getStatusClass(doc.status)">{{ doc.status }}</span>
                  </div>
                </div>
              </div>

              <div class="flex items-center gap-3 self-end md:self-center">
                <button class="w-12 h-12 rounded-xl bg-slate-50 text-slate-400 hover:bg-[#1a150e] hover:text-[#f3c969] transition-all"><i class="fas fa-eye"></i></button>
                <button class="w-12 h-12 rounded-xl bg-slate-50 text-slate-400 hover:bg-[#1a150e] hover:text-[#f3c969] transition-all"><i class="fas fa-download"></i></button>
                <button class="w-12 h-12 rounded-xl bg-slate-50 text-red-300 hover:bg-red-500 hover:text-white transition-all"><i class="fas fa-trash-alt"></i></button>
              </div>

            </div>
          </div>
        </div>

        <div class="space-y-8">
          <div class="bg-[#1a150e] rounded-[2.5rem] p-8 text-white relative overflow-hidden shadow-2xl">
            <div class="relative z-10">
              <h3 class="font-serif text-xl font-bold mb-6 text-[#f3c969]">Active Visas</h3>
              <div class="space-y-6">
                <div v-for="visa in visas" :key="visa.country" class="border-b border-white/10 pb-6 last:border-0">
                  <div class="flex justify-between items-center mb-2">
                    <span class="text-xs font-bold tracking-widest uppercase">{{ visa.country }}</span>
                    <span class="text-[10px] text-emerald-400 font-black uppercase tracking-widest">Valid</span>
                  </div>
                  <div class="text-[10px] text-slate-400 uppercase tracking-widest mb-4">Expires: {{ visa.expiry }}</div>
                  <div class="h-1 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-emerald-500" :style="{ width: visa.progress + '%' }"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-[#f3c969] rounded-[2.5rem] p-8">
            <i class="fas fa-user-shield text-2xl mb-4 text-[#1a150e]"></i>
            <h4 class="font-serif text-lg font-bold text-[#1a150e] mb-2">Biometric Lock</h4>
            <p class="text-[11px] font-medium text-[#1a150e]/70 leading-relaxed uppercase tracking-tight">
              All documents are protected by AES-256 encryption. Physical copies are available for delivery via Indoria Courier upon request.
            </p>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script setup>
const documents = [
  { id: 1, name: 'Passport - Main Page', date: '22 Dec 2025', status: 'Verified', icon: 'fas fa-address-card', ext: 'PDF' },
  { id: 2, name: 'Indian Heritage Visa', date: '18 Dec 2025', status: 'Verified', icon: 'fas fa-stamp', ext: 'JPG' },
  { id: 3, name: 'Medical Clearance', date: '10 Dec 2025', status: 'Pending', icon: 'fas fa-file-medical', ext: 'PDF' },
  { id: 4, name: 'Travel Insurance Policy', date: '05 Dec 2025', status: 'Verified', icon: 'fas fa-umbrella', ext: 'PDF' },
]

const visas = [
  { country: 'United Kingdom', expiry: 'Jun 2026', progress: 85 },
  { country: 'United Arab Emirates', expiry: 'Jan 2026', progress: 15 },
]

const getStatusClass = (status) => {
  const base = "text-[9px] font-black uppercase tracking-widest px-3 py-1 rounded-full border "
  return status === 'Verified' 
    ? base + "bg-emerald-50 text-emerald-600 border-emerald-100" 
    : base + "bg-amber-50 text-amber-600 border-amber-100"
}
</script>

<style scoped>
.font-serif { font-family: 'Playfair Display', serif; }
</style> -->





















<!-- <template>
  <div class="min-h-screen bg-[#fafaf9] pb-32 font-sans text-[#1a150e]">
    
    <input 
      type="file" 
      ref="fileInput" 
      class="hidden" 
      accept=".pdf,.jpg,.jpeg,.png" 
      @change="handleFileSelection"
    />

    <header class="bg-[#1a150e] text-white pt-24 pb-32 relative overflow-hidden">
      <div class="absolute inset-0 opacity-5 pointer-events-none">
        <i class="fas fa-passport text-[280px] absolute -bottom-10 -right-10 -rotate-12"></i>
      </div>
      
      <div class="max-w-6xl mx-auto px-4 relative z-10">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-8">
          <div class="space-y-4">
            <div class="inline-flex items-center gap-2 bg-[#f3c969]/10 border border-[#f3c969]/30 px-4 py-1.5 rounded-full">
              <span class="relative flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#f3c969] opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-[#f3c969]"></span>
              </span>
              <span class="text-[9px] font-black uppercase tracking-[0.3em] text-[#f3c969]">Secure Encrypted Vault</span>
            </div>
            <h1 class="font-serif text-4xl md:text-5xl font-bold tracking-tight">Global <span class="text-[#f3c969]">Credentials</span></h1>
            <p class="text-slate-400 max-w-md text-sm leading-relaxed">
              Access your travel visas, identification, and health permits. Verified by Indoria Concierge for seamless border crossings.
            </p>
          </div>

          <div 
            class="group cursor-pointer" 
            @click="triggerFileInput"
            :class="{ 'opacity-50 pointer-events-none': isUploading }"
          >
            <div class="bg-white/5 border border-white/10 p-8 rounded-[2rem] hover:bg-white/10 transition-all duration-500 flex flex-col items-center text-center relative overflow-hidden">
              
              <div v-if="isUploading" class="absolute inset-0 flex items-center justify-center bg-[#1a150e]/80 z-20">
                <i class="fas fa-circle-notch animate-spin text-[#f3c969] text-xl"></i>
              </div>

              <div class="w-12 h-12 bg-[#f3c969] text-[#1a150e] rounded-full flex items-center justify-center mb-4 shadow-[0_0_20px_rgba(243,201,105,0.3)]">
                <i :class="isUploading ? 'fas fa-shield-alt' : 'fas fa-plus'" class="transition-transform group-hover:rotate-90"></i>
              </div>
              <span class="text-[10px] font-black uppercase tracking-widest text-white">
                {{ isUploading ? 'Encrypting...' : 'Upload New' }}
              </span>
              <p class="text-[9px] text-slate-500 uppercase mt-1 tracking-tighter">Max 10MB (PDF, JPG)</p>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="max-w-6xl mx-auto px-4 -mt-16 relative z-20">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
        
        <div class="lg:col-span-2 space-y-6">

          <div v-if="isLoading" class="space-y-6">
            <div v-for="n in 3" :key="n" class="skeleton-card rounded-[2rem] p-6 md:p-8">
              <div class="skeleton-shimmer"></div> 
              <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div class="flex items-start gap-6">
                  <div class="skeleton-bone bone-icon"></div>
                  <div class="w-16 h-20 bg-slate-100 rounded-lg"></div>
                  <div class="space-y-3">
                    <div class="h-6 bg-slate-100 rounded-md w-48"></div>
                    <div class="flex gap-4">
                      <div class="h-3 bg-slate-50 rounded w-20"></div>
                      <div class="h-3 bg-slate-50 rounded w-16"></div>
                    </div>
                  </div>
                </div>
                <div class="flex items-center gap-3">
                  <div class="w-12 h-12 rounded-xl bg-slate-50"></div>
                  <div class="w-12 h-12 rounded-xl bg-slate-50"></div>
                  <div class="w-12 h-12 rounded-xl bg-slate-50"></div>
                </div>
              </div>
            </div>
          </div>

          <template v-else-if="documents.length > 0">
                  <div v-for="doc in documents" :key="doc.id" 
                    class="bg-white rounded-[2rem] p-6 md:p-8 border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-500 group">
                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                      
                      <div class="flex items-start gap-6">
                        <div class="w-16 h-20 bg-[#fcf9f4] rounded-lg border border-slate-100 flex flex-col items-center justify-center text-slate-400 group-hover:bg-[#1a150e] group-hover:text-[#f3c969] transition-colors duration-500">
                          <i :class="doc.icon || 'fas fa-file-alt'" class="text-2xl mb-1"></i>
                          <span class="text-[8px] font-black uppercase tracking-tighter">{{ doc.ext }}</span>
                        </div>
                        <div>
                          <h4 class="font-serif text-xl font-bold mb-1">{{ doc.name }}</h4>
                          <div class="flex flex-wrap gap-4 items-center">
                            <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Added: {{ doc.date }}</span>
                            <span :class="getStatusClass(doc.status)">{{ doc.status }}</span>
                          </div>
                        </div>
                      </div>

                      <div class="flex items-center gap-3 self-end md:self-center">
                        <button 
                          @click="previewDocument(doc.url)"
                          class="w-12 h-12 rounded-xl bg-slate-50 text-slate-400 hover:bg-[#1a150e] hover:text-[#f3c969] transition-all">
                          <i class="fas fa-eye"></i>
                        </button>
                        
                        <a :href="doc.url" target="_blank" download class="flex items-center justify-center w-12 h-12 rounded-xl bg-slate-50 text-slate-400 hover:bg-[#1a150e] hover:text-[#f3c969] transition-all">
                          <i class="fas fa-download"></i>
                        </a>

                        <button 
                          @click="handleDelete(doc.id, doc.public_id)"
                          class="w-12 h-12 rounded-xl bg-slate-50 text-red-300 hover:bg-red-500 hover:text-white transition-all">
                          <i class="fas fa-trash-alt"></i>
                        </button>
                      </div>
                    </div>
                  </div>
                </template>

                  <div v-else class="text-center py-20 bg-white rounded-[2rem] border-2 border-dashed border-slate-100">
                    <i class="fas fa-folder-open text-4xl text-slate-200 mb-4"></i>
                    <p class="text-slate-400 text-sm font-medium">No credentials uploaded yet.</p>
                  </div>
                </div>

        <div class="space-y-8">
          <div class="bg-[#1a150e] rounded-[2.5rem] p-8 text-white relative overflow-hidden shadow-2xl">
            <div class="relative z-10">
              <h3 class="font-serif text-xl font-bold mb-6 text-[#f3c969]">Active Visas</h3>
              <div class="space-y-6">
                <div v-for="visa in visas" :key="visa.country" class="border-b border-white/10 pb-6 last:border-0">
                  <div class="flex justify-between items-center mb-2">
                    <span class="text-xs font-bold tracking-widest uppercase">{{ visa.country }}</span>
                    <span class="text-[10px] text-emerald-400 font-black uppercase tracking-widest">Valid</span>
                  </div>
                  <div class="text-[10px] text-slate-400 uppercase tracking-widest mb-4">Expires: {{ visa.expiry }}</div>
                  <div class="h-1 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-emerald-500" :style="{ width: visa.progress + '%' }"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-[#f3c969] rounded-[2.5rem] p-8">
            <i class="fas fa-user-shield text-2xl mb-4 text-[#1a150e]"></i>
            <h4 class="font-serif text-lg font-bold text-[#1a150e] mb-2">Biometric Lock</h4>
            <p class="text-[11px] font-medium text-[#1a150e]/70 leading-relaxed uppercase tracking-tight">
              All documents are protected by AES-256 encryption. Physical copies are available for delivery via Indoria Courier upon request.
            </p>
          </div>
        </div>

      </div>
    </div>
  </div>
</template> -->


<template>
  <div class="min-h-screen bg-[#fafaf9] pb-32 font-sans text-[#1a150e]">
    
    <input 
      type="file" 
      ref="fileInput" 
      class="hidden" 
      accept=".pdf,.jpg,.jpeg,.png" 
      @change="handleFileSelection"
    />

    <header class="bg-[#1a150e] text-white pt-24 pb-32 relative overflow-hidden">
      <div class="absolute inset-0 opacity-5 pointer-events-none">
        <i class="fas fa-passport text-[280px] absolute -bottom-10 -right-10 -rotate-12"></i>
      </div>
      
      <div class="max-w-6xl mx-auto px-4 relative z-10">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-8">
          <div class="space-y-4">
            <div class="inline-flex items-center gap-2 bg-[#f3c969]/10 border border-[#f3c969]/30 px-4 py-1.5 rounded-full">
              <span class="relative flex h-2 w-2">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#f3c969] opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-[#f3c969]"></span>
              </span>
              <span class="text-[9px] font-black uppercase tracking-[0.3em] text-[#f3c969]">Secure Encrypted Vault</span>
            </div>
            <h1 class="font-serif text-4xl md:text-5xl font-bold tracking-tight">Global <span class="text-[#f3c969]">Credentials</span></h1>
            <p class="text-slate-400 max-w-md text-sm leading-relaxed">
              Access your travel visas, identification, and health permits. Verified by Indoria Concierge for seamless border crossings.
            </p>
          </div>

          <div 
            class="group cursor-pointer" 
            @click="triggerFileInput"
            :class="{ 'opacity-50 pointer-events-none': isUploading }"
          >
            <div class="bg-white/5 border border-white/10 p-8 rounded-[2rem] hover:bg-white/10 transition-all duration-500 flex flex-col items-center text-center relative overflow-hidden">
              <div v-if="isUploading" class="absolute inset-0 flex items-center justify-center bg-[#1a150e]/80 z-20">
                <i class="fas fa-circle-notch animate-spin text-[#f3c969] text-xl"></i>
              </div>
              <div class="w-12 h-12 bg-[#f3c969] text-[#1a150e] rounded-full flex items-center justify-center mb-4 shadow-[0_0_20px_rgba(243,201,105,0.3)]">
                <i :class="isUploading ? 'fas fa-shield-alt' : 'fas fa-plus'" class="transition-transform group-hover:rotate-90"></i>
              </div>
              <span class="text-[10px] font-black uppercase tracking-widest text-white">
                {{ isUploading ? 'Encrypting...' : 'Upload New' }}
              </span>
              <p class="text-[9px] text-slate-500 uppercase mt-1 tracking-tighter">Max 10MB (PDF, JPG)</p>
            </div>
          </div>
        </div>
      </div>
    </header>

    <div class="max-w-6xl mx-auto px-4 -mt-16 relative z-20">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-10">
        
        <div class="lg:col-span-2 space-y-6">
          
          <div v-if="isLoading" class="space-y-6">
            <div v-for="n in 3" :key="n" class="skeleton-card rounded-[2rem] p-6 md:p-8">
              <div class="skeleton-shimmer"></div> 
              <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 relative z-10">
                <div class="flex items-start gap-6">
                  <div class="skeleton-bone bone-icon"></div>
                  <div class="flex-1 space-y-3">
                    <div class="skeleton-bone bone-title"></div>
                    <div class="flex gap-4">
                      <div class="skeleton-bone bone-meta"></div>
                      <div class="skeleton-bone bone-meta" style="width: 20%"></div>
                    </div>
                  </div>
                </div>
                <div class="flex items-center gap-3 self-end md:self-center">
                  <div class="skeleton-bone bone-btn"></div>
                  <div class="skeleton-bone bone-btn"></div>
                  <div class="skeleton-bone bone-btn"></div>
                </div>
              </div>
            </div>
          </div>

          <template v-else-if="documents.length > 0">
            <div v-for="doc in documents" :key="doc.id" 
              class="bg-white rounded-[2rem] p-6 md:p-8 border border-slate-100 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-500 group">
              <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                
                <div class="flex items-start gap-6">
                  <div class="w-16 h-20 bg-[#fcf9f4] rounded-lg border border-slate-100 flex flex-col items-center justify-center text-slate-400 group-hover:bg-[#1a150e] group-hover:text-[#f3c969] transition-colors duration-500">
                    <i :class="doc.icon || 'fas fa-file-alt'" class="text-2xl mb-1"></i>
                    <span class="text-[8px] font-black uppercase tracking-tighter">{{ doc.ext }}</span>
                  </div>
                  <div>
                    <h4 class="font-serif text-xl font-bold mb-1">{{ doc.name }}</h4>
                    <div class="flex flex-wrap gap-4 items-center">
                      <span class="text-[10px] font-bold text-slate-400 uppercase tracking-widest">Added: {{ doc.date }}</span>
                      <span :class="getStatusClass(doc.status)">{{ doc.status }}</span>
                    </div>
                  </div>
                </div>

                <div class="flex items-center gap-3 self-end md:self-center">
                  <button 
                    @click="previewDocument(doc.url)"
                    class="w-12 h-12 rounded-xl bg-slate-50 text-slate-400 hover:bg-[#1a150e] hover:text-[#f3c969] transition-all">
                    <i class="fas fa-eye"></i>
                  </button>
                  
                  <a :href="doc.url" target="_blank" download class="flex items-center justify-center w-12 h-12 rounded-xl bg-slate-50 text-slate-400 hover:bg-[#1a150e] hover:text-[#f3c969] transition-all">
                    <i class="fas fa-download"></i>
                  </a>

                  <button 
                    @click="handleDelete(doc.id, doc.public_id)"
                    class="w-12 h-12 rounded-xl bg-slate-50 text-red-300 hover:bg-red-500 hover:text-white transition-all">
                    <i class="fas fa-trash-alt"></i>
                  </button>
                </div>
              </div>
            </div>
          </template>

          <div v-else class="text-center py-20 bg-white rounded-[2rem] border-2 border-dashed border-slate-100">
            <i class="fas fa-folder-open text-4xl text-slate-200 mb-4"></i>
            <p class="text-slate-400 text-sm font-medium">No credentials uploaded yet.</p>
          </div>
        </div>

        <div class="space-y-8">
          <div class="bg-[#1a150e] rounded-[2.5rem] p-8 text-white relative overflow-hidden shadow-2xl">
            <div class="relative z-10">
              <h3 class="font-serif text-xl font-bold mb-6 text-[#f3c969]">Active Visas</h3>
              <div class="space-y-6">
                <div v-for="visa in visas" :key="visa.country" class="border-b border-white/10 pb-6 last:border-0">
                  <div class="flex justify-between items-center mb-2">
                    <span class="text-xs font-bold tracking-widest uppercase">{{ visa.country }}</span>
                    <span class="text-[10px] text-emerald-400 font-black uppercase tracking-widest">Valid</span>
                  </div>
                  <div class="text-[10px] text-slate-400 uppercase tracking-widest mb-4">Expires: {{ visa.expiry }}</div>
                  <div class="h-1 bg-white/10 rounded-full overflow-hidden">
                    <div class="h-full bg-emerald-500" :style="{ width: visa.progress + '%' }"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="bg-[#f3c969] rounded-[2.5rem] p-8">
            <i class="fas fa-user-shield text-2xl mb-4 text-[#1a150e]"></i>
            <h4 class="font-serif text-lg font-bold text-[#1a150e] mb-2">Biometric Lock</h4>
            <p class="text-[11px] font-medium text-[#1a150e]/70 leading-relaxed uppercase tracking-tight">
              All documents are protected by AES-256 encryption. Physical copies are available for delivery via Indoria Courier upon request.
            </p>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>





<script setup>
import { ref, onMounted, inject } from 'vue';
import axios from 'axios';

// --- INJECTIONS ---
const setGlobalLoading = inject('setGlobalLoading');

// --- STATE MANAGEMENT ---
const fileInput = ref(null);
const isUploading = ref(false);
const isLoading = ref(true);
const documents = ref([]);

// --- CUSTOM ALERT LOGIC ---
const alerts = ref([]);
let alertCount = 0;

const getIcon = (type) => {
  if (type === 'success') return 'fas fa-shield-check';
  if (type === 'error') return 'fas fa-exclamation-triangle';
  return 'fas fa-bell';
};

const getDefaultTitle = (type) => {
  if (type === 'success') return 'Vault Verified';
  if (type === 'error') return 'System Alert';
  return 'Notification';
};

const notify = (message, type = 'success', duration = 5000) => {
  const id = alertCount++;
  const newAlert = {
    id,
    message,
    type,
    progress: 100,
    offset: alerts.value.length * 90 
  };
  
  alerts.value.push(newAlert);

  const start = Date.now();
  const timer = setInterval(() => {
    const elapsed = Date.now() - start;
    newAlert.progress = Math.max(0, 100 - (elapsed / duration) * 100);
    if (newAlert.progress <= 0) clearInterval(timer);
  }, 10);

  setTimeout(() => removeAlert(id), duration);
};

const removeAlert = (id) => {
  const index = alerts.value.findIndex(a => a.id === id);
  if (index > -1) {
    alerts.value.splice(index, 1);
    alerts.value.forEach((alert, i) => {
      alert.offset = i * 90;
    });
  }
};

const visas = ref([
  { country: 'United Kingdom', expiry: 'Jun 2026', progress: 85 },
  { country: 'United Arab Emirates', expiry: 'Jan 2026', progress: 15 },
]);

// Helper to get token safely
const getAuthHeader = () => {
  const token = localStorage.getItem('user_token');
  if (!token) return {};
  // Ensure we don't double up "Bearer" if it's already in the string
  const prefix = token.startsWith('Bearer ') ? '' : 'Bearer ';
  return { 'Authorization': `${prefix}${token}` };
};


// New helper to get the ID from localstorage
const getCustomHeaders = () => {
  const userData = localStorage.getItem('user_data');
  if (!userData) return {};
  
  const user = JSON.parse(userData);
  // We send X-User-Id to match the new backend requirement
  return { 'X-User-Id': user.id }; 
};

// --- API FETCHING ---

const fetchDocuments = async () => {
  const headers = getCustomHeaders();
  if (!headers['X-User-Id']) {
    notify("Authentication missing. Please sign in.", "error");
    isLoading.value = false;
    return;
  }
  isLoading.value = true;
  try {
    const response = await axios.get('https://travel-xxnc.onrender.com/api/user/documents', { headers });
    
    // Safety check: ensure response data is an array
    const data = Array.isArray(response.data) ? response.data : [];
    
    documents.value = data.map(doc => ({
      id: doc.id,
      public_id: doc.public_id,
      name: doc.doc_name || 'Unnamed Document',
      // Added safety for date parsing
      date: doc.uploaded_at 
        ? new Date(doc.uploaded_at).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
        : 'Recently',
      status: doc.status || 'Pending',
      url: doc.file_url || '#',
      type: doc.doc_type,
      icon: getIconByType(doc.doc_type),
      ext: doc.file_url ? doc.file_url.split('.').pop().toUpperCase().substring(0, 3) : 'DOC'
    }));
  } catch (error) {
    console.error("Error loading documents:", error.response || error);
    if (error.response?.status === 422 || error.response?.status === 401) {
       notify("Token invalid or expired.", "error");
    }
  } finally {
    setTimeout(() => {
    isLoading.value = false;
    }, 600);
  }
};

// --- UPLOAD LOGIC ---

const triggerFileInput = () => {
  fileInput.value.click();
};

const handleFileSelection = async (event) => {
  const file = event.target.files[0];
  if (!file) return;

  const formData = new FormData();
  formData.append('file', file);
  formData.append('doc_type', 'Passport'); 
  formData.append('doc_name', file.name.split('.')[0]);

  isUploading.value = true;

  try {
    const response = await axios.post('https://travel-xxnc.onrender.com/api/user/documents/upload', formData, {
      headers: {
        ...getCustomHeaders(),
        'Content-Type': 'multipart/form-data'
      }
    });

    if (response.data.success) {
      await fetchDocuments(); 
      notify("Credential secured in Indoria Vault.", "success");
    }
  } catch (error) {
    console.error("Upload failed:", error.response?.data || error.message);
    notify("Upload failed. Verify file size and connection.", "error");
  } finally {
    isUploading.value = false;
    event.target.value = ''; // Reset for same-file re-uploads
  }
};

// --- HELPERS ---

const getIconByType = (type) => {
  const icons = {
    'Passport': 'fas fa-address-card',
    'Visa': 'fas fa-stamp',
    'Insurance': 'fas fa-umbrella',
    'Health': 'fas fa-file-medical'
  };
  return icons[type] || 'fas fa-file-alt';
};

const getStatusClass = (status) => {
  const base = "text-[9px] font-black uppercase tracking-widest px-3 py-1 rounded-full border ";
  if (status === 'Verified') return base + "bg-emerald-50 text-emerald-600 border-emerald-100";
  if (status === 'Expired') return base + "bg-red-50 text-red-600 border-red-100";
  return base + "bg-amber-50 text-amber-600 border-amber-100"; 
};

const handleDelete = async (id) => {
  if (!confirm("Permanent deletion from secure vault?")) return;
  try {
    await axios.delete(`https://travel-xxnc.onrender.com/api/user/documents/${id}`, {
      headers: getCustomHeaders()
    });
    documents.value = documents.value.filter(d => d.id !== id);
    notify("Credential deleted from vault.", "success");
  } catch (error) {
    console.error("Delete failed:", error);
    notify("Deletion failed.", "error");
  }
};

const previewDocument = (url) => {
  if (url && url !== '#') window.open(url, '_blank');
  const clearUrl = url.includes('?') ? `${url}&t=${Date.now()}` : `${url}?t=${Date.now()}`;
  window.open(clearUrl, '_blank', 'noopener,noreferrer');
};



onMounted(() => {
  fetchDocuments();
});
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Inter:wght@300;400;600;900&display=swap');

.font-serif { font-family: 'Playfair Display', serif; }
.font-sans { font-family: 'Inter', sans-serif; }

/* Luxury Shadow for the Document Cards */
.shadow-sm {
  /* shadow-color: rgba(26, 21, 14, 0.03); */
  box-shadow: 0 10px 40px -10px rgba(26, 21, 14, 0.05);
}

.hover\:shadow-xl:hover {
  box-shadow: 0 25px 50px -12px rgba(26, 21, 14, 0.12);
}

/* Glassmorphism for the Header Stats */
.bg-white\/5 {
  background-color: rgba(255, 255, 255, 0.05);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
}

/* Custom scrollbar for a cleaner look */
::-webkit-scrollbar {
  width: 6px;
}
::-webkit-scrollbar-track {
  background: #fafaf9;
}
::-webkit-scrollbar-thumb {
  background: #e2e8f0;
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: #f3c969;
}

/* Smooth transition for the "Plus" icon rotation */
.group:hover .fa-plus {
  transform: rotate(90deg);
}

/* Animated Loading Spinner for Upload */
@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.animate-spin {
  animation: spin 1s linear infinite;
}

/* Progress Bar Shine Effect */
.bg-emerald-500 {
  position: relative;
  overflow: hidden;
}
.bg-emerald-500::after {
  content: "";
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.2),
    transparent
  );
  animation: shine 3s infinite;
}

@keyframes shine {
  0% { left: -100%; }
  100% { left: 100%; }
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .rounded-\[2rem\] {
    border-radius: 1.5rem;
  }
  header {
    padding-top: 4rem;
    padding-bottom: 6rem;
  }
}

  

/* --- SKELETON LOADING SYSTEM --- */

/* Base container for skeleton cards */
.skeleton-card {
  position: relative;
  overflow: hidden; /* Clips the shimmer */
  background: white;
  border: 1px solid #e2e8f0; /* slate-100 */
}

/* The Animated Shimmer Layer */
.skeleton-shimmer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    90deg,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 0.8) 50%,
    rgba(255, 255, 255, 0) 80%
  );
  background-size: 200% 100%;
  animation: shimmer-swipe 1.5s infinite linear;
  pointer-events: none;
  z-index: 5;
}

@keyframes shimmer-swipe {
  0% { background-position: -150% 0; }
  100% { background-position: 150% 0; }
}

/* Skeleton Pulse Animation for child elements */
.skeleton-bone {
  background-color: #f1f5f9; /* slate-50 */
  border-radius: 0.5rem;
  position: relative;
  overflow: hidden;
  animation: bone-pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes bone-pulse {
  0%, 100% { background-color: #f1f5f9; }
  50% { background-color: #e2e8f0; }
}

/* Luxury rounded corners consistency */
@media (max-width: 768px) {
  .skeleton-card {
    border-radius: 1.5rem;
  }
}

/* Specific Bone Sizes to match your Template */
.bone-icon { width: 4rem; height: 5rem; border-radius: 0.5rem; }
.bone-title { height: 1.75rem; width: 70%; margin-bottom: 0.5rem; }
.bone-meta { height: 0.75rem; width: 40%; background-color: #e2e8f0; }
.bone-btn { width: 3rem; height: 3rem; border-radius: 0.75rem; }
</style>
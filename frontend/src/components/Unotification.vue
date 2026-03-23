<template>
  <div 
    ref="notificationRef"
    class="fixed inset-x-4 top-20 z-50 mt-0 flex flex-col overflow-hidden rounded-2xl border border-[#f3c969]/20 bg-white shadow-2xl ring-1 ring-black ring-opacity-5 focus:outline-none sm:absolute sm:right-4 sm:top-16 sm:inset-x-auto sm:w-96 origin-top-right transition-all"
  >
    <div class="flex items-center justify-between border-b border-[#f3c969]/10 bg-[#1a150e] px-4 py-3.5">
      <h3 class="text-sm font-bold text-[#f3c969] font-serif tracking-wide">Notifications</h3>
      <div class="flex items-center gap-3">
        <button 
          v-if="notifications.length > 0"
          @click="markAllAsRead" 
          class="text-[11px] font-bold uppercase tracking-widest text-[#f3c969]/80 hover:text-[#f3c969] transition-colors"
        >
          Mark all read
        </button>
        <button @click="$emit('close')" class="rounded-full p-1 text-[#f3c969]/50 hover:bg-white/10 hover:text-[#f3c969] transition-all">
          <svg class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>
    </div>

    <div class="max-h-[calc(100vh-250px)] sm:max-h-[420px] overflow-y-auto overscroll-contain custom-scrollbar bg-[#fcf9f4]/30">
      <div v-if="notifications.length > 0">
        <div 
          v-for="item in notifications" 
          :key="item.id" 
          @click="handleNotificationClick(item)"
          :class="[
            'group relative px-5 py-4 border-b border-[#f3c969]/5 transition-all cursor-pointer hover:bg-white', 
            !item.read ? 'unread-glow' : 'opacity-80'
          ]"
        >
          <div class="flex gap-4">
            <div :class="['mt-1 flex h-9 w-9 flex-shrink-0 items-center justify-center rounded-xl shadow-sm border border-white/20', item.iconBg]">
              <component :is="item.icon" class="h-4 w-4 text-white" />
            </div>

            <div class="flex-1">
              <div class="flex justify-between items-start">
                <p :class="['text-[13px] leading-snug', !item.read ? 'font-bold text-slate-900' : 'text-slate-600 font-medium']">
                  {{ item.title }}
                </p>
                <span class="text-[10px] font-bold text-slate-400 whitespace-nowrap ml-2 uppercase tracking-tighter">{{ item.time }}</span>
              </div>
              <p class="text-xs text-slate-500 mt-1 leading-relaxed line-clamp-2">
                {{ item.message }}
              </p>
            </div>

            <div v-if="!item.read" class="absolute left-1.5 top-1/2 -translate-y-1/2 w-1.5 h-1.5 bg-[#e8b34b] rounded-full shadow-[0_0_8px_#f3c969]"></div>
          </div>
        </div>
      </div>

      <div v-else class="py-16 text-center">
        <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-[#fcf9f4] border border-[#f3c969]/20 text-[#e8b34b] mb-4 shadow-inner">
          <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v1m6 0H9" />
          </svg>
        </div>
        <p class="brand-gold-text text-sm font-bold uppercase tracking-widest">All caught up</p>
        <p class="text-xs text-slate-400 mt-1 font-medium">Your heritage journey is on track</p>
      </div>
    </div>

    <div class="bg-[#fcf9f4] px-4 py-3 border-t border-[#f3c969]/10">
      <button class="view-all-btn">
        View All Notifications
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { Plane, CheckCircle, Gift } from 'lucide-vue-next';

const emit = defineEmits(['close']);
const notificationRef = ref(null);

const notifications = ref([
  {
    id: 1,
    title: 'Flight Delayed',
    message: 'Your flight to Paris (AF202) is delayed by 45 mins. Check gate for updates.',
    time: '2m ago',
    read: false,
    iconBg: 'bg-red-500',
    icon: Plane
  },
  {
    id: 2,
    title: 'Booking Confirmed',
    message: 'Hotel Hilton Tokyo is now confirmed. View your itinerary for details.',
    time: '3h ago',
    read: true,
    iconBg: 'bg-emerald-600',
    icon: CheckCircle
  },
  {
    id: 3,
    title: 'New Reward Earned',
    message: 'You just earned 500 bonus points from your last trip to Bali!',
    time: '1d ago',
    read: true,
    iconBg: 'bg-[#e8b34b]',
    icon: Gift
  }
]);

const markAllAsRead = () => {
  notifications.value.forEach(n => n.read = true);
};

const handleNotificationClick = (item) => {
  item.read = true;
  // logic to navigate
};

const handleClickOutside = (event) => {
  if (notificationRef.value && !notificationRef.value.contains(event.target)) {
    emit('close');
  }
};

onMounted(() => {
  setTimeout(() => {
    document.addEventListener('click', handleClickOutside);
  }, 10);
});

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside);
});
</script>

<style scoped>
.font-serif {
  font-family: Georgia, 'Times New Roman', serif;
}

.brand-gold-text {
  background: linear-gradient(90deg, #f3c969, #e8b34b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.unread-glow {
  background-color: rgba(243, 201, 105, 0.04);
}

.view-all-btn {
  width: 100%;
  border-radius: 0.75rem;
  background: white;
  border: 1px solid rgba(243, 201, 105, 0.3);
  padding: 0.625rem;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: #475569;
  transition: all 0.2s;
  box-shadow: 0 2px 4px rgba(0,0,0,0.02);
}

.view-all-btn:hover {
  background-color: #1a150e;
  color: #f3c969;
  border-color: #1a150e;
}

/* Custom Scrollbar */
.custom-scrollbar::-webkit-scrollbar {
  width: 4px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: #f3c969;
  border-radius: 10px;
}
.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background: #e8b34b;
}
</style>
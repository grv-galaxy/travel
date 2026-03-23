<template>
  <div class="concierge-container">
    <div class="concierge-layout">
      
      <aside class="request-sidebar" :class="{ 'mobile-hidden': activeChat }">
        <div class="sidebar-header">
          <h2 class="text-white font-bold text-xl uppercase tracking-tighter">Live Requests</h2>
          <span class="online-indicator"></span>
        </div>
        
        <div class="request-list">
          <div 
            v-for="req in requests" 
            :key="req.id" 
            class="request-item"
            :class="{ 'active': selectedRequestId === req.id }"
            @click="selectedRequestId = req.id"
          >
            <div class="item-top">
              <span class="text-white font-bold text-sm">{{ req.vipName }}</span>
              <span class="time">{{ req.time }}</span>
            </div>
            <p class="preview text-slate-400">{{ req.lastMessage }}</p>
            <div class="tags">
              <span class="category" :class="req.priority">{{ req.category }}</span>
            </div>
          </div>
        </div>
      </aside>

      <main class="chat-area" :class="{ 'mobile-visible': activeChat }">
        <header class="chat-header">
          <button class="hide-desktop back-btn" @click="activeChat = null">
            <i class="fa-solid fa-chevron-left"></i>
          </button>
          <div class="user-meta">
            <h3 class="text-white font-bold">{{ activeRequest.vipName }}</h3>
            <span class="text-[#c5a059] text-[10px] font-bold uppercase tracking-widest">Protocol: {{ activeRequest.priority }}</span>
          </div>
          <div class="header-actions">
            <button class="action-icon"><i class="fa-solid fa-phone"></i></button>
            <button class="action-icon"><i class="fa-solid fa-shield-halved"></i></button>
          </div>
        </header>

        <div class="chat-messages">
          <div v-for="msg in messages" :key="msg.id" :class="['message', msg.sender]">
            <div class="message-content">
              <p class="font-medium">{{ msg.text }}</p>
              <span class="msg-time">{{ msg.time }}</span>
            </div>
          </div>
        </div>

        <footer class="chat-input-area">
          <div class="input-wrapper">
            <button class="attach-btn"><i class="fa-solid fa-plus"></i></button>
            <input type="text" placeholder="Type instructions for VIP..." v-model="newMessage" />
            <button class="send-btn"><i class="fa-solid fa-paper-plane"></i></button>
          </div>
        </footer>
      </main>

      <aside class="intelligence-panel">
        <div class="panel-section">
          <h4 class="section-label">VIP Status</h4>
          <div class="vip-card">
            <img src="https://i.pravatar.cc/150?u=9" alt="VIP" class="vip-avatar" />
            <div class="text-center mt-3">
              <p class="text-white font-bold">Maharaja Vikram</p>
              <span class="tier-gold">ELITE MEMBER</span>
            </div>
          </div>
        </div>

        <div class="panel-section">
          <h4 class="section-label">Active Deployment</h4>
          <div class="asset-mini-card">
            <i class="fa-solid fa-car-side text-[#c5a059]"></i>
            <div>
              <p class="text-white font-bold text-xs">Phantom VIP-001</p>
              <p class="text-slate-500 text-[10px]">Driver: Arjun S.</p>
            </div>
          </div>
        </div>

        <button class="resolve-btn">Resolve Request</button>
      </aside>

    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const selectedRequestId = ref(1);
const activeChat = ref(true); // For mobile toggle
const newMessage = ref('');

const requests = ref([
  { id: 1, vipName: 'Maharaja Vikram', lastMessage: 'Need security detail for tonight...', time: '2m ago', category: 'Security', priority: 'high' },
  { id: 2, vipName: 'Sonia Malhotra', lastMessage: 'Dinner reservation for 10 confirmed?', time: '15m ago', category: 'Dining', priority: 'medium' },
  { id: 3, vipName: 'Elena Rodriguez', lastMessage: 'Flight delay at London Heathrow.', time: '1h ago', category: 'Logistics', priority: 'urgent' },
]);

const messages = ref([
  { id: 1, sender: 'vip', text: 'I require a private security detail for the Gala at 9 PM.', time: '14:20' },
  { id: 2, sender: 'admin', text: 'Protocol initialized. Elite Team B has been assigned to your location.', time: '14:22' },
  { id: 3, sender: 'vip', text: 'Excellent. Ensure the Phantom is waiting.', time: '14:25' },
]);

const activeRequest = computed(() => requests.value.find(r => r.id === selectedRequestId.value));
</script>

<style scoped>
.concierge-container {
  height: calc(100vh - 120px);
  animation: fadeIn 0.5s ease;
}

.concierge-layout {
  display: grid;
  grid-template-columns: 320px 1fr 280px;
  height: 100%;
  background: #080808;
  border-radius: 20px;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.05);
}

/* Sidebar */
.request-sidebar {
  background: #0c0c0c;
  border-right: 1px solid rgba(255,255,255,0.05);
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid rgba(255,255,255,0.03);
}

.online-indicator { width: 8px; height: 8px; background: #00ff88; border-radius: 50%; box-shadow: 0 0 10px #00ff88; }

.request-list { flex: 1; overflow-y: auto; }

.request-item {
  padding: 1.2rem;
  border-bottom: 1px solid rgba(255,255,255,0.02);
  cursor: pointer;
  transition: 0.3s;
}

.request-item:hover, .request-item.active { background: rgba(197, 160, 89, 0.05); }
.request-item.active { border-left: 3px solid #c5a059; }

.item-top { display: flex; justify-content: space-between; margin-bottom: 4px; }
.time { font-size: 10px; color: #555; font-weight: bold; }
.preview { font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

.category {
  font-size: 9px; font-weight: 900; text-transform: uppercase;
  padding: 2px 8px; border-radius: 4px; margin-top: 8px; display: inline-block;
}
.category.high { background: rgba(255, 77, 77, 0.1); color: #ff4d4d; }
.category.urgent { background: #ff4d4d; color: white; }
.category.medium { background: rgba(197, 160, 89, 0.1); color: #c5a059; }

/* Chat Area */
.chat-area { display: flex; flex-direction: column; background: #0f0f0f; }

.chat-header {
  padding: 1rem 2rem;
  background: #111;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}

.chat-messages { flex: 1; padding: 2rem; overflow-y: auto; display: flex; flex-direction: column; gap: 1.5rem; }

.message { max-width: 70%; display: flex; flex-direction: column; }
.message.admin { align-self: flex-end; }
.message.vip { align-self: flex-start; }

.message-content {
  padding: 1rem;
  border-radius: 15px;
  font-size: 13px;
  position: relative;
}

.admin .message-content { background: #c5a059; color: black; border-bottom-right-radius: 2px; }
.vip .message-content { background: #1a1a1a; color: white; border-bottom-left-radius: 2px; border: 1px solid rgba(255,255,255,0.1); }

.msg-time { font-size: 9px; opacity: 0.6; margin-top: 5px; display: block; }

.chat-input-area { padding: 1.5rem 2rem; background: #0c0c0c; }
.input-wrapper {
  background: #1a1a1a;
  border-radius: 12px;
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  gap: 1rem;
}

.input-wrapper input { background: transparent; border: none; color: white; flex: 1; outline: none; font-size: 14px; }

/* Intelligence Panel */
.intelligence-panel {
  background: #0c0c0c;
  border-left: 1px solid rgba(255,255,255,0.05);
  padding: 1.5rem;
}

.section-label { color: #555; font-size: 10px; font-weight: 900; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1rem; }

.vip-avatar { width: 80px; height: 80px; border-radius: 50%; border: 2px solid #c5a059; margin: 0 auto; display: block; }
.tier-gold { color: #c5a059; font-size: 10px; font-weight: 900; letter-spacing: 2px; }

.asset-mini-card {
  background: #151515; padding: 12px; border-radius: 12px;
  display: flex; align-items: center; gap: 12px; border: 1px solid rgba(255,255,255,0.05);
}

.resolve-btn {
  width: 100%; margin-top: 2rem; padding: 12px;
  background: white; color: black; border: none;
  border-radius: 10px; font-weight: 800; text-transform: uppercase; font-size: 11px; cursor: pointer;
}

@media (max-width: 1100px) { .intelligence-panel { display: none; } .concierge-layout { grid-template-columns: 300px 1fr; } }

@media (max-width: 768px) {
  .concierge-layout { grid-template-columns: 1fr; }
  .mobile-hidden { display: none; }
  .chat-area { display: none; }
  .chat-area.mobile-visible { display: flex; position: absolute; inset: 0; z-index: 100; }
  .back-btn { background: none; border: none; color: white; font-size: 1.2rem; margin-right: 1rem; }
}
</style>
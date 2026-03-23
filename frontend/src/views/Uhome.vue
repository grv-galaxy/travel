<template>
  <div class="flex flex-col h-screen bg-[#f8f7f4] overflow-hidden">
    <UHeader />

    <div class="flex-1 h-[calc(100vh-64px)] overflow-hidden">
      <Uslider /> 
    </div>
  </div>
</template>

<script setup>
import UHeader from '../components/Uheader.vue';
import Uslider from '../components/Uslider.vue';
</script>
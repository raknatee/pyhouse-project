
<template>
  <router-view></router-view>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'
import { UserService } from './service/UserService'

export default defineComponent({
  setup() {
    onMounted(async()=>{
      await UserService.getInstance().fetch()
    })
  },
})
</script>

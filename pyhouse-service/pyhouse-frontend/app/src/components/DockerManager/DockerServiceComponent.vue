<template>
    <h1>Your Service(s) / Container(s)</h1>
    <template v-for="containerInfo in containerInfos" :key="containerInfo.containerName">
        <DockerServieInfoVue :containerName="containerInfo.containerName" :basedImage="containerInfo.basedImage" />
    </template>
</template>

<script lang="ts">
import { defineComponent, onMounted } from 'vue'
import { DockerService } from './DockerService';
import DockerServieInfoVue from './components/DockerServieInfo.vue';
export default defineComponent({
    components:{
        DockerServieInfoVue
    },
    setup() {
        const containerInfos = DockerService.getInstance().containerInfos
        onMounted(()=>{
            DockerService.getInstance().fetch()
        })
        return {containerInfos}
    },
})
</script>

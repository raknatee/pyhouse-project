<template>
    <h2>{{props.containerName}}</h2>
    <h2>{{props.basedImage}}</h2>
    <a :href="jupyterUrl" target="_blank" >JupyterLab</a>
    <hr>
</template>


<script setup lang="ts">import { ref } from 'vue';
import { UserService } from '../../../service/UserService';

interface Props {
    containerName: string
    basedImage: string
}
const props = defineProps<Props>();
const username = UserService.getInstance().getUsernameRef()
const jupyterUrl = ref("")
jupyterUrl.value = `/container/${username.value}/${props.containerName}`

</script>

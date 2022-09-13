<template>
    <h2>{{props.containerName}}</h2>
    <h2>{{props.basedImage}}</h2>
    <a :href="jupyterUrl" target="_blank" :class="{'non-clickable':!isContainerUp}">Click here for JupyterLab</a>
    <button @click="removeService()" >delete this service</button>
    <hr>
</template>

<style lang="scss" scoped>
.non-clickable {
    pointer-events: none;
    text-decoration: line-through;
}
</style>
<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { restAPIGet, restAPIMethod } from '../../../script/RestAPIHelper';
import { UserService } from '../../../service/UserService';
import {sleep} from "../../../script/Time"
import { DockerService } from '../DockerService';
interface Props {
    containerName: string
    basedImage: string
}
const props = defineProps<Props>();
const username = UserService.getInstance().getUsernameRef()
const jupyterUrl = ref("")
jupyterUrl.value = `/container/${username.value}/${props.containerName}`

const isContainerUp = ref(false)

onMounted(async () => {

        const ff = async() => {
            await restAPIGet(`/manager/api/container?filter_name=${props.containerName}`, () => {
            isContainerUp.value = true
        }, async() => { 
            await sleep(1000)
            await ff() })
        }
        await ff()
        

})
async function removeService(){
            await restAPIMethod(`/manager/api/container?filter_name=${props.containerName}`,"DELETE",null,async (resp:Response)=>{
                await DockerService.getInstance().fetch()
            },(resp:Response)=>{
                console.log(resp)
            })
        }


</script>



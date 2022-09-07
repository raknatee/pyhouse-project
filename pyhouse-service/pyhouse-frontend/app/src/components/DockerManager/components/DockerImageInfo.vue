<template>
     <h2>{{imagename}}</h2>
        <h3>Configurations</h3>
        <label>Attach GPU</label><button disabled>False</button>
        <br>
        <button @click="createContainer()" :disabled="disableCreateContainer">Create the Container from this Image</button>
        <hr>
</template>

<script lang="ts">
import { defineComponent, ref, defineProps } from 'vue'
import { restAPIMethod } from '../../../script/RestAPIHelper'
import { DockerService } from '../DockerService'

export default defineComponent({
    props:{
        imagename:String
    },
    setup(props) {
        // interface Props{
        //     imagename:string
        // }
        // const props = defineProps<Props>()

        const imagename = props.imagename
        const isGPU = ref(false)
        const disableCreateContainer = ref(false)

        async function createContainer():Promise<void>{
            disableCreateContainer.value = true
        await restAPIMethod('/manager/api/create_container',"POST",{
          "docker_image_name": props.imagename,
          "attach_gpu":isGPU.value
        },
        async (resp:Response)=>{
            let jsonData = await resp.json()
            console.log(jsonData)
            disableCreateContainer.value = false
            DockerService.getInstance().fetch()
        },()=>{}
        )
    }
        return {"imagename":imagename,"createContainer":createContainer,disableCreateContainer}
    },
})
</script>

<template>

  <br>
  <div class="nar">
    <p>I'm {{username}}</p>
    <router-link to="/login">Login</router-link>
  <router-link to="/register">Register</router-link>
  <router-link to="/forget-mypassword">Forget password</router-link>
  </div>
  <div>
    <h1>Builded Docker Image</h1>
    <div v-for="imagename in dockerImageNames" :key="imagename">
      {{imagename}}

    </div>
  </div>

 
</template>


<script lang="ts">
import { defineComponent,onMounted, Ref, ref } from 'vue'
import { restAPIGet } from '../script/RestAPIHelper';
import { UserService } from '../service/UserService';

export default defineComponent({
  setup() {
    let dockerImageNames:Ref<string[]>= ref([]);
    onMounted(async()=>{
       await restAPIGet("/manager/api/images",async (resp:Response)=>{
        type ImageNames = {
          'images':string[]
        }
        let jsonData:ImageNames = await resp.json();
        console.log(jsonData)
        dockerImageNames.value = jsonData.images

      },()=>{
        console.log("Hello")
      })
    })

    let username= UserService.getInstance().getUsernameRef()
    console.log(username.value)


    return {
      dockerImageNames,
      username
    }
  },
})
</script>

<style lang="scss" scoped>
a {
  display: grid;
}
.nar{
  display: flex;
  gap: 10rem;
}
</style>
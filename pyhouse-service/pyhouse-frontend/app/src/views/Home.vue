<template>

  <br>
  <div class="nar">
    <p>I'm {{username}}</p>
    <router-link to="/login">Login</router-link>
  <router-link to="/register">Register</router-link>
  <router-link to="/forget-mypassword">Forget password</router-link>
  </div>


  <DockerImageComponentVue/>
  <DockerServiceComponentVue/>
  
</template>


<script lang="ts">
import { defineComponent,onMounted, Ref, ref } from 'vue'
import { restAPIGet } from '../script/RestAPIHelper';
import { UserService } from '../service/UserService';
import DockerImageComponentVue from '../components/DockerManager/DockerImageComponent.vue';
import DockerServiceComponentVue from '../components/DockerManager/DockerServiceComponent.vue';
export default defineComponent({
  components:{
    DockerImageComponentVue,
    DockerServiceComponentVue
  },
  setup() {
   

    let username= UserService.getInstance().getUsernameRef()
    console.log(username.value)


    return {
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
<template>
  <h1>Builded Docker Image</h1>
  <template v-for="imagename in dockerImageNames" :key="imagename">
  
  <DockerImageInfoVue :imagename="imagename"></DockerImageInfoVue>     
    
  </template>
 
</template>
<script lang="ts">
import { defineComponent, onMounted, Ref, ref } from "vue";
import { restAPIGet, restAPIMethod } from "../../script/RestAPIHelper";
import DockerImageInfoVue from "./components/DockerImageInfo.vue";
export default defineComponent({
  components: {
    DockerImageInfoVue,
  },
  setup() {
    let dockerImageNames: Ref<string[]> = ref([]);
    onMounted(async () => {
      await restAPIGet(
        "/manager/api/images",
        async (resp: Response) => {
          type ImageNames = {
            images: string[];
          };
          let jsonData: ImageNames = await resp.json();
          console.log(jsonData);
          dockerImageNames.value = jsonData.images;
        },
        () => {
          console.log("Hello");
        }
      );
    });

    return { dockerImageNames};
  },
});
</script>

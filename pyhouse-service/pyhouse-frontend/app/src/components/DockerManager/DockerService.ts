import { ref, Ref } from "vue";
import { restAPIGet } from "../../script/RestAPIHelper";

class ContainerInfo{
    containerName:string
    basedImage:string
    constructor(containerName:string,basedImage:string){
        this.containerName = containerName;
        this.basedImage = basedImage;
    }
}
class DockerService{
    
    private static instance:DockerService|undefined
    containerInfos:Ref<ContainerInfo[]>

    private constructor(){
        this.containerInfos = ref([])
    }

    public static getInstance():DockerService{
        if(DockerService.instance === undefined){
            DockerService.instance = new DockerService()
        }
        return DockerService.instance
    }

    public async fetch():Promise<void>{
        this.containerInfos.value = []
        await restAPIGet("/manager/api/containers",async (resp:Response)=>{
            type Output={
                "services":string[][]
            }
            let jsonData:Output = await resp.json()
            for(let i=0;i<jsonData.services.length;i++){
                let t = new ContainerInfo(jsonData.services[i][0],jsonData.services[i][1])
                this.containerInfos.value.push(t)
            }
           
            
        },
        () =>{})
    }
    
}

export {DockerService}
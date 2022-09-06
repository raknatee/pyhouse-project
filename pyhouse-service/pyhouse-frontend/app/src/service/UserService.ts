import { ref, Ref } from "vue";
import { restAPIGet } from "../script/RestAPIHelper";

class UserService{
    private static instance: UserService;
    private user_id:string|undefined
    private username:string|undefined
    private usernameRef:Ref<string>
    private constructor(){
        this.usernameRef = ref("")
    }
    public static getInstance():UserService{
        if(UserService.instance === undefined || UserService.instance === null){
            UserService.instance = new UserService();
        }
        return UserService.instance
    }
    async fetch(){
        await restAPIGet('/manager/api/who_am_i',async (resp:Response)=>{
            const jsonData = await resp.json()
            this.username = jsonData['username']
            this.usernameRef.value = this.username!
            this.user_id = jsonData['user_id']
        },(resp:Response)=>{
            console.log(resp.status)
        })
    }
    getUsernameRef():Ref<string>{
        return this.usernameRef;
    }
}


export {UserService}
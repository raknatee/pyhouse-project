const restAPIGet = async(path:string,onSuccess:(resp:Response)=>void, onFailure:(resp:Response)=>void):Promise<any> => {
    const resp:Response = await fetch(path, { method: "GET" })
    if (resp.status === 200) {
        onSuccess(resp)
    } else {
        onFailure(resp)
        
    }
}

const restAPIMethod = async(path:string, method:string, body:any, onSuccess:(resp:Response) => void, onFailure:(resp:Response) => void) => {
    
    const resp = await fetch(path, {
        method,
        headers: {
            'Content-Type': 'application/json'
        },
        "body": JSON.stringify(body)
    })
    if (resp.status === 200) {
        onSuccess(resp)
    } else {
        onFailure(resp)
    }
}

export { restAPIGet, restAPIMethod }
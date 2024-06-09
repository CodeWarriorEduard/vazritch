import axios from "axios";

class HttpClient{

    private axiosInstance;

    constructor(url:string){
        this.axiosInstance = axios.create({baseURL: url});
    }

    get axiosProperties(){
        return this.axiosInstance;
    }

    getMethod(url:string, options={}) {
        return this.axiosInstance.get(url, options)
         
    }

    postMethod(url: string, data?:string|null|undefined, options={}){
        return this.axiosInstance.post(url, data, options)
    }

}


export default HttpClient;
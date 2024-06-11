import axios from "axios";

class HttpClient{

    private axiosInstance;

    constructor(url: string) {
        this.axiosInstance = axios.create({
            baseURL: url,
            headers: { 'Content-Type': 'application/json' }
        });
    }
    
    get axiosProperties(){
        return this.axiosInstance;
    }

    getMethod(url:string, options={}) {
        return this.axiosInstance.get(url, options)
         
    }

    postMethod(url: string, data: string|null|undefined, params = {}) {
        console.log(params)
        return this.axiosInstance.post(url, data, { params });
    }

}


export default HttpClient;
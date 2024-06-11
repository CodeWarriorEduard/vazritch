/* eslint-disable no-useless-catch */

import HttpClient from "../adapters/Axios.adapter";


const url = process.env.REACT_APP_BACKEND;
const client = new HttpClient(url?? '');


async function getHealth(endpoint:string){

    try {
        const response = await client.getMethod(endpoint);
        return response.data;
    } catch (error) {
        throw error;
    }
}

async function processCode(endpoint: string, data:string|null|undefined, options = {}) {

    try {
        const response = await client.postMethod(endpoint, data ,options);
        console.log(response)
        return response.data;
    } catch (error) {
        throw error;
    }
}



export {getHealth, processCode}
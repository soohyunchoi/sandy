import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class SurfSpotService{

    constructor(){}


    getSurfSpots() {
        const url = `${API_URL}/api/surfspots/`;
        return axios.get(url).then(response => response.data);
    }
    getSurfSpotsByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
    getSurfSpot(pk) {
        const url = `${API_URL}/api/surfspots/${pk}`;
        return axios.get(url).then(response => response.data);
    }
    deleteSurfSpot(surfspot){
        const url = `${API_URL}/api/surfspots/${surfspot.pk}`;
        return axios.delete(url);
    }
    createSurfSpot(surfspot){
        const url = `${API_URL}/api/surfspots/`;
        return axios.post(url,surfspot);
    }
    updateSurfSpot(surfspot){
        const url = `${API_URL}/api/surfspots/${surfspot.pk}`;
        return axios.put(url,surfspot);
    }
}
import { type Plant } from '../types/plant';

const API_URL = 'http://localhost:5239/api/plant';

export const fetchPlants = async (): Promise<Plant[]> => {
    const response = await fetch(API_URL);

    if (!response.ok) {
        throw new Error(`Failed to fetch ${response.statusText}`)
    }

    return response.json();
}
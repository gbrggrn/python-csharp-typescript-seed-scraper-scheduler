import { type Garden } from '../types/garden';

const API_URL = '/api/garden';

export const fetchGardens = async (): Promise<Garden[]> => {
    const response = await fetch(API_URL);

    if (!response.ok) {
        throw new Error(`Failed to fetch ${response.statusText}`)
    }

    return response.json();
}
import { type Garden } from '../types/garden';

const API_URL = '/api/garden';

export const fetchGardens = async (): Promise<Garden[]> => {
    const response = await fetch(API_URL);

    if (!response.ok) {
        throw new Error(`Failed to fetch ${response.statusText}`)
    }

    return response.json();
}

export default async function postGarden(name: string, lat: string, lon: string): Promise<boolean> {
    const payload = {
        Name: name,
        Latitude: parseFloat(lat),
        Longitude: parseFloat(lon)
    }

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {'Content-type': 'application/json'},
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            return true;
        }
    } catch (error) {
        console.error("Failed to save garden...", error)
        return false;
    }

    return false;
}
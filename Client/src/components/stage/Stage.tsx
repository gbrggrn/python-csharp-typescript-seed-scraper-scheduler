import { type Plant } from '../types/plant'

interface StageProps {
    selectedIds: string [];
    allPlants: Plant[];
}

export default function Stage({ selectedIds, allPlants }: StageProps) {
    const activePlants = allPlants.filter(p => selectedIds.includes(p.uid))

    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Okt', 'Nov', 'Dec']

    
}
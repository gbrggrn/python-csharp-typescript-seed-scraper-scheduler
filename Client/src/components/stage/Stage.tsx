import { type Plant } from '../types/plant'

interface StageProps {
    selectedIds: string [];
    allPlants: Plant[];
}

export default function Stage({ selectedIds, allPlants }: StageProps) {
    const activePlants = allPlants.filter(p => selectedIds.includes(p.uid))

    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Okt', 'Nov', 'Dec']

    return (
        <main className="stage">
            <h2>Såddschema</h2>
            
            <div className="gantt-chart">
                {/* HEADER */}
                <div className="chart-row header-row">
                    <div className="cell-name">Grönsak</div>
                    { months.map(m => <div key={m} className="cell-month">{m}</div>)}
                </div>

                
            </div>
        </main>
    )
}
import './Stage.css'
import { type Plant } from '../../types/plant'

interface StageProps {
    selectedIds: number [];
    allPlants: Plant[];
}

export default function Stage({ selectedIds, allPlants }: StageProps) {
    const activePlants = allPlants.filter(p => selectedIds.includes(p.id))

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

                {/* DATA ROWS */}
                { activePlants.map(plant => (
                    <div key="{plant.id}" className="chart-row">
                        <div className="cell-name">{plant.name}</div>

                    {/* TIMELINE */}
                    <div className="timeline-track">
                        <div className="sow-bar"
                            style={{
                                gridColumnStart: plant.minSowMonth + 1,
                                gridColumnEnd: plant.maxSowMonth + 2
                            }}
                            >Såddfönster</div>
                        <div className="harvest-bar"
                            style={{
                                gridColumnStart: plant.minHarvestMonth + 1,
                                gridColumnEnd: plant.maxHarvestMonth + 2
                            }}
                            >Skördefönster</div>
                    </div>
                </div>
                ))}
                { activePlants.length === 0 && (
                    <div className="empty-stage">Välj grönsaker för att generera såddschema</div>
                )}
            </div>
        </main>
    )
}
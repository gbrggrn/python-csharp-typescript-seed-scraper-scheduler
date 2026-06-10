import type { Plant } from "../../types/plant";

export function RenderSowTrack(plant: Plant) : React.ReactNode {
    const startSow = plant.minSowMonth;
    const endSow = plant.maxSowMonth;
    const startHarvest = plant.minHarvestMonth;
    const endHarvest = plant.maxHarvestMonth;

    switch(true) {

        case (!startSow && !endSow && !startHarvest && !endHarvest):
            return <span className="no-data-text">Ingen sådd- eller skördedata tillgänglig</span>
        
        case (startSow && !endSow && !startHarvest && !endHarvest):
            return (
            <div className="timeline-track">
                <div className="sow-bar" 
                    style={{ 
                        gridColumnStart: startSow, 
                        gridColumnEnd: startSow + 1 }}
                        >
                        Såddfönster
                </div>
                <span className="no-data-text">Ingen skördedata tillgänglig</span>
            </div>);

        case (startSow && endSow && !startHarvest && !endHarvest):
            return (
            <div className="timeline-track">
                <div className="sow-bar" 
                    style={{ 
                        gridColumnStart: startSow, 
                        gridColumnEnd: endSow + 1 }}
                        >
                        Såddfönster
                </div>
                <span className="no-data-text">Ingen skördedata tillgänglig</span>
            </div>);

        case (startSow && endSow && startHarvest && !endHarvest):
            return (
            <div className="timeline-track">
                <div className="sow-bar" 
                    style={{ 
                        gridColumnStart: startSow, 
                        gridColumnEnd: endSow + 1 
                    }}>
                        Såddfönster
                </div>
                <div className="harvest-bar"
                    style={{
                        gridColumnStart: startHarvest,
                        gridColumnEnd: startHarvest + 1
                    }}>
                        Skördefönster
                </div>
            </div>);

        default:
            return (
            <div className="timeline-track">
                <div className="sow-bar" 
                    style={{ 
                        gridColumnStart: startSow, 
                        gridColumnEnd: endSow + 1 
                    }}>
                        Såddfönster
                </div>
                <div className="harvest-bar"
                    style={{
                        gridColumnStart: startHarvest,
                        gridColumnEnd: endHarvest + 1
                    }}>
                        Skördefönster
                </div>
            </div>);
    }
}
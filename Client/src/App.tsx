import { useState } from 'react'
import { useEffect } from 'react'
import Header from './components/header/Header'
import Sidebar from './components/sidebar/Sidebar'
import Stage from './components/stage/Stage'
import { type Plant } from './types/plant'
import { type Garden } from './types/garden'
import { fetchPlants } from './services/plantService'
import './App.css'

export function App() {
  const [plants, setPlants] = useState<Plant[]>([]);
  const [selectedIds, setSelectedIds] = useState<number[]>([])
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  const handleToggleSelect = (id:number) => {
    setSelectedIds((prev) => {
      if (prev.includes(id)) {
        return prev.filter(rid => rid !== id);
      } else {
        return [...prev, id];
      }
    });
  };

  useEffect(() => {
    const loadData = async () => {
      try {
        setLoading(true);
        const plants = await fetchPlants();
        setPlants(plants);
      } catch (err) {
        setError("Failed to load plants.");
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const [detailsPlant, setDetailsPlant] = useState<Plant | null>(null);
  const [detailsGarden, setDetailsGarden] = useState<Garden | null>(null);
  const clearSelectedIds = () => { setSelectedIds([])}
  const [isGardenModal, setIsGardenModal] = useState<false | true>(Boolean);
  const [gardenName, setGardenName] = useState<string>("");
  const [lat, setLat] = useState<string>("");
  const [lon, setLon] = useState<string>("");

  return (
    <div className="ide-wrapper">
      <Header />
      <div className="workspace">
        <Sidebar 
          plants={plants}
          selectedIds={selectedIds}
          onToggle={handleToggleSelect}
          onClear={clearSelectedIds}
          onDoubleClickPlant={(plant) => setDetailsPlant(plant)}
          onAddGarden={() => setIsGardenModal(true)} />

        {detailsPlant && (
          <div className="modal-overlay" onClick={() => setDetailsPlant(null)}>
            <div className="modal-window" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h3>{ detailsPlant.name }</h3>
                <button className="modal-close" onClick={() => setDetailsPlant(null)}>X</button>
              </div>
              <div className="modal-body">
                <p>Tidigast sådd: { monthHelper(detailsPlant.minSowMonth) }</p>
                <p>Senast sådd: { monthHelper(detailsPlant.maxSowMonth) }</p>
                <p>Tidigast grodd: { detailsPlant.minGerminationDays } dagar</p>
                <p>Senaste grodd: { detailsPlant.maxGerminationDays } dagar</p>
                <p>Plantavstånd: { detailsPlant.plantSpacing }cm</p>
                <p>Radavstånd: { detailsPlant.rowSpacing }cm</p>
                <p>Tidigast skörd: { monthHelper(detailsPlant.minHarvestMonth) }</p>
                <p>Senast skörd: { monthHelper(detailsPlant.maxHarvestMonth) }</p>
                <p>Maxhöjd: { detailsPlant.maxHeight }cm</p>
              </div>
            </div>
          </div>
        )}

        {isGardenModal && (
          <div className="modal-overlay" onClick={() => setIsGardenModal(false)}>
            <div className="modal-window" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h3>Lägg till en trädgård</h3>
                <button className="modal-close" onClick={() => setIsGardenModal(false)}>X</button>
              </div>
              <div className="modal-body">
                <form onSubmit=
              </div>
            </div>
          </div>
        )}
        <Stage 
          allPlants = {plants}
          selectedIds={selectedIds}/>
      </div>
      {error && <div className="status-bar error">{error}</div>}
    </div>
  );
}

function monthHelper (month: number): string {
  if (month == 1)
    return 'januari'
  if (month == 2)
    return 'februari'
  if (month == 3)
    return 'mars'
  if (month == 4)
    return 'april'
  if (month == 5)
    return 'maj'
  if (month == 6)
    return 'juni'
  if (month == 7)
    return 'juli'
  if (month == 8)
    return 'augusti'
  if (month == 9)
    return 'september'
  if (month == 10)
    return 'oktober'
  if (month == 11)
    return 'november'
  if (month == 12)
    return 'december'
  else
    return 'ingen månad registrerad'
}
import { useState } from 'react'
import { useEffect } from 'react'
import Header from './components/header/Header'
import Sidebar from './components/sidebar/Sidebar'
import Stage from './components/stage/Stage'
import { type Plant } from './types/plant'
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
        const data = await fetchPlants();
        setPlants(data);
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

  return (
    <div className="ide-wrapper">
      <Header />
      <div className="workspace">
        <Sidebar 
          plants={plants}
          selectedIds={selectedIds}
          onToggle={handleToggleSelect}
          onDoubleClickPlant={(plant) => setDetailsPlant(plant)} />

        {detailsPlant && (
          <div className="modal-overlay" onClick={() => setDetailsPlant(null)}>
            <div className="modal-window" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h3>Plant Details: { detailsPlant.name }</h3>
                <button className="modal-close" onClick={() => setDetailsPlant(null)}>X</button>
              </div>
              <div className="modal-body">
                <p>Tidigast sådd: { monthHelper(detailsPlant.minSowMonth) }</p>
                <p>Senast sådd: { detailsPlant.maxSowMonth }</p>
                <p>Tidigast grodd: { detailsPlant.minGerminationDays }</p>
                <p>Senaste grodd: { detailsPlant.maxGerminationDays }</p>
                <p>Plantavstånd: { detailsPlant.plantSpacing }cm</p>
                <p>Radavstånd: { detailsPlant.rowSpacing }cm</p>
                <p>Tidigast skörd: { detailsPlant.minHarvestMonth }</p>
                <p>Senast skörd: { detailsPlant.maxHarvestMonth }</p>
                <p>Maxhöjd: { detailsPlant.maxHeight }cm</p>
              </div>
            </div>
          </div>
        )}
        <Stage />
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
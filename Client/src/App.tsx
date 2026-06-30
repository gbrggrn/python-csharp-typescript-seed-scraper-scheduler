import { useState, useEffect } from 'react'
import { type SubmitEvent } from 'react'
import Header from './components/header/Header'
import Sidebar from './components/sidebar/Sidebar'
import Gardenbar from './components/gardenbar/Gardenbar'
import Stage from './components/stage/Stage'
import { type Plant } from './types/plant'
import { type Garden } from './types/garden'
import { fetchPlants } from './services/plantService'
import { fetchGardens } from './services/gardenService'
import { postGarden } from './services/gardenService'
import './App.css'

export function App() {
  const [plants, setPlants] = useState<Plant[]>([]);
  const [selectedIds, setSelectedIds] = useState<number[]>([])
  const [gardens, setGardens] = useState<Garden[]>([]);
  const [selectedGardenIds, setSelectedGardenIds] = useState<number[]>([]);
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

  const handleToggleSelectGarden = (id:number) => {
    setSelectedGardenIds((prev) => {
      if (prev.includes(id)) {
        return prev.filter(rid => rid !== id);
      } else {
        return [id];
      }
    });
  }

  useEffect(() => {
    const loadData = async () => {
      try {
        setLoading(true);
        const plants = await fetchPlants();
        if (Array.isArray(plants)) {
          setPlants(plants);
        }

        const gardens = await fetchGardens();
        console.log()
        if (Array.isArray(gardens)) {
          setGardens(gardens);
        }
      } catch (err) {
        setError("Kunde inte ladda data");
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
  async function addGarden(e: SubmitEvent) {
    e.preventDefault();

    var response = await postGarden(gardenName, lat, lon);
    if (response) {
      setIsGardenModal(false)
    } else {
      setIsGardenModal(true)
    }
  }

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
        <Stage 
          allPlants = {plants}
          selectedIds={selectedIds}/>
        <Gardenbar 
          gardens={gardens}
          selectedGardenIds={selectedGardenIds}
          onToggle={handleToggleSelectGarden}
          onDoubleClickGarden={(garden) => setDetailsGarden(garden)}
          onAddGarden={() => setIsGardenModal(true)} />

          {isGardenModal && (
          <div className="modal-overlay" onClick={() => setIsGardenModal(false)}>
            <div className="modal-window" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h3>Lägg till en trädgård</h3>
                <button className="modal-close" onClick={() => setIsGardenModal(false)}>X</button>
              </div>
              <div className="modal-body">
                <form onSubmit={addGarden} className="add-garden-form">
                  <input
                    type="text"
                    placeholder="Namn"
                    value={gardenName}
                    onChange={(e) => setGardenName(e.target.value)}/>
                  <input 
                    type="text"
                    placeholder="Latitud"
                    value={lat}
                    onChange={(e) => setLat(e.target.value)}/>
                  <input 
                    type="text"
                    placeholder="Longitud"
                    value={lon}
                    onChange={(e) => setLon(e.target.value)}/>

                  <button type="submit" className="clear-btn">Spara</button>
                </form>
              </div>
            </div>
          </div>
        )}

        {detailsGarden && (
          <div className="modal-overlay" onClick={() => setDetailsPlant(null)}>
            <div className="modal-window" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <h3>{ detailsGarden.name }</h3>
                <button className="modal-close" onClick={() => setDetailsGarden(null)}>X</button>
              </div>
              <div className="modal-body">
                <p>Trädgårdens namn: { detailsGarden.name }</p>
                <p>Latitud: { detailsGarden.latitude }</p>
                <p>Longitud: { detailsGarden.longitude }</p>
                <p>Genomsnittlig sista frost: </p>
                <p>Genomsnittlig första frost: </p>
                <h4>Sammanfattning av förutsättningar</h4>
                <p>Förutsättningar...</p>
              </div>
            </div>
          </div>
        )}
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
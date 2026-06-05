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

  return (
    <div className="ide-wrapper">
      <Header />
      <div className="workspace">
        <Sidebar 
          plants={plants}
          selectedIds={selectedIds}
          onToggle={handleToggleSelect} />

        <div id="plant-details" className="modal-overlay">
          <div className="modal-window">
            <div className="modal-header">
              <h3>Plant Details</h3>
              <a href="#" className="modal-close">X</a>
            </div>
            <div className="modal-body">
              <p>PLACEHOLDER: SEED DATA TO GO HERE</p>
            </div>
          </div>
        </div>
        <Stage />
      </div>
      {error && <div className="status-bar error">{error}</div>}
    </div>
  );
}
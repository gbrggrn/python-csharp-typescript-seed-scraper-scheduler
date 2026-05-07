import { useState } from 'react'
import { useEffect } from 'react'
import Header from './components/header/Header'
import Sidebar from './components/sidebar/Sidebar'
import Stage from './components/stage/Stage'
import { type Plant } from './types/plant'
import { fetchPlants } from './services/plantService'
import './App.css'

function App() {
  const [plants, setPlants] = useState<Plant[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        const data = await fetchPlants();
        setPlants(data);
      } catch (err) {
        setError("Failed to load plants.");
        console.error(err);
      }
    };

    loadData();
  }, []);

  return (
    <div className="ide-wrapper">
      <Header />
      <div className="workspace">
        <Sidebar plants={plants} />
        <Stage />
      </div>
    </div>
  );
}
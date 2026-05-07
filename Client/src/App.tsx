import { useState } from 'react'
import Header from './components/header/Header'
import Sidebar from './components/sidebar/Sidebar'
import Stage from './components/stage/Stage'
import { type Plant } from './types/plant'
import './App.css'

function App() {
  const [plants, setPlants] = useState<Plant[]>([])

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
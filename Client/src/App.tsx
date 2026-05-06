import { useState } from 'react'
import Header from './components/header'
import Sidebar from './components/sidebar'
import GanttChart from './components/stage'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="ide-wrapper">
      <Header />
      <div className="workspace">
        <main className="stage">
          <GanttChart selectedPlants={selectedPlants} />
        </main>
        <aside className="sidebar-right">
          <PlantExplorer
            plants={plants}
            onToggle={togglePlantSelection}
            />
        </aside>
      </div>
    </div>
  );
}
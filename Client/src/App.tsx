import { useState } from 'react'
import Header from './components/header/Header'
import Sidebar from './components/sidebar/Sidebar'
import Stage from './components/stage/Stage'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="ide-wrapper">
      <Header />
      <div className="workspace">
        <Stage />
        <Sidebar />
      </div>
    </div>
  );
}
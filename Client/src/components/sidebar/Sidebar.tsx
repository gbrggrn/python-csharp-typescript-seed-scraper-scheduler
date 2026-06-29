import './Sidebar.css'
import { type Plant } from '../../types/plant'
import { useState } from 'react';

interface SidebarProps {
    plants: Plant[];
    selectedIds: number[];
    onToggle: (id: number) => void;
    onClear: () => void;
    onDoubleClickPlant: (Plant: Plant) => void;
    onAddGarden: (boolean: true) => void;
}

const Sidebar = ({plants, selectedIds, onToggle, onClear, onDoubleClickPlant, onAddGarden}: SidebarProps) => {

    // Local state for sidebar search query
    const [searchTerm, setSearchTerm] = useState('');

    // Derived state for sidebar search query (filter on every keystroke)
    const filteredPlants = plants.filter((plant) =>
        plant.name.toLowerCase().includes(searchTerm.toLowerCase()));

    return (
        <aside className="sidebar">
            <div className="add-garden-btn">
                <button
                    onClick={() => onAddGarden(true)}
                    >
                        Lägg till trädgård
                    </button>
            </div>
            <div className="garden-list">

            </div>
            <div className="clear-btn">
                <button
                    onClick={() => onClear()}
                    >
                        Rensa schema
                    </button>
            </div>
            <div className="search-box">
                <input 
                    type="text" 
                    placeholder="Sök grönsaker..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    />
            </div>
            <div className="plant-list">
                {filteredPlants.map((plant) => (
                    <button
                        key={plant.id}
                        className={`list-item ${selectedIds.includes(plant.id) ? 'is-selected' : ''}`}
                        onClick={() => onToggle(plant.id)}
                        onDoubleClick={() => onDoubleClickPlant(plant)}
                        >
                            <span className="plant-name">{plant.name}</span>
                        </button>
                ))}

                {filteredPlants.length === 0 && (
                    <div className="no-results">Inga grönsaker matchar: "{searchTerm}"</div>
                )}
            </div>
        </aside>
    )
}

export default Sidebar;
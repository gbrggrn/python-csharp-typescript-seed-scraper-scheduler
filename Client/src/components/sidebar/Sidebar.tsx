import './Sidebar.css'
import { type Plant } from '../../types/plant'
import { useState } from 'react';

interface SidebarProps {
    plants: Plant[];
    selectedIds: number[];
    onToggle: (id: number) => void;
    onClear: () => void;
    onDoubleClickPlant: (Plant: Plant) => void;
}

const Sidebar = ({plants, selectedIds, onToggle, onClear, onDoubleClickPlant}: SidebarProps) => {

    // Local state for sidebar search query
    const [searchTerm, setSearchTerm] = useState('');

    // Derived state for sidebar search query (filter on every keystroke)
    const filteredPlants = plants.filter((plant) =>
        plant.name.toLowerCase().includes(searchTerm.toLowerCase()));

    return (
        <aside className="sidebar">
            <div className="clear-btn">
                <button
                    onClick={() => onClear()}
                    >
                        Rensa
                    </button>
            </div>
            <div className="search-box">
                <input 
                    type="text" 
                    placeholder="Filter plants..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    className="search-input"
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
                    <div className="no-results">No plants match "{searchTerm}"</div>
                )}
            </div>
        </aside>
    )
}

export default Sidebar;
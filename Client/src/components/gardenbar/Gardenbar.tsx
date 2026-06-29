import './Gardenbar.css'
import { type Garden } from '../../types/garden'
import { useState } from 'react';

interface GardenbarProps {
    gardens: Garden[];
    selectedIds: number[];
    onToggle: (id: number) => void;
    onClear: () => void;
    onDoubleClickGarden: (Garden: Garden) => void;
    onAddGarden: (boolean: true) => void;
}

const Gardenbar = ({gardens, selectedIds, onToggle, onClear, onDoubleClickGarden, onAddGarden}: GardenbarProps) => {

    // Local state for sidebar search query
    const [searchTerm, setSearchTerm] = useState('');

    // Derived state for sidebar search query (filter on every keystroke)
    const filteredGardens = gardens.filter((garden) =>
        garden.name.toLowerCase().includes(searchTerm.toLowerCase()));

    return (
        <aside className="gardenbar">
            <div className="add-garden-btn">
                <button
                    onClick={() => onAddGarden(true)}
                    >
                        Lägg till trädgård
                    </button>
            </div>
            <div className="garden-list">

            </div>
            <div className="search-box">
                <input 
                    type="text" 
                    placeholder="Sök trädgårdar..."
                    value={searchTerm}
                    onChange={(e) => setSearchTerm(e.target.value)}
                    />
            </div>
            <div className="garden-list">
                {filteredGardens.map((garden) => (
                    <button
                        key={garden.id}
                        className={`list-item ${selectedIds.includes(garden.id) ? 'is-selected' : ''}`}
                        onClick={() => onToggle(garden.id)}
                        onDoubleClick={() => onDoubleClickGarden(garden)}
                        >
                            <span className="plant-name">{garden.name}</span>
                        </button>
                ))}

                {filteredGardens.length === 0 && (
                    <div className="no-results">Inga trädgårdar matchar: "{searchTerm}"</div>
                )}
            </div>
        </aside>
    )
}

export default Gardenbar;
import './Sidebar.css'
import { type Plant } from '../../types/plant'

interface SidebarProps {
    plants: Plant[];
    selectedIds: number[];
    onToggle: (id: number) => void;
}

const Sidebar = ({plants, selectedIds, onToggle}: SidebarProps) => {
    return (
        <aside className="sidebar">
            <div className="search-box">
                <input type="text" placeholder="Filter plants..." />
            </div>
            <div className="plant-list">
                {plants.map((plant) => (
                    <button
                        key={plant.id}
                        className={`list-item ${selectedIds.includes(plant.id) ? 'is-selected' : ''}`}
                        onClick={() => onToggle(plant.id)}
                        >
                            <span className="plant-name">{plant.name}</span>
                        </button>
                ))}
            </div>
        </aside>
    )
}

export default Sidebar;
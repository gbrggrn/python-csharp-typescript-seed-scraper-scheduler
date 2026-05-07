import './Sidebar.css'
import { type Plant } from '../../types/plant'

interface SidebarProps {
    plants: Plant[];
}

const Sidebar = ({plants}: SidebarProps) => {
    return (
        <aside className="sidebar">
            <div className="plant-list">
                {plants.map(plant => (
                    <div key={plant.id}>
                        {plant.name}
                    </div>
                ))}
            </div>
        </aside>
    )
}

export default Sidebar;
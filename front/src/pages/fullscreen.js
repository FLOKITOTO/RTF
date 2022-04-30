import { MapContainer, TileLayer, ScaleControl } from 'react-leaflet';
import 'leaflet-fullscreen/dist/Leaflet.fullscreen.js';
import 'leaflet-fullscreen/dist/leaflet.fullscreen.css';
import tileLayer from '../util/tileLayer';

const center = [52.22977, 21.01178];

const MapWrapper = () => {
  return (
    <MapContainer
      fullscreenControl={true}
      center={center}
      zoom={13}
      scrollWheelZoom={true}
    >

      <TileLayer {...tileLayer} />

      <ScaleControl imperial={false} />
    </MapContainer>
  )
}

export default MapWrapper;
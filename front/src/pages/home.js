import { MapContainer, TileLayer, Marker, ScaleControl } from 'react-leaflet';
import tileLayer from '../util/tileLayer';
import L from "leaflet";
import 'leaflet-fullscreen/dist/Leaflet.fullscreen.js';
import 'leaflet-fullscreen/dist/leaflet.fullscreen.css';
import { useEffect } from 'react';
import newMarker from "../data/asset/pin.png";
import axios from 'axios'
// import res from 'express/lib/response';

const center = [46.227638, 2.213749];

const pointerIcon = new L.Icon({
  iconUrl: newMarker,
  iconSize: [100, 100], // size of the icon
  iconAnchor: [20, 58], // changed marker icon position
});

const MyMarkers = ({ data }) => {
  return data.map(({ lat, lng }, index) => (
    <Marker
      key={index}
      position={{ lat, lng }}
      icon={pointerIcon}
    >
    </Marker>
  ));
}

const MapWrapper = () => {
  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect( async () => {
    // eslint-disable-next-line react-hooks/exhaustive-deps
    markers = (await componentDataMarkers()).data
    console.log(markers);
  }, [])
  const componentDataMarkers = async () => await axios.get(`http://localhost:5000/plane/latlong`)
  var markers = []



  return (
    <MapContainer
    fullscreenControl={true}
    center={center}
    zoom={13}
    scrollWheelZoom={true}
    >

      <TileLayer {...tileLayer} />

      <MyMarkers data={markers} />
      <ScaleControl imperial={false} />
    </MapContainer>
  )
}

export default MapWrapper;
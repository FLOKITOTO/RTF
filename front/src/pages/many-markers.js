import { MapContainer, TileLayer, Marker, Popup, ScaleControl } from 'react-leaflet';
import tileLayer from '../util/tileLayer';
import 'leaflet-fullscreen/dist/Leaflet.fullscreen.js';
import 'leaflet-fullscreen/dist/leaflet.fullscreen.css';
import { useEffect } from 'react';

import axios from 'axios'

const center = [52.22977, 21.01178];


const MyMarkers = ({ data }) => {
  return data.map(({ lat, lng, title }, index) => (
    <Marker
      key={index}
      position={{ lat, lng }}
    >
      <Popup>{title}</Popup>
    </Marker>
  ));
}


const MapWrapper = () => {
  // useEffect(() => {
  //   componentDataMarkers()
  // }, [])
  // const componentDataMarkers = () => {
  //   axios.get(`http://localhost:5000/plane/latlong`)
  //     .then(res => {
  //       console.log(res)
  //       const markers = res.data;
  
  //     })
  return (
    <MapContainer
    fullscreenControl={true}
    center={center}
    zoom={13}
    scrollWheelZoom={true}
    >

      <TileLayer {...tileLayer} />

      {/* <MyMarkers data={points} /> */}
      <ScaleControl imperial={false} />
    </MapContainer>
  )
}

export default MapWrapper;
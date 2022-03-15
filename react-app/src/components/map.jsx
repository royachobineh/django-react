import { useState } from 'react';
import {
  withScriptjs,
  withGoogleMap,
  GoogleMap,
  Marker,
  InfoWindow,
} from 'react-google-maps';

const Map = props => {
  const [selectedMarker, setSelectedMarker] = useState(null);

  return (
    <GoogleMap
      defaultZoom={10}
      defaultCenter={{ lat: 23.777176, lng: 90.399452 }}
    >
      {props.markers?.map(marker => (
        <Marker
          key={`${marker.latitude}${marker.longitude}`}
          position={{
            lat: parseFloat(marker.latitude),
            lng: parseFloat(marker.longitude),
          }}
          onClick={() => setSelectedMarker(marker)}
        />
      ))}

      {selectedMarker && (
        <InfoWindow
          onCloseClick={() => setSelectedMarker(null)}
          position={{
            lat: parseFloat(selectedMarker.latitude),
            lng: parseFloat(selectedMarker.longitude),
          }}
        >
          <div>
            <h4>{selectedMarker.name}</h4>
          </div>
        </InfoWindow>
      )}
    </GoogleMap>
  );
};

const WrappedMap = withScriptjs(withGoogleMap(Map));

export default WrappedMap;

import { useEffect } from 'react';
import { connect } from 'react-redux';
import ProtectedLayout from '../../components/layout/protected-layout';

import WrappedMap from '../../components/map';
import { fetchLocations } from '../../store/actions';

const googleMapURL = `https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places?key=${process.env.REACT_APP_MAPS_KEY}`;

function Map({ locations, dispatch }) {
  useEffect(() => {
    fetchLocations(dispatch);
  }, []);

  return (
    <WrappedMap
      markers={locations}
      googleMapURL={googleMapURL}
      loadingElement={<div style={{ height: `100%` }} />}
      containerElement={<div style={{ height: '100%', width: '100%' }} />}
      mapElement={<div style={{ height: `100%`, width: '100%' }} />}
    />
  );
}

const mapStateToProps = state => {
  return {
    locations: state.app.locations,
  };
};

function ProtectedMap(props) {
  return (
    <ProtectedLayout>
      <Map {...props} />
    </ProtectedLayout>
  );
}

export default connect(mapStateToProps, null)(ProtectedMap);

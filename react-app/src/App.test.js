import { render, screen } from '@testing-library/react';
import Home from './containers/home';
import WrappedMap from './components/map';

test('renders welcome text', () => {
  render(<Home />);
  const linkElement = screen.getByText(/welcome!/i);
  expect(linkElement).toBeInTheDocument();
});

test('renders google map', () => {
  render(
    <WrappedMap
      markers={[]}
      googleMapURL="https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places"
      loadingElement={<div style={{ height: `100%` }} />}
      containerElement={<div style={{ height: '100%', width: '100%' }} />}
      mapElement={<div style={{ height: `100%`, width: '100%' }} />}
    />
  );
});

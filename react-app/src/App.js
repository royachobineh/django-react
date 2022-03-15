import { useEffect } from 'react';
import { connect } from 'react-redux';
import { Routes, Route } from 'react-router-dom';
import './App.css';

import Home from './containers/home';
import Map from './containers/map';
import Login from './containers/auth/login';
import Register from './containers/auth/register';

import SideNav from './components/nav/side-nav';
import useLocalStorage from './utils/use-local-storage';
import http from './utils/http';
import { validateToken } from './store/actions';

function App({ dispatch, loadStatus, user }) {
  const [token, setToken] = useLocalStorage('token', '');

  useEffect(() => {
    validateToken(dispatch, token);
  }, []);

  useEffect(() => {
    if (!loadStatus) {
      setToken(user?.token);
      http.defaults.headers.common.Authorization = user?.token
        ? `JWT ${user.token}`
        : undefined;
    }
  }, [user, loadStatus, setToken]);

  return (
    <>
      <SideNav />

      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/map" element={<Map />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </main>
    </>
  );
}

const mapStateToProps = state => ({
  loadStatus: state.app.loadStatus,
  user: state.app.user,
});

export default connect(mapStateToProps, null)(App);

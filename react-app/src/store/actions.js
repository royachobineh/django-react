import * as types from './constants';
import http from '../utils/http';

export const fetchLocations = async dispatch => {
  try {
    const { data } = await http.get('/user/location/');
    dispatch({ type: types.RECEIVED_LOCATIONS, payload: data });
  } catch (ex) {
    console.error(ex.message);
  }
};

export const loginUser = async (dispatch, payload) => {
  try {
    const { data } = await http.post('/user/login/', payload);
    dispatch({ type: types.SET_USER, payload: data });
    http.defaults.headers.common.Authorization = `JWT ${data.token}`;
  } catch (ex) {
    console.error(ex.message);
  }
};

export const registerUser = async (dispatch, payload) => {
  try {
    const { data } = await http.post('/user/register/', payload);
    dispatch({ type: types.SET_USER, payload: data });
  } catch (ex) {
    console.error(ex.message);
  }
};

export const logoutUser = dispatch => {
  dispatch({ type: types.SET_USER, payload: null });
};

export const validateToken = async (dispatch, token) => {
  try {
    if (token) {
      const { data } = await http.post('/user/api-token-verify/', { token });
      dispatch({ type: types.SET_USER, payload: data });
    }
  } catch (ex) {
  } finally {
    dispatch({ type: types.SET_LOAD_STATUS, payload: false });
  }
};

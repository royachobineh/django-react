import { combineReducers } from 'redux';
import * as types from './constants';

export const initialState = {
  loadStatus: true,
  user: null,
  locations: [],
};

export const AppReducer = (state = initialState, action) => {
  switch (action.type) {
    case types.RECEIVED_LOCATIONS: {
      return { ...state, locations: action.payload };
    }

    case types.SET_USER: {
      return { ...state, user: action.payload };
    }

    case types.SET_LOAD_STATUS: {
      return { ...state, loadStatus: action.payload };
    }

    default:
      return state;
  }
};

export const reducer = combineReducers({ app: AppReducer });

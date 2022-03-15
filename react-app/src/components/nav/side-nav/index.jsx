import './styles.css';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { connect } from 'react-redux';

import { logoutUser } from '../../../store/actions';

function SideNav({ dispatch, user }) {
  const location = useLocation();
  const navigate = useNavigate();

  const handleLogout = () => {
    logoutUser(dispatch);
    navigate('/');
  };

  const getClassName = path => {
    if (location.pathname === path) return 'active-nav-item';
    return 'nav-item';
  };

  return (
    <div className="sidenav-wrapper">
      <ul>
        <li className={getClassName('/')}>
          <Link to="/">Home</Link>
        </li>

        <li className={getClassName('/map')}>
          <Link to="/map">Map</Link>
        </li>

        {user && (
          <li className={getClassName('#')} onClick={handleLogout}>
            <Link to="#">Logout</Link>
          </li>
        )}
      </ul>
    </div>
  );
}

const mapStateToProps = state => ({
  user: state.app.user,
});

export default connect(mapStateToProps, null)(SideNav);

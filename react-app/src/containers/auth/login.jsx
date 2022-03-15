import { Link, useNavigate } from 'react-router-dom';
import { connect } from 'react-redux';

import './styles.css';
import Input from '../../components/ui/input';
import { loginUser } from '../../store/actions';
import { useEffect } from 'react';

function Login({ dispatch, user }) {
  const navigate = useNavigate();

  useEffect(() => {
    if (user) {
      navigate('/');
    }
  }, [user, navigate]);

  const handleLogin = e => {
    e.preventDefault();

    const { email, password } = e.target;
    loginUser(dispatch, { email: email.value, password: password.value });
  };

  return (
    <>
      <h1>Login</h1>

      <div className="authForm">
        <form onSubmit={handleLogin}>
          <Input label="Email" name="email" type="email" required />
          <Input label="Password" name="password" type="password" required />
          <button type="submit">Login</button>
        </form>

        <h5 style={{ fontWeight: 400, margin: '25px 0px' }}>Or</h5>
        <Link to="/register">Register</Link>
      </div>
    </>
  );
}

const mapStateToProps = state => ({
  user: state.app.user,
});

export default connect(mapStateToProps, null)(Login);

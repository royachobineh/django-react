import { Link, useNavigate } from 'react-router-dom';
import { connect } from 'react-redux';

import './styles.css';
import Input from '../../components/ui/input';
import { registerUser } from '../../store/actions';
import { useEffect } from 'react';

function Register({ dispatch, user }) {
  const navigate = useNavigate();

  useEffect(() => {
    if (user) {
      navigate('/');
    }
  }, [user, navigate]);

  const handleRegister = e => {
    e.preventDefault();

    const { email, password, firstName, lastName } = e.target;
    registerUser(dispatch, {
      email: email.value,
      password: password.value,
      first_name: firstName.value,
      last_name: lastName.value,
    });
  };

  return (
    <>
      <h1>Register</h1>

      <div className="authForm">
        <form onSubmit={handleRegister}>
          <Input label="First Name" name="firstName" required />
          <Input label="Last Name" name="lastName" required />
          <Input label="Email" name="email" type="email" required />
          <Input label="Password" name="password" type="password" required />
          <button type="submit">Register</button>
        </form>

        <h5 style={{ fontWeight: 400, margin: '25px 0px' }}>Or</h5>
        <Link to="/login">Login</Link>
      </div>
    </>
  );
}

const mapStateToProps = state => ({
  user: state.app.user,
});

export default connect(mapStateToProps, null)(Register);

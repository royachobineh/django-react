import { useEffect } from 'react';
import { useStore } from 'react-redux';
import { useNavigate } from 'react-router-dom';

const ProtectedLayout = ({ children }) => {
  const { getState } = useStore();
  const { user, loadStatus } = getState().app;
  const navigate = useNavigate();

  useEffect(() => {
    if (!loadStatus && !user) {
      navigate('/login');
    }
  }, [navigate, user, loadStatus]);

  if (!user) {
    return null;
  }

  return <>{children}</>;
};

export default ProtectedLayout;

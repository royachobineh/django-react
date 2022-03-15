import './styles.css';

const Input = ({ error, label, name, placeholder, type, ...props }) => (
  <div className="styledInput">
    <label>
      {label && <span>{label}</span>}
      <input
        type={type || 'text'}
        name={name}
        placeholder={placeholder}
        {...props}
      />
    </label>

    {error && <span className="error-msg">{error}</span>}
  </div>
);

export default Input;

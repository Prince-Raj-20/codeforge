import logo from "../logo.png";
import {Link} from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  const token = localStorage.getItem("token");

  return (
    <nav className="navbar">
      <div className="navbar-inner">

        <Link to="/" className="navbar-brand">
          <img
            src={logo}
            alt="CodeForge logo"
            className="brand-logo"
          />
        </Link>

        <div className="navbar-links">
          <Link to="/problems">Problems</Link>
          <Link to="/contests">Contests</Link>

          {token ? (
            <>
              <Link to="/dashboard">Dashboard</Link>
              <Link to="/profile">Profile</Link>
            </>
          ) : (
            <>
              <Link to="/login">Login</Link>
              <Link to="/signup">Sign Up</Link>
            </>
          )}
        </div>

      </div>
    </nav>
  );
}

export default Navbar;
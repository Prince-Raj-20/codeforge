import { Link } from "react-router-dom";
import "./Home.css";

function Home() {
  return (
    <div className="home-page">
      <section className="hero">

        <div className="hero-content">
          <p className="hero-label">CodeForge</p>

          <h1>
            Practice. Solve. Improve.
          </h1>

          <p className="hero-description">
            Solve programming problems, submit your code,
            and track your progress.
          </p>

          <div className="hero-buttons">
            <Link to="/problems" className="primary-button">
              Start Coding
            </Link>

            <Link to="/login" className="secondary-button">
              Sign In
            </Link>
          </div>
        </div>

      </section>
    </div>
  );
}

export default Home;
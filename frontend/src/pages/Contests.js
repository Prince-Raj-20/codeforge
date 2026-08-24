import "./Contests.css";

function Contests() {
return ( <main className="contests-page"> <div className="contests-container">

    <div className="contest-icon">
      🏆
    </div>

    <h1>Contests Are Coming Soon</h1>

    <p className="contest-subtitle">
      Get ready to compete, sharpen your skills,
      and climb the leaderboard.
    </p>

    <div className="contest-features">

      <div className="contest-feature">
        <span>⚡</span>
        <h3>Live Contests</h3>
        <p>
          Compete against other programmers
          in timed coding challenges.
        </p>
      </div>

      <div className="contest-feature">
        <span>🏅</span>
        <h3>Rankings</h3>
        <p>
          Track your performance and climb
          the competitive leaderboard.
        </p>
      </div>

      <div className="contest-feature">
        <span>🔥</span>
        <h3>Challenges</h3>
        <p>
          Test your problem-solving skills
          with carefully designed problems.
        </p>
      </div>

    </div>

    <div className="coming-soon">
      <span>COMING SOON</span>
    </div>

  </div>
</main>

);
}

export default Contests;

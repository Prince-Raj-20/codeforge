import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import API_BASE from "../api";
import "./Dashboard.css";

function Dashboard() {
  
  const [profile, setProfile] = useState(null);
  const [submissions, setSubmissions] = useState([]);
  const [weaknesses, setWeaknesses] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboardData = async () => {
      const token = localStorage.getItem("token");

      if (!token) {
        setLoading(false);
        return;
      }

      try {
        const headers = {
          Authorization: `Bearer ${token}`
        };

        const [
          profileResponse,
          submissionsResponse,
          weaknessesResponse,
          recommendationsResponse
        ] = await Promise.all([
          fetch(`${API_BASE}/auth/me`, {
            headers
          }),

          fetch(`${API_BASE}/submissions/`, {
            headers
          }),

          fetch(`${API_BASE}/submissions/weaknesses`, {
            headers
          }),

          fetch(`${API_BASE}/submissions/recommendations`, {
            headers
          })
        ]);

        if (
          profileResponse.status === 401 ||
          submissionsResponse.status === 401 ||
          weaknessesResponse.status === 401 ||
          recommendationsResponse.status === 401
        ) {
          localStorage.removeItem("token");
          window.location.href = "/login";
          return;
        }

        if (profileResponse.ok) {
          const profileData = await profileResponse.json();
          setProfile(profileData);
        }

        if (submissionsResponse.ok) {
          const submissionData =
            await submissionsResponse.json();

          setSubmissions(submissionData);
        }

        if (weaknessesResponse.ok) {
          const weaknessData =
            await weaknessesResponse.json();

          setWeaknesses(weaknessData);
        }

        if (recommendationsResponse.ok) {
          const recommendationData =
            await recommendationsResponse.json();

          setRecommendations(recommendationData);
        }
      } catch (error) {
        console.error(
          "Unable to load dashboard data:",
          error
        );
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  const acceptedSubmissions = submissions.filter(
    (submission) =>
      submission.status === "Accepted"
  ).length;

  const solvedProblems = new Set(
    submissions
      .filter(
        (submission) =>
          submission.status === "Accepted"
      )
      .map(
        (submission) =>
          submission.problem_id
      )
  ).size;

  const acceptanceRate =
    submissions.length > 0
      ? ((acceptedSubmissions / submissions.length) * 100).toFixed(2)
      : "0.00";

  if (loading) {
    return (
      <main className="dashboard-page">
        <div className="dashboard-content">
          <p className="dashboard-loading">
            Loading dashboard...
          </p>
        </div>
      </main>
    );
  }

  return (
    <main className="dashboard-page">
      <div className="dashboard-content">

        <section className="dashboard-header">
          <p className="dashboard-label">
            ForgeR DASHBOARD
          </p>

          <h1>
            Welcome back
            {profile?.username
              ? `, ${profile.username}`
              : ""}
            !
          </h1>

          <p className="dashboard-subtitle">
            Track your coding progress, improve your
            weak areas, and keep solving problems.
          </p>
        </section>

        <section className="dashboard-stats">

          <div className="dashboard-stat-card">
            <span className="stat-label">
              Problems Solved
            </span>

            <strong className="stat-value">
              {solvedProblems}
            </strong>
          </div>

          <div className="dashboard-stat-card">
            <span className="stat-label">
              Submissions
            </span>

            <strong className="stat-value">
              {submissions.length}
            </strong>
          </div>

          <div className="dashboard-stat-card">
            <span className="stat-label">
              Acceptance Rate
            </span>

            <strong className="stat-value">
              {acceptanceRate}%
            </strong>
          </div>

        </section>

        <section className="dashboard-main-grid">

          <div className="dashboard-section recommendation-section">

            <div className="section-heading">
              <div>
                <p className="section-label">
                  FOR YOU
                </p>

                <h2>
                  Recommended Problems
                </h2>
              </div>
            </div>

            {recommendations.length === 0 ? (
              <p className="empty-message">
                No recommendations available yet.
              </p>
            ) : (
              <div className="recommendation-list">

                {recommendations.map((problem) => (
                  <Link
                    key={problem.id}
                    to={`/problems/${problem.id}`}
                    className="recommendation-item recommendation-link"
                  >
                    <div>
                      <h3>
                        {problem.title}
                      </h3>

                      <p>
                        {problem.topic || "General"}
                      </p>

                      {problem.reason && (
                        <small className="recommendation-reason">
                          {problem.reason}
                        </small>
                      )}
                    </div>

                    <span
                      className={`difficulty-badge ${problem.difficulty?.toLowerCase()}`}
                    >
                      {problem.difficulty}
                    </span>
                  </Link>
                ))}

              </div>
            )}

          </div>

          <div className="dashboard-section weakness-section">

            <div className="section-heading">
              <div>
                <p className="section-label">
                  PERFORMANCE
                </p>

                <h2>
                  Your Weak Areas
                </h2>
              </div>
            </div>

            {weaknesses.length === 0 ? (
              <p className="empty-message">
                No submission data available yet.
              </p>
            ) : (
              <div className="weakness-list">

                {weaknesses.map((weakness) => (
                  <div
                    key={weakness.topic}
                    className="weakness-item"
                  >
                    <div className="weakness-top">

                      <h3>
                        {weakness.topic}
                      </h3>

                      <span
                        className={`strength-badge ${weakness.weakness?.toLowerCase()}`}
                      >
                        {weakness.weakness}
                      </span>

                    </div>

                    <div className="weakness-stats">
                      <span>
                        {weakness.attempts} attempts
                      </span>

                      <span>
                        {weakness.accepted} accepted
                      </span>

                      <span>
                        {weakness.acceptance_rate}%
                      </span>
                    </div>

                    <div className="progress-track">
                      <div
                        className="progress-bar"
                        style={{
                          width: `${Math.min(
                            weakness.acceptance_rate,
                            100
                          )}%`
                        }}
                      />
                    </div>

                  </div>
                ))}

              </div>
            )}

          </div>

        </section>

      </div>
    </main>
  );
}

export default Dashboard;
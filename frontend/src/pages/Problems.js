import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import API_BASE from "../api";
import "./Problems.css";

function Problems() {
  const [problems, setProblems] = useState([]);
  const [search, setSearch] = useState("");
  const [difficulty, setDifficulty] = useState("All");
  const [topic, setTopic] = useState("All");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProblems = async () => {
      try {
        const response = await fetch(`${API_BASE}/problems/`);

        if (!response.ok) {
          throw new Error("Failed to fetch problems.");
        }

        const data = await response.json();
        setProblems(data);
      } catch (err) {
        setError("Unable to load problems.");
      } finally {
        setLoading(false);
      }
    };

    fetchProblems();
  }, []);

  const topics = [
    "All",
    ...new Set(
      problems
        .map((problem) => problem.topic)
        .filter(Boolean)
    )
  ];

  const filteredProblems = problems.filter((problem) => {
    const matchesSearch = problem.title
      .toLowerCase()
      .includes(search.toLowerCase());

    const matchesDifficulty =
      difficulty === "All" ||
      problem.difficulty === difficulty;

    const matchesTopic =
      topic === "All" ||
      problem.topic === topic;

    return (
      matchesSearch &&
      matchesDifficulty &&
      matchesTopic
    );
  });

  if (loading) {
    return (
      <main className="problems-page">
        <div className="problems-container">
          <p className="problems-loading">
            Loading problems...
          </p>
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="problems-page">
        <div className="problems-container">
          <p className="problems-error">
            {error}
          </p>
        </div>
      </main>
    );
  }

  return (
    <main className="problems-page">
      <div className="problems-container">

        <div className="problems-header">
          <div>
            <p className="problems-label">
              PRACTICE
            </p>

            <h1>Problem Set</h1>

            <p className="problems-subtitle">
              Sharpen your problem-solving skills with
              coding challenges.
            </p>
          </div>

          <div className="problem-count">
            <strong>{problems.length}</strong>
            <span>Problems</span>
          </div>
        </div>

        <div className="problem-filters">

          <div className="search-box">
            <span>⌕</span>

            <input
              type="text"
              placeholder="Search problems..."
              value={search}
              onChange={(e) =>
                setSearch(e.target.value)
              }
            />
          </div>

          <select
            value={difficulty}
            onChange={(e) =>
              setDifficulty(e.target.value)
            }
          >
            <option value="All">
              All Difficulties
            </option>
            <option value="Easy">
              Easy
            </option>
            <option value="Medium">
              Medium
            </option>
            <option value="Hard">
              Hard
            </option>
          </select>

          <select
            value={topic}
            onChange={(e) =>
              setTopic(e.target.value)
            }
          >
            {topics.map((currentTopic) => (
              <option
                key={currentTopic}
                value={currentTopic}
              >
                {currentTopic === "All"
                  ? "All Topics"
                  : currentTopic}
              </option>
            ))}
          </select>

        </div>

        <div className="problems-table">

          <div className="problems-table-header">
            <span>#</span>
            <span>Problem</span>
            <span>Difficulty</span>
            <span>Topic</span>
          </div>

          {filteredProblems.length === 0 ? (
            <div className="no-problems">
              <h2>No problems found</h2>
              <p>
                Try changing your search or filters.
              </p>
            </div>
          ) : (
            filteredProblems.map((problem, index) => (
              <Link
                key={problem.id}
                to={`/problems/${problem.id}`}
                className="problem-row"
              >

                <span className="problem-number">
                  {index + 1}
                </span>

                <div className="problem-info">
                  <h2>{problem.title}</h2>

                  <p>
                    {problem.description}
                  </p>
                </div>

                <span
                  className={`difficulty-badge ${problem.difficulty.toLowerCase()}`}
                >
                  {problem.difficulty}
                </span>

                <span className="topic-badge">
                  {problem.topic || "General"}
                </span>

              </Link>
            ))
          )}

        </div>

        <p className="results-count">
          Showing {filteredProblems.length} of{" "}
          {problems.length} problems
        </p>

      </div>
    </main>
  );
}

export default Problems;
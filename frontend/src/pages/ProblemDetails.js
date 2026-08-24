import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import API_BASE from "../api";
import "./ProblemDetails.css";

function ProblemDetails() {
  const { id } = useParams();

  const [problem, setProblem] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [code, setCode] = useState(
`#include <bits/stdc++.h>
using namespace std;

int main() {
    // Write your solution here

    return 0;
}`
  );

  const [submitResult, setSubmitResult] = useState(null);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    const fetchProblem = async () => {
      try {
        const response = await fetch(`${API_BASE}/problems/${id}`);

        if (!response.ok) {
          throw new Error("Problem not found.");
        }

        const data = await response.json();
        setProblem(data);
      } catch (err) {
        setError("Unable to load problem.");
      } finally {
        setLoading(false);
      }
    };

    fetchProblem();
  }, [id]);

  const handleSubmit = async () => {
    const token = localStorage.getItem("token");

    if (!token) {
      setSubmitResult({
        status: "Login required",
        error: "Please login before submitting code."
      });
      return;
    }

    setSubmitting(true);
    setSubmitResult(null);

    try {
      const response = await fetch(`${API_BASE}/submissions/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          problem_id: Number(id),
          code: code,
          language: "cpp",
          solve_time: 0
        })
      });

      const data = await response.json();

      if (response.status === 401) {
        localStorage.removeItem("token");
        window.location.href = "/login";
        return;
      }

      if (response.status === 401) {
        localStorage.removeItem("token");
        window.location.href = "/login";
        return;
      }

      if (!response.ok) {
        setSubmitResult({
          status: "Submission failed",
          error: data.detail || "Unable to submit code."
        });
        return;
      }

      setSubmitResult(data);
    } catch (err) {
      setSubmitResult({
        status: "Network Error",
        error: "Unable to connect to the backend."
      });
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <main className="problem-loading">
        Loading problem...
      </main>
    );
  }

  if (error) {
    return (
      <main className="problem-error">
        {error}
      </main>
    );
  }

  return (
    <main className="problem-details-page">

      <div className="problem-workspace">

        {/* LEFT SIDE — PROBLEM */}
        <section className="problem-panel">

          <div className="problem-title-row">
            <div>
              <h1>{problem.title}</h1>

              <div className="problem-meta">
                <span
                  className={`difficulty ${problem.difficulty
                    .toLowerCase()
                    .replace(/\s+/g, "-")}`}
                >
                  {problem.difficulty}
                </span>

                {problem.topic && (
                  <span className="topic-tag">
                    {problem.topic}
                  </span>
                )}
              </div>
            </div>
          </div>

          <div className="problem-section">
            <h2>Description</h2>
            <p>{problem.description}</p>
          </div>

          <div className="problem-section">
            <h2>Input Format</h2>
            <p>{problem.input_format}</p>
          </div>

          <div className="problem-section">
            <h2>Output Format</h2>
            <p>{problem.output_format}</p>
          </div>

          <div className="problem-section">
            <h2>Constraints</h2>
            <p>{problem.constraints}</p>
          </div>

          <div className="example-grid">

            <div className="example-box">
              <h2>Sample Input</h2>
              <pre>{problem.sample_input}</pre>
            </div>

            <div className="example-box">
              <h2>Sample Output</h2>
              <pre>{problem.sample_output}</pre>
            </div>

          </div>

        </section>

        {/* RIGHT SIDE — CODE EDITOR */}
        <section className="editor-panel">

          <div className="editor-header">
            <div>
              <span className="editor-language">
                C++17
              </span>
            </div>

            <span className="editor-label">
              Solution
            </span>
          </div>

          <textarea
            className="code-editor"
            value={code}
            onChange={(e) => setCode(e.target.value)}
            spellCheck="false"
          />

          <div className="editor-footer">

            <button
              className="submit-button"
              onClick={handleSubmit}
              disabled={submitting}
            >
              {submitting
                ? "Submitting..."
                : "Submit Code"}
            </button>

          </div>

          {submitResult && (
            <div className="submission-result">

              <div className="result-header">
                <h2>Submission Result</h2>

                <span
                  className={`result-status ${submitResult.status
                    .toLowerCase()
                    .replace(/\s+/g, "-")}`}
                >
                  {submitResult.status}
                </span>
              </div>

              {submitResult.execution_time !== undefined && (
                <p className="execution-time">
                  Execution Time:{" "}
                  <strong>
                    {submitResult.execution_time} ms
                  </strong>
                </p>
              )}

              {submitResult.error && (
                <pre className="submission-error">
                  {submitResult.error}
                </pre>
              )}

            </div>
          )}

        </section>

      </div>

    </main>
  );
}

export default ProblemDetails;

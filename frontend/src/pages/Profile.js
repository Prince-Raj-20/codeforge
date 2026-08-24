import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API_BASE from "../api";
import "./Profile.css";

function Profile() {
  const [user, setUser] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  useEffect(() => {
    const fetchUser = async () => {
      const token = localStorage.getItem("token");

      if (!token) {
        navigate("/login");
        return;
      }

      try {
        const response = await fetch(`${API_BASE}/auth/me`, {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        if (response.status === 401) {
          localStorage.removeItem("token");
          navigate("/login");
          return;
        }

        if (!response.ok) {
          setError("Unable to load profile.");
          return;
        }

        const data = await response.json();
        setUser(data);
      } catch (err) {
        setError("Unable to load profile.");
      } finally {
        setLoading(false);
      }
    };

    fetchUser();
  }, [navigate]);

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  const handleDeleteAccount = async () => {
    const confirmed = window.confirm(
      "Are you sure you want to permanently delete your account? This action cannot be undone."
    );

    if (!confirmed) {
      return;
    }

    const token = localStorage.getItem("token");

    if (!token) {
      navigate("/login");
      return;
    }

    try {
      const response = await fetch(`${API_BASE}/auth/account`, {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });

      const data = await response.json();

      if (response.status === 401) {
        localStorage.removeItem("token");
        navigate("/login");
        return;
      }

      if (!response.ok) {
        alert(data.detail || "Unable to delete account.");
        return;
      }

      localStorage.removeItem("token");

      alert("Your account has been deleted successfully.");

      navigate("/");
    } catch (error) {
      console.error("Delete account error:", error);
      alert("Unable to connect to the backend.");
    }
  }; 

  if (loading) {
    return <main className="profile-page">Loading profile...</main>;
  }

  if (error) {
    return <main className="profile-page">{error}</main>;
  }

  return (
    <main className="profile-page">
      <div className="profile-container">

        <section className="profile-header">
          <p className="profile-label">
            ACCOUNT
          </p>

          <h1>
            Your Profile
          </h1>

          <p className="profile-subtitle">
            Manage your account information and preferences.
          </p>
        </section>

        <section className="profile-card">

          <div className="profile-identity">

            <div className="profile-avatar">
              {user.username?.charAt(0).toUpperCase()}
            </div>

            <div>
              <h2>
                {user.username}
              </h2>

              <p>
                CodeForger
              </p>
            </div>

          </div>

          <div className="profile-divider" />

          <div className="profile-details">

            <div className="profile-detail">
              <span>
                USERNAME
              </span>

              <strong>
                {user.username}
              </strong>
            </div>

            <div className="profile-detail">
              <span>
                EMAIL ADDRESS
              </span>

              <strong>
                {user.email}
              </strong>
            </div>

            <div className="profile-detail">
              <span>
                ACCOUNT ID
              </span>

              <strong>
                #{user.id}
              </strong>
            </div>

          </div>

        </section>

        <section className="profile-actions-card">

          <div>
            <p className="profile-action-label">
              ACCOUNT ACTIONS
            </p>

            <h2>
              Manage Account
            </h2>

            <p>
              Sign out of your account or permanently delete it.
            </p>
          </div>

          <div className="profile-actions">
            <button
              className="profile-logout-button"
              onClick={handleLogout}
            >
              Logout
            </button>

            <button
              className="profile-delete-button"
              onClick={handleDeleteAccount}
            >
              Delete Account
            </button>
          </div>
        </section>

      </div>
    </main>
  );
}

export default Profile;
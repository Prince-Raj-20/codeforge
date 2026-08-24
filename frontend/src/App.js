import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ProblemDetails from "./pages/ProblemDetails";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Problems from "./pages/Problems";
import Dashboard from "./pages/Dashboard";
import Profile from "./pages/Profile";
import Contests from "./pages/Contests";


function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <main className="app">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/problems" element={<Problems />} />
          <Route path="/problems/:id" element={<ProblemDetails />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/contests" element={<Contests />} />
        </Routes>
      </main>
    </BrowserRouter>
  );
}

export default App;
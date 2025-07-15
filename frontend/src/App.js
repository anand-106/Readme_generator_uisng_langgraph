import { Route, Routes, useLocation } from "react-router-dom";
import { HomePage } from "./pages/HomePage";
import { ReadMePage } from "./pages/ReadmePage";
import { AnimatePresence } from "framer-motion";
import { GitLogin } from "./pages/github/githubLogin";
import { GithubDashboard } from "./pages/github/githubDashboard";
import { RepoPage } from "./pages/github/repoPage";
import { AuthWrapper } from "./pages/github/auth/authWrapper";
import { Profile } from "./pages/github/profilePage";

function App() {
  const location = useLocation();

  return (
    <div className="w-screen h-[100dvh]  overflow-hidden relative bg-[#030617]">
      <AnimatePresence mode="wait" initial={false}>
        <Routes location={location} key={location.pathname}>
          <Route path="/" element={<HomePage />} />
          <Route path="/readme" element={<ReadMePage />} />
          <Route path="/github" element={<AuthWrapper />} />
          <Route path="/github/login" element={<GitLogin />} />
          <Route path="/github/:username" element={<GithubDashboard />} />
          <Route path="/github/:username/:reponame" element={<RepoPage />} />
          <Route path="/github/:username/profile" element={<Profile />} />
        </Routes>
      </AnimatePresence>
    </div>
  );
}

export default App;

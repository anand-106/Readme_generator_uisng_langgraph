import { Route, Routes, useLocation } from "react-router-dom";
import { HomePage } from "./pages/HomePage";
import { ReadMePage } from "./pages/ReadmePage";
import { AnimatePresence } from "framer-motion";

function App() {
  const location = useLocation();

  return (
    <div className="w-screen h-[100dvh]  overflow-hidden relative bg-[#030617]">
      <AnimatePresence mode="wait" initial={false}>
        <Routes location={location} key={location.pathname}>
          <Route path="/" element={<HomePage />} />
          <Route path="/readme" element={<ReadMePage />} />
        </Routes>
      </AnimatePresence>
    </div>
  );
}

export default App;

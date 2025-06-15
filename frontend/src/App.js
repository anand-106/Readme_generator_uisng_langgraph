import { Route, Routes } from "react-router-dom";
import { HomePage } from "./pages/HomePage";
import { ReadMePage } from "./pages/ReadmePage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/readme" element={<ReadMePage />} />
    </Routes>
  );
}

export default App;

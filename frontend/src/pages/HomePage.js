import { LinkTextBox } from "../components/home/LinkTextBox";
import { Title } from "../components/home/Title";
import Aurora from "../src/pages/Aurora/Aurora";

export function HomePage() {
  return (
    <div className="min-h-screen bg-[#030617] w-full relative flex flex-col items-center justify-start overflow-hidden">
      <Aurora
        className="absolute  w-full h-full top-0 z-1 pointer-events-none"
        colorStops={["#02c6ff", "#0066ff", "#da00ff"]}
        blend={1}
        amplitude={1.0}
        speed={0.5}
      />
      <Title />
      <LinkTextBox />
    </div>
  );
}

import { LinkTextBox } from "../components/home/LinkTextBox";
import { Title } from "../components/home/Title";

export function HomePage() {
  return (
    <div className="min-h-screen bg-[#0a0a0a] flex flex-col items-center justify-center">
      <Title />
      <LinkTextBox />
    </div>
  );
}

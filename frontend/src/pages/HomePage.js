import { LinkTextBox } from "../components/home/LinkTextBox";
import { Title } from "../components/home/Title";

export function HomePage() {
  return (
    <div className="min-h-screen bg-gray-900 flex flex-col items-center justify-start pt-36">
      <Title />
      <LinkTextBox />
    </div>
  );
}

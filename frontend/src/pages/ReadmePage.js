import { useLocation } from "react-router-dom";
import { MarkdownViewer } from "../components/ReadmePage/markdownComp";

export function ReadMePage() {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const repoUrl = searchParams.get("repo");

  return (
    <div className="min-h-screen bg-[#14191f] flex flex-col items-center justify-center">
      <MarkdownViewer repoUrl={repoUrl} />
    </div>
  );
}

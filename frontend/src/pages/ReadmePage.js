import { useLocation } from "react-router-dom";
import { MarkdownViewer } from "../components/ReadmePage/markdownComp";
import { Preferences } from "../components/ReadmePage/preferencesComp";
import { useState } from "react";

export function ReadMePage() {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const repoUrl = searchParams.get("repo");
  const [readmeData, setReadmeData] = useState("");

  return (
    <div className="h-screen bg-[#14191f] flex overflow-hidden">
      <Preferences repoUrl={repoUrl} setReadmeData={setReadmeData} />
      <MarkdownViewer readmeData={readmeData} />
    </div>
  );
}

import { useLocation } from "react-router-dom";
import { MarkdownViewer } from "../components/ReadmePage/markdownComp";
import { Preferences } from "../components/ReadmePage/preferencesComp";
import { useState } from "react";

export function ReadMePage() {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const repoUrl = searchParams.get("repo");
  const [readmeData, setReadmeData] = useState("");
  const [firstGenerate, setFirstGenerate] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [generateError, setGenerateError] = useState("");

  return (
    <div className="h-screen bg-[#030617] flex overflow-hidden selection:bg-white/30">
      <Preferences
        repoUrl={repoUrl}
        setReadmeData={setReadmeData}
        setFirstGenerate={setFirstGenerate}
        isLoading={isLoading}
        setIsLoading={setIsLoading}
        setGenerateError={setGenerateError}
      />
      <MarkdownViewer
        readmeData={readmeData}
        firstGenerate={firstGenerate}
        isLoading={isLoading}
        generateError={generateError}
      />
    </div>
  );
}

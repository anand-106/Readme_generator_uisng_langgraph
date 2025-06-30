import { useLocation } from "react-router-dom";
import { MarkdownViewer } from "../components/ReadmePage/markdownComp";
import { Preferences } from "../components/ReadmePage/preferencesComp";
import { useState } from "react";
import SlidePageWrapper from "../animations/SlidePageWrapper";
import Hamburger from "hamburger-react";

export function ReadMePage() {
  const location = useLocation();
  const searchParams = new URLSearchParams(location.search);
  const repoUrl = searchParams.get("repo");
  const [readmeData, setReadmeData] = useState("");
  const [firstGenerate, setFirstGenerate] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [generateError, setGenerateError] = useState("");
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <SlidePageWrapper>
      <div className="h-screen bg-[#030617] flex relative selection:bg-white/30">
        <div className="absolute top-3 block md:hidden left-4 z-50 ">
          <Hamburger
            color="white"
            toggled={menuOpen}
            toggle={setMenuOpen}
            size={21}
          />
        </div>

        <div
          className={`absolute max-w-[400px] w-full h-screen overflow-y-auto z-10 block md:hidden transition-transform duration-300 bg-[#030617]  ease-in-out ${
            menuOpen ? "translate-x-0" : "-translate-x-full"
          } `}
        >
          <Preferences
            repoUrl={repoUrl}
            setReadmeData={setReadmeData}
            setFirstGenerate={setFirstGenerate}
            isLoading={isLoading}
            setIsLoading={setIsLoading}
            setGenerateError={setGenerateError}
          />
        </div>
        <div className="hidden md:block w-full max-w-[400px]">
          <Preferences
            repoUrl={repoUrl}
            setReadmeData={setReadmeData}
            setFirstGenerate={setFirstGenerate}
            isLoading={isLoading}
            setIsLoading={setIsLoading}
            setGenerateError={setGenerateError}
          />
        </div>

        <MarkdownViewer
          readmeData={readmeData}
          firstGenerate={firstGenerate}
          isLoading={isLoading}
          generateError={generateError}
        />
      </div>
    </SlidePageWrapper>
  );
}

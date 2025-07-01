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
  const [menuOpen, setMenuOpen] = useState(true);

  return (
    <SlidePageWrapper>
      <div className="w-full h-full min-h-0 bg-[#030617] flex relative selection:bg-white/30">
        <div className="absolute overflow-hidden h-fit top-3 block md:hidden left-4 z-50 ">
          <Hamburger
            color="white"
            toggled={menuOpen}
            toggle={setMenuOpen}
            size={21}
          />
        </div>

        <div
          className={`fixed top-0 left-0 max-w-[400px] w-full h-full   z-40 block md:hidden transition-transform duration-300 bg-[#030617]/60 backdrop-blur-md  ease-in-out ${
            menuOpen ? "translate-x-0" : "-translate-x-full"
          } `}
        >
          <div className="w-full h-full overflow-y-auto scrollbar-none flex flex-col">
            <Preferences
              repoUrl={repoUrl}
              setReadmeData={setReadmeData}
              setFirstGenerate={setFirstGenerate}
              isLoading={isLoading}
              setIsLoading={setIsLoading}
              setGenerateError={setGenerateError}
              setMenuOpen={setMenuOpen}
            />
          </div>
        </div>
        <div className="hidden md:block h-full w-full max-w-[400px] min-h-0 overflow-hidden">
          <Preferences
            repoUrl={repoUrl}
            setReadmeData={setReadmeData}
            setFirstGenerate={setFirstGenerate}
            isLoading={isLoading}
            setIsLoading={setIsLoading}
            setGenerateError={setGenerateError}
            setMenuOpen={setMenuOpen}
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

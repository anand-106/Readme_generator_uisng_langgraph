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
  const [proj_description, setDescription] = useState("");

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
          className={`
    h-full max-w-[400px] min-h-0 overflow-hidden z-40
    transition-transform duration-300 ease-in-out
    bg-[#030617]/60 backdrop-blur-md
    ${menuOpen ? "translate-x-0" : "-translate-x-full"}
    fixed top-0 left-0 w-full md:relative md:translate-x-0
  `}
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
              proj_description={proj_description}
              setDescription={setDescription}
            />
          </div>
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

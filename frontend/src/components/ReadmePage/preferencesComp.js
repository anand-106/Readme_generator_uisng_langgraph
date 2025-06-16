import { useState } from "react";
import { callApi } from "../../utils/api/ApiCaller";

export function Preferences({ repoUrl, setReadmeData }) {
  const [isLoading, setIsLoading] = useState(false);
  const [proj_description, setDescription] = useState();

  const GenerateRequest = async () => {
    setIsLoading(true);
    const readmeResponse = await callApi({
      url: "http://localhost:8000/api/readme/generate",
      method: "POST",
      payload: {
        github_url: repoUrl,
        project_description: proj_description,
        preferences: {
          include_badges: true,
          license: "MIT",
          frameworks: ["FastAPI", "LangGraph"],
        },
        session_id: "demo-session-001",
      },
    }).catch((err) => console.error(err));
    setReadmeData(readmeResponse);
    setIsLoading(false);
  };
  return (
    <div className="w-1/4 h-full border-r border-gray-200 flex flex-col justify-between p-4">
      <h1 className="text-white text-center font-bold text-xl">
        AI Readme Generator
      </h1>
      <Description setDescription={setDescription} />
      <CheckList />
      <div className="w-full mt-auto">
        <button
          onClick={GenerateRequest}
          className={`text-black font-semibold min-w-full min-h-10 bg-slate-50 rounded-lg border-blue-400 border-2 ${
            isLoading ? "opacity-50 cursor-not-allowed" : ""
          }`}
          disabled={isLoading}
        >
          {isLoading ? "Generating..." : "Generate"}
        </button>
      </div>
    </div>
  );
}

function CheckList() {
  const [title, setTitle] = useState(true);
  const [badge, setBadge] = useState(true);
  const [introduction, setIntroduction] = useState(true);
  const [TOC, setTOC] = useState(true);
  const [keyFeatures, setKeyFeatures] = useState(true);
  const [installationGuide, setInstallationGuide] = useState(true);
  const [usage, setUsage] = useState(true);
  const [api, setAPI] = useState(true);
  const [envVar, setEnv] = useState(true);
  const [projectStructure, setProjectStructure] = useState(true);
  const [technologiesUsed, setTechnologiesUsed] = useState(true);
  const [license, setLicense] = useState(true);

  return (
    <div className="mt-4 pl-1 pb-4 w-full flex flex-col gap-4 overflow-y-auto scrollbar-none">
      <CheckListItem text={"Title"} setText={setTitle} setTextText={title} />
      <CheckListItem text={"Badge"} setText={setBadge} setTextText={badge} />
      <CheckListItem
        text={"Introduction"}
        setText={setIntroduction}
        setTextText={introduction}
      />
      <CheckListItem
        text={"Table of Contents"}
        setText={setTOC}
        setTextText={TOC}
      />
      <CheckListItem
        text={"Key Features"}
        setText={setKeyFeatures}
        setTextText={keyFeatures}
      />
      <CheckListItem
        text={"Installation Guide"}
        setText={setInstallationGuide}
        setTextText={installationGuide}
      />
      <CheckListItem text={"Usage"} setText={setUsage} setTextText={usage} />
      <CheckListItem
        text={"API Reference"}
        setText={setAPI}
        setTextText={api}
      />
      <CheckListItem
        text={"Environment Variables"}
        setText={setEnv}
        setTextText={envVar}
      />
      <CheckListItem
        text={"Project Structure"}
        setText={setProjectStructure}
        setTextText={projectStructure}
      />
      <CheckListItem
        text={"Technologies Used"}
        setText={setTechnologiesUsed}
        setTextText={technologiesUsed}
      />
      <CheckListItem
        text={"License"}
        setText={setLicense}
        setTextText={license}
      />
    </div>
  );
}
function CheckListItem({ text, setText, setTextText }) {
  return (
    <label className="flex items-center gap-3 p-3 rounded-lg bg-[#1e2733] hover:bg-[#2a3442] transition duration-500 ease-in-out cursor-pointer">
      <input
        type="checkbox"
        checked={setTextText}
        onChange={(e) => setText(e.target.checked)}
        className="w-5 h-5 text-blue-500 accent-blue-500 bg-gray-800 border-r border-gray-600 rounded focus:ring-2 focus:ring-blue-400 transition duration-500 ease-in-out"
      />
      <span className="text-white text-lg font-medium">{text}</span>
    </label>
  );
}

function Description({ setDescription }) {
  return (
    <div className="w-full h-72 border-blue-500 rounded-lg border-2 mt-5">
      <textarea
        className="h-full w-full rounded-lg bg-inherit text-white p-2"
        onChange={(e) => {
          setDescription(e.target.value);
        }}
      ></textarea>
    </div>
  );
}

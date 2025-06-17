import { useState } from "react";
import { callApi } from "../../utils/api/ApiCaller";

export function Preferences({ repoUrl, setReadmeData }) {
  const [isLoading, setIsLoading] = useState(false);
  const [proj_description, setDescription] = useState("");
  const [isRegenerate, setIsRegenerate] = useState(false);

  const [preferences, setPreferences] = useState({
    title: true,
    badge: true,
    introduction: true,
    table_of_contents: true,
    key_features: true,
    install_guide: true,
    usage: true,
    api_ref: true,
    env_var: true,
    project_structure: true,
    tech_used: true,
    licenses: true,
  });

  const GenerateRequest = async () => {
    setIsLoading(true);
    const readmeResponse = await callApi({
      url: "http://localhost:8000/api/readme/generate",
      method: "POST",
      payload: {
        github_url: repoUrl,
        project_description: proj_description,
        preferences: preferences,
        session_id: "demo-session-001",
      },
    }).catch((err) => console.error(err));

    setReadmeData(readmeResponse);
    setIsLoading(false);
    setIsRegenerate(true);
  };

  const reGenerateRequest = async () => {
    setIsLoading(true);
    const readmeResponse = await callApi({
      url: "http://localhost:8000/api/readme/resume",
      method: "POST",
      payload: {
        session_id: "demo-session-001",
        action: "regenerate",
        project_description: proj_description,
        preferences: preferences,
      },
    }).catch((err) => console.log(err));
    setReadmeData(readmeResponse);
    setIsLoading(false);
  };

  return (
    <div className="w-1/4 h-full border-r border-gray-200 flex flex-col justify-between p-4">
      <h1 className="text-white text-center font-bold text-xl">
        AI Readme Generator
      </h1>

      <Description setDescription={setDescription} />

      <CheckList preferences={preferences} setPreferences={setPreferences} />

      <div className="w-full mt-auto">
        {isRegenerate ? (
          <button
            onClick={reGenerateRequest}
            className={`text-black font-semibold min-w-full min-h-10 bg-slate-50 rounded-lg border-blue-400 border-2 ${
              isLoading ? "opacity-50 cursor-not-allowed" : ""
            }`}
            disabled={isLoading}
          >
            {isLoading ? "Regnerating..." : "Regenerate"}
          </button>
        ) : (
          <button
            onClick={GenerateRequest}
            className={`text-black font-semibold min-w-full min-h-10 bg-slate-50 rounded-lg border-blue-400 border-2 ${
              isLoading ? "opacity-50 cursor-not-allowed" : ""
            }`}
            disabled={isLoading}
          >
            {isLoading ? "Generating..." : "Generate"}
          </button>
        )}
      </div>
    </div>
  );
}

function CheckList({ preferences, setPreferences }) {
  const handleChange = (key) => (e) => {
    setPreferences((prev) => ({
      ...prev,
      [key]: e.target.checked,
    }));
  };

  return (
    <div className="mt-4 pl-1 pb-4 w-full flex flex-col gap-4 overflow-y-auto scrollbar-none">
      {[
        ["title", "Title"],
        ["badge", "Badge"],
        ["introduction", "Introduction"],
        ["table_of_contents", "Table of Contents"],
        ["key_features", "Key Features"],
        ["install_guide", "Installation Guide"],
        ["usage", "Usage"],
        ["api_ref", "API Reference"],
        ["env_var", "Environment Variables"],
        ["project_structure", "Project Structure"],
        ["tech_used", "Technologies Used"],
        ["licenses", "License"],
      ].map(([key, label]) => (
        <CheckListItem
          key={key}
          text={label}
          checked={preferences[key]}
          onChange={handleChange(key)}
        />
      ))}
    </div>
  );
}

function CheckListItem({ text, checked, onChange }) {
  return (
    <label className="flex items-center gap-3 p-3 rounded-lg bg-[#1e2733] hover:bg-[#2a3442] transition duration-500 ease-in-out cursor-pointer">
      <input
        type="checkbox"
        checked={checked}
        onChange={onChange}
        className="w-5 h-5 text-blue-500 accent-blue-500 bg-gray-800 border border-gray-600 rounded focus:ring-2 focus:ring-blue-400 transition duration-500 ease-in-out"
      />
      <span className="text-white text-lg font-medium">{text}</span>
    </label>
  );
}

function Description({ setDescription }) {
  return (
    <div className="w-full h-72 border-blue-500 rounded-lg border-2 mt-5">
      <textarea
        className="h-full w-full rounded-lg bg-inherit text-white p-2 resize-none"
        onChange={(e) => {
          setDescription(e.target.value);
        }}
      ></textarea>
    </div>
  );
}

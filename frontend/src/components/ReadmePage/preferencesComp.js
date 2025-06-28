import { useState, useEffect } from "react";
import { callApi } from "../../utils/api/ApiCaller";
import axios from "axios";

export function Preferences({
  repoUrl,
  setReadmeData,
  setFirstGenerate,
  isLoading,
  setIsLoading,
  setGenerateError,
}) {
  const [proj_description, setDescription] = useState("");
  const [isRegenerate, setIsRegenerate] = useState(false);
  const [sessionReady, setSessionReady] = useState(false);

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

  useEffect(() => {
    axios
      .post(
        "https://readme-generator-uisng-langgraph.onrender.com/api/readme/start",
        {},
        { withCredentials: true }
      )
      .then((res) => {
        setSessionReady(true);
        console.log("Session Started");
      })
      .catch((err) => {
        console.log("Error starting session", err);
      });
  }, []);

  const GenerateRequest = async () => {
    if (!sessionReady) return;
    setGenerateError(null);
    console.log("generating with preferences:", preferences);
    console.log("Description:", proj_description);
    setIsLoading(true);
    const readmeResponse = await callApi({
      url: "https://readme-generator-uisng-langgraph.onrender.com/api/readme/generate",
      method: "POST",
      payload: {
        github_url: repoUrl,
        project_description: proj_description,
        preferences: preferences,
      },
    }).catch((err) => {
      console.error(err);

      setGenerateError(err);
    });

    setReadmeData(readmeResponse);
    setIsLoading(false);
    setIsRegenerate(true);
    setFirstGenerate(true);
  };

  const reGenerateRequest = async () => {
    if (!sessionReady) return;
    setGenerateError(null);
    console.log("Regenerating with preferences:", preferences);
    console.log("Description:", proj_description);
    setIsLoading(true);
    const readmeResponse = await callApi({
      url: "https://readme-generator-uisng-langgraph.onrender.com/api/readme/resume",
      method: "POST",
      payload: {
        action: "regenerate",
        project_description: proj_description,
        preferences: preferences,
      },
    }).catch((err) => {
      console.log(err);

      setGenerateError(err);
    });
    setReadmeData(readmeResponse);
    setIsLoading(false);
  };

  return (
    <div className="w-1/4 h-full border-r border-gray-200 flex flex-col justify-between p-4">
      <h1 className="text-white text-center font-bold text-2xl gradient-text">
        AI Readme Generator
      </h1>

      <Description setDescription={setDescription} />

      <CheckList preferences={preferences} setPreferences={setPreferences} />

      <div className="w-full mt-auto">
        <div className=" rounded-lg p-[3px] bg-gradient-to-r from-[#02c6ff] via-[#0066ff] to-[#da00ff] transition-all duration-300 hover:scale-105 hover:shadow-[0_0_15px_10px_rgba(0,128,255,0.3)] ease-out shadow-[0_0_10px_3px_rgba(0,128,255,0.5)]">
          {isRegenerate ? (
            <button
              onClick={reGenerateRequest}
              className={`text-white font-semibold min-w-full min-h-10 bg-[#030617] rounded-lg  ${
                isLoading ? "opacity-50 cursor-not-allowed" : ""
              }`}
              disabled={isLoading || !sessionReady}
            >
              {sessionReady
                ? isLoading
                  ? "Regenerating..."
                  : "Regenerate"
                : "Server starting please wait.."}
            </button>
          ) : (
            <button
              onClick={GenerateRequest}
              className={`text-white font-semibold min-w-full min-h-10 bg-[#030617] rounded-lg  ${
                isLoading ? "opacity-50 cursor-not-allowed" : ""
              }`}
              disabled={isLoading || !sessionReady}
            >
              {sessionReady
                ? isLoading
                  ? "Generating..."
                  : "Generate"
                : "Server starting please wait.."}
            </button>
          )}
        </div>
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
    <label className="flex items-center gap-3 p-3 shadow-md rounded-lg bg-white/10 backdrop-blur-md hover:bg-white/15 transition-all duration-300 ease-in-out cursor-pointer">
      <input
        type="checkbox"
        checked={checked}
        onChange={onChange}
        className="w-5 h-5 bg-transparent accent-white/10 opacity-75 focus:opacity-50 rounded-lg  transition duration-500 ease-in-out"
      />
      <span className="text-white text-lg font-medium">{text}</span>
    </label>
  );
}

function Description({ setDescription }) {
  return (
    <div className="w-full h-72  rounded-lg  mt-5">
      <textarea
        className="h-full w-full rounded-lg bg-white/10 backdrop-blur-md text-white p-2 resize-none focus:border-none focus:ring-0 outline-none"
        onChange={(e) => {
          setDescription(e.target.value);
        }}
        placeholder="short description..."
      ></textarea>
    </div>
  );
}

import { callApi } from "../../utils/api/ApiCaller";

export function Preferences({ repoUrl, setReadmeData }) {
  const GenerateRequest = async () => {
    const readmeResponse = await callApi({
      url: "http://localhost:8000/api/readme/generate",
      method: "POST",
      payload: {
        github_url:
          "https://github.com/anand-106/Ticket_classifier_using_LangGraph",
        project_description:
          "A project to demonstrate automated README generation using LangGraph and Tree-sitter.",
        preferences: {
          include_badges: true,
          license: "MIT",
          frameworks: ["FastAPI", "LangGraph"],
        },
        session_id: "demo-session-001",
      },
    }).catch((err) => console.error(err));
    setReadmeData(readmeResponse);
  };
  return (
    <div className="w-1/4 h-full border-r border-gray-200 flex flex-col justify-between p-4">
      <h1 className="text-white text-center font-bold text-xl">
        AI Readme Generator
      </h1>
      <div className="w-full mt-auto">
        <button
          onClick={GenerateRequest}
          className="text-black font-semibold min-w-full min-h-10 bg-slate-50 rounded-lg border-blue-400 border-2"
        >
          Generate
        </button>
      </div>
    </div>
  );
}

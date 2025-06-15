import { useState } from "react";
import { callApi } from "../../utils/api/ApiCaller";
import ReactMarkdown from "react-markdown";

export function MarkdownViewer({ repoUrl }) {
  const [readmeData, setReadmeData] = useState();

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
    <div className="h-full ">
      {readmeData?.readme && (
        <div className="prose prose-invert max-w-none">
          <ReactMarkdown>{readmeData.readme}</ReactMarkdown>
        </div>
      )}
      <button onClick={GenerateRequest} className="text-white">
        Generate
      </button>
    </div>
  );
}

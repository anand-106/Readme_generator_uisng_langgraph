import { useState } from "react";
import { useNavigate } from "react-router-dom";
import DOMPurify from "dompurify";

export function LinkTextBox() {
  const [repoUrl, setRepoUrl] = useState("");
  const navigate = useNavigate();
  const handleSubmit = () => {
    const sanitized_url = DOMPurify.sanitize(repoUrl.trim());
    const isValidGitHubUrl =
      /^https:\/\/(www\.)?github\.com\/[^/]+\/[^/]+\/?$/.test(sanitized_url);

    if (sanitized_url && isValidGitHubUrl) {
      navigate(`/readme?repo=${encodeURIComponent(sanitized_url)}`);
    } else {
      alert("Please enter a valid GitHub URL.");
    }
  };

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        handleSubmit();
      }}
      className="w-full max-w-md flex"
    >
      <div className="w-full max-w-md flex">
        <div className="bg-white rounded-l-xl shadow-md w-full max-w-md">
          <input
            type="url"
            placeholder="Enter your Github Repo URL"
            className="w-full p-3 border border-gray-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition duration-200 ease-in-out"
            value={repoUrl}
            onChange={(e) => setRepoUrl(e.target.value)}
          ></input>
        </div>
        <div className="bg-white rounded-r-xl ml-0">
          <button
            className="w-full h-full border border-gray-300 rounded-r-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-center text-gray-800 p-3 transition duration-200 ease-in-out"
            type="submit"
          >
            Submit
          </button>
        </div>
      </div>
    </form>
  );
}

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
    <div className="w-full max-w-2xl bg-gray-800 p-7 rounded-lg shadow-2xl">
      <p className="text-white mb-2">Enter your GitHub Repo Url</p>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleSubmit();
        }}
        className="w-full  flex"
      >
        <div className="w-full  flex gap-2">
          <div className="bg-white rounded-xl shadow-md w-full">
            <input
              type="url"
              placeholder="https://github.com/username/repository"
              className="w-full p-3 bg-gray-700 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 transition duration-200 ease-in-out text-white"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
            ></input>
          </div>
          <div className=" rounded-xl">
            <button
              className="w-full h-full  bg-indigo-500  rounded-lg focus:outline-none focus:bg-indigo-600 text-center text-white font-semibold p-3 transition duration-200 ease-in-out"
              type="submit"
            >
              Submit
            </button>
          </div>
        </div>
      </form>
    </div>
  );
}

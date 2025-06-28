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
    <div className="w-full max-w-2xl bg-[#030617] p-7 rounded-lg shadow-2xl">
      <p className="text-white mb-2">Enter your GitHub Repo Url</p>
      <form
        onSubmit={(e) => {
          e.preventDefault();
          handleSubmit();
        }}
        className="w-full  flex"
      >
        <div className="w-full  flex gap-2">
          <div className=" rounded-lg shadow-md w-full">
            <input
              type="url"
              placeholder="https://github.com/username/repository"
              className="w-full h-full p-3 bg-white/10 border backdrop-blur-md border-white/70 rounded-lg placeholder-white/50 text-white transition-all duration-400 ease-out focus:shadow-[0_0_75px_10px_rgba(255,255,255,0.3)] hover:shadow-[0_0_15px_3px_rgba(255,255,255,0.3)]"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
            ></input>
          </div>
          <div className=" rounded-lg p-[3px] bg-gradient-to-r from-[#02c6ff] via-[#0066ff] to-[#da00ff] transition-all duration-300 hover:scale-105 hover:shadow-[0_0_15px_10px_rgba(0,128,255,0.3)] ease-out shadow-[0_0_5px_3px_rgba(0,128,255,0.5)]">
            <button
              className="w-full h-full  bg-[#030617]  rounded-lg  text-center text-white font-semibold p-3  "
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

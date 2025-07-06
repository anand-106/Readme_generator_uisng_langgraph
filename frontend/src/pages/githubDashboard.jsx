import axios from "axios";
import { useEffect, useState } from "react";

export function GithubDashboard() {
  const [userData, setUserData] = useState({});

  const handleGithubUser = () => {
    axios.get("http://localhost:8000/api/github/user").then((res) => {
      const {
        avatar,
        username,
        name,
        public_repos,
        public_repos_count,
        private_repos,
        private_repos_count,
      } = res.data;
      setUserData({
        avatar,
        username,
        name,
        public_repos_count,
        public_repos,
        private_repos_count,
        private_repos,
      });
    });
  };

  useEffect(handleGithubUser, []);

  return (
    <div className="w-full h-full text-white p-4 overflow-y-auto">
      <div className="flex items-center space-x-4">
        <img
          src={userData.avatar}
          alt="Avatar"
          className="w-16 h-16 rounded-full"
        />
        <div>
          <h1 className="text-xl font-semibold">
            {userData.name} (@{userData.username})
          </h1>
          <p>
            Public Repos: {userData.public_repos_count} | Private Repos:{" "}
            {userData.private_repos_count}
          </p>
        </div>
      </div>

      <div className="mt-6">
        <h2 className="text-lg font-semibold">Public Repositories:</h2>
        <ul className="list-disc ml-6">
          {userData.public_repos?.map((repo, idx) => (
            <li key={idx}>
              <a
                href={repo.html_url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-400 underline"
              >
                {repo.full_name}
              </a>{" "}
              ⭐ {repo.stars} | 🍴 {repo.forks}
            </li>
          ))}
        </ul>
      </div>

      <div className="mt-6">
        <h2 className="text-lg font-semibold">Private Repositories:</h2>
        <ul className="list-disc ml-6">
          {userData.private_repos?.map((repo, idx) => (
            <li key={idx}>
              <span>{repo.full_name}</span> ⭐ {repo.stars} | 🍴 {repo.forks}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

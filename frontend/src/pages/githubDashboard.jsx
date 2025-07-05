import axios from "axios";
import { useEffect, useState } from "react";

export function GithubDashboard() {
  const [userData, setUserData] = useState({});

  const handleGithubUser = () => {
    axios.get("http://localhost:8000/api/github/user").then((res) => {
      setUserData({
        avatar: res.data.avatar,
        username: res.data.username,
        name: res.data.name,
        public_repos: res.data.public_repos,
        private_repos: res.data.private_repos,
      });
    });
  };

  useEffect(handleGithubUser, []);

  return (
    <div className="w-full h-full text-white">
      <img
        src={userData.avatar}
        alt="Avatar"
        className="w-16 h-16 rounded-full"
      />
      <h1>
        {userData.name} (@{userData.username})
      </h1>
      <p>Public Repos: {userData.public_repos}</p>
      <p>Private Repos: {userData.private_repos}</p>
    </div>
  );
}

import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export function GithubDashboard() {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const navigator = useNavigate();

  const handleGithubUser = async () => {
    try {
      const res = await axios.get("http://localhost:8000/api/github/user", {
        withCredentials: true,
      });
      const { avatar, username, name, repos } = res.data;
      setUserData({
        avatar,
        username,
        name,
        repos,
      });
    } catch (err) {
      console.error("Error fetching GitHub user:", err);
      setError("Failed to fetch GitHub user info.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    handleGithubUser();
  }, []);

  if (loading) {
    return <p className="text-white p-4">Loading GitHub data...</p>;
  }

  if (error) {
    return <p className="text-red-500 p-4">{error}</p>;
  }

  if (!userData) {
    return <p className="text-yellow-400 p-4">No user data available.</p>;
  }

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
        </div>
      </div>

      <div className="mt-6">
        <h2 className="text-lg font-semibold">Repositories:</h2>
        {userData.repos?.length > 0 ? (
          <ul className="list-disc ml-6">
            {userData.repos.map((repo, idx) => (
              <li
                key={idx}
                onClick={() => {
                  navigator("/github/repo", {
                    state: {
                      username: userData.username,
                      repo_name: repo.repo_fullname,
                      repo_url: repo.html_url,
                      repo_id: repo.repo_id,
                    },
                  });
                }}
              >
                <div className="text-blue-400 underline">
                  {repo.repo_fullname}
                </div>{" "}
                ⭐ {repo.stars} | 🍴 {repo.forks}
              </li>
            ))}
          </ul>
        ) : (
          <p className="text-gray-400 ml-2">No repositories found.</p>
        )}
      </div>
    </div>
  );
}

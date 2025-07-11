import axios from "axios";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaRegStar } from "react-icons/fa";
import { FaCodeFork } from "react-icons/fa6";

export function GithubDashboard() {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [reposData, setReposData] = useState(null);
  const [error, setError] = useState("");

  const handleGithubUser = async () => {
    try {
      const res = await axios.get("http://localhost:8000/api/github/user", {
        withCredentials: true,
      });
      console.log(res.data);
      const { avatar, username, name, repos, whrepos } = res.data;
      setReposData(whrepos);
      setUserData({
        avatar,
        username,
        name,
        repos,
        whrepos,
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
    <div className="w-full h-full font-figtree overflow-y-auto text-white">
      {/* <div className="">
        <img
          src={userData.avatar}
          alt="Avatar"
          className="w-16 h-16 rounded-full"
        />
        <div>
          <h1 className="">
            {userData.name} (@{userData.username})
          </h1>
        </div>
      </div> */}
      <Header userData={userData} />

      <div className="p-6">
        <div>
          <h2 className="">Active Repositories:</h2>
          <WebhookList userData={userData} />
        </div>
        <h2 className="">All Repositories:</h2>
        <RepoList userData={userData} />
      </div>
    </div>
  );
}

function Header({ userData }) {
  const navigator = useNavigate();
  return (
    <div className="w-full flex p-5 pl-5 justify-between">
      <div
        className="flex gap-2 cursor-pointer"
        onClick={() => {
          navigator("/");
        }}
      >
        <img src="/assets/logo160.png" alt="logo" className="w-7 h-7" />
        <h1 className="font-semibold text-2xl">Dashboard</h1>
      </div>
      <img src={userData.avatar} alt="Avatar" className="w-10 rounded-full" />
    </div>
  );
}

function WebhookList({ userData }) {
  return userData.whrepos?.length > 0 ? (
    <ul className="flex flex-wrap">
      {userData.whrepos.map((repo, idx) => (
        <WhRepoItem idx={idx} userData={userData} repo={repo} />
      ))}
    </ul>
  ) : (
    <p className="text-gray-400 ml-2">No repositories found.</p>
  );
}
function WhRepoItem({ idx, userData, repo }) {
  const navigator = useNavigate();
  return (
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
      <div className="p- w-[300px] h-24 backdrop:blur-md bg-transparent border-white border-solid border-2 p-3 rounded-lg flex flex-col justify-between  m-5 cursor-pointer hover:scale-105 transition-all duration-300 ease-out hover:shadow-[0_0_15px_3px_rgba(255,255,255,0.3)]">
        <h1 className="truncate">{repo.repo_fullname}</h1>
        <div className="flex gap-3">
          <div className="flex justify-center items-center gap-1">
            <FaRegStar />
            <h1>{repo.stars}</h1>
          </div>
          <div className="flex justify-center items-center gap-1">
            <FaCodeFork />
            <h1>{repo.forks}</h1>
          </div>
        </div>
      </div>
    </li>
  );
}

function RepoList({ userData }) {
  return userData.repos?.length > 0 ? (
    <ul className="flex flex-wrap">
      {userData.repos.map((repo, idx) => (
        <RepoItem idx={idx} userData={userData} repo={repo} />
      ))}
    </ul>
  ) : (
    <p className="text-gray-400 ml-2">No repositories found.</p>
  );
}

function RepoItem({ idx, userData, repo }) {
  const navigator = useNavigate();
  return (
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
      <div className="p- w-[300px] h-24 backdrop:blur-md bg-transparent border-white border-solid border-2 p-3 rounded-lg flex flex-col justify-between  m-5 cursor-pointer hover:scale-105 transition-all duration-300 ease-out hover:shadow-[0_0_15px_3px_rgba(255,255,255,0.3)]">
        <h1 className="truncate">{repo.repo_fullname}</h1>
        <div className="flex gap-3">
          <div className="flex justify-center items-center gap-1">
            <FaRegStar />
            <h1>{repo.stars}</h1>
          </div>
          <div className="flex justify-center items-center gap-1">
            <FaCodeFork />
            <h1>{repo.forks}</h1>
          </div>
        </div>
      </div>
    </li>
  );
}

import axios from "axios";
// import Beams from "../../Beams/Beams";

import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaRegStar } from "react-icons/fa";
import { FaCodeFork } from "react-icons/fa6";
import Aurora from "../../src/pages/Aurora/Aurora";
import SlidePageWrapper from "../../animations/SlidePageWrapper";
import { RiRadioButtonLine } from "react-icons/ri";

export function GithubDashboard() {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const handleGithubUser = async () => {
    try {
      const res = await axios.get("http://localhost:8000/api/github/user", {
        withCredentials: true,
      });
      console.log(res.data);
      const { avatar, username, name, repos, whrepos } = res.data;
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
    <SlidePageWrapper>
      <div className="w-full h-full font-figtree  text-white relative">
        <div>
          <Aurora
            className=""
            colorStops={["#02c6ff", "#0066ff", "#da00ff"]}
            blend={1}
            amplitude={1.0}
            speed={0.5}
          />
        </div>

        <div className="absolute z-40 overflow-y-auto  inset-0 scrollbar-none">
          <Header userData={userData} />

          <div className="p-6">
            <div>
              <h2 className="">Auto Readme Repositories:</h2>
              <WebhookList userData={userData} />
            </div>
            <h2 className="">All Repositories:</h2>
            <RepoList userData={userData} />
          </div>
        </div>
      </div>
    </SlidePageWrapper>
  );
}

function Header({ userData }) {
  const navigator = useNavigate();
  return (
    <div className="w-full flex p-5 pl-5 justify-between">
      <div
        className="flex gap-2 cursor-pointer"
        onClick={() => {
          // navigator("/");
        }}
      >
        <img src="/assets/logo160.png" alt="logo" className="w-7 h-7" />
        <h1 className="font-semibold text-2xl">Dashboard</h1>
      </div>
      {userData && (
        <div className="bg-white/10 border border-white/50 backdrop-blur-md w-12 h-12 rounded-full items-center mt-[-7px] cursor-pointer justify-center flex">
          <ProfileIcon userData={userData} />
        </div>
      )}
    </div>
  );
}

function ProfileIcon({ userData }) {
  const navigator = useNavigate();
  return (
    <img
      src={userData.avatar}
      onClick={() => {
        navigator(`/github/${userData.username}/profile`, {
          state: userData,
        });
      }}
      alt="Avatar"
      className="w-10 rounded-full"
    />
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
        navigator(`/github/${repo.repo_fullname}`, {
          state: {
            username: userData.username,
            repo_name: repo.repo_fullname,
            repo_url: repo.html_url,
            repo_id: repo.repo_id,
          },
        });
      }}
    >
      <div className="p- w-[300px] h-24 backdrop-blur-md bg-white/10 border-white/20 border-solid border p-3 rounded-lg flex flex-col justify-between  m-5 cursor-pointer hover:scale-105 transition-all duration-300 ease-out">
        <h1 className="truncate">{repo.repo_fullname}</h1>
        <div className="flex justify-between">
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
          <div className="flex text-green-400  items-end">
            <RiRadioButtonLine />
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
        navigator(`/github/${repo.repo_fullname}`, {
          state: {
            username: userData.username,
            repo_name: repo.repo_fullname,
            repo_url: repo.html_url,
            repo_id: repo.repo_id,
          },
        });
      }}
    >
      <div className="p- w-[300px] h-24 backdrop-blur-md bg-white/10 border-white/20 border-solid border p-3 rounded-lg flex flex-col justify-between  m-5 cursor-pointer hover:scale-105 transition-all duration-300 ease-out  ">
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

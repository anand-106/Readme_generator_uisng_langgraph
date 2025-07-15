import { FaGithub } from "react-icons/fa";

export function GitLogin() {
  const GITHUB_CLIENT_ID = process.env.REACT_APP_GITHUB_CLIENT_ID;

  const githubRedirect = () => {
    const GithubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${GITHUB_CLIENT_ID}&scope=repo user admin:repo_hook`;
    window.location.href = GithubAuthUrl;
  };

  return (
    <div className="text-white w-full h-full flex flex-col justify-center items-center">
      <div className="flex flex-col gap-3 mt-[-200px] items-center w-full justify-center text-center">
        <h1 className="text-3xl font-bold font">Signin to Readme AI</h1>
        <div
          className="flex mt-3 justify-center text-center font-medium items-center gap-2 w-[250px] cursor-pointer bg-white/10 border border-white/50 backdrop-blur-md rounded-3xl h-10"
          onClick={githubRedirect}
        >
          <FaGithub />
          <h1 className="">Continue with GitHub</h1>
        </div>
        <h1 className="text-white/50">
          Click once. Never write a README manually again.
        </h1>
      </div>
    </div>
  );
}

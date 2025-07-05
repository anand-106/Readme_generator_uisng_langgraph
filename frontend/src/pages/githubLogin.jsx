export function GitLogin() {
  const GITHUB_CLIENT_ID = process.env.REACT_APP_GITHUB_CLIENT_ID;

  const githubRedirect = () => {
    const GithubAuthUrl = `https://github.com/login/oauth/authorize?client_id=${GITHUB_CLIENT_ID}&scope=repo user admin:repo_hook`;
    window.location.href = GithubAuthUrl;
  };
  return (
    <div className="text-white">
      <button onClick={githubRedirect}>GitHub Login</button>
    </div>
  );
}

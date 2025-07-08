import axios from "axios";
import { useLocation } from "react-router-dom";

export function RepoPage() {
  const { state } = useLocation();

  console.log(state);

  const { username, repo_name, repo_url, repo_id } = state || {};

  const handleWebhook = () => {
    console.log("Sending webhook request with:", {
      username,
      repo_name,
      repo_url,
      repo_id,
    });
    axios
      .post(
        "http://localhost:8000/api/github/create-webhook",
        {
          username,
          repo_name,
          repo_url,
          repo_id,
        },
        {
          withCredentials: true,
          headers: {
            "Content-Type": "application/json",
          },
        }
      )
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="text-white">
      <h1>{repo_name}</h1>
      <button onClick={handleWebhook}>Create Webhook</button>
    </div>
  );
}

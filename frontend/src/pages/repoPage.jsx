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

  const disable_webhook = (isActive) => {
    axios
      .post(
        "http://localhost:8000/api/github/disable-webhook",
        {
          repo_id: repo_id,
          isActive: isActive,
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

  const delete_webhook = () => {
    axios
      .post(
        "http://localhost:8000/api/github/delete-webhook",
        {
          repo_id: repo_id,
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
    <div className="text-white flex-col">
      <h1>{repo_name}</h1>
      <button onClick={handleWebhook}>Create Webhook</button>
      <button
        onClick={() => {
          disable_webhook(false);
        }}
      >
        Disable Webhook
      </button>
      <button
        onClick={() => {
          disable_webhook(true);
        }}
      >
        Enable Webhook
      </button>
      <button
        onClick={() => {
          delete_webhook();
        }}
      >
        Delete Webhook
      </button>
    </div>
  );
}

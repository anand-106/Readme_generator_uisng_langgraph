import axios from "axios";
import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import toast, { Toaster } from "react-hot-toast";
import { IoMdSettings } from "react-icons/io";
import { FaPlusCircle } from "react-icons/fa";
import { FaCircleStop } from "react-icons/fa6";
import { MdDelete } from "react-icons/md";
import { MdElectricBolt } from "react-icons/md";
import { IoArrowBackSharp } from "react-icons/io5";

export function RepoPage() {
  const [isWhCreated, setIsWhCreated] = useState(false);
  const [preferences, setPreferences] = useState({
    title: true,
    badge: true,
    introduction: true,
    table_of_contents: true,
    key_features: true,
    install_guide: true,
    usage: true,
    api_ref: true,
    env_var: true,
    project_structure: true,
    tech_used: true,
    licenses: true,
  });

  const [description, setDescription] = useState("");

  const { state } = useLocation();

  const { username, repo_name, repo_url, repo_id } = state || {};

  const handleUpdateWebhook = () => {
    const toastId = toast.loading("Applying settings...");
    axios
      .post(
        "https://readme-generator-uisng-langgraph.onrender.com/api/github/update-webhook",
        {
          repo_id,
          preferences,
          description,
        },
        {
          withCredentials: true,
        }
      )
      .then((res) => {
        console.log(res);
        toast.success("Settings applied!", { id: toastId });
      })
      .catch((err) => {
        console.log(err);
        const errorMessage = err.response?.data?.detail || err.message || "Failed to apply settings.";
        toast.error(errorMessage, { id: toastId });
      });
  };

  useEffect(() => {
    axios
      .post(
        "https://readme-generator-uisng-langgraph.onrender.com/api/github/webhook",
        {
          repo_id,
        },
        {
          withCredentials: true,
        }
      )
      .then((res) => {
        console.log(res);
        if (res.data.available) {
          setIsWhCreated(true);
          setDescription(res.data.description);
          setPreferences(res.data.preferences);
        } else {
          setIsWhCreated(false);
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }, [repo_id]);

  return (
    <div className="text-white w-full h-full flex justify-center lg:items-center relative overflow-y-auto">
      <div className="absolute top-0 z-10  left-0 m-4 text-lg font-semibold">
        <Toaster
          position="top-center"
          reverseOrder={false}
          toastOptions={{
            style: {
              border: "1px solid #ffffff",
              padding: "16px",
              color: "#ffffff",
              background: "#030617",
            },
            iconTheme: {
              primary: "#ffffff",
              secondary: "#030617",
            },
          }}
        />
        <Header />
      </div>
      <div className="w-[1200px] h-fit bg-white/5 rounded-2xl p-5 border border-white/50 max-lg:mt-14">
        <h1 className="font-semibold text-lg">{repo_name}</h1>
        <div className="flex justify-center items-center max-sm:flex-col w-full">
          <div className="sm:max-w-[600px] sm:min-w-[400px] h-[300px] max-sm:w-full m-5 flex flex-col gap-2">
            <Description
              description={description}
              setDescription={setDescription}
            />
            <button
              className="bg-white/10 border border-white/50 rounded-lg h-10 flex justify-center items-center gap-2"
              onClick={() => {
                if (isWhCreated) {
                  handleUpdateWebhook();
                } else {
                  console.log("settings Updated");
                }
              }}
            >
              <IoMdSettings />
              <h1>Apply Settings</h1>
            </button>
          </div>

          <Preferences
            preferences={preferences}
            setPreferences={setPreferences}
          />
        </div>
        <div className="w-full ">
          <WebhookButtons
            username={username}
            repo_name={repo_name}
            repo_url={repo_url}
            repo_id={repo_id}
            description={description}
            preferences={preferences}
            isWhCreated={isWhCreated}
          />
        </div>
      </div>
    </div>
  );
}

function Header() {
  const navigator = useNavigate();
  return (
    <div className="flex justify-center items-center gap-2">
      <div
        className="cursor-pointer text-2xl"
        onClick={() => {
          navigator(-1);
        }}
      >
        <IoArrowBackSharp />
      </div>
      <h1>Auto Readme Settings</h1>
    </div>
  );
}

function Description({ description, setDescription }) {
  return (
    <div className="w-full h-full  rounded-xl bg-transparent border border-white/50 ">
      <textarea
        className="w-full h-full p-3 rounded-xl bg-transparent resize-none"
        value={description}
        onChange={(e) => {
          setDescription(e.target.value);
        }}
      />
    </div>
  );
}

function Preferences({ preferences, setPreferences }) {
  const handleChange = (key) => (e) => {
    setPreferences((prev) => ({
      ...prev,
      [key]: e.target.checked,
    }));
  };

  return (
    <div className="mt-4 pl-1 pb-4 max-h-[300px] scrollbar-none w-full justify-center items-center flex flex-wrap gap-4 overflow-y-auto">
      {[
        ["title", "Title"],
        ["badge", "Badge"],
        ["introduction", "Introduction"],
        ["table_of_contents", "Table of Contents"],
        ["key_features", "Key Features"],
        ["install_guide", "Installation Guide"],
        ["usage", "Usage"],
        ["api_ref", "API Reference"],
        ["env_var", "Environment Variables"],
        ["project_structure", "Project Structure"],
        ["tech_used", "Technologies Used"],
        ["licenses", "License"],
      ].map(([key, label]) => (
        <PreferenceItem
          key={key}
          text={label}
          checked={preferences[key]}
          onChange={handleChange(key)}
        />
      ))}
    </div>
  );
}

function PreferenceItem({ text, checked, onChange }) {
  return (
    <label className="flex items-center gap-3 p-3 sm:w-56 max-sm:w-full shadow-md rounded-lg bg-white/10 backdrop-blur-md hover:bg-white/15 transition-all duration-300 ease-in-out cursor-pointer">
      <input
        type="checkbox"
        checked={checked}
        onChange={onChange}
        className="w-5 h-5 accent-[#030617] rounded  appearance-auto"
      />
      <span className="text-white font-figtree text-base font-medium">
        {text}
      </span>
    </label>
  );
}

function WebhookButtons({
  username,
  repo_name,
  repo_url,
  repo_id,
  description,
  preferences,
  isWhCreated,
}) {
  const handleWebhook = () => {
    console.log("Sending webhook request with:", {
      username,
      repo_name,
      repo_url,
      repo_id,
    });
    const toastId = toast.loading("Creating webhook...");
    axios
      .post(
        "https://readme-generator-uisng-langgraph.onrender.com/api/github/create-webhook",
        {
          username,
          repo_name,
          repo_url,
          repo_id,
          description: description,
          preferences: preferences,
        },
        {
          withCredentials: true,
          headers: { "Content-Type": "application/json" },
        }
      )
      .then((res) => {
        console.log(res);
        toast.success("Webhook created successfully!", { id: toastId });
      })
      .catch((err) => {
        console.log(err);
        const errorMessage = err.response?.data?.detail || err.message || "Failed to create webhook.";
        toast.error(errorMessage, { id: toastId });
      });
  };

  const disable_webhook = (isActive) => {
    const actionText = isActive ? "Enabling" : "Disabling";
    const toastId = toast.loading(`${actionText} webhook...`);
    axios
      .post(
        "https://readme-generator-uisng-langgraph.onrender.com/api/github/disable-webhook",
        { repo_id, isActive },
        {
          withCredentials: true,
          headers: { "Content-Type": "application/json" },
        }
      )
      .then((res) => {
        console.log(res);
        toast.success(`Webhook ${isActive ? 'enabled' : 'disabled'} successfully!`, { id: toastId });
      })
      .catch((err) => {
        console.log(err);
        const errorMessage = err.response?.data?.detail || err.message || `Failed to ${isActive ? 'enable' : 'disable'} webhook.`;
        toast.error(errorMessage, { id: toastId });
      });
  };

  const delete_webhook = () => {
    const toastId = toast.loading("Deleting webhook...");
    axios
      .post(
        "https://readme-generator-uisng-langgraph.onrender.com/api/github/delete-webhook",
        { repo_id },
        {
          withCredentials: true,
          headers: { "Content-Type": "application/json" },
        }
      )
      .then((res) => {
        console.log(res);
        toast.success("Webhook deleted successfully!", { id: toastId });
      })
      .catch((err) => {
        console.log(err);
        const errorMessage = err.response?.data?.detail || err.message || "Failed to delete webhook.";
        toast.error(errorMessage, { id: toastId });
      });
  };

  return (
    <div className="flex flex-wrap justify-center gap-4 w-full mt-4 ">
      <ActionButton
        disabled={isWhCreated}
        onClick={handleWebhook}
        Icon={<FaPlusCircle />}
        customCss={`${isWhCreated ? "cursor-not-allowed" : ""}`}
      >
        Create Webhook
      </ActionButton>
      <ActionButton
        disabled={!isWhCreated}
        onClick={() => disable_webhook(false)}
        Icon={<FaCircleStop />}
        customCss={`${!isWhCreated ? "cursor-not-allowed" : ""}`}
      >
        Disable Webhook
      </ActionButton>
      <ActionButton
        disabled={!isWhCreated}
        onClick={() => disable_webhook(true)}
        Icon={<MdElectricBolt />}
        customCss={`${!isWhCreated ? "cursor-not-allowed" : ""}`}
      >
        Enable Webhook
      </ActionButton>
      <ActionButton
        disabled={!isWhCreated}
        onClick={delete_webhook}
        Icon={<MdDelete />}
        customCss={`${!isWhCreated ? "cursor-not-allowed" : ""}`}
      >
        Delete Webhook
      </ActionButton>
    </div>
  );
}

function ActionButton({ disabled, onClick, children, Icon, customCss }) {
  return (
    <button
      className={`${customCss} flex-shrink-0 flex justify-center items-center gap-2 bg-white/10 border border-white/50 rounded-lg h-10 w-[250px] hover:bg-white/20 transition`}
      onClick={onClick}
      disabled={disabled}
    >
      {Icon}
      <h1>{children}</h1>
    </button>
  );
}

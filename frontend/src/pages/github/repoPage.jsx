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
        "http://localhost:8000/api/github/update-webhook",
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
        toast.success("✅ Settings applied!", { id: toastId });
      })
      .catch((err) => {
        console.log(err);
        toast.error("❌ Failed to apply settings.", { id: toastId });
      });
  };

  useEffect(() => {
    axios
      .post(
        "http://localhost:8000/api/github/webhook",
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
  }, []);

  return (
    <div className="text-white w-full h-full flex justify-center items-center relative">
      <div className="absolute top-0 z-10  left-0 m-4 text-lg font-semibold">
        <Toaster
          position="top-center"
          reverseOrder={false}
          toastOptions={{
            style: {
              border: "1px solid #713200",
              padding: "16px",
              color: "#030617",
            },
          }}
        />
        <Header />
      </div>
      <div className="w-[1200px] h-[500px] bg-white/5 rounded-2xl p-5 border border-white/50">
        <h1 className="font-semibold text-lg">{repo_name}</h1>
        <div className="flex">
          <div className="w-1/2 h-[300px] m-5 flex flex-col gap-2">
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
    <div className="mt-4 pl-1 pb-4 max-h-[300px] scrollbar-none w-full flex flex-wrap gap-4 overflow-y-auto">
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
    <label className="flex items-center gap-3 p-3 w-56 shadow-md rounded-lg bg-white/10 backdrop-blur-md hover:bg-white/15 transition-all duration-300 ease-in-out cursor-pointer">
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
    axios
      .post(
        "http://localhost:8000/api/github/create-webhook",
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
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  };

  const disable_webhook = (isActive) => {
    axios
      .post(
        "http://localhost:8000/api/github/disable-webhook",
        { repo_id, isActive },
        {
          withCredentials: true,
          headers: { "Content-Type": "application/json" },
        }
      )
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  };

  const delete_webhook = () => {
    axios
      .post(
        "http://localhost:8000/api/github/delete-webhook",
        { repo_id },
        {
          withCredentials: true,
          headers: { "Content-Type": "application/json" },
        }
      )
      .then((res) => console.log(res))
      .catch((err) => console.log(err));
  };

  return (
    <div className="flex flex-wrap justify-center gap-4 w-full mt-4">
      <ActionButton onClick={handleWebhook} Icon={<FaPlusCircle />}>
        Create Webhook
      </ActionButton>
      <ActionButton
        disabled={!isWhCreated}
        onClick={() => disable_webhook(false)}
        Icon={<FaCircleStop />}
      >
        Disable Webhook
      </ActionButton>
      <ActionButton
        disabled={!isWhCreated}
        onClick={() => disable_webhook(true)}
        Icon={<MdElectricBolt />}
      >
        Enable Webhook
      </ActionButton>
      <ActionButton
        disabled={!isWhCreated}
        onClick={delete_webhook}
        Icon={<MdDelete />}
      >
        Delete Webhook
      </ActionButton>
    </div>
  );
}

function ActionButton({ disabled, onClick, children, Icon }) {
  return (
    <button
      className="flex-shrink-0 flex justify-center items-center gap-2 bg-white/10 border border-white/50 rounded-lg h-10 w-[250px] hover:bg-white/20 transition"
      onClick={onClick}
      disabled={disabled}
    >
      {Icon}
      <h1>{children}</h1>
    </button>
  );
}

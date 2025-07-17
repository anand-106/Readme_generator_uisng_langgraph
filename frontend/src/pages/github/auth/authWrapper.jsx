import axios from "axios";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export function AuthWrapper() {
  const navigator = useNavigate();

  useEffect(() => {
    axios
      .get(
        "https://readme-generator-uisng-langgraph.onrender.com/api/github/login",
        {
          withCredentials: true,
        }
      )
      .then((res) => {
        if (res.data.username) {
          navigator(`/github/${res.data.username}`);
        } else {
          navigator("/github/login");
        }
      });
  });

  return (
    <div className="h-full w-full items-center justify-center">
      <h1 className="text-white/50">
        Please Wait...The sever may be Booting Up...
      </h1>
    </div>
  );
}

import { useLocation, useNavigate } from "react-router-dom";
import { TbLogout } from "react-icons/tb";
import axios from "axios";
import { IoArrowBackSharp } from "react-icons/io5";

export function Profile() {
  const { state } = useLocation();
  const naviagtor = useNavigate();
  const handleLogout = () => {
    axios
      .post(
        "http://localhost:8000/api/github/logout",
        {},
        {
          withCredentials: true,
        }
      )
      .then((res) => {
        naviagtor("/github");
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <div className="w-full h-full flex items-center justify-center text-white">
      <div className="absolute top-0 z-10  left-0 m-4 text-lg font-semibold">
        <Header />
      </div>
      <div className="w-[400px] h-[450px] mx-6 flex justify-center bg-white/5 backdrop-blur-md rounded-xl border border-white/20 p-6">
        <div className="flex flex-col gap-3 h-full w-full items-center ">
          <div className="bg-white/10 border border-white/50 backdrop-blur-md w-[88px] h-[88px] rounded-full items-center justify-center flex">
            <img
              src={state.avatar}
              alt="profile"
              className="rounded-full w-20 h-20 "
            />
          </div>
          <div>
            <h1 className="text-center font-bold text-xl">{state.name}</h1>
            <h1 className="text-center font-medium text-base text-white/50">
              {`@${state.username}`}
            </h1>
          </div>
          <div className="w-full p-6 flex flex-col gap-4 mt-8">
            <div className="w-full flex justify-between">
              <h1>{`Total Repos:`}</h1>
              <h1>{state.repos.length}</h1>
            </div>
            <div className="w-full flex justify-between">
              <h1>{`Auto Readme Repos:`}</h1>
              <h1>{state.whrepos.length}</h1>
            </div>
          </div>
          <div
            className="flex mt-5 justify-center font-medium items-center gap-2 w-[90%] cursor-pointer bg-white/10 border border-white/50 backdrop-blur-md rounded-3xl h-10"
            onClick={handleLogout}
          >
            <TbLogout />
            <h1 className="">Logout</h1>
          </div>
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
      <h1>Profile</h1>
    </div>
  );
}

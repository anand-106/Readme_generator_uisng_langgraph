import { useNavigate } from "react-router-dom";

export function AutomateSec() {
  const navigator = useNavigate();
  return (
    <div className="flex flex-col justify-center items-center">
      <div className="text-white w-full flex items-center justify-center gap-4 my-3">
        <div className="w-1/3 h-px bg-gray-600" />
        <span className="text-sm text-gray-300">or</span>
        <div className="w-1/3 h-px bg-gray-600" />
      </div>
      <h1 className="text-white text-lg  mb-4">
        ⚡ Auto-generate & auto-commit README.md - every time you push.
      </h1>
      <div
        className="rounded-full w-52 h-[60px] p-[0px] bg-gradient-to-r from-[#02c6ff] via-[#0066ff] to-[#da00ff] transition-all duration-300 hover:scale-105 relative group overflow-hidden"
        onClick={() => {
          navigator("/github");
        }}
      >
        <span
          className="absolute w-full h-full  bg-gradient-to-r from-transparent via-white/30 to-transparent bg-[length:200%_100%]
      bg-right
      group-hover:animate-shimmer "
        />
        <button
          className="relative z-10 w-full h-full font-figtree  bg-transparent  rounded-full  text-center text-white font-semibold "
          type="submit"
        >
          Get Started
        </button>
      </div>
    </div>
  );
}

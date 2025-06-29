import SlidePageWrapper from "../animations/SlidePageWrapper";
import { LinkTextBox } from "../components/home/LinkTextBox";
import { Title } from "../components/home/Title";
import Aurora from "../src/pages/Aurora/Aurora";
import { FaGithub } from "react-icons/fa";
import { Link } from "react-router-dom";

export function HomePage() {
  return (
    <SlidePageWrapper>
      <div className="min-h-screen bg-[#030617] w-full relative flex flex-col items-center justify-start overflow-hidden">
        <Header />
        <Title />
        <LinkTextBox />
        <Footer />
      </div>
    </SlidePageWrapper>
  );
}

function Header() {
  return (
    <>
      <Aurora
        className="absolute  w-full h-full top-0 z-10 pointer-events-none"
        colorStops={["#02c6ff", "#0066ff", "#da00ff"]}
        blend={1}
        amplitude={1.0}
        speed={0.5}
      />
      <div className="absolute top-0 text-white right-0 z-20 mt-7 mr-12">
        <a
          href="https://github.com/anand-106/Readme_generator_uisng_langgraph"
          target="_blank"
          rel="noopener noreferrer"
        >
          <div className="bg-white/10 px-3 py-2 rounded-full backdrop-blur-md border-white/30 flex justify-center items-center gap-2 border ">
            <FaGithub />
            <h1 className="font-semibold font-figtree">GitHub</h1>
          </div>
        </a>
      </div>
      <div className="absolute top-0 text-white left-0 z-20 mt-7 ml-12">
        <Link to={"/"}>
          <div className="flex justify-center items-center gap-2">
            <img src="assets/logo160.png" alt="logo" className="w-7" />
            <h1 className="font-semibold font-figtree text-2xl">Readme AI</h1>
          </div>
        </Link>
      </div>
    </>
  );
}

function Footer() {
  return (
    <div className="absolute bottom-0 mb-3">
      <p className="text-white/40">
        © 2025 Readme AI · Built by{" "}
        {<a href="https://github.com/anand-106">@anand-106</a>} · v1.0
      </p>
    </div>
  );
}

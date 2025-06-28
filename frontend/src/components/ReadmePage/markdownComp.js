import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";
import rehypeHighlight from "rehype-highlight";
import "highlight.js/styles/github-dark.css";
import { useState } from "react";
import { Download, Copy, CopyCheck } from "lucide-react";
// import { DotLottieReact } from "@lottiefiles/dotlottie-react";

export function MarkdownViewer({
  readmeData,
  firstGenerate,
  isLoading,
  generateError,
}) {
  const [activeTab, setActiveTab] = useState("preview");

  return (
    <div className="h-full w-3/4 overflow-y-auto px-12 py-10 bg-[#030617] text-white font-sans relative scrollbar-thin scrollbar-track-slate-800 scrollbar-thumb-gray-300">
      {/* <h1 className="text-3xl font-sans font-bold text-transparent bg-clip-text bg-gradient-to-r from-[#ff6ec4] via-white to-[#7873f5] bg-[length:300%_100%] animate-shimmer">
        Generating Readme...
      </h1> */}
      {isLoading ? (
        <Loader />
      ) : (
        firstGenerate &&
        readmeData?.readme && (
          <>
            <div className="fixed right-10 bottom-5 z-20 shadow-md">
              <ToggleSwitch activeTab={activeTab} setActiveTab={setActiveTab} />
            </div>
            <div className="fixed bottom-6 z-20 shadow-md">
              <CopyDownload readmeData={readmeData} />
            </div>
          </>
        )
      )}

      {readmeData?.readme &&
        (activeTab === "preview" ? (
          <div
            className="markdown-viewer prose prose-invert max-w-none markdown-rendered
            prose-pre:rounded-lg prose-pre:px-4 prose-pre:py-3
           prose-code:rounded prose-code:px-1 prose-code:py-0.5
            prose-code:font-[SFMono-Regular,Consolas,Liberation_Mono,Menlo,monospace]
            prose-h1:mt-3 prose-h2:mt-2 prose-p:my-2 prose-li:my-1 prose-ul:my-1 prose-ol:my-1
            prose-a:text-blue-400 hover:prose-a:underline
            prose-table:border prose-th:border prose-td:border
            leading-[1.4]
            transition-all duration-150"
          >
            <ReactMarkdown
              children={readmeData.readme}
              remarkPlugins={[remarkGfm]}
              rehypePlugins={[rehypeRaw, rehypeHighlight]}
            />
          </div>
        ) : (
          <div className="h-full w-full bg-inherit text-white">
            <pre className="whitespace-pre-wrap break-words font-mono text-sm bg-inherit pb-20">
              <code className="language-markdown text-sm font-mono">
                {readmeData.readme}
              </code>
            </pre>
          </div>
        ))}
      {generateError && (
        <div className="mt-4 text-red-400 w-full h-full font-semibold text-center flex justify-center items-center">
          <h4>❌ Failed to generate README. Please try again.</h4>
        </div>
      )}
    </div>
  );
}

function ToggleSwitch({ setActiveTab, activeTab }) {
  return (
    <div className="h-10 w-36 bg-white/20 backdrop-blur-md rounded-lg flex gap-2  relative border-white/50 border-2">
      <div
        className={`absolute bottom-0 h-full shadow-sm w-1/2 rounded-lg bg-[#030617]/80 backdrop-blur-sm  transition-transform duration-500 ease-in-out ${
          activeTab === "preview" ? "translate-x-0" : "translate-x-full"
        }`}
      />

      <button
        className={`min-h-full w-1/2 z-10 transition-colors duration-500 ${
          activeTab === "preview" ? "text-white" : "text-white"
        } `}
        onClick={() => setActiveTab("preview")}
      >
        Preview
      </button>
      <button
        className={`min-h-full w-1/2 z-10 transition-colors duration-500 ${
          activeTab === "preview" ? "text-white" : "text-white"
        } `}
        onClick={() => setActiveTab("code")}
      >
        Code
      </button>
    </div>
  );
}

function CopyDownload({ readmeData }) {
  const [copied, setCopied] = useState(false);

  const copyToClipboard = async () => {
    try {
      await navigator.clipboard.writeText(readmeData.readme);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (e) {
      console.error("error copying :", e);
    }
  };

  const handleDownload = () => {
    const blob = new Blob([readmeData.readme], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "Readme.md";
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="h-10 w-38 flex  gap-2 text-white text-sm ">
      <div className="h-full w-16 bg-[#030617]/10 backdrop-blur-md hover:scale-105 transition-all duration-300 ease-out border-white/50 border-[1px] rounded-lg">
        <button
          className="h-full w-full"
          onClick={copyToClipboard}
          title="Copy to clipboard"
        >
          {copied ? (
            <CopyCheck className="w-full h-full p-[6px]" />
          ) : (
            <Copy className="w-full h-full p-[6px]" />
          )}
        </button>
      </div>
      <div className="h-full w-16 bg-[#030617]/10 backdrop-blur-md hover:scale-105 transition-all duration-300 border-white/50 border-[1px] rounded-lg">
        <button className="h-full w-full" onClick={handleDownload}>
          <Download className="w-full h-full p-[6px]" />
        </button>
      </div>
    </div>
  );
}

function Loader() {
  return (
    <div className="absolute top-0 left-0 h-full w-full flex justify-center items-center bg-[#0d1017] bg-opacity-90 z-50">
      <h1 className="text-3xl font-sans font-bold text-transparent bg-clip-text bg-gradient-to-r from-pink-400 via-white to-purple-500 bg-[length:300%_100%] animate-shimmer leading-[1.4] pb-1">
        Generating Readme...
      </h1>
    </div>
  );
}

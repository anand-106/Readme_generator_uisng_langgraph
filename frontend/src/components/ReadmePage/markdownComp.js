import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";
import rehypeHighlight from "rehype-highlight";
import "highlight.js/styles/github-dark.css";

export function MarkdownViewer({ readmeData }) {
  return (
    <div className="h-full w-3/4 overflow-y-auto px-12 py-10 bg-[#0d1017] text-white font-sans">
      {readmeData?.readme && (
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
      )}
      <ToggleSwitch />
    </div>
  );
}

function ToggleSwitch() {
  return <div className="h-10 w-36 bg-white rounded-lg"></div>;
}

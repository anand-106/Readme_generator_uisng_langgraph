import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";
import rehypeHighlight from "rehype-highlight";
import "highlight.js/styles/github-dark.css"; // ✅ For consistent dark theme

export function MarkdownViewer({ readmeData }) {
  return (
    <div className="h-full w-3/4 overflow-y-auto px-12 py-10 bg-[#141b23]">
      {readmeData?.readme && (
        <div
          className="prose prose-invert max-w-none
            prose-pre:bg-[#0d1017] prose-pre:text-[#c9d1d9] prose-pre:rounded-lg prose-pre:px-4 prose-pre:py-3
            prose-code:bg-[#0d1017] prose-code:text-[#c9d1d9] prose-code:rounded prose-code:px-2 prose-code:py-1
            prose-code:font-githubCode
            prose-p:my-3 prose-li:my-1 prose-a:text-blue-400 hover:prose-a:underline transition-all duration-150"
        >
          <ReactMarkdown
            children={readmeData.readme}
            remarkPlugins={[remarkGfm]}
            rehypePlugins={[rehypeRaw, rehypeHighlight]}
          />
        </div>
      )}
    </div>
  );
}

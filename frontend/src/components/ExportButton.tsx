import { ChatMessage } from "../types/rag.types";

interface ExportButtonProps {
  messages: ChatMessage[];
}

function buildMarkdown(messages: ChatMessage[]): string {
  const lines = [
    "# RAG Document Knowledge — Conversation Export",
    "",
    `_Exported on ${new Date().toLocaleString()}_`,
    "",
  ];

  for (const message of messages) {
    const heading = message.role === "user" ? "### Question" : "### Answer";
    lines.push(heading, "", message.content, "");

    if (message.sources && message.sources.length > 0) {
      lines.push("**Sources:**", "");
      for (const source of message.sources) {
        lines.push(
          `- ${source.title} (document: ${source.document_id}, chunk #${source.chunk_index}, score ${source.score.toFixed(2)})`
        );
      }
      lines.push("");
    }
  }

  return lines.join("\n");
}

export function ExportButton({ messages }: ExportButtonProps) {
  function handleExport(): void {
    const markdown = buildMarkdown(messages);
    const blob = new Blob([markdown], { type: "text/markdown" });
    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = `rag-conversation-${Date.now()}.md`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);

    URL.revokeObjectURL(url);
  }

  return (
    <button
      type="button"
      onClick={handleExport}
      disabled={messages.length === 0}
      className="rounded-md border border-sage-300 bg-white px-4 py-2 text-sm font-medium text-sage-700 transition hover:bg-sage-50 disabled:cursor-not-allowed disabled:border-sand-200 disabled:text-ink/30"
    >
      Export conversation (Markdown)
    </button>
  );
}

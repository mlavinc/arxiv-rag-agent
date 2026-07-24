import { ChatMessage } from "../types/rag.types";
import { SourceDetails } from "./SourceDetails";

interface MessageBubbleProps {
  message: ChatMessage;
}

export function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.role === "user";

  return (
    <div className={`flex ${isUser ? "justify-end" : "justify-start"}`}>
      <div
        className={`max-w-[80%] rounded-lg px-4 py-3 text-sm leading-relaxed shadow-sm ${
          isUser
            ? "bg-sand-100 text-ink"
            : "border border-sand-200 bg-white text-ink"
        }`}
      >
        <p className="whitespace-pre-wrap">{message.content}</p>
        {message.sources && <SourceDetails sources={message.sources} />}
      </div>
    </div>
  );
}

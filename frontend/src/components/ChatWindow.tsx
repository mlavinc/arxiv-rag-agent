import { FormEvent, useEffect, useRef, useState } from "react";

import { ChatMessage } from "../types/rag.types";
import { MessageBubble } from "./MessageBubble";

const EXAMPLE_QUESTIONS = [
  "What is PyramidTNT?",
  "Summarize this paper",
  "What are the main contributions?",
];

interface ChatWindowProps {
  messages: ChatMessage[];
  isAsking: boolean;
  error: string | null;
  onAsk: (question: string) => void;
}

export function ChatWindow({
  messages,
  isAsking,
  error,
  onAsk,
}: ChatWindowProps) {
  const [input, setInput] = useState("");
  const scrollAnchorRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollAnchorRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isAsking]);

  function handleSubmit(event: FormEvent): void {
    event.preventDefault();
    if (!input.trim() || isAsking) {
      return;
    }

    onAsk(input);
    setInput("");
  }

  return (
    <section className="flex h-full flex-col rounded-lg border border-sand-200 bg-white shadow-sm">
      <header className="border-b border-sand-200 px-5 py-4">
        <h2 className="font-serif text-lg text-ink">Conversation</h2>
        <p className="mt-1 text-sm text-ink/60">
          Ask questions about the documents you have uploaded.
        </p>
      </header>

      <div className="flex-1 space-y-3 overflow-y-auto px-5 py-4">
        {messages.length === 0 && (
          <div className="flex h-full flex-col items-center justify-center gap-3 text-center text-ink/40">
            <p className="text-sm">Try one of these to get started:</p>
            <div className="flex flex-wrap justify-center gap-2">
              {EXAMPLE_QUESTIONS.map((example) => (
                <button
                  key={example}
                  type="button"
                  onClick={() => onAsk(example)}
                  className="rounded-full border border-sage-200 bg-sage-50 px-3 py-1.5 text-xs text-sage-700 transition hover:bg-sage-100"
                >
                  {example}
                </button>
              ))}
            </div>
          </div>
        )}

        {messages.map((message) => (
          <MessageBubble key={message.id} message={message} />
        ))}

        {isAsking && (
          <div className="flex justify-start">
            <div className="rounded-lg border border-sand-200 bg-white px-4 py-3 text-sm text-ink/40">
              Thinking…
            </div>
          </div>
        )}

        <div ref={scrollAnchorRef} />
      </div>

      {error && (
        <p className="mx-5 mb-2 rounded-md bg-clay-50 px-3 py-2 text-sm text-clay-500">
          {error}
        </p>
      )}

      <form
        onSubmit={handleSubmit}
        className="flex items-center gap-2 border-t border-sand-200 px-5 py-4"
      >
        <input
          type="text"
          value={input}
          onChange={(event) => setInput(event.target.value)}
          placeholder="Ask something about your document…"
          className="flex-1 rounded-md border border-sand-200 bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-sage-400"
        />
        <button
          type="submit"
          disabled={isAsking || !input.trim()}
          className="rounded-md bg-sage-600 px-4 py-2 text-sm font-medium text-white transition hover:bg-sage-700 disabled:cursor-not-allowed disabled:bg-sand-200 disabled:text-ink/40"
        >
          Ask
        </button>
      </form>
    </section>
  );
}

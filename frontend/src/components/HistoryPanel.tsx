import { ChatMessage } from "../types/rag.types";

interface HistoryPanelProps {
  messages: ChatMessage[];
  onClear: () => void;
}

export function HistoryPanel({ messages, onClear }: HistoryPanelProps) {
  const questionCount = messages.filter((m) => m.role === "user").length;

  return (
    <section className="rounded-lg border border-sand-200 bg-white p-5 shadow-sm">
      <div className="flex items-center justify-between">
        <h2 className="font-serif text-lg text-ink">Session history</h2>
        {messages.length > 0 && (
          <button
            type="button"
            onClick={onClear}
            className="text-xs font-medium text-clay-500 underline decoration-dotted underline-offset-2 hover:text-clay-500/80"
          >
            Clear
          </button>
        )}
      </div>

      <p className="mt-1 text-sm text-ink/60">
        {questionCount === 0
          ? "No questions asked yet this session."
          : `${questionCount} question${questionCount === 1 ? "" : "s"} asked this session.`}
      </p>

      {messages.length > 0 && (
        <ol className="mt-3 max-h-48 space-y-2 overflow-y-auto">
          {messages
            .filter((message) => message.role === "user")
            .map((message, index) => (
              <li
                key={message.id}
                className="rounded-md bg-paper px-3 py-2 text-sm text-ink/70"
              >
                <span className="mr-2 text-xs text-ink/40">{index + 1}.</span>
                {message.content}
              </li>
            ))}
        </ol>
      )}
    </section>
  );
}

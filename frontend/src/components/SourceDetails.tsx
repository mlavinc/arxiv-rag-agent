import { useState } from "react";

import { SearchSource } from "../types/rag.types";

interface SourceDetailsProps {
  sources: SearchSource[];
}

export function SourceDetails({ sources }: SourceDetailsProps) {
  const [isExpanded, setIsExpanded] = useState(false);

  if (sources.length === 0) {
    return null;
  }

  return (
    <div className="mt-2">
      <button
        type="button"
        onClick={() => setIsExpanded((value) => !value)}
        className="text-xs font-medium text-sage-600 underline decoration-dotted underline-offset-2 hover:text-sage-700"
      >
        {isExpanded ? "Hide sources" : `View sources (${sources.length})`}
      </button>

      {isExpanded && (
        <ul className="mt-2 space-y-2">
          {sources.map((source) => (
            <li
              key={`${source.document_id}-${source.chunk_index}`}
              className="rounded-md border border-sand-200 bg-paper px-3 py-2 text-xs text-ink/70"
            >
              <div className="flex items-center justify-between">
                <span className="font-medium text-ink">{source.title}</span>
                <span className="text-ink/40">
                  score {source.score.toFixed(2)}
                </span>
              </div>
              <div className="mt-1 text-ink/40">
                document: {source.document_id} · chunk #{source.chunk_index}
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

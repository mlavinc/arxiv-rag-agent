class ChunkingService:
    """
    Splits PDF pages into smaller chunks.
    """

    def split(
        self,
        pages: list[dict],
        chunk_size: int = 1000,
        overlap: int = 200,
    ) -> list[dict]:

        chunks = []

        chunk_id = 0

        for page in pages:

            text = page["text"]
            page_number = page["page_number"]

            start = 0

            while start < len(text):

                end = start + chunk_size

                chunk_text = text[start:end]

                chunks.append(
                    {
                        "chunk_id": chunk_id,
                        "page_number": page_number,
                        "text": chunk_text,
                    }
                )

                chunk_id += 1

                start += chunk_size - overlap

        return chunks


chunking_service = ChunkingService()
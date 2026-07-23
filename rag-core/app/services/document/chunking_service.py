class ChunkingService:
    """
    Splits documents into smaller chunks.
    """

    def split(
        self,
        text: str,
        chunk_size: int = 500,
        overlap: int = 50,
    ) -> list[str]:

        chunks = []

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start += chunk_size - overlap

        return chunks


chunking_service = ChunkingService()
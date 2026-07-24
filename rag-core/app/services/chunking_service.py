class ChunkingService:
    """
    Splits documents into smaller text chunks.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap


    def split(self, text: str) -> list[str]:
        chunks = []

        start = 0

        while start < len(text):
            end = start + self.chunk_size

            chunk = text[start:end]

            chunks.append(chunk)

            start = end - self.overlap

        return chunks


chunking_service = ChunkingService()
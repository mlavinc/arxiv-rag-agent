from pathlib import Path


class DocumentLoader:
    """
    Responsible for loading raw document content.
    """

    def load(self, file_path: str) -> str:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Document not found: {file_path}"
            )

        if path.suffix != ".txt":
            raise ValueError(
                "Only txt files are supported currently"
            )

        return path.read_text(
            encoding="utf-8"
        )


document_loader = DocumentLoader()
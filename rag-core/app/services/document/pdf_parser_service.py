import fitz


class PDFParserService:
    """
    Extracts text content from PDF documents.
    """

    def extract_text(self, file_path: str) -> dict:
        document = fitz.open(file_path)

        pages_text = []

        for page in document:
            pages_text.append(
                page.get_text()
            )

        document.close()

        return {
            "text": "\n".join(pages_text),
            "pages": len(pages_text),
        }


pdf_parser_service = PDFParserService()

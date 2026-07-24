import fitz


class PDFParserService:
    """
    Extracts text content from PDF documents
    while preserving page information.
    """

    def extract_text(self, file_path: str) -> dict:

        document = fitz.open(file_path)

        pages = []

        for index, page in enumerate(document):

            pages.append(
                {
                    "page_number": index + 1,
                    "text": page.get_text(),
                }
            )

        document.close()

        return {
            "pages": pages,
            "page_count": len(pages),
        }


pdf_parser_service = PDFParserService()

from pathlib import Path
import httpx


class PDFDownloaderService:
    """
    Downloads paper PDFs from external sources.
    """

    def __init__(self):
        self.storage_path = Path("data/papers")
        self.storage_path.mkdir(
            parents=True,
            exist_ok=True
        )


    async def download(
        self,
        paper_id: str
    ) -> str:

        paper_identifier = paper_id.split("/")[-1]

        pdf_url = (
            f"https://arxiv.org/pdf/{paper_identifier}.pdf"
        )

        file_path = (
            self.storage_path /
            f"{paper_identifier}.pdf"
        )

        async with httpx.AsyncClient(
            follow_redirects=True
        ) as client:

            response = await client.get(
                pdf_url,
                timeout=60.0
            )

            response.raise_for_status()

            file_path.write_bytes(
                response.content
            )

        return str(file_path)


pdf_downloader_service = PDFDownloaderService()

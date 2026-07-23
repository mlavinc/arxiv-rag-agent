import httpx
import xml.etree.ElementTree as ET


class ArxivService:
    """
    Handles interaction with ArXiv API.
    """

    BASE_URL = "https://export.arxiv.org/api/query"

    async def search(self, query: str, max_results: int = 1) -> list[dict]:
        async with httpx.AsyncClient(follow_redirects=True) as client:
            response = await client.get(
                self.BASE_URL,
                params={
                    "search_query": f"all:{query}",
                    "start": 0,
                    "max_results": max_results,
                },
                timeout=30.0,
            )

        response.raise_for_status()

        return self._parse_response(response.text)


    def _parse_response(self, xml_data: str) -> list[dict]:
        root = ET.fromstring(xml_data)

        namespace = {
            "atom": "http://www.w3.org/2005/Atom"
        }

        papers = []

        for entry in root.findall("atom:entry", namespace):
            papers.append(
                {
                    "title": entry.find(
                        "atom:title",
                        namespace
                    ).text.strip(),

                    "summary": entry.find(
                        "atom:summary",
                        namespace
                    ).text.strip(),

                    "id": entry.find(
                        "atom:id",
                        namespace
                    ).text.strip(),

                }
            )

        return papers


arxiv_service = ArxivService()
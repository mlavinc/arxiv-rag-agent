from app.services.document.pdf_parser_service import pdf_parser_service


result = pdf_parser_service.extract_text(
    "data/papers/2201.00978v1.pdf"
)

print(result.keys())

print(
    result["pages"][0]["page_number"]
)

print(
    result["pages"][0]["text"][:200]
)

print(
    "Total pages:",
    result["page_count"]
)
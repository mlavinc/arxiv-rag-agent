from app.services.chunking_service import chunking_service
from app.services.document.pdf_parser_service import pdf_parser_service


pdf = pdf_parser_service.extract_text("data/papers/2201.00978v1.pdf")

pages = pdf["pages"]

chunks = chunking_service.split(
    pages,
    chunk_size=1000,
    overlap=200
)

print("Number of chunks:")
print(len(chunks))

print("\nFirst chunk:")
print(chunks[0])
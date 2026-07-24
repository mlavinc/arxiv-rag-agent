from app.services.document_loader import document_loader

text = document_loader.load(
    "test_document.txt"
)

print(text)
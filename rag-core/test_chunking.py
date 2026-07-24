from app.services.chunking_service import chunking_service


text = """
PyramidTNT is a transformer based object detector.
It uses a pyramid architecture.
This architecture improves object detection performance.
"""


chunks = chunking_service.split(text)


for i, chunk in enumerate(chunks):
    print("CHUNK", i)
    print(chunk)
    print("----------------")
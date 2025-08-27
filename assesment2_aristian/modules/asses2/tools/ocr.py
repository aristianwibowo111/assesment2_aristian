import os
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()
mistral_client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

def exporttomd():
    uploaded_pdf = mistral_client.files.upload(
        file = {
            "file_name": "exsummary.pdf",
            "content": open("exsummary.pdf", "rb")
        },
        purpose="ocr"
    )

    signed_url = mistral_client.files.get_signed_url(file_id=uploaded_pdf.id)

    ocr_response = mistral_client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type":"document_url",
            "document_url": signed_url.url,
        }
    )

    pages = ocr_response.model_dump().get("pages")
    all_text = ""
    for page in pages:
        all_text += page.get("markdown")
    with open("ocr_response.md", "w", encoding="utf-8") as f:
        f.write(all_text)





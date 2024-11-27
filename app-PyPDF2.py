from PyPDF2 import PdfReader

# Caminho do arquivo PDF
caminho_pdf = "CAMINHO_DO_ARQUIVO"

# Ler o PDF
reader = PdfReader(caminho_pdf)
texto_completo = ""

for pagina in reader.pages:
    texto_completo += pagina.extract_text()

print(texto_completo)
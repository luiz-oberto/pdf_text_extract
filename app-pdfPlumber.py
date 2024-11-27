import pdfplumber

# Caminho do arquivo PDF
caminho_pdf = "CAMINHO_DO_ARQUIVO"

# Abrir o PDF e extrair o texto
with pdfplumber.open(caminho_pdf) as pdf:
    texto_completo = ""
    for pagina in pdf.pages:
        texto_completo += pagina.extract_text()

# Exibir o texto extraído
print("texto extraido: ", texto_completo)


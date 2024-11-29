import pytesseract
from pdf2image import convert_from_path

# Configure o caminho do Tesseract (necessário no Windows)
pytesseract.pytesseract.tesseract_cmd = r"TESSERACT_PATH"

# Caminho do PDF
caminho_pdf = "CAMINHO_DO_ARQUIVO"

# Adicionando o PATH do poppler
poppler_path = r"POPPLER_PATH"

# Converter o PDF em imagens
paginas = convert_from_path(caminho_pdf, dpi=300, poppler_path=poppler_path)

# Processar OCR em cada página
texto_completo = ""
for i, pagina in enumerate(paginas):
    texto = pytesseract.image_to_string(pagina, lang="por")  # 'por' para português
    texto_completo += f"\n--- Página {i + 1} ---\n{texto}"

# extrair todo texto para um arquivo .txt
with open('__PATH_TO_EXTRACTED_FILE__\\texto-extraido.txt', 'w', encoding='utf-8') as file:
    file.write(texto_completo)

print("Extração concluida.")

# PDF text Extract
Este repositório foi feito com o intuito de extrair texto contido em qualquer arquivo em formato PDF, seja um PDF editável ou apenas imagens escaneadas.

### Neste repositório foi usada as seguintes bibliotecas:
#### 1. pdfplumber
```
pip install pdfplumber
```

#### 2. PyPDF2
```
pip install PyPDF2
```

#### 3. pytesseract
```
pip install pytesseract
```

#### 4. pdf2image
```
pip install pdf2image
```

#### 5. Pillow
```
pip install pillow
```

### Progamas e Ferramentas Externas
1. [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
2. [Poppler](https://github.com/oschwartz10612/poppler-windows/releases)
3. [Arquivos de idioma do Tesseract](https://github.com/tesseract-ocr/tessdata)

### DEV LOG:
- Fazer filtros mais específicos para obter as informações que preciso extrair de acordo com cada página do arquivo 
    - Ex: preciso da contagem de folhas COLOR quando a impressora é colorida.

03/12/2024
- Consegui achar um jeito de saber se a impressora é COLOR ou MONO;
- atualizar a lógica para inserir no arquivo txt as informações da contagem de páginas COLOR e páginas P&B das impressoras coloridas
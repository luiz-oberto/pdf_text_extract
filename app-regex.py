import re


def extrair_padroes(content, patterns):
    """Extrai padrões do conteúdo e retorna como lista."""
    return {key: re.findall(pattern, content) for key, pattern in patterns.items()}


def agrupar_pares(lista, step=2):
    """Agrupa itens de uma lista em pares."""
    return [tuple(lista[i:i + step]) for i in range(0, len(lista), step)]


def processar_arquivo(input_file, output_file):
    # Padrões para busca
    patterns = {
        "serial_MONO": r"Número de série:X3BK03\w{4,}",
        "serial_COLOR": r"Número de série:XBJZ02\w{4,}",
        "serial_COLOR_2": r"Número de série: XBJ\w{4,}", 
        "total_count": r"Número total de páginas:\w{3,}",
        "paginas_pb_cor": r"Número total de páginas a .{3,}"
    }

    # Ler o conteúdo do arquivo
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extrair padrões
    dados = extrair_padroes(content, patterns)

    # Verificar consistência de dados extraídos
    if not dados["serial_MONO"] or not dados["serial_COLOR"]:
        print("Erro: Não foram encontrados números de série suficientes.")
        return

    if len(dados["paginas_pb_cor"]) % 2 != 0:
        print("Erro: Número de páginas P&B e Coloridas não estão agrupados corretamente.")
        return

    # Agrupar contadores P&B e Coloridos
    paginas_pb_cor_pares = agrupar_pares(dados["paginas_pb_cor"])

    # Criar zips
    zip_MONO = list(zip(dados["serial_MONO"], dados["total_count"]))
    zip_COLOR = list(zip(dados["serial_COLOR"], paginas_pb_cor_pares))
    zip_COLOR_2 = list(zip(dados["serial_COLOR_2"], paginas_pb_cor_pares))

    # Escrever no arquivo de saída
    with open(output_file, 'w', encoding="utf-8") as file:
        for sn in zip_MONO:
            file.write(f'{sn}\n')
        for sn in zip_COLOR:
            file.write(f'{sn}\n')
        for sn in zip_COLOR_2:
            file.write(f'{sn}\n')

    print('Informações extraídas com sucesso!')


# Executar função principal
processar_arquivo('texto-extraido.txt', 'texto-filtrado.txt')



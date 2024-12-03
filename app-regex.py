import re

'''
regex - número de série-> Número de série:\w{10}
regex - contadores totais->  
regex - páginas P&B-> Número total de páginas a .{3,}

regex - páginas cor-> Número total de páginas a Cor:\w{3,}
'''

with open('texto-extraido.txt', 'r', encoding='utf-8') as file:
    content = file.read()

pattern_sn = 'Número de série:\w{10}'
pattern_total_count = 'Número total de páginas:\w{3,}'
pattern_paginas_pb_cor = 'Número total de páginas a .{3,}'


# achar todos os Números de série
serial_number  = re.findall(pattern_sn, content)

# achar seus respectivos contadores
total_count = re.findall(pattern_total_count, content)

# achar contadores P&B e COR
paginas_pb_cor =re.findall(pattern_paginas_pb_cor, content)

lista_zip = list(zip(serial_number, total_count))

print(f'Número serial e seus respectivos contadores totais: {lista_zip}')
print()
print(f'Páginas preto e branco e coloridas: {paginas_pb_cor}')
print()

with open("texto-filtrado.txt", 'w', encoding="utf-8") as file:
    for sn in lista_zip:
        for serial_number in sn:
            # verificar se modelo é COLOR
            if "Número de série:XBJZ02" in serial_number:
                print(f'Número de série achado {serial_number}')
        file.write(f'{sn} \n')
        

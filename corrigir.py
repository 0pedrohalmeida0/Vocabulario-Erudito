import json

# 1. Abre o arquivo limpo
with open('palavras_limpo.json', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()

# 2. Dicionário de tradução dos caracteres corrompidos comuns
substituicoes = {
    'prop¾sito': 'propósito',
    '¾': 'ó',
    'Æ': 'ã',
    '¡': 'á',
    '¡': 'í',
    'à': 'é',
}

# Aplica as correções no texto bruto do arquivo
for errado, correto in substituicoes.items():
    texto = texto.replace(errado, correto)

# 3. Salva o texto corrigido de volta
with open('palavras_limpo.json', 'w', encoding='utf-8') as arquivo:
    arquivo.write(texto)

print("📝 Acentos corrigidos no arquivo JSON!")
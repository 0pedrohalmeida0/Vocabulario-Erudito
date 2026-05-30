import json

# 1. Abre o teu arquivo novo e limpo para leitura
with open('palavras_limpo.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# 2. Percorre a lista de palavras
for item in dados:
    fields = item['fields']
    
    # Se a chave 'idioma' não existir ou estiver vazia, define como 'pt-br'
    if 'idioma' not in fields or fields['idioma'] == '':
        fields['idioma'] = 'pt-br'

# 3. Guarda o arquivo corrigido com encoding UTF-8 perfeito
with open('palavras_limpo.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)

print("✅ Arquivo palavras_limpo.json atualizado com 'pt-br' em todas as palavras!")
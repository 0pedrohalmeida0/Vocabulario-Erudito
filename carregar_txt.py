import os
import django

# 1. Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup_projeto.settings')
django.setup()

from core.models import Palavra  # Certifique-se de que 'core' é o seu app

def importar_palavras():
    caminho_txt = 'palavras.txt'
    
    if not os.path.exists(caminho_txt):
        print(f"❌ Erro: O arquivo {caminho_txt} não foi encontrado!")
        return

    # Limpa as palavras antigas e misturadas do banco local para não duplicar
    print("🧹 Limpando dados misturados do banco local...")
    Palavra.objects.all().delete()

    palavras_para_salvar = []
    
    with open(caminho_txt, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha:
                continue
            
            partes = linha.split('|')
            
            # Se tiver 3 partes: Português (Termo | Significado | Exemplo)
            if len(partes) == 3:
                termo, significado, exemplo = partes
                idioma = 'pt-br'
            # Se tiver 4 partes: Outros idiomas (Termo | Significado | Exemplo | Idioma)
            elif len(partes) == 4:
                termo, significado, exemplo, idioma = partes  # CORRIGIDO: agora com 'x'!
            else:
                continue
                
            palavras_para_salvar.append(
                Palavra(
                    termo=termo.strip(),
                    significado=significado.strip(),
                    exemplo=exemplo.strip(),
                    idioma=idioma.strip().lower()
                )
            )
    
    if palavras_para_salvar:
        Palavra.objects.bulk_create(palavras_para_salvar)
        print(f"🚀 SUCESSO! {len(palavras_para_salvar)} palavras recarregadas com os exemplos corretos!")

if __name__ == '__main__':
    importar_palavras()
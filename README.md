# Vocabulário Erudito 

O **Vocabulário Erudito** é uma aplicação web e PWA (Progressive Web App) desenvolvida para auxiliar no enriquecimento vocabular diário. O sistema permite ao usuário focar seus estudos em diferentes idiomas (Português Erudito, Inglês Avançado e Alemão), trazendo definições e exemplos práticos armazenados no banco de dados.

O grande diferencial do projeto é a sua capacidade de ser instalado no computador ou celular como um aplicativo nativo, contando com automação de notificações na tela do usuário.

---

## Demonstração em Produção

O projeto foi publicado com sucesso na nuvem e pode ser testado diretamente pelo navegador ou instalado no seu dispositivo através do link abaixo:

**Acesse o aplicativo:** https://vocabularioerudito.pythonanywhere.com/

---

## Tecnologias Utilizadas

- **Python & Django:** Arquitetura do back-end, gerenciamento do banco de dados, filtragem dinâmica de termos e renderização de templates.
- **JavaScript (ES6):** Lógica de front-end responsável pelo registro assíncrono do Service Worker e controle da *Web Notifications API*.
- **PWA (Progressive Web App):** Integração de `manifest.json` e `sw.js` para suporte offline, cache de arquivos estáticos e instalabilidade.
- **Web Notifications API:** Mecanismo automático que identifica a palavra do dia enviada pelo Django e dispara uma notificação nativa no sistema do usuário.
- **CSS3:** Interface responsiva e minimalista, utilizando gradientes dinâmicos e tipografia otimizada para leitura (Inter e Playfair Display).
- **Hospedagem:** Deploy em ambiente de produção na nuvem através do **PythonAnywhere**.

---

## Desafios Técnicos Superados (Deploy & Infraestrutura)

Desenvolver em ambiente local (localhost) é completamente diferente de colocar uma aplicação PWA em produção. Durante o ciclo de desenvolvimento e deploy, foram superados os seguintes marcos de engenharia de software:

1. **Escopo do Service Worker:** Configuração de rotas estáticas personalizadas na raiz do servidor web (`/sw.js` e `/manifest.json`), garantindo que o navegador mapeasse o escopo do PWA para todo o site e não apenas para uma pasta isolada de blocos estáticos.
2. **Resolução de Erros 404:** Ajuste fino entre o motor do `collectstatic` do Django e as tabelas de diretórios do PythonAnywhere para a entrega correta de recursos de imagem (`icon-192.png`).
3. **Gerenciamento de Cache de Templates:** Implementação de estratégias de limpeza de cache no navegador para garantir o correto carregamento do HTML atualizado sem redundâncias de tags.

---

## Como Executar o Projeto Localmente

### Pré-requisitos
- Python 3.x instalado
- Git instalado

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone [https://github.com/TEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/TEU_USUARIO/NOME_DO_REPOSITORIO.git)
   cd NOME_DO_REPOSITORIO

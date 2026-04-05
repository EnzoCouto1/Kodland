# 🔗 Encurtador de Links Mágico | Projeto Pedagógico Kodland

Bem-vindo ao repositório do **Encurtador de Links**! Este projeto foi desenvolvido como uma API REST em Python usando Flask. 

Ele foi desenhado com um propósito muito claro: **ensinar conceitos fundamentais de Back-end para adolescentes de 13 a 17 anos** de forma visual, engajadora e sem frustrações iniciais.

---

## 🎯 O Diferencial Pedagógico 

Para ensinar programação, o código precisa fazer sentido imediato e gerar uma "recompensa" rápida. As decisões técnicas deste projeto refletem essa metodologia:

1. **Estrutura de Dados Visuais:** Em vez de frustrar o aluno iniciante com a instalação de bancos de dados complexos, utilizamos um **Dicionário em Memória** (`banco_de_links = {}`). Isso permite que o aluno visualize perfeitamente o conceito de `Chave: Valor` e entenda como a busca $O(1)$ funciona na prática.
   
2. **Programação Funcional Simplificada:** Para evitar a barreira inicial da Orientação a Objetos (`classes`, `self`, `__init__`), o projeto utiliza funções com nomenclaturas extremamente descritivas (ex: `gerar_codigo_curto()`, `salvar_link()`).


3. **Conceitos Profissionais na Prática:**
   Mesmo sendo simples, o projeto introduz o aluno ao mundo real do desenvolvimento web: **Verbos HTTP** (GET e POST), **Status Codes** (201, 400, 404) e **Respostas em JSON**.

---

## 🚀 Como rodar o projeto na sua máquina

Certifique-se de ter o Python instalado. É recomendado o uso de um ambiente virtual (venv).

**1. Clone o repositório:**
```bash
git clone [https://github.com/EnzoCouto1/Kodland.git](https://github.com/EnzoCouto1/Kodland.git)
cd Kodland
´´´

**2. Instale as dependências:**
```bash
pip install -r requirements.txt

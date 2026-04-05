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
git clone https://github.com/EnzoCouto1/Kodland
```

**2. Navegue até a pasta do projeto**

```bash
cd Kodland
```

**3. Crie um ambiente virtual (Opcional, mas recomendado):**
```bash
python -m venv venv
```


**4. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**5. Inicie o servidor Flask:**

```bash
python app.py
```


A aplicação estará rodando localmente no endereço: http://127.0.0.1:5000


## Como testar?

Para testar o funcionamento da aplicação (recomenda-se o uso do Thunder Client ou Postman).

1 - Para utilizar o Thunder Client basta fazer a instalação de uma extensão no (VSCode)
2 - Assim que instalar, vai aparecer um ícone de um raio ⚡ na sua barra lateral. Clique nele.
3 - Clique no botão New Request.

Com a tela do Thunder Client aberta, siga estes passos para testar o encurtamento:

Ao lado da barra de endereço, mude a caixinha de GET para POST.

Na barra de endereço, digite: http://127.0.0.1:5000/encurtar

Logo abaixo, clique na aba Body e depois selecione a opção JSON.

Na área de texto que vai aparecer, cole o link a ser encurtado no formato JSON, Ex:

{
  "url": "https://www.kodland.org/pt/courses/coding/programming-on-python-pro"
}

Clique no botão azul Send.

Na tela da direita, você verá a sua API respondendo imediatamente com a mensagem de sucesso e o seu link curtinho da seguinte maneira:

{
  "codigo": "3NZ01",
  "link_curto": "[http://127.0.0.1:5000/3NZ01](http://127.0.0.1:5000/3NZ01)",
  "mensagem": "Link encurtado com sucesso!"
}


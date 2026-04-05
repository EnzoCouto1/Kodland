from flask import Flask, request, jsonify, redirect

# Trazendo o "banco de dados" que criamos no outro arquivo
import database 

# criando o aplicativo
app = Flask(__name__)


# O @app.route são as rotas do site
# 'POST' significa que o usuário está ENVIANDO algo
@app.route('/encurtar', methods=['POST'])
def criar_link():

    # request.get_json() é oque o usuário mandou no formato JSON
    dados = request.get_json()
    
    # Tentamos pegar o item chamado "url"
    url_original = dados.get("url")

    # Por segurança se não tiver a "url", a gente barra na porta.
    # O código 400 significa: "Erro seu, você esqueceu de mandar a URL!"
    if not url_original:
        return jsonify({"erro": "Você precisa enviar uma 'url'"}), 400

    # Mandamos a URL longa para o nosso banco de dados e ele nos devolve o código curto (ex: 3NZ01)
    codigo_gerado = database.salvar_link(url_original)

    # Montamos o link final, juntando o endereço do nosso computador com o código sorteado
    link_curto = f"http://127.0.0.1:5000/{codigo_gerado}"
    
    # jsonify é o nosso tradutor, ele empacota nossa resposta no formato JSON.
    # O código 201 significa "Sucesso! Item Criado!"
    return jsonify({
        "mensagem": "Link encurtado com sucesso!",
        "link_curto": link_curto,
        "codigo": codigo_gerado
    }), 201


# Essa porta pega qualquer código curto que venha logo após a barra (ex: /3NZ01))
# 'GET' significa que o usuário está PEDINDO para ler ou acessar algo.
@app.route('/<codigo>', methods=['GET'])
def redirecionar(codigo):

    # Vamos no nosso dicionário procurar se esse código curto existe lá dentro
    link_salvo = database.banco_de_links.get(codigo)

    # O if verifica se o link foi encontrado

    if link_salvo:
        # Se o link existe, a gente aumenta o contador de cliques em 1
        link_salvo["cliques"] += 1
        
        # O 'redirect' pega o usuário e joga ele pro site verdadeiro.
        return redirect(link_salvo["url_original"])
        
    # Se o código não existir
    else:
        # Erro 404 é o "Página não encontrada!"
        return jsonify({"erro": "Esse link não existe!"}), 404


# Uma rota para verificar informações sobre o site
# Como não vamos alterar dados, o método é 'GET'
@app.route('/status/<codigo>', methods=['GET'])
def ver_status(codigo):
    # Procuramos o link de novo no banco de dados
    link_salvo = database.banco_de_links.get(codigo)
    
    if link_salvo:
        # Mostramos o site verdadeiro e quantas pessoas já clicaram
        return jsonify({
            "url_original": link_salvo["url_original"],
            "total_de_cliques": link_salvo["cliques"]
        }), 200
    else:
        return jsonify({"erro": "Link não encontrado!"}), 404


# Essa é a linha que liga a nossa API
if __name__ == '__main__':
    # debug=True é quem vai nos ajudar se o código quebrar, ele nos avisa exatamente onde foi o erro!
    app.run(debug=True)
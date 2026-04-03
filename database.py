import string
import random



banco_de_links = {} # Dicionário para guardar os links.

def gerar_codigo_curto(tamanho=5): #Gerador de código curto com 5 caracteres.


    #Armazenando letras e números em uma váriavel para usar no sorteio.
    letras_e_numeros = string.ascii_letters + string.digits
    

    while True: # Estrutura de repetição (Loop infinito)

        # Sorteando 5 caracteres aleatórios
        # random.choices() faz a escolha de caracteres aleatórios
        # k=tamanho define a quantidade de caracteres a serem sorteados
        caracter_sorteados = random.choices(letras_e_numeros, k=tamanho)

        #caracter_sorteados é uma lista de caracteres sorteados, por exemplo: ['a', 'B', '3', 'x', '9']


        #Adicionando os caracteres sorteados em uma string
        # ''.join() junta os caracteres sorteados em uma única string, sem espaços entre eles
        codigo = ''.join(caracter_sorteados)

        #codigo é a string resultante do sorteio, por exemplo: 'aB3x9'

        # Se o código já existir, ele sorteia de novo!
        if codigo not in banco_de_links:
            return codigo

def salvar_link(url_original):

    #Armazenando o código gerado em uma variável
    codigo_novo = gerar_codigo_curto()
    
    banco_de_links[codigo_novo] = {
        "url_original": url_original,
        "cliques": 0
    }
    
    return codigo_novo
from django.http import HttpResponse
from django.shortcuts import render



def hello(request):
    return render(request, 'index.html')

def articles(resquest, year):
    return HttpResponse('O ano é: ' + str(year))


def lerdobanco(nome):
    lista = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Joao', 'idade': 27},
        {'nome': 'Maria', 'idade': 18}
    ]

    for pessoa in lista:
        # Aqui ele vai fazer um loop, passando de objeto em objeto

        if nome.lower() in pessoa['nome'].lower():
            '''
            Aqui ele vai verificar se o nome passado como parametro na request
            está contido no dicionário que possui a chave 'nome'.
            O ".lower()" serve para transformar uma string que 
            contem caracteres caixa grande em caixa pequena
            assim a busca se tornará efetiva.
            OBS: Voce pode substituir o .lower() por .upper()
            '''
            return dict(zip(['nome', 'idade'], [pessoa['nome'], pessoa['idade']]))
            '''
            No return eu utilizo um metodo de construção de dicionarios,
            onde os dois elementos da primeira lista são as chaves
            que vão receber os valores da segunda lista.
            Para compreender melhor leia o artigo:
            http://www.bogotobogo.com/python/python_dictionary_comprehension_with_zip_from_list.php
            '''
    return 'Pessoa não encontrada!'
    '''
    Caso o IF nao achar a string passada como parametro no request
    ira retornar uma mensagem de "Pessoa não encontrada!"
    '''


def fname(request, nome):
    retorno = lerdobanco(nome)
    '''
    Declarei uma variavel para receber um dos retornos da função "lerdobanco()"
    Aqui ela vai retornar o dicionario com o nome e a idade 
    ou irá receber uma mensagem de erro caso não encontre o parametro passado na request.
    '''
    if type(retorno) == dict:
        '''
        Se a variavel retorno for do tipo dicionário ele irá executar a linha de codigo abaixo.
        '''
        return HttpResponse('Pessoa encontrada! Nome: ' + str(retorno['nome']) + ' Idade: ' + str(retorno['idade']))
    '''
    Caso o retorno for uma string, como no nosso contexto é "Pessoa não encontrada!" 
    irá executar a linha de codigo abaixo.
    '''
    return HttpResponse(retorno)

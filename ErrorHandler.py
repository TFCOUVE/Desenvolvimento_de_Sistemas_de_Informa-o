#################################################
# Servidor Web - Tratamento de Erros HTTP
#################################################
from Main import App
from flask import Response

@App.errorhandler(500)
def TratarServerError(error):
    return Response("Houve um erro interno no servidor, desculpe-nos pelo transtorno. Detalhe: {0}".format(error),500)

@App.errorhandler(400)
def TratarClientError(error):
    return Response("Houve um erro no seu pedido. Detalhe: {0}".format(error),400)

@App.errorhandler(404)
def TratarNotFound(error):
    return Response("Acao nao disponivel", 404)
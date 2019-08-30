from main import App
from flask import Response


@App.errorhandler(500)
def deal_with_server_error(error):
    return Response("Houve um erro interno no servidor, desculpe-nos pelo transtorno. Detalhe: {0}".format(error), 500)


@App.errorhandler(400)
def deal_with_client_error(error):
    return Response("Houve um erro no seu pedido. Detalhe: {0}".format(error), 400)


@App.errorhandler(404)
def deal_with_not_found(error):
    return Response("Acao nao disponivel", 404)

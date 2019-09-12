import re


def valida_nome(nome):
    default = re.search("^[a-zA-Z0-9_.-]+$", nome) is not None
    return default

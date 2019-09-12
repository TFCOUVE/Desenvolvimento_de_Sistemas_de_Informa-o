import re


def verify_email(email):
    default = re.search(r'[a-zA-Z0-9.-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', email) is not None
    print(default)
    # return re.search(r'^[\w]+@[\w]+\.[\w]{2,4}', email) != None

    if default:
        return True
    else:
        return False


def verify_telegram(name):
    default = re.search("^[a-zA-Z0-9_.-]+$", name) is not None
    return default


def ValidaDDD(numero):
    return (numero[:2])


def Rownumber(numero):
    if re.search('R', numero, re.IGNORECASE):
        if len(numero) > 11 and len(numero) < 17:  # FIXO + RAMAL 1199999999
            return 16
        if len(numero) > 11 and len(numero) < 18:  # Celular + RAMAL 11999999999
            return 17
        else:
            print("Por favor insira um ramal após o R. ")
    elif len(numero) == 11:
        return 11
    elif len(numero) == 10:
        return 10
    else:
        return False


def verifica_main(numero):
    DDD_valido = ["11", "19", "21", "22", "24", "27", "28", "31", "35", "37", "38", "41", "49", "51", "53", "54", "55",
                  "61", "69", "71", "73", "75", "77", "79", "81", "89", "91", "99"]
    if ValidaDDD(numero) in DDD_valido:
        if Rownumber(numero) == 17:
            padrao = re.search("[0-9]{2}[0-9]{9}R[0-9*??????]", numero) != None
            print(padrao)
            if padrao:
                return True
            else:
                print("O numero não é valido")
                return False
        if Rownumber(numero) == 16:
            padrao = re.search("[0-9]{2}[0-9]{8}R[0-9*??????]", numero) != None
            print(padrao)
            if padrao:
                return True
            else:
                print("O numero não é valido")
                return False
        if Rownumber(numero) == 11:
            padrao = re.search("[0-9]{2}[0-9]{9}", numero) != None
            print(padrao)
            if padrao:
                return True
            else:
                print("O numero não é valido")
                return False
        if Rownumber(numero) == 10:
            padrao = re.search("[0-9]{2}[0-9]{8}", numero) != None
            print(padrao)
            if padrao:
                return True
            else:
                print("O numero não é valido")
                return False
        else:
            False
    else:
        False
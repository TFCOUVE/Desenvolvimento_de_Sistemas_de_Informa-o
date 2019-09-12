import re
def verifica(email):
    padrao = re.search(r'[a-zA-Z0-9.-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', email) !=None
    print (padrao)
   # return re.search(r'^[\w]+@[\w]+\.[\w]{2,4}', email) != None
    
    if padrao:
        return True
    else:
        return False


verifica("ig.silva.fsfgmail.com")

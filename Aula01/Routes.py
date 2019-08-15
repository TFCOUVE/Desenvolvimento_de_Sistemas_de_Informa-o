from Main import App

@App.route('/', methods=["GET"])
def first_response():
    return 'Oi'
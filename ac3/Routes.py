from main import App


@App.route('/status', methods=["GET"])
def first_response():
    return 'Everything Ok. :)', 200

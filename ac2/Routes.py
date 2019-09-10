from flask import request, jsonify, Response
from main import App


@App.route('/status')
def status():
    return Response('Everything Ok. :)', 200)


@App.route('/create_user', methods=["POST"])
def insert_user():
    data = request.get_json()
    from ac2.Services.UserService import verify_json
    boolean_json = verify_json(data)
    if boolean_json is not True:
        return Response('Json format incorrect')
    else:
        from ac2.Services.UserService import verify_db_value
        boolean_value = verify_db_value(data["value"], data["type"])
        if boolean_value is not None:
            return Response('Confirmed Value Already Recorded')
        else:
            try:
                from ac2.Services.UserService import create_value
                response = create_value(data["user_id"], data["value"], data["type"])
                return jsonify(response), 200
            except Exception as e:
                print(e)
                return Response(e, 500)


@App.route('/confirm_value', methods=["POST"])
def confirm_value():
    data = request.get_json()
    from ac2.Services.UserService import verify_json
    boolean_json = verify_json(data)
    if boolean_json is not True:
        return Response('Json format incorrect')
    else:
        from ac2.Services.UserService import verify_value
        boolean_db_value = verify_value()
        if boolean_db_value is False:
            return Response('Value Incorrect', 406)
        else:
            from ac2.Services.UserService import verify_db_value
            boolean_value = verify_db_value(data["value"], data["type"])
            if boolean_value is not None:
                from ac2.Services.UserService import activate_value
                response = activate_value(boolean_db_value)
                return jsonify(response), 200
            else:
                return Response('Value not registered', 406)


@App.route('/cancel_value', methods=["POST"])
def cancel_value():
    data = request.get_json()
    from ac2.Services.UserService import verify_json
    boolean_json = verify_json(data)
    if boolean_json is not True:
        return Response('Json format incorrect')
    else:
        from ac2.Services.UserService import verify_value
        boolean_db_value = verify_value()
        if boolean_db_value is False:
            return Response('Value Incorrect', 406)
        else:
            from ac2.Services.UserService import verify_db_value
            boolean_value = verify_db_value(data["value"], data["type"])
            if boolean_value is not None:
                from ac2.Services.UserService import canceled_value
                response = canceled_value(boolean_db_value)
                return jsonify(response), 200
            else:
                return Response('Value not registered', 406)


@App.route('/list_by_user_id', methods=["POST"])
def list_by_user_id():
    data = request.get_json()
    from ac2.Services.UserService import listing_by_user_id
    try:
        response = listing_by_user_id(data)
        if len(response) == 0:
            return jsonify('not found'), 204
        else:
            return jsonify(response), 200
    except Exception as e:
        print(e)
        return Response(e, 500)


@App.route('/list_by_value', methods=["POST"])
def list_by_value():
    data = request.get_json()
    from ac2.Services.UserService import listing_by_value
    try:
        response = listing_by_value(data)
        if len(response) == 0:
            return jsonify('not found'), 200
        else:
            return jsonify(response), 200
    except Exception as e:
        print(e)
        return Response(e, 500)

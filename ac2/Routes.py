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

# from ac2.Services.UserService import recovery_value
# x = recovery_value(value, value_type)
# if x is not None:
#     return 'Value already registered', 200
# else:
#     try:
#         from ac2.Services.UserService import create_value
#         record_id = create_value(user, value, value_type)
#        from ac2.Utils.Config import generic_response
#         response = generic_response('Succeed', 'Value Creation succeed', record_id)
#         return jsonify(response), 200
#     except Exception as e:
#         print(e)
#         return Response(e, 500)
#
#
# @App.route('/list_values/<int:user_id>')
# def list_values(user_id):
#     from ac2.Services.UserService import list_many_values
#     try:
#         from ac2.Utils.Config import generic_response
#         data = list_many_values(user_id)
#         response = generic_response('Succeed', 'Found Value', data=data)
#         return jsonify(response), 200
#     except Exception as e:
#         print(e)
#         return e
#
#
# @App.route('/activate_value', methods=["POST"])
# def activate_value():
#     from ac2.Services.UserService import activate_value
#     data = request.get_json()
#     user_id = data["id"]
#     if user_id is None:
#         return 'Need Id'
#     value = data["value"]
#     if value is None:
#         return 'Need Value'
#     value_type = data["type"]
#     if value_type is None:
#         return 'Need Type'
#     from ac2.Services.UserService import recovery_value
#     x = recovery_value(value, value_type)
#     if x is None:
#         return 'Value not registered', 200
#     try:
#         record_id = activate_value(value, value_type, user_id)
#         from ac2.Utils.Config import generic_response
#         response = generic_response('Succeed', 'Value activation succeed', record_id)
#         return jsonify(response), 200
#     except Exception as e:
#         print(e)
#         return e
#
#
# @App.route('/cancel_value', methods=["POST"])
# def value_cancel():
#     from ac2.Services.UserService import activate_value
#     data = request.get_json()
#     user_id = data["id"]
#     if user_id is None:
#         return 'Need Id'
#     value = data["value"]
#     if value is None:
#         return 'Need Value'
#     value_type = data["type"]
#     if value_type is None:
#         return 'Need Type'
#     from ac2.Services.UserService import recovery_value
#     x = recovery_value(value, value_type)
#     if x is None:
#         return 'Value not registered', 200
#     try:
#         record_id = activate_value(value, value_type, user_id)
#         from ac2.Utils.Config import generic_response
#         response = generic_response('Succeed', 'Value activation succeed', record_id)
#         return jsonify(response), 200
#     except Exception as e:
#         print(e)
#         return e
#
#
# @App.route('/list_by_value_type', methods=["POST"])
# def list_value():
#     pass
#
#
# @App.route('/verify_value', methods=["POST"])
# def create_user():
#     pass

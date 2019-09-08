from flask import request, jsonify
from main import App


@App.route('/status')
def status():
    return 'Everything Ok. :)', 200


# TODO NEED TO VERIFY IF THE VALUE HAS ALL THE REQUIREMENTS TO ENTER DATABASE LIKE _ IN TELEGRAM AND @ IN EMAIL
@App.route('/create_user', methods=["POST"])
def insert_user():
    from ac2.Services.UserService import recovery_value
    from ac2.Services.UserService import create_value
    data = request.get_json()
    user = data["id"]
    if user is None:
        return 'Need User'
    value = data["value"]
    if value is None:
        return 'Need Value'
    value_type = data["type"]
    if value_type is None:
        return 'Need Type'
    x = recovery_value(value, value_type)
    if x is not None:
        return 'Value already registered', 200
    else:
        try:
            record_id = create_value(user, value, value_type)
            from ac2.Utils.Config import generic_response
            response = generic_response('Succeed', 'Value Creation succeed', record_id)
            return jsonify(response), 200
        except Exception as e:
            print(e)
            return e


@App.route('/list_values/<int:user_id>')
def list_values(user_id):
    from ac2.Services.UserService import list_many_values
    try:
        from ac2.Utils.Config import generic_response
        data = list_many_values(user_id)
        response = generic_response('Succeed', 'Found Value', data=data)
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return e


# TODO LEFT TO FINISH
@App.route('/activate_value', methods=["PUT"])
def activate_value():
    from ac2.Services.UserService import activate_value
    data = request.get_json()
    user_id = data["id"]
    if user_id is None:
        return 'Need Id'
    value = data["value"]
    if value is None:
        return 'Need Value'
    value_type = data["type"]
    if value_type is None:
        return 'Need Type'
    from ac2.Services.UserService import recovery_value
    x = recovery_value(value, value_type)
    if x is None:
        return 'Value not registered', 200
    try:
        record_id = activate_value(value, value_type, user_id)
        from ac2.Utils.Config import generic_response
        response = generic_response('Succeed', 'Value activation succeed', record_id)
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return e


@App.route('/cancel_value', methods=["POST"])
def value_cancel():
    from ac2.Services.UserService import activate_value
    data = request.get_json()
    user_id = data["id"]
    if user_id is None:
        return 'Need Id'
    value = data["value"]
    if value is None:
        return 'Need Value'
    value_type = data["type"]
    if value_type is None:
        return 'Need Type'
    from ac2.Services.UserService import recovery_value
    x = recovery_value(value, value_type)
    if x is None:
        return 'Value not registered', 200
    try:
        record_id = activate_value(value, value_type)
        from ac2.Utils.Config import generic_response
        response = generic_response('Succeed', 'Value activation succeed', record_id)
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return e


@App.route('/list_by_value_type',  methods=["POST"])
def list_value():
    pass

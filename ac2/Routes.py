from flask import request, jsonify
from main import App


@App.route('/status')
def status():
    return 'Everything Ok. :)', 200


@App.route('/create_user', methods=["POST"])
def insert_user():
    from ac2.Services.UserService import verify_value
    from ac2.Services.UserService import create_value
    data = request.get_json()
    user = data["user_id"]
    if user is None:
        return 'Need User'
    value = data["value"]
    if value is None:
        return 'Need Value'
    value_type = data["type"]
    if value_type is None:
        return 'Need Type'
    x = verify_value(value)
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


@App.route('/list_user/<int:user_id>')
def list_user(user_id):
    from ac2.Services.UserService import list_many_values
    try:
        from ac2.Utils.Config import generic_response
        data = list_many_values(user_id)
        response = generic_response('Succeed', 'Found Value', data=data)
        return jsonify(response), 200
    except Exception as e:
        print(e)
        return e
    pass


# TODO NEED TO DO BEACUSE IT'S NOT ENDED IS DOING EXCEPTION
@App.route('/delete_value/<int:value_id>', methods=["DELETE"])
def exclude_user(value_id):
    from ac2.Model.Record import Record
    from main import db
    rec = Record()
    rec.id = value_id
    try:
        db.session.delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return e
    from ac2.Utils.Config import generic_response
    response = generic_response('Succeed', 'Value Deleted', ' ')
    return jsonify(response), 200


@App.route('/update_value', methods=["PUT"])
def update_user():
    pass

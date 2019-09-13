from sqlalchemy import and_


def verify_json(json):
    user = json["user_id"]
    if user is None:
        return False
    value = json["value"]
    if value is None:
        return False
    value_type = json["type"]
    if value_type is None:
        return False
    else:
        if value_type == 'email' or value_type == 'telefone' or value_type == 'telegram':
            return True


def verify_db_value(json_value, json_value_type):
    from ac2.Model.Record import Record
    data = Record.query.filter_by(value=json_value, value_type=json_value_type).first()
    if data is None:
        return None
    else:
        return data.id


def create_value(json_user_id, json_value, json_value_type):
    from ac2.Model.Record import Record
    rec = Record()
    rec.value_type = json_value_type.lower()
    rec.value = json_value
    rec.user_id = json_user_id
    from main import db
    db.session.add(rec)
    db.session.commit()
    return rec.id


def verify_value(value_type, value):
    from ac2.Utils.Utils import verify_email, verify_telegram, verifica_main
    if value_type == 'email':
        return verify_email(value)
    elif value_type == 'telefone':
        return verifica_main(value)
    elif value_type == 'telegram':
        return verify_telegram(value)
    else:
        return False


def activate_value(record_id):
    from ac2.Model.Record import Record
    from main import db
    rec = Record.query.filter_by(id=record_id).first()
    rec_id = rec.id
    rec_value = rec.value
    rec.confirmed_status = 'Confirmed'
    db.session.commit()
    data = Record.query.filter(and_(Record.id.notilike(rec_id), Record.value.like(rec_value)))
    for row in data:
        row.confirmed_status = 'Canceled'
        db.session.commit()
    return 'Value Activated', 200


def canceled_value(record_id):
    from ac2.Model.Record import Record
    from main import db
    rec = Record.query.filter_by(id=record_id).first()
    rec.confirmed_status = 'Canceled'
    db.session.commit()
    return 'Value Cancel', 200


def listing_by_user_id(json):
    from ac2.Model.Record import Record
    list_of_dic = []
    for row in json:
        data = Record.query.filter(Record.user_id.like(row))
        if data is None:
            continue
        else:
            for i in data:
                list_of_dic.append(
                    {"user_id": i.user_id, "value": i.value, "type": i.value_type, "status": i.confirmed_status})
    return list_of_dic


def listing_by_value(json):
    from ac2.Model.Record import Record
    list_of_dic = []
    for row in json:
        data = Record.query.filter_by(value=row["value"], value_type=row["type"]).all()
        if data is None:
            continue
        else:
            for i in data:
                list_of_dic.append(
                    {"user_id": i.user_id, "value": i.value, "type": i.value_type, "status": i.confirmed_status})
    return list_of_dic

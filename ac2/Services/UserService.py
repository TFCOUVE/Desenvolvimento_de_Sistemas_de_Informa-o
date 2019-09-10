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
        if value_type == 'email' and value_type == 'telefone' and value_type == 'telegram':
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


def verify_value():
    return True


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

# def create_value(user_id, value, value_type):
#     from ac2.Model.Record import Record
#     rec = Record()
#     rec.telephone_flag = False
#     rec.telegram_flag = False
#     rec.email_flag = False
#     if value_type == 'telegram':
#         rec.telegram_flag = True
#     elif value_type == 'telephone':
#         rec.telephone_flag = True
#     elif value_type == 'email':
#         rec.email_flag = True
#     else:
#         return 'Type Value Incorrect'
#     rec.value = value
#     rec.user_id = user_id
#     from main import db
#     db.session.add(rec)
#     db.session.commit()
#     return rec.id
#
#
# def recovery_value(value, value_type):
#     from ac2.Model.Record import Record
#     data = Record.query.filter_by(value=value, value_type=value_type, confirmed_status='Confirmed').first()
#     if data is None:
#         return None
#     else:
#         return data.id
#
#
# def list_many_values(user_id):
#     from ac2.Model.Record import Record
#     data = Record.query.filter_by(user_id=user_id)
#     records = []
#     if data is None:
#         return None
#     else:
#         for row in data:
#             dic = {"ID": row.id, "USER_ID": row.user_id, "VALUE": row.value}
#             if row.telephone_flag is True:
#                 dic.update({"TYPE": 'Telephone'})
#             elif row.telegram_flag is True:
#                 dic.update({"TYPE": 'Telegram'})
#             elif row.email_flag is True:
#                 dic.update({"TYPE": 'Email'})
#             else:
#                 dic.update({"TYPE": 'Not Recorded'})
#             records.append(dic)
#     return records
#
#
# def activate_value(value, value_type, user_id):
#     from ac2.Model.Record import Record
#     from main import db
#     record_id = recovery_value(value, value_type)
#     rec = Record.query.filter_by(id=record_id).first()
#     if rec.user_id == user_id:
#         rec.id = record_id
#     else:
#         return 'User/Type Incorrect', 409
#     rec.confirmed_status = 'Confirmed'
#     db.session.commit()
#     return 'Value Activated'
#
#
# def cancel_value(value, value_type, user_id):
#     from ac2.Model.Record import Record
#     from main import db
#     record_id = recovery_value(value, value_type)
#     rec = Record.query.filter_by(id=record_id).first()
#     if rec.user_id == user_id:
#         rec.id = record_id
#     else:
#         return 'User Id Incorrect'
#     rec.confirmed_status = 'Cancel'
#     db.session.commit()
#     return 'Value Canceled'

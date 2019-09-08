def create_value(user_id, value, value_type):
    from ac2.Model.Record import Record
    rec = Record()
    rec.telephone_flag = False
    rec.telegram_flag = False
    rec.email_flag = False
    if value_type == 'telegram':
        rec.telegram_flag = True
    elif value_type == 'telephone':
        rec.telephone_flag = True
    elif value_type == 'email':
        rec.email_flag = True
    else:
        return 'Type Value Incorrect'
    rec.value = value
    rec.user_id = user_id
    from main import db
    db.session.add(rec)
    db.session.commit()
    return rec.id


def recovery_value(value, value_type):
    from ac2.Model.Record import Record
    email = 0
    telegram = 0
    telephone = 0
    if value_type == 'email':
        email = 1
    elif value_type == 'telegram':
        telegram = 1
    elif value_type == 'telephone':
        telephone = 1
    data = Record.query.filter_by(value=value, email_flag=email, telephone_flag=telephone,
                                  telegram_flag=telegram).first()
    if data is None:
        return None
    else:
        return data.id


def list_many_values(user_id):
    from ac2.Model.Record import Record
    data = Record.query.filter_by(user_id=user_id)
    records = []
    if data is None:
        return None
    else:
        for row in data:
            dic = {"ID": row.id, "USER_ID": row.user_id, "VALUE": row.value}
            if row.telephone_flag is True:
                dic.update({"TYPE": 'Telephone'})
            elif row.telegram_flag is True:
                dic.update({"TYPE": 'Telegram'})
            elif row.email_flag is True:
                dic.update({"TYPE": 'Email'})
            else:
                dic.update({"TYPE": 'Not Recorded'})
            records.append(dic)
    return records


def activate_value(value, value_type, user_id):
    from ac2.Model.Record import Record
    from main import db
    record_id = recovery_value(value, value_type)
    rec = Record.query.filter_by(id=record_id).first()
    if rec.user_id == user_id:
        rec.id = record_id
    else:
        return 'User Id Incorrect'
    rec.confirmed_status = 'Confirmed'
    db.session.commit()
    return 'Value Activated'


def cancel_value(value, value_type, user_id):
    from ac2.Model.Record import Record
    from main import db
    record_id = recovery_value(value, value_type)
    rec = Record.query.filter_by(id=record_id).first()
    if rec.user_id == user_id:
        rec.id = record_id
    else:
        return 'User Id Incorrect'
    rec.confirmed_status = 'Cancel'
    db.session.commit()
    return 'Value Canceled'

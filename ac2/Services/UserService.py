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


def verify_value(value, value_type):
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


def update_value(record_id, user_id, value, value_type, value_status):
    from ac2.Model.Record import Record
    from main import db
    rec = Record.query.filter_by(id=record_id).first()
    rec.id = record_id
    rec.value = value
    rec.user_id = user_id
    rec.confirmed_status = value_status
    rec.email_flag = False
    rec.telephone_flag = False
    rec.telegram_flag = False
    if value_type == 'email':
        rec.email_flag = True
    elif value_type == 'telegram':
        rec.telegram_flag = True
    elif value_type == 'telephone':
        rec.telephone_flag = True
    dic = {"ID": rec.id, "USER_ID": rec.user_id, "VALUE": rec.value}
    if rec.telephone_flag is True:
        dic.update({"TYPE": 'Telephone'})
    elif rec.telegram_flag is True:
        dic.update({"TYPE": 'Telegram'})
    elif rec.email_flag is True:
        dic.update({"TYPE": 'Email'})
    else:
        dic.update({"TYPE": 'Not Recorded'})
    x = verify_value(rec.value, value_type)
    if x is not None:
        return 'Already exist'
    else:
        db.session.commit()
        return dic

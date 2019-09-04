def create_value(user_id, value, value_type):
    from ac2.Model.Record import Record
    rec = Record()
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


def verify_value(value):
    from ac2.Model.Record import Record
    data = Record.query.filter_by(value=value, confirmed_status='Confirmed')
    return data


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


def list_value(value_id):
    pass


def update_value(user_id, value, value_type, value_status):
    pass


def delete_value():
    pass

# -*- coding: utf-8 -*-


from db import db as _db
from util import util


def _convert_time(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        for item in r:
            item['time'] = unicode(item['time'])[0: 16]
        return r

    return wrapper


def get_enter_info(enterprise_id):
    sql = 'select ' \
          'e.id, e.company as companyId, e.name, e.address, ' \
          'e.time, e.nick, e.introduction, e.jobs, e.apply, e.collect ' \
          'from company_info as e where e.company = %s' % enterprise_id
    r = _db.query_one(sql)
    if r is not None:
        r['time'] = unicode(r['time'])[0: 10]
    return r


def is_email_existed(email):
    return _db.query_one('select id from company where email = %s' % email) is not None


def login(email, password):
    r = _db.query_one('select id, email, password, salt from company where email = %s' % email)
    if r is None:
        return {'status': False, 'msg': '该邮箱未被注册'}
    if not util.bcrypt_check(password + r['salt'], r['password']):
        return {'status': False, 'msg': '邮箱或密码错误'}
    else:
        return {'status': True, 'cid': r['id']}


def register_company(email, password):
    salt = util.generate_salt()
    _db.insert('company', {'email': email, 'password': util.bcrypt_password(password + salt), 'salt': salt})
    cid = _db.query_one('select id from company where email = %s' % email)
    _db.insert('company_info', {'company': cid})
    return True


def get_cities():
    return _db.query('select * from cities')


def get_provinces():
    return _db.query('select * from provinces')
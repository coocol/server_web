# -*- coding: utf-8 -*-


from db import db as _db


def _convert_time(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        for item in r:
            item['time'] = unicode(item['time'])[0: 16]
        return r

    return wrapper


def reject_applicant(job_id, user_id):
    sql = 'update apply_user set status = 2 where user = %s and job = %s' % (user_id, job_id)
    _db.execute(sql)
    return True


def accept_applicant(job_id, user_id):
    sql = 'update apply_user set status = 1 where user = %s and job = %s' % (user_id, job_id)
    _db.execute(sql)
    return True


def update_applicant(job_id, user_id, status):
    sql = 'update apply_user set status = %s where user = %s and job = %s' % (status, user_id, job_id)
    _db.execute(sql)
    return True


def get_user_info(user_id):
    sql = 'select u.user as Id, u.nick, u.signature, p.phone ' \
          'from user_info as u join user as p on p.id = u.user and u.user = %s' % user_id
    return _db.query_one(sql)


def get_resume(user_id):
    sql = 'select id, phone, email, birthday, college_time as collegeTime, experience, profess, ' \
          'gender, place, hometown, award, english, description, name ' \
          'from resume where user = %s ' % user_id
    return _db.query_one(sql)
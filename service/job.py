# -*- coding: utf-8 -*-

from db import db as _db


def _pop_id_field(func):
    def wrapper(*args, **kwargs):
        kwargs.pop('id', '')
        r = func(*args, **kwargs)
        return r

    return wrapper


def _convert_time(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        for item in r:
            item['time'] = unicode(item['time'])[0: 16]
        return r

    return wrapper


@_convert_time
def get_job_applicants(job_id, start_id):
    sql_limit = '' if start_id == -1 else '%s,' % start_id
    sql = 'select ' \
          'a.id, a.user as userId, r.name as userName, a.time, a.status ' \
          'from apply_job as a ' \
          'join resume as r on a.job = %s and a.user = r.user ' \
          'order by a.id desc limit %s 10 ' % (job_id, sql_limit)
    return _db.query(sql)


def delete_job(job_id, company_id):
    sql = 'update job set available = %s where id = %s and company = %s' % (False, job_id, company_id)
    _db.execute(sql)
    return True


@_pop_id_field
def create_job(values_dict):
    _db.insert('job', values_dict)


@_pop_id_field
def update_job(values_dict):
    pass


def get_job_info(job_id):
    sql = 'select ' \
          'j.id, j.name, j.address, j.time, j.apply, j.collect, j.company as companyId, ' \
          'j.content, j.requirement, j.period, j.salary, j.other, c.name as company ,c.nick ' \
          'from job as j ' \
          'join company_info as c ' \
          'on j.company = c.company and j.id = %s;' % job_id
    r = _db.query_one(sql)
    if r is not None:
        r['time'] = unicode(r['time'])[0: 10]
    return r


@_convert_time
def get_all_jobs(company_id, start_id):
    sql_limit = '' if start_id < 1 else '%s, ' % start_id
    sql = 'select ' \
          'j.id, j.name, j.address, j.time, j.apply, j.collect ' \
          'from job as j ' \
          'where company = %s ' \
          'order by id desc limit %s 10;' % (company_id, sql_limit)
    return _db.query(sql)

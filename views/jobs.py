# -*- coding: utf-8 -*-

from flask import Blueprint, request
import json
from service import job

jobs_app = Blueprint('jobs_view', __name__)


@jobs_app.route('/jobs', methods=['GET'])
def get_jobs():
    company_id = int(request.args.get('company_id', -1))
    start_id = int(request.args.get('start_id', -1))
    r = job.get_all_jobs(company_id, start_id)
    return _make_success(r)


@jobs_app.route('/job/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    if job.delete_job(job_id, company_id=9):
        return _make_success('')
    else:
        return _make_error('')


@jobs_app.route('/job/<int:job_id>', methods=['POST'])
def update_job(job_id):
    if job.update_job(None):
        return _make_success('')
    else:
        return _make_error('')


@jobs_app.route('/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
    r = job.get_job_info(job_id)
    if r is not None:
        return _make_success(r)
    else:
        return _make_error('')


_error_resp = dict(status='fail', msg='')
_success_resp = dict(status='success')


def _make_error(content):
    _error_resp['msg'] = content
    res = json.dumps(_error_resp)
    return res


def _make_success(data):
    _success_resp['data'] = json.dumps(data)
    res = json.dumps(_success_resp)
    return res

# -*- coding: utf-8 -*-

from flask import Blueprint, request
from service import applicant
import json

users_app = Blueprint("users_app", __name__)


@users_app.route('/applicant/<int:user_id>', methods=['GET'])
def get_applicant(user_id):
    r = applicant.get_user_info(user_id)
    return _make_success(r) if r is not None else _make_error('')


@users_app.route('/applicant/<int:user_id>', methods=['POST'])
def handle_applicant(user_id):
    data = json.loads(request.data)
    return _make_success('') if applicant.update_applicant(data['job_id'], user_id, data['status']) else _make_error('')


@users_app.route('/resume/<int:user_id>', methods=["GET"])
def get_resume(user_id):
    r = applicant.get_resume(user_id)
    return _make_success(r) if r is not None else _make_error('')


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

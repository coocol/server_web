# -*- coding: utf-8 -*-

from flask import Blueprint, request
from service import enterprise
import json

enters_app = Blueprint('enters_app', __name__)


@enters_app.route('/enterprise/<int:company_id>/profile', methods=['GET'])
def get_enter_info(company_id):
    r = enterprise.get_enter_info(company_id)
    if r is not None:
        return _make_success(r)
    return _make_error('error id')


@enters_app.route('/register', methods=['POST'])
def register():
    data = json.loads(request.data)
    if not enterprise.is_email_existed(data['email']):
        return _make_error('该邮箱已被占用')
    enterprise.register_company(data['email'], data['password'])
    return _make_success('')


@enters_app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data)
    r = enterprise.login(data['email'], data['password'])
    if not r['status']:
        return _make_error(r['msg'])
    return _make_success({'cid': r['id']})


@enters_app.route('/enterprise/<int:company_id>/logo', methods=["POST"])
def save_logo(company_id):
    try:
        f = request.files['file']
        f.save('static/logo/%s.jpg' % company_id)
        return _make_success('')
    except Exception, e:
        print e.message
        return _make_error('')


@enters_app.route('/provinces', methods=['GET'])
def get_provinces():
    return _make_success(enterprise.get_provinces())


@enters_app.route('/cities', methods=['GET'])
def get_cities():
    return _make_success(enterprise.get_cities())


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
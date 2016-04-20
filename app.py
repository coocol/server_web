# -*- coding: utf-8 -*-

"""
    views for web server
"""

from flask import Flask, send_from_directory, safe_join, request, make_response, sessions, render_template
from werkzeug.wsgi import SharedDataMiddleware

from views import enterprises, jobs, applicants
from service import job
import config
import os

app = Flask(__name__, static_url_path=config.STATIC_PATH)
template_folder=os.path.join('.', 'output/templates')
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/': os.path.join('.', 'output')
})

app.register_blueprint(enterprises.enters_app)
app.register_blueprint(jobs.jobs_app)
app.register_blueprint(applicants.users_app)


@app.route('/static/<path:path>')
def get_static(path):
    return send_from_directory('static', path)


@app.route('/<path:path>')
def get_static_html(path):
    return render_template(path)


@app.route('/')
def get_index():
    enter_id = 20
    all_jobs = job.get_all_jobs(enter_id, 0)
    return render_template('joblist.html', all_jobs=all_jobs)


app.secret_key = 'SBV61518S_SE2X R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

import os

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def main():
        temp_data={
            "now":12,
            "daily_list":[12,0,32,41,32,42,47,32],
            "weekly_list":[16,22,32,15,32,42,47,12,52,42,22,11,22,42,47,32],
            "monthly_list":[16,22,32,15,32,42,47,12,52,42,22,11,22,42,47,32],
            }
        return render_template('main.html',temp_data=temp_data)

    return app
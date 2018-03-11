'''the main mod of ika'''
import random
from string import ascii_letters as al
import flask
from flask_bootstrap import Bootstrap
from frontend import frontend
from endpoint import app
from endpoint import get_topics


Bootstrap(app)
app.register_blueprint(frontend)
# app config for image upload
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024
app.config['SECRET_KEY'] = ''.join(random.choices(al, k=15))
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 20


@app.errorhandler(404)
def page_not_found(err):
    '''page not found'''
    return flask.render_template('404.html', topics=get_topics()), 404


if __name__ == '__main__':
    app.run(debug=True)

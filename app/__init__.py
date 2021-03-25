import logging
import os

from flask            import Flask, request
from config           import Config
from flask_babel      import Babel
from flask_bootstrap  import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate    import Migrate
from flask_moment     import Moment
from flask_babel      import Babel, lazy_gettext as _l
from flask_login      import LoginManager
from flask_mail       import Mail
from logging.handlers import SMTPHandler, RotatingFileHandler
from elasticsearch    import Elasticsearch

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
babel = Babel()

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)
  app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
      if app.config['ELASTICSEARCH_URL'] else None


  db.init_app(app)
  migrate.init_app(app, db)
  login.init_app(app)
  mail.init_app(app)
  bootstrap.init_app(app)
  moment.init_app(app)
  babel.init_app(app)

  from app.errors import bp as errors_bp
  app.register_blueprint(errors_bp)

  from app.auth import bp as auth_bp
  app.register_blueprint(auth_bp, url_prefix='/auth')

  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  if not app.debug and not app.testing:
    if app.config['MAIL_SERVER']:
      auth = None
      if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
        auth = (app.config['MAIL_USERNAME'],
                app.config['MAIL_PASSWORD'])
      secure = None
      if app.config['MAIL_USE_TLS']:
        secure = ()
      mail_handler = SMTPHandler(
        mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
        fromaddr='no-reply@' + app.config['MAIL_SERVER'],
        toaddrs=app.config['ADMINS'], subject='Dumb Twitter Failure',
        credentials=auth, secure=secure)
      mail_handler.setLevel(logging.ERROR)
      app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
      os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/dumbtwitter.log',
                                       maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
      '%(asctime)s %(levelname)s: %(message)s '
      '[in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Dumb Twitter startup')

  return app

from app import models



aries = {
    'name': 'aries',
    'strengths': ['courageous', 'determined', 'confident', 'enthusiastic', 'optimistic', 'honest', 'passionate'],
    'weaknesses': ['impatient', 'moody', 'short-tempered', 'impulsive', 'aggressive']
}

taurus = {
    'name': 'taurus',
    'strengths': ['reliable', 'patient', 'practical', 'devoted', 'responsible', 'stable'],
    'weaknesses': ['stubborn', 'possessive', 'uncompromising']
}
gemini = {
    'name': 'gemini',
    'strengths': ['gentle', 'affectionate', 'curious', 'adaptable', 'fast-learner'],
    'weaknesses': ['nervous', 'inconsistent', 'indecisive']
}
cancer = {
    'name': 'cancer',
    'strengths': ['tenacious', 'imaginative', 'loyal', 'emotional', 'sympathetic', 'persuasive'],
    'weaknesses': ['moody', 'pessimistic', 'suspicious', 'manipulative', 'insecure']
}
leo = {
    'name': 'leo',
    'strengths': ['creative', 'passionate', 'generous', 'warm-hearted', 'cheerful', 'humorous'],
    'weaknesses': ['arrogant', 'stubborn', 'self-centered', 'lazy', 'inflexible']
}
libra = {
    'name': 'libra',
    'strengths': ['cooperative', 'diplomatic', 'gracious', 'fair-minded', 'social'],
    'weaknesses': ['indecisive', 'stubborn', 'self-pity']
}
scorpio = {
    'name': 'scorpio',
    'strengths': ['resourceful', 'brave', 'passionate', 'stubborn', 'friendly'],
    'weaknesses': ['distrusting', 'jealous', 'secretive', 'violent']
}
sagittarius = {
    'name': 'sagittarius',
    'strengths': ['generous', 'idealistic', 'funny'],
    'weaknesses': ['over-promises', 'impatient', 'word-vomit']
}
capricorn = {
    'name': 'capricorn',
    'strengths': ['responsible', 'disciplined', 'self-control', 'leader'],
    'weaknesses': ['know-it-all', 'unforgiving', 'condescending']
}
aquarius = {
    'name': 'aquarius',
    'strengths': ['progressive', 'original', 'independent', 'humanitarian'],
    'weaknesses': ['unemotional', 'temperamental', 'uncompromising', 'aloof']
}
pisces = {
    'name': 'pisces',
    'strengths': ['compassionate', 'artistic', 'intuitive', 'gentle', 'wise', 'musical'],
    'weaknesses': ['fearful', 'trusting', 'sad', 'escapist', 'victim']
}

virgo = {
  'name': 'virgo',
  'strengths': ['loyal', 'analytical', 'kind', 'hardworking', 'practical'],
  'weaknesses': ['shy', 'worry', 'critical']
}

signs = [aries, taurus, gemini, cancer, leo, libra, scorpio, sagittarius, capricorn, aquarius, pisces, virgo]

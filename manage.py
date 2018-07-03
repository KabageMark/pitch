from app import app
from  flask_script import Manager,Server
from app import db
from app.models import Pitches
from  flask_migrate import Migrate, MigrateCommand


manager = Manager(app)
manager.add_command('server',Server)
db.init_app(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
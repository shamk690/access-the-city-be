import os
# import file from different folder
from db.data.test_data.users import users
from flask import Flask, request, jsonify
from file import function

from flask_sqlalchemy import SQLAlchemy


# relative path
dirname = os.path.relpath(__file__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://marco:password@localhost:5000/access_test'
db = SQLAlchemy(app)

print(db)


@app.route('/api')
def response():
    return jsonify(users)


if __name__ == '__main__':
    app.run()

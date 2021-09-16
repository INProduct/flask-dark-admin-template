from flask import Flask
from dark_admin.dark_admin import dark_admin
from site_info_de import site_info


app = Flask(__name__)
app.register_blueprint(dark_admin, url_prefix='/admin')


@app.route('/')
def index():
    return 'Main-Index'


if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, render_template, flash
from site_info_de import site_info

dark_admin = Blueprint('dark_admin', __name__, static_folder='static', template_folder='templates/dark-admin')


@dark_admin.route('/')
def index():
    flash('hello', 'warning')
    flash('haudi', 'success')
    return render_template('index.html', site_info=site_info)

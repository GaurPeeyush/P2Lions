from flask import Blueprint, render_template

gamereview_bp2 = Blueprint('gamereview2', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@gamereview_bp2.route('/')
def index():
    return render_template("andrewhome.html")

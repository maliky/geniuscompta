"""
views for my flask app
"""

from flask import render_template, Blueprint

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/", methods=(["GET"]))
def accueil():
    noms = ("technologie", "fiscalite", "cabinet")
    labels = ["Innovation", "Documents", "La vie du cabinet"]

    return render_template("accueil.html", data=list(zip(noms, labels)))

from flask import Blueprint, render_template, url_for, redirect, flash, request
from flask_login import login_required, current_user
from .forms import AccountDetails
from . import db
from .models import Accounts

views = Blueprint("views", __name__,
                  template_folder="templates", static_folder="static")


@views.route("/")
def index():
    return redirect(url_for("auth.login"))


@views.route("/dashboard", methods=['POST', "GET"])
@login_required
def dashboard():
    form = AccountDetails()
    if request.method == "POST":

        if form.validate_on_submit():
            new_account = Accounts(
                name=request.form.get("name"),
                username=request.form.get("username"),
                password=request.form.get("password"),
                website=request.form.get("website"),
                notes=request.form.get("notes"),
                user_id=current_user.id
            )

            db.session.add(new_account)
            db.session.commit()

            flash("new account added", category='success')

        else:
            flash("Kindly fill all the area with *", category='error')
    return render_template("dashboard.html", user=current_user, form=form)


@views.route("/account/delete/<id>")
@login_required
def delete_account(id):
    pass


@views.route("/account/move-to-trash/<id>")
@login_required
def move_to_trash(id):
    pass

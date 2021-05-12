"""
	login and signup
"""
from . import db
from .models import User, Accounts
from flask import Blueprint, render_template, request, flash, url_for, redirect
from .forms import UserLoginForm, UserSignUpForm
import sqlalchemy
from flask_login import current_user, login_required, login_user, logout_user


auth = Blueprint("auth", __name__)


@auth.route("/auth/login", methods=["GET", "POST"])
def login():
    form = UserLoginForm()

    if request.method == 'POST':

        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first_or_404(
                "The user with that email cannot be found. Make sure the username is correct or create an account")

            if user:
                if user.is_correct_password(form.master_password.data):
                    login_user(user, remember=form.remember_me.data)

                    flash(f"Welcome back, {user.username}", category='success')
                    return redirect(url_for("views.dashboard"))
                else:
                    flash("incorrect username or password", "errors")
                    return redirect(url_for("auth.login"))
            else:
                return redirect(url_for("auth.signup"))

    return render_template("login.html", form=form,  user=current_user)


@auth.route("/auth/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/auth/sign-up", methods=["GET", "POST"])
def signup():
    form = UserSignUpForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            if form.validate_password():

                try:
                    # create new user
                    new_user = User(
                        username=form.username.data,
                        email=form.email.data,
                        password=form.master_password.data
                    )

                    db.session.add(new_user)
                    db.session.commit()

                    # logs in the user
                    login_user(new_user, remember=form.remember_me.data)

                    flash(f"Welcome, {form.username.data} ",
                          category='success')

                    return redirect(url_for("views.dashboard"))
                except sqlalchemy.exc.IntegrityError:
                    flash("the username or email exists, try another one",
                          category="error")
            else:
                flash(
                    "Password's minimun length is 8, it should contain upper and lowercase letters and at least 1 number", category='error')
        # else:
        #     flash(
        #         "Kindly check and confirm your details before submitting", category='error')
    return render_template("sign-up.html", form=form,  user=current_user)

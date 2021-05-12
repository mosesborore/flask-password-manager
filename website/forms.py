from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo
from .utils.password_validator import validate


class UserLoginForm(FlaskForm):
    # username = StringField("Username", validators=[
    #                        DataRequired(), Length(min=8)])
    email = StringField("Email", validators=[DataRequired()])
    master_password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Log In")


class UserSignUpForm(FlaskForm):
    username = StringField("Username", validators=[
                           DataRequired(), Length(min=8)])
    email = StringField("Email", validators=[DataRequired()])
    master_password = PasswordField("Password", validators=[
                                    DataRequired(), EqualTo("confirm_password", "Password must match ")])
    confirm_password = PasswordField(
        "Repeat Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")

    submit = SubmitField("Sign In")

    def validate_password(self):
        """ validate whether password meets all the required standards 
            like: min-length of 8
                at least 1 number, special characters and uppercase
        """
        return validate(self.master_password.data)


class AccountDetails(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    website = StringField("Website", validators=[Length(max=1000)])
    notes = TextAreaField("Notes", validators=[Length(max=2000)])
    submit = SubmitField()

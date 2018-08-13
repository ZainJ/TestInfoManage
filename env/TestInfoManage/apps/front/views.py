from flask import Blueprint, url_for, redirect, render_template, views, flash, request, session
from .forms import RegisterForm, LoginForm
from exts import db
from .models import User
import config
from .decorators import login_required,keep_login_status
at = Blueprint('front', __name__)


@at.route('/interfacemanage/')
@login_required
def interfacemanage():
    return render_template('interfacemanage.html')
@at.route('/bigscreen/')
@login_required
def bigscreen():
    return render_template('bigscreen.html')

@at.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('front.login'))


class Register(views.MethodView):
    decorators = [keep_login_status]
    def get(self, message=None):
        return render_template('register.html', message=message)

    def post(self):
        form = RegisterForm(request.form)
        if form.validate():
            user = User(username=form.username.data,
                        password=form.password.data,
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash('注册成功')
            return redirect(url_for('front.login'))
        else:
            message = form.get_error()
            return self.get(message=message)


class Login(views.MethodView):
    decorators = [keep_login_status]
    def get(self, message=None):
        return render_template('login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                return redirect(url_for('front.interfacemanage'))
            else:
                return self.get(message='用户名或密码错误')
        else:
            message = form.get_error()
            return self.get(message=message)

at.add_url_rule('/register/', view_func=Register.as_view('register'))
at.add_url_rule('/', view_func=Login.as_view('login'))

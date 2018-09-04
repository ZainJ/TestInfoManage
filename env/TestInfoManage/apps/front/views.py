from flask import Blueprint, url_for, redirect, render_template, views, flash, request, session
from .forms import RegisterForm, LoginForm,ProjectForm
from exts import db
from .models import User,ProjectModel
import config
from .decorators import login_required,keep_login_status
from utils import restful
from flask_restful import Resource,Api,fields,marshal_with
from flask import jsonify,json
from flask_paginate import Pagination,get_page_parameter
at = Blueprint('front', __name__)
api=Api(at)

@at.route('/interfacemanage/')
@login_required
def interfacemanage():
    return render_template('interfacemanage/interfacemanage.html')
#接口管理模块
@at.route('/interfacelist/')
@login_required
def interfacelist():
    return render_template('interfacemanage/children/interfacelist.html')
@at.route('/interfacecase/')
@login_required
def interfacecase():
    return render_template('interfacemanage/children/interfacecase.html')
@at.route('/publicparameter/')
@login_required
def publicparameter():
    return render_template('interfacemanage/children/publicparameter.html')
@at.route('/sqlmanage/')
@login_required
def sqlmanage():
    return render_template('interfacemanage/children/sqlmanage.html')
###################################################################
#系统管理模块
#添加项目
class Project(views.MethodView):
    decorators = [login_required]
    def get(self,message=None):
        page=request.args.get(get_page_parameter(),type=int,default=1)
        start=(page-1)*config.PER_PAGE
        end=start+config.PER_PAGE
        projects=ProjectModel.query.order_by(ProjectModel.join_time.desc()).slice(start,end)
        pagination=Pagination(bs_version=3,page=page,total=ProjectModel.query.count())
        context={
            'projects':projects,
            'pagination':pagination
        }
        return render_template('sysmanage/project.html',message=message,**context)

    def post(self):
        form=ProjectForm(request.form)
        projectdescription=request.form['projectdescription']
        if form.validate():
            if projectdescription:
                project=ProjectModel(project=form.project.data,
                                creator=form.creater.data,
                                projectdescription=projectdescription)
            else:
                project=ProjectModel(project=form.project.data,
                                creator=form.creater.data)
            db.session.add(project)
            db.session.commit()
            return restful.success(message='恭喜，项目添加成功！！')
        else:
            message=form.get_error()
            return restful.validation_error(message=message)

@at.route('/moudel/')
@login_required
def moudel():
    return render_template('sysmanage/moudel.html')

@at.route('/clientmanage/')
@login_required
def clientmanage():
    return render_template('sysmanage/clientmanage.html')

@at.route('/dbmanage/')
@login_required
def dbmanage():
    return render_template('sysmanage/dbmanage.html')
############################################################
#大屏模块
@at.route('/bigscreen/')
@login_required
def bigscreen():
    return render_template('bigscreen/bigscreen.html')
#############################################################
#登录注册模块
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
#路由管理
at.add_url_rule('/register/', view_func=Register.as_view('register'))
at.add_url_rule('/', view_func=Login.as_view('login'))
at.add_url_rule('/project/',view_func=Project.as_view('project'))
# api.add_resource(GetProject,'/getproject/','/getproject/')
#######################################################################
from wtforms import Form,StringField,IntegerField,PasswordField,SubmitField,BooleanField
from wtforms.validators import Email,InputRequired,Length,EqualTo,DataRequired,ValidationError,InputRequired
from ..forms import BaseForm
from apps.front import models
from flask_wtf import FlaskForm


#用户注册表单
class RegisterForm(BaseForm):
    username=StringField('用户名',validators=[Length(5,20,message='用户名只能在5-20字符之间'),DataRequired(message='用户名不能为空')])
    password=PasswordField('密码',validators=[Length(6,20,message='密码只能在6-20字符之间'),DataRequired(message='密码不能为空')])
    confirm=PasswordField('确认密码',validators=[EqualTo('password',message='两次密码不一致')])
    email=StringField('邮箱',validators=[Email(message='无效邮箱格式'),DataRequired(message="邮箱不能为空")])

    #自定义用户名验证器
    def validators_username(self,field):
        if models.User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已注册，请选用其他名称')


    def validators_email(self,field):
        if models.User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已存在，请选用其他邮箱')


class LoginForm(BaseForm):
    username=StringField('用户名',validators=[DataRequired(message='用户名不能为空'),Length(5,20,message='用户名为5-20字符')])
    password=PasswordField('密码',validators=[Length(6,20,message='密码为6-20字符'),InputRequired(message='密码不能为空')])
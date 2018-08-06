from  flask import session,redirect,url_for
from functools import wraps
import config
def login_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if config.CMS_USER_ID in session:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('front.login'))
    return inner

def keep_login_status(func):
    @wraps(func)
    def inner(*args,**kwargs):
        if config.CMS_USER_ID in session:
            return redirect(url_for('front.index'))
        else:
            return func(*args,**kwargs)
    return inner
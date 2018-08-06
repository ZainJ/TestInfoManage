from .views import at
import config
from .models import User
from flask import session,g

@at.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = User.query.get(user_id)
        if user:
            g.user=user
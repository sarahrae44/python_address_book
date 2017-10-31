from functools import wraps
from flask import request, abort

def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        if request.args.get('key') and request.args.get('key') == 170SWEET6862:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function
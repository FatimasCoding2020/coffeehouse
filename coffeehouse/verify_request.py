from django.shortcuts import render
import traceback
from functools import wraps


def verify_request(f):
    @wraps(f)
    def decorated_function(request, *args, **kws):
        try:
            return f(request, *args, **kws)
        except Exception as e:
            trackerror = traceback.format_exc()
            print("error",trackerror)
            return render(request, 'error.html', {})

    return decorated_function
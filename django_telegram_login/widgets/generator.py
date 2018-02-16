"""
Widgets generator interface.
"""
from functools import wraps

from django_telegram_login.widgets.constants import SMALL


def widget(f):
    @wraps(f)
    def create_common_widget(bot_name, size=SMALL, corner_radius=None, show_photo=True, access_write=True, **kwargs):
        body = f(**kwargs)
        script_start = (
            '<script async src="https://telegram.org/js/telegram-widget.js?3" '
            'data-telegram-login="{0}" data-size="{1}" '''.format(bot_name, size))
        userpic = 'data-userpic="{}" '.format(str(show_photo).lower()) if not show_photo else ''
        corner_radius = 'data-radius="{}" '.format(corner_radius) if corner_radius else ''
        access = 'data-request-access="write"' if access_write else ''
        script_end = '></script>'
        widget_script = script_start + userpic + corner_radius + body + access + script_end
        return widget_script

    return create_common_widget


@widget
def create_callback_login_widget():
    """
    Create callback widget, that allows to handle user data in JavaSccript.
    """
    return 'data-onauth="onTelegramAuth(user)" '


@widget
def create_redirect_login_widget(redirect_url):
    """
    Create redirect widget, that allows to handle user data as get request params.
    """
    return 'data-auth-url="{}" '.format(redirect_url)


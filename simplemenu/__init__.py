"""
A  simple menu app for Django with ordering in admin interface and ability to link menu with model instance, view or URL.
"""
# setup.py imports this module to gather package version so we must not crash since Django is not loaded
try:
    from simplemenu.pages import register
except ImportError:

    pass

VERSION = (0, 5, 0)

__version__ = '.'.join((str(each) for each in VERSION[:4]))

def get_version():
    """
    Returns shorter version (digit parts only) as string.
    """
    return '.'.join((str(each) for each in VERSION[:4]))



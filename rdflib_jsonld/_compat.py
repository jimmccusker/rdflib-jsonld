from past.builtins import basestring
import sys

IS_PY3 = sys.version_info[0] >= 3

basestring = str if IS_PY3 else basestring  # noqa
str = str if IS_PY3 else str  # noqa

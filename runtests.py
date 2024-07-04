#!/usr/bin/env python

"""
Setup for running tests for this app
"""

# stdlib
from os.path import abspath, dirname
import sys
import warnings

# django
import django
from django.conf import settings
from django.core.management import execute_from_command_line

# local django


warnings.simplefilter("always", DeprecationWarning)

sys.stderr.write("Using Python version {0} from {1}\n".format(sys.version[:5], sys.executable))
sys.stderr.write("Using Django version {0} from {1}\n".format(django.get_version(), dirname(abspath(django.__file__))))

if not settings.configured:
    settings.configure(
        DEBUG=False,
        DATABASES={"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}},
        TEST_RUNNER="django.test.runner.DiscoverRunner",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.messages",
            "django.contrib.sessions",
            "django.contrib.sites",
            "django_measurement",
            "tests",
        ],
        MIDDLEWARE=(
            "django.middleware.common.CommonMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.csrf.CsrfViewMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
        ),
        ROOT_URLCONF=None,
        SECRET_KEY="supersecret",
    )

DEFAULT_TEST_APPS = ["tests"]


def runtests():
    other_args = list(filter(lambda arg: arg.startswith("-"), sys.argv[1:]))
    test_apps = list(filter(lambda arg: not arg.startswith("-"), sys.argv[1:])) or DEFAULT_TEST_APPS
    argv = sys.argv[:1] + ["test", "--traceback"] + other_args + test_apps
    execute_from_command_line(argv)


if __name__ == "__main__":
    runtests()

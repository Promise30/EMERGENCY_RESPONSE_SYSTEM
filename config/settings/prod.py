from .dev import *
import dj_database_url


DATABASES = {
    'default': dj_database_url.parse(
        os.getenv('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(",")
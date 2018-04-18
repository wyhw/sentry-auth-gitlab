from __future__ import absolute_import, print_function

from django.conf import settings

CLIENT_ID = getattr(settings, 'GITLAB_APP_ID', None)

CLIENT_SECRET = getattr(settings, 'GITLAB_API_SECRET', None)

# we request repo as we share scopes with the other GitLab integration
SCOPE = getattr(settings, 'GITLAB_SCOPE', 'api')

# deprecated please use GITLAB_API_DOMAIN and GITLAB_BASE_DOMAIN
DOMAIN = getattr(settings, 'GITLAB_DOMAIN', 'api.gitlab.com')

BASE_DOMAIN = getattr(settings, 'GITLAB_BASE_DOMAIN', 'gitlab.com')
API_DOMAIN = getattr(settings, 'GITLAB_API_DOMAIN', DOMAIN)

ACCESS_TOKEN_URL = 'https://{0}/oauth/access_token'.format(BASE_DOMAIN)
AUTHORIZE_URL = 'https://{0}/oauth/authorize'.format(BASE_DOMAIN)

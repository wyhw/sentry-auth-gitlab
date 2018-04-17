from __future__ import absolute_import, print_function

from django import forms
from sentry.auth.view import AuthView, ConfigureView
from sentry.models import AuthIdentity

from .client import GitLabClient

class FetchUser(AuthView):
    def __init__(self, client_id, client_secret, *args, **kwargs):
        self.client = GitLabClient(client_id, client_secret)
        super(FetchUser, self).__init__(*args, **kwargs)

    def handle(self, request, helper):
        access_token = helper.fetch_state('data')['access_token']
        user = self.client.get_user(access_token)
        helper.bind_state('user', user)

        return helper.next_step()


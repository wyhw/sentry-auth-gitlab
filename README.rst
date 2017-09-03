GitLab Auth for Sentry
======================

An SSO provider for Sentry which enables GitLab organization-restricted authentication.

Install
-------

::

    $ pip install https://gitlab.com/getsentry/sentry-auth-gitlab/archive/master.zip

Setup
-----

Create a new application under your organization in GitLab. Enter the **Authorization
callback URL** as the prefix to your Sentry installation:

::

    https://example.sentry.com


Once done, grab your API keys and drop them in your ``sentry.conf.py``:

.. code-block:: python

    GITLAB_APP_ID = ""

    GITLAB_API_SECRET = ""


Verified email addresses can optionally be required:

.. code-block:: python

    GITLAB_REQUIRE_VERIFIED_EMAIL = True


Optionally you may also specify the domain (for GHE users):

.. code-block:: python

    GITLAB_BASE_DOMAIN = "git.example.com"

    GITLAB_API_DOMAIN = "api.git.example.com"


If Subdomain isolation is disabled in GHE:

.. code-block:: python

    GITLAB_BASE_DOMAIN = "git.example.com"

    GITLAB_API_DOMAIN = "git.example.com/api/v3"

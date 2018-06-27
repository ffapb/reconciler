# reconciler
Django app for users to upload pairs of files for reconciliation.

Originally meant for financial institution to reconcile margins on CFDs with their provider.


## Usage

- copy `reconciler/settings_override.py.dist` to `reconciler/settings_override.py` and edit as needed
- Standard django-fu
- `./manage.py test reconciler.core.tests`

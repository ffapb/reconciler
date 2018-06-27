# reconciler
Django app for users to upload pairs of files for reconciliation.

Originally meant for financial institution to reconcile margins on CFDs with their provider.


## Installation

- copy `reconciler/settings_override.py.dist` to `reconciler/settings_override.py` and edit as needed
- `./manage.py test reconciler.core.tests`
- Standard django-fu


## Usage

- go to `localhost:8888/admin`
- upload first file `saxo_20180627.csv` in `FileModel`
- upload a second file `ffa_20180627.csv` in `FileModel`
- add a new `ReconciliationModel` object, and choose `file_1 = first file above` and `file_2 = second file above`
- save
- The name of the `ReconciliationModel` object just created will either be `saxo... vs ffa...: OK`  or `saxo... vs ffa...: diff`


## TODO

- make "ok / diff" more advanced
  - more details for side-by-side comparison
  - add django views
  - kind of like http://pbpython.com/excel-diff-pandas.html

## Changelog

Version 0.1 (2018-07-??)
- first commit with models and reconciliation based on `pandas.assert_frame_equal`

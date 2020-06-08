# Copyright 2012-2020 Akretion France (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


{
    'name': 'Account Move Import',
    'version': '13.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Import account moves generated by external software',
    'license': 'AGPL-3',
    'description': """
Account Move Import
===================

This module handle the import of one or several account moves from a file
(CSV, TXT, XLS or any other format). The name of this module
is account_move_csv_import, but it is not limited to the import of CSV files
(this is an historic name and I didn't want to change it).
This module currently supports:

* LibreOffice CSV export files,
* MeilleureGestion.com payroll CSV files,
* Quadra export files,
* In Extenso,
* Ciel paye,
* Payfit,
* FEC (text format).

This module can easily be extended to support other formats.

This module also supports account move line reconciliation (used for FEC import).

There are many community modules that handle the import of account moves
via CSV/TXT files.
But I decided to develop this module because I wanted a module with
the following design guidelines:

* code is easy to read
* code is easy to debug
* expressive error messages

This module has been written by Alexis de Lattre
from Akretion (alexis.delattre@akretion.com).
    """,
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'depends': ['account'],
    'demo': ['demo/demo.xml'],
    'external_dependencies': {'python': ['unicodecsv', 'xlrd']},
    'data': [
        'data/sequence.xml',
        'wizard/import_move_view.xml',
    ],
    'installable': True,
}

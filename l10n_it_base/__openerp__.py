# -*- coding: utf-8 -*-
#
# Copyright 2010-18 - Associazione Odoo Italia <https://odoo-italia.org>
# Copyright 2014-19 - SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'Italian Localisation - Base',
    'version': '7.0.0.2.15',
    'category': 'Localisation/Italy',
    'author': 'Odoo Italia Associazione,'
              'Odoo Community Association (OCA),'
              'SHS-AV s.r.l.',
    'website': 'https://odoo-italia.org/',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_view.xml',
        'views/company_view.xml',
        'views/city_view.xml',
        'views/province_view.xml',
        'data/res.region.csv',
        'data/res.province.csv',
        'data/res.country.state.csv',
        'data/res.city.csv',
        'data/res.partner.title.csv',
    ],
    'test': ['test/res_partner.yml'],
    'installable': True,
    'description': r'''
Overview / Panoramica
=====================

|en| Italy Base localization
-----------------------

This module add following data:

* Italian cities
* Titles
* Provinces (districts) and Regions

|

|it| Localizzazione italiana di base
-------------------------------

Questo modulo fornisce i dati precompilati di:

* Comuni italiani (aggiornati al 2014)
* Titoli
* Province e regioni aggiornati

Inoltre gestisce alcuni automatistmi durante la compilazione del campi anagrafici.

La videata dell'anagrafica è modificata come da consuetudine italiana:

CAP - Località - Provincia

mentre nella versione origiale di Odoo il CAP è posto dopo la provincia (formato anglosassone).


|

Features / Caratteristiche
--------------------------

+----------------------------------------------------------------+----------+----------------------------------------------+
| Feature / Funzione                                             |  Status  | Notes / Note                                 |
+----------------------------------------------------------------+----------+----------------------------------------------+
| City from ZIP / Città da CAP                                   | |check|  | Propone città da CAP; città modificabile     |
+----------------------------------------------------------------+----------+----------------------------------------------+
| Multizone ZIP  / CAP Multizona                                 | |check|  | Riconoscimento CAP multizona                 |
+----------------------------------------------------------------+----------+----------------------------------------------+
| District from ZIP / Provincia da CAP                           | |check|  | Compila la provincia dal CAP                 |
+----------------------------------------------------------------+----------+----------------------------------------------+
| Check for ZIP & district / Controllo coerenza CAP e provincia  | |check|  | Verifica coerenza di CAP e provincia         |
+----------------------------------------------------------------+----------+----------------------------------------------+

|

Usage / Utilizo
---------------

|it| Durante l'inserimento dell'anagrafica rispettare le seguenti regole:

* Inserire sempre la nazione: serve per attivare i successivi controlli sul CAP e provincia
* Dopo l'inserimento del CAP appare un comune e la provincia; poichè esistono più comuni con lo stesso CAP potete correggere il dato
* Inserire la partita IVA con il prefisso ISO della nazione: ad esempio per una p.IVA italiana digitate IT12345670017

|
|

Support / Supporto
------------------


|Zeroincombenze| This module is maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__
and support is supplied through `Odoo Italia Associazione Forum <https://odoo-italia.org/index.php/kunena/recente>`__


|
|

Credits / Titoli di coda
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


|

Authors / Autori
-----------------


* `Innoviu srl <http://www.innoviu.com>`__
* `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__

Contributors / Collaboratori
----------------------------


* Davide Corio <davide.corio@domsense.com>
* Luca Subiaco <subluca@gmail.com>
* Simone Orsi <simone.orsi@domsense.com>
* Mario Riva <mario.riva@domsense.com>
* Mauro Soligo <mauro.soligo@katodo.com>
* Giovanni Barzan <giovanni.barzan@gmail.com>
* Lorenzo Battistini <lorenzo.battistini@domsense.com>
* Roberto Onnis <onnis.roberto@gmail.com>
* Antonio M. Vigliotti <info@shs-av.com>

|

----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato di `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sullla propria infrastuttura.
La distribuzione `Zeroincombenze® è progettata per le esigenze del mercato italiano.

|

Last Update / Ultimo aggiornamento: 2018-11-15

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/l10n-italy.svg?branch=7.0
    :target: https://travis-ci.org/zeroincombenze/l10n-italy
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/l10n-italy/badge.svg?branch=7.0
    :target: https://coveralls.io/github/zeroincombenze/l10n-italy?branch=7.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/l10n-italy/branch/7.0
    :alt: Codecov
.. |OCA project| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg
    :target: https://github.com/OCA/l10n-italy/tree/7.0
    :alt: OCA
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/7.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/7.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg
    :target: https://erp7.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov Status| image:: Unknown badge-oca-codecov
    :target: Unknown oca-codecov-URL
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/groups/openerp.italia/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/DesktopTelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://raw.githubusercontent.com/zeroincombenze/grymbcertificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b
''',
}

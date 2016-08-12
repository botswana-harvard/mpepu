
https://clinicaltrials.gov/ct2/show/NCT01229761

Uses Django 1.6 / PY2 and older edc modules.

This system is no longer in development. 

===============================================

v1.2.6

you will also need to add in bhp056 (where manage.py is) three repos

git clone git@gitserver:edc
git clone git@gitserver:edc_templates templates
git clone git@gitserver:lis

project structure is

apps: MPEPU specific apps
edc: core edc apps and code
lis: core lis apps and code that edc and bcpp use
locale:
media:
static: (be sure to run collectstatic)
templates: (clone of edc_templates)
keys:
bhp056: settings and urls

-erik


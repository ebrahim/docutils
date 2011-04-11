# $Id: en.py 4564 2006-05-21 20:44:42Z wiemann $
# Author: Mohammad Ebrahim Mohammadi Panah <ebrahim@mohammadi.ir>
# Copyright: This module has been placed in the public domain.

# New language mappings are welcome.  Before doing a new translation, please
# read <http://docutils.sf.net/docs/howto/i18n.html>.  Two files must be
# translated for each language: one in docutils/languages, the other in
# docutils/parsers/rst/languages.

"""
Persian-language mappings for language-dependent features of Docutils.
"""

__docformat__ = 'reStructuredText'

labels = {
      # fixed: language-dependent
      'author': u'نویسنده',
      'authors': u'نویسندگان',
      'organization': u'سازمان',
      'address': u'نشانی',
      'contact': u'تماس',
      'version': u'نسخه',
      'revision': u'بازبینی',
      'status': u'وضعیت',
      'date': u'تاریخ',
      'copyright': u'حق نشر',
      'dedication': u'تقدیم به',
      'abstract': u'چکیده',
      'attention': u'توجه!',
      'caution': u'هشدار!',
      'danger': u'!خطر!',
      'error': u'خطا',
      'hint': u'تذکر',
      'important': u'مهم',
      'note': u'یادداشت',
      'tip': u'نکته',
      'warning': u'اخطار',
      'contents': u'فهرست'}
"""Mapping of node class name to label text."""

bibliographic_fields = {
      # language-dependent: fixed
      u'نویسنده': 'author',
      u'نویسندگان': 'authors',
      u'سازمان': 'organization',
      u'نشانی': 'address',
      u'تماس': 'contact',
      u'نسخه': 'version',
      u'بازبینی': 'revision',
      u'وضعیت': 'status',
      u'تاریخ': 'date',
      u'حق نشر': 'copyright',
      u'تقدیم': 'dedication',
      u'چکیده': 'abstract'}
"""Persian to canonical name mapping for bibliographic fields."""

author_separators = [';', ',', u'،', u'؛']
"""List of separator strings for the 'Authors' bibliographic field. Tried in
order."""

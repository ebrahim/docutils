# coding=utf8
# $Id: en.py 6460 2010-10-29 22:18:44Z milde $
# Author: Mohammad Ebrahim Mohammadi Panah <ebrahim@mohammadi.ir>
# Copyright: This module has been placed in the public domain.

# New language mappings are welcome.  Before doing a new translation, please
# read <http://docutils.sf.net/docs/howto/i18n.html>.  Two files must be
# translated for each language: one in docutils/languages, the other in
# docutils/parsers/rst/languages.

"""
Persian-language mappings for language-dependent features of
reStructuredText.
"""

__docformat__ = 'reStructuredText'


directives = {
      # language-dependent: fixed
      u'توجه': 'attention',
      u'هشدار': 'caution',
      u'خطر': 'danger',
      u'خطا': 'error',
      u'تذکر': 'hint',
      u'مهم': 'important',
      u'یادداشت': 'note',
      u'نکته': 'tip',
      u'اخطار': 'warning',
      u'نصیحت': 'admonition',
      u'حاشیه': 'sidebar',
      u'موضوع': 'topic',
      u'قطعه-خط': 'line-block',
      u'لفظی-تجزیه‌شده': 'parsed-literal',
      u'سرفصل': 'rubric',
      u'سرلوحه': 'epigraph',
      u'اهم': 'highlights',
      u'نقل-گزیده': 'pull-quote',
      u'مرکب': 'compound',
      u'ظرف': 'container',
      #'questions': 'questions',
      u'جدول': 'table',
      u'جدول-csv': 'csv-table',
      u'جدول-فهرستی': 'list-table',
      #'qa': 'questions',
      #'faq': 'questions',
      u'فرا': 'meta',
      u'ریاضی': 'math',
      #'imagemap': 'imagemap',
      u'تصویر': 'image',
      u'شکل': 'figure',
      u'شمول': 'include',
      u'خام': 'raw',
      u'جایگزینی': 'replace',
      u'یونی‌کد': 'unicode',
      u'تاریخ': 'date',
      u'رده': 'class',
      u'نقش': 'role',
      u'نقش-پیش‌فرض': 'default-role',
      u'عنوان': 'title',
      u'فهرست': 'contents',
      u'شماره‌دهی': 'sectnum',
      u'سربرگ': 'header',
      u'ته‌برگ': 'footer',
      #'footnotes': 'footnotes',
      #'citations': 'citations',
      u'یادداشت‌های-مقصد': 'target-notes',
      u'رهنمود-آزمایشی-رستراکچردتکست': 'restructuredtext-test-directive'}
"""Persian name to registered (in directives/__init__.py) directive name
mapping."""

roles = {
    # language-dependent: fixed
    u'مخفف': 'abbreviation',
    u'سرنام': 'acronym',
    u'نمایه': 'index',
    u'زیر': 'subscript',
    u'زبر': 'superscript',
    u'ارجاع-عنوان': 'title-reference',
    u'عنوان': 'title-reference',
    u'ارجاع-pep': 'pep-reference',
    'pep': 'pep-reference',
    u'ارجاع-rfc': 'rfc-reference',
    'rfc': 'rfc-reference',
    u'تأکید': 'emphasis',
    u'تاکید': 'emphasis',
    u'ضخیم': 'strong',
    u'لفظی': 'literal',
    u'ریاضی': 'math',
    u'ارجاع-با-نام': 'named-reference',
    u'ارجاع-ناشناس': 'anonymous-reference',
    u'ارجاع-پاورقی': 'footnote-reference',
    u'ارجاع-نقل': 'citation-reference',
    u'ارجاع-جانشانی': 'substitution-reference',
    u'مقصد': 'target',
    u'ارجاع-نشانی': 'uri-reference',
    u'ارجاع-uri': 'uri-reference',
    u'نشانی': 'uri-reference',
    'uri': 'uri-reference',
    'url': 'uri-reference',
    u'خام': 'raw',}
"""Mapping of Persian role names to canonical role names for interpreted text.
"""

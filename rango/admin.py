#!/usr/bin/env python
# encoding: utf-8
"""
admin.py

Created by Luis C. Berrocal on 2013-10-20.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""
from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)



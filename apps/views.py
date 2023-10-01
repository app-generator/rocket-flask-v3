# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template, request, redirect
from jinja2  import TemplateNotFound

# App modules
from apps import app

# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/')
def index():
  try:
    return render_template( 'pages/index.html', segment='dashboard', parent='dashboard')
  except TemplateNotFound:
    return render_template('pages/index.html'), 404

# Pages

@app.route('/pages/tables/')
def pages_tables():
  return render_template('pages/tables.html', segment='tables', parent='pages')

@app.route('/pages/billing/')
def pages_billing():
  return render_template('pages/billing.html', segment='billing', parent='pages')

@app.route('/pages/virtual-reality/')
def pages_virtual_reality():
  return render_template('pages/virtual-reality.html', segment='virtual_reality', parent='pages')

@app.route('/pages/rtl/')
def pages_rtl():
  return render_template('pages/rtl.html', segment='rtl', parent='pages')

@app.route('/pages/profile/')
def pages_profile():
  return render_template('pages/profile.html', segment='profile', parent='pages')

@app.route('/accounts/login/')
def accounts_login():
  return render_template('accounts/login.html', segment='login', parent='accounts')

@app.route('/accounts/register/')
def accounts_register():
  return render_template('accounts/register.html', segment='register', parent='accounts')

@app.route('/accounts/password-change/')
def accounts_password_change():
  return render_template('accounts/password_change.html', segment='password_change', parent='accounts')

@app.route('/accounts/password-change-done/')
def accounts_password_change_done():
  return render_template('accounts/password_change_done.html', segment='password_change_done', parent='accounts')

@app.template_filter(name = 'replace_value')
def replace_value(value, arg):
  return value.replace(arg, ' ').title()


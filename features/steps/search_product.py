# -*- coding: utf-8 -*-

from behave import given, when, then

@given(u'I launch browser on desktop PC')
def step_impl(context):
    print('Tutaj odpalamy przegladarke')

@when('I search for any product')
def step_impl(context):
    print('Tutaj szukamy produktu')

@then('Relevant search results should be shown')
def step_impl(context):
    print('Tutaj sprawdzamy wyniki wyszukiwania')

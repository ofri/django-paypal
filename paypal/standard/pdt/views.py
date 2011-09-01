#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.http import require_GET
from paypal.standard.pdt.models import PayPalPDT
from paypal.standard.pdt.forms import PayPalPDTForm
from django.views.decorators.csrf import csrf_exempt 
 
# 09/23/2011 - Cole Krumbholz
# Paypal has started POSTing to the return_url
# GET QueryDict still contains expected parameters
# POST QueryDict now includes:
#  <QueryDict: {u'merchant_return_link': [u'click here'], u'form_charset': [u'UTF-8']}>
# Removing the require_GET decorator keeps a 405 error from hitting the user
# The view still operates as expected, albeit after limited testing
#
# @require_GET

@csrf_exempt
def pdt(request, item_check_callable=None, template="pdt/pdt.html", context=None):
    """Payment data transfer implementation: http://tinyurl.com/c9jjmw"""
    context = context or {}
    pdt_obj = None
    txn_id = request.GET.get('tx')
    failed = False
    if txn_id is not None:
        # If an existing transaction with the id tx exists: use it
        try:
            pdt_obj = PayPalPDT.objects.get(txn_id=txn_id)
        except PayPalPDT.DoesNotExist:
            # This is a new transaction so we continue processing PDT request
            pass
        
        if pdt_obj is None:
            form = PayPalPDTForm(request.GET)
            if form.is_valid():
                try:
                    pdt_obj = form.save(commit=False)
                except Exception, e:
                    error = repr(e)
                    failed = True
            else:
                error = form.errors
                failed = True
            
            if failed:
                pdt_obj = PayPalPDT()
                pdt_obj.set_flag("Invalid form. %s" % error)
            
            pdt_obj.initialize(request)
        
            if not failed:
                pdt_obj.txn_id = txn_id
                # The PDT object gets saved during verify
                pdt_obj.verify(item_check_callable)
    else:
        pass # we ignore any PDT requests that don't have a transaction id
 
    context.update({"failed":failed, "pdt_obj":pdt_obj})
    return render_to_response(template, context, RequestContext(request))

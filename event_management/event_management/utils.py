# -*- coding: utf-8 -*-
# Copyright (c) 2019, Paul Pereira and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


@frappe.whitelist()
def create_docs(n, doctype, parent_field, parent_name):
    """
    Create `n` documents of type `doctype`, linked to `parent_name`

    params:
    n -- 
    doctype -- 
    parent_field --
    parent_name -- 
    """
    for row in range(1, int(n) + 1):
        try:
            doc = frappe.get_doc({
                "doctype": doctype,
                "title": "{}".format(row),
                parent_field: parent_name
            })
            doc.insert()
        except frappe.DuplicateEntryError:
            continue

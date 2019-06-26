# -*- coding: utf-8 -*-
# Copyright (c) 2019, Paul Pereira and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Block(Document):
	pass

@frappe.whitelist()
def create_rows(amount,block):
	for row in range(1,int(amount) + 1):
		try:
			doc = frappe.get_doc({
				"doctype": "Row",
				"title": "{}".format(row),
				"block": block
			})
			doc.insert()
		except frappe.DuplicateEntryError:
			continue
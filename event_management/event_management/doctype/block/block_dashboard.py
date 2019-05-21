
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'block',
		'transactions': [
			{
				'label': _('Rows'),
				'items': ['Row','Seat']
			}
		]
	}


from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'venue',
		'transactions': [
			{
				'label': _('Blocks'),
				'items': ['Block','Row','Seat']
			}
		]
	}

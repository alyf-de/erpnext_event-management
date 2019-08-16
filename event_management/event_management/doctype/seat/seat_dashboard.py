from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'seat',
		'transactions': [
			{
				'label': _('Reservations'),
				'items': ['Reservation', 'Season Pass']
                        }
		]
	}

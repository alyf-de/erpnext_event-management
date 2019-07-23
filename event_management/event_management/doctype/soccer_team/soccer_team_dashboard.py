from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'fieldname': 'soccer_team',
		'non_standard_fieldnames': {
			'Match Day': ('home_team', 'guest_team')
		},
		'transactions': [
			{
				'label': _('Matches'),
				'items': ['Match Day']
			}
		]
	}

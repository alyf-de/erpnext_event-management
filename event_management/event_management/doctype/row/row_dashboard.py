
from __future__ import unicode_literals
from frappe import _

def get_data():
        return {
                'fieldname': 'row',
                'transactions': [
                        {
                                'label': _('Seats'),
                                'items': ['Seat']
                        }
                ]
        }


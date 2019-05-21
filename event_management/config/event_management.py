
from __future__ import unicode_literals

from frappe import _


def get_data():
    return [
        {
            "label": _("Venues"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Venue",
                    "label": _("Venue"),
                    "description": _("Venue")
                },
                {
                    "type": "doctype",
                    "name": "Block",
                    "label": _("Block"),
                    "description": _("Block")
                },
                {
                    "type": "doctype",
                    "name": "Row",
                    "label": _("Row"),
                    "description": _("Row")
                },
                {
                    "type": "doctype",
                    "name": "Seat",
                    "label": _("Seat"),
                    "description": _("Seat")
                },
            ]
        },
        {
            "label": _("Events"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Event",
                    "label": _("Event"),
                    "description": _("Event")
                },
                {
                    "type": "doctype",
                    "name": "Reservation",
                    "label": _("Reservation"),
                    "description": _("Reservation")
                }
            ]
        }
    ] 


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
        },
        {
            "label": _("Sport"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Match Day",
                    "label": _("Match Day"),
                    "description": _("Match Day")    
                },
                {
                    "type": "doctype",
                    "name": "Season",
                    "label": _("Season"),
                    "description": _("Season")    
                },               
                {
                    "type": "doctype",
                    "name": "Season Pass",
                    "label": _("Season Pass"),
                    "description": _("Season Pass")    
                },   
                {
                    "type": "doctype",
                    "name": "Soccer Team",
                    "label": _("Soccer Team"),
                    "description": _("Soccer Team")    
                },
                {
                    "type": "doctype",
                    "name": "League",
                    "label": _("League"),
                    "description": _("League")    
                } 
            ]
        }
    ] 

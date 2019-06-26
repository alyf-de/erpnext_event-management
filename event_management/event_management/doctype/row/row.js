// Copyright (c) 2019, Paul Pereira and contributors
// For license information, please see license.txt

frappe.ui.form.on('Row', {
	refresh: function(frm) {
		frm.add_custom_button(__("Create Seats"), function () {
			frappe.call({
				method: "event_management.event_management.utils.create_docs",
				args: {
					n: frm.doc.number_of_seats,
					doctype: "Seat",
					parent_field: "row",
					parent_name: frm.doc.name,
				}
			}).then(() => frm.refresh());
		});
	}
});

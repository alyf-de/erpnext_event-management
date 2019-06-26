// Copyright (c) 2019, Paul Pereira and contributors
// For license information, please see license.txt

frappe.ui.form.on('Block', {
	refresh: function (frm) {
		frm.add_custom_button(__("Create Rows"), function () {
			frappe.call({
				method: "event_management.event_management.doctype.block.block.create_rows",
				args: {
					amount: frm.doc.number_of_rows,
					block: frm.doc.name
				}
			});
		});

	}
});

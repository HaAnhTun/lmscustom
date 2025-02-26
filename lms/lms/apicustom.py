
import frappe
import json

@frappe.whitelist(allow_guest=True)
def get_all():
	data = frappe.get_all(
			"Meme",
			fields=["*"],
			order_by="score desc",
		)
	return data

@frappe.whitelist(allow_guest=True)
def get_by_name(name):
	if not frappe.db.exists("Meme", name):
		return {"ok": False, "error": "Meme not found"}

	data = frappe.get_doc("Meme", name)
	return {"ok": True, "data": data}

@frappe.whitelist(allow_guest=True)
def get_by_name():
	name = frappe.local.form_dict.name
	
	if not name:
		return {"ok": False, "error": "Missing parameter: name"}

	if not frappe.db.exists("Meme", name):
		return {"ok": False, "error": "Meme not found"}

	data = frappe.get_doc("Meme", name)
	return {"ok": True, "data": data}

@frappe.whitelist(allow_guest=True)
def create_or_update_meme(data):
	meme_name = data.get("meme_name")

	if not meme_name:
		return {"ok": False, "error": "Meme name is required"}
	
	if frappe.db.exists("Meme", {"meme_name": meme_name}):
		doc = frappe.get_doc("Meme", {"meme_name": meme_name})
		doc.update(data)
		doc.save()
		frappe.db.commit()
		return {"ok": True, "status": "Meme updated successfully", "meme_id": doc.name}
	else:
		doc = frappe.new_doc("Meme")
		doc.update(data)
		doc.insert()
		frappe.db.commit()
		return {"ok": True, "status": "Meme created successfully", "meme_id": doc.name}
	
@frappe.whitelist(allow_guest=True)
def delete_meme(meme_name):
	if not frappe.db.exists("Meme", {"meme_name": meme_name}):
		return {"ok": False, "error": "Meme not found"}

	doc = frappe.get_doc("Meme", {"meme_name": meme_name})
	doc.delete()
	frappe.db.commit()

	return {"ok": True, "status": "Meme deleted successfully"}






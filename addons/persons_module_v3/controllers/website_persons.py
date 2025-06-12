from odoo import http
from odoo.http import request


class WebsitePersons(http.Controller):

    @http.route("/persons", type="http", auth="public", website=True)
    def persons_list(self, **kwargs):
        persons = (
            request.env["persons.person"].sudo().search([], limit=5, order="id desc")
        )
        return request.render("persons_module_v3.person_template", {"persons": persons})

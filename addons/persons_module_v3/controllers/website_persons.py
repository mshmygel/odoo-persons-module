from odoo import http
from odoo.http import request


class WebsitePersons(http.Controller):
    """
    Website controller responsible for rendering the list of persons
    on the public '/persons' webpage using QWeb template.
    """

    @http.route("/persons", type="http", auth="public", website=True)
    def persons_list(self, **kwargs):
        # Fetch the 5 most recently created person records (visible publicly)
        persons = (
            request.env["persons.person"].sudo().search([], limit=5, order="id desc")
        )
        # Render the QWeb template with the list of persons
        return request.render("persons_module_v3.person_template", {"persons": persons})

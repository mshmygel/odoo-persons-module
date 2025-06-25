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

    @http.route("/persons/new", type="http", auth="public", website=True)
    def person_form(self, **kwargs):
        # Render a blank HTML form for user to submit person data
        companies = request.env["res.company"].sudo().search([])
        return request.render("persons_module_v3.person_form_template", {"companies": companies})

    @http.route("/persons/create", type="http", auth="public", website=True, methods=["POST"], csrf=True)
    def person_create(self, **post):
        company_id = post.get("company_id")
        new_company_name = post.get("new_company")

        if not company_id and new_company_name:
            # Create new company if only new name provided
            company = request.env["res.company"].sudo().create({"name": new_company_name})
            company_id = company.id

        request.env["persons.person"].sudo().create({
            "first_name": post.get("first_name"),
            "last_name": post.get("last_name"),
            "birthday": post.get("birthday"),
            "sex": post.get("sex"),
            "company_id": int(company_id) if company_id else False,
        })
        return request.redirect("/persons")
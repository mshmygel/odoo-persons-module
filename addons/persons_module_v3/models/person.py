from odoo import models, fields, api
from datetime import date


class Person(models.Model):
    _name = "persons.person"
    _description = "Person"

    # Required text field
    first_name = fields.Char(required=True)

    # Required text field
    last_name = fields.Char(required=True)

    # Computed full name field
    full_name = fields.Char(compute="_compute_full_name", store=True)

    # Optional birth date field
    birthday = fields.Date()

    # Computed age field
    age = fields.Integer(compute="_compute_age", store=True)

    # Sex selection
    sex = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("non-binary", "Non-binary"),
        ],
        string="Sex"
    )

    # Required company reference, defaults to current user's company
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company
    )

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for rec in self:
            rec.full_name = f"{rec.first_name or ''} {rec.last_name or ''}".strip()

    @api.depends("birthday")
    def _compute_age(self):
        for rec in self:
            if rec.birthday:
                today = date.today()
                rec.age = (
                    today.year - rec.birthday.year
                    - ((today.month, today.day) < (rec.birthday.month, rec.birthday.day))
                )
            else:
                rec.age = 0

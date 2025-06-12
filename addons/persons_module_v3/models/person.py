from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date


class Person(models.Model):
    """
    Model for storing personal information of individuals,
    including name, birthday, gender, company, and age.
    """

    _name = "persons.person"
    _description = "Person"
    _order = "create_date desc"
    _rec_name = "full_name"

    first_name = fields.Char(string="First Name", required=True, size=50)
    last_name = fields.Char(string="Last Name", required=True, size=50)
    full_name = fields.Char(
        string="Full Name", compute="_compute_full_name", store=True
    )
    birthday = fields.Date(string="Birth Date")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    sex = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("non-binary", "Non-binary"),
        ],
        string="Gender",
    )
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        default=lambda self: self.env.company,
    )
    active = fields.Boolean(default=True)

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        """Concatenate first name and last name to form the full name."""
        for rec in self:
            rec.full_name = f"{rec.first_name or ''} {rec.last_name or ''}".strip()

    @api.depends("birthday")
    def _compute_age(self):
        """Calculate age from birth date."""
        for rec in self:
            if rec.birthday:
                today = date.today()
                rec.age = (
                    today.year
                    - rec.birthday.year
                    - (
                        (today.month, today.day)
                        < (rec.birthday.month, rec.birthday.day)
                    )
                )
            else:
                rec.age = 0

    @api.constrains("birthday")
    def _check_birthday(self):
        """Ensure that birth date is not in the future."""
        for rec in self:
            if rec.birthday and rec.birthday > date.today():
                raise ValidationError(_("Birth date cannot be in the future!"))

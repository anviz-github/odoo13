# Copyright 2019 Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Applicant  Validation",
    "summary": "Extends the functionality of Recruitment "
    "support a tier validation process.",
    "version": "13.0.1.0.0",
    "category": "HR",
    "website": "https://www.anviz.com",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": ["base", "hr",'hr_recruitment', "base_tier_validation"],
    "data": ["views/hr_applicant_view.xml"],
}

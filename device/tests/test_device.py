from odoo.tests.common import TransactionCase


class TestDevice(TransactionCase):
    def setUp(self, *args, **kwargs):
        result = super().setUp(*args, **kwargs)
        user_admin = self.env.ref(base.user_admin)
        self.env = self.env(user=user_admin)
        self.Server = self.env['Device.Server']
        self.server_ode = self.server.create({
            'name': 'Odoo Development Essentials',
            'server_id': '879-1-78439-279-6'})
        return result

    def test_create(self):
        "Test Books are active by default"
        self.assertEqual(self.server_ode.active, True)

    def test_check_server_id(self):
        "Check valid ISBN"
        self.assertTrue(self.server_ode._check_server_id)

    
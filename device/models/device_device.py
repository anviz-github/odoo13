from odoo import fields, models, api
import requests
from odoo import fields
import json
import sys
#if sys.__stdin__.isatty():
#    import pdb; pdb.set_trace()

class Device(models.Model):
    _name = 'device.device'
    _description = 'Device'
    name = fields.Char('Device Name', required=True)
    server_id = fields.Many2one('device.server', string='Server ID')
    device_id = fields.Char('Device ID')
    active = fields.Boolean('Active', default=True)
    platform = fields.Char()
    date_registed = fields.Date()
    device_key1 = fields.Char()
    device_key2 = fields.Char()
    device_key3 = fields.Char()
    device_key4 = fields.Char()
    device_key5 = fields.Char()
    restkeycount = fields.Integer()
    #_sql_constraints = [
    #   ('device_id', 'unique(device_id)', 'Device ID already exists!')
    #]
    _sql_constraints = [
        ('device_id', ' CHECK(1=1)', 'Device ID already exists!')
    ]
    #@api.constrains('device_id')
    #def _check_id(self):
    #    device_rec = self.env['device.device'].search(
    #        [('device_id', '=', self.device_id)])
    #    print('device_rec', device_rec.device_id)
    #    if device_rec:
    #       raise Warning(self.device_id,' Exists ! Already a id exists ')


    @staticmethod
    def get_key(request_device_id):
        if request_device_id=='':
            return 0
        host = "https://pro-device-auth.anvizsys.com:6062"


        client_key = '01673a2b-8522-3464-9977-54d9fab10718'
        client_secret = 'MgVciC6uFFNt2t6GBgkYdXhgFrvcovG8mp0Ym9J9Hlk='
        try:
            endpoint = r"/token"
            url = ''.join([host, endpoint])
            r1 = requests.post(url, data={'client_key': client_key, 'client_secret': client_secret})
            token = r1.json()['data']['token']
            #print('token', token)
            if token:
                endpoint = r"/service/auth"
                url = ''.join([host, endpoint])
                headers = {
                    'token': token,
                }
                body = {
                    "id": request_device_id,
                }
                try:

                    # r = requests.post(url,headers=headers,data=json.dumps(body))
                    r = requests.post(url, headers=headers, json=body)
                    #print('r.text', r.text)
                    #print('return', r.json()['code'])
                    if r.json()['code'] == 0:
                        return_data = r.json()['data']
                        #print(return_data)
                        return return_data
                    else:
                        return False
                except:
                    return False
            else:
                return False
        except:
            return False



    #@api.onchange('server_id', 'device_id')
    def _request_key(self, device,platform):
        #a20_id = '373734bb2920013106060809ffff0303'
        #print('device_id', device.device_id)
        #print('server_id', device.server_id.id)
        server = self.env['device.server'].search([('id', '=', device.server_id.id)])
        #print('server search return', server)
        #print('quota', server.server_quota)


        if server.server_quota>0 and server.platform == platform:

            return_data = Device.get_key(device.device_id)
            #print('return_data', return_data)
            if return_data == False:
                return False
            else:
                if 'key1'in return_data:
                    if return_data['key1']:
                        server.server_quota -= 1
                        device.device_key1 = str(return_data['key1'])
                        if return_data['platform'] == 'a20':

                            device.device_key2 = str(return_data['key2'])
                            device.device_key3 = str(return_data['key3'])
                            device.device_key4 = str(return_data['key4'])
                            device.device_key5 = str(return_data['key5'])

                    device.restkeycount = return_data['restKeyCount']
                    device.platform = return_data['platform']
                    return True

                else:
                    return False
    @api.model
    def create(self, vals):
        new_id = super(Device, self).create(vals)
        # print('created id', new_id)
        # #device = self.browse(new_id)
        # print('create id ', new_id)
        # print('device_id', new_id.device_id)
        if 'facepass' in new_id.device_id:
            platform = 'facepass'
        else:
            platform = 'a20'
        device_exist = self.env['device.device'].search([('id', '!=', new_id.id), ('device_id', '=', new_id.device_id)])
        if device_exist:
            #new_id.device_id = new_id.device_id + '_duplicate'
            return new_id
        else:
            return_key = self._request_key(new_id, platform)
            # print("retrun_key", return_key)

            if return_key:
                return new_id
            else:
                new_id.device_id = new_id.device_id + '_get_key_fail' + str(fields.Datetime.now())
                return new_id







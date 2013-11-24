import requests  # pip install requests


class TortoiseLabs():

    username = ""
    password = ""

    vps = None
    support = None
    billing = None
    dns = None

    def __init__(self, username, key):
        self.username = username
        self.password = key

        self.vps = VPS(self)
        self.support = Support(self)
        self.billing = Billing(self)
        self.dns = DNS(self)

    def send_request(self, file, params=None, method="GET", location="https://manage.tortois.es"):
        if method == "GET":
            r = requests.get(location + file, params=params, auth=(self.username, self.password))
        elif method == "POST":
            r = requests.post(location + file, data=params, auth=(self.username, self.password))
        data = r.json()
        return data


class API():
    tl = None

    def __init__(self, tl):
        self.tl = tl

    def get(self, file):
        return self.tl.send_request(file)

    def post(self, file, params):
        return self.tl.send_request(file, params, method="POST")


class VPS(API):
    def list_all(self):
        return self.get('/vps/list')
    def signup_available(self):
        return self.get('/vps/signup')
    def signup(self, plan, region):
        return self.post('/vps/signup', {'plan': plan, 'region': region})
    def info(self, id):
        return self.get('/vps/%s' % id)
    def deploy_templates(self, id):
        return self.get('/vps/%s/deploy' % id)
    def deploy(self, image, password, arch):
        return self.post('/vps/%s/deploy' % id, {'imagename': image, 'rootpass': password, 'arch': arch})
    def set_nickname(self, id, nickname):
        return self.post('/vps/%s/setnickname' % id, {'nickname': nickname})
    def monitoring_enable(self, id):
        return self.get('/vps/%s/monitoring/enable' % id)
    def monitoring_disable(self, id):
        return self.get('/vps/%s/monitoring/disable' % id)
    def hvm(self, id):
        return self.get('/vps/%s/hvm' % id)
    def hvm_set_iso(self, id, iso):
        return self.post('/vps/%s/hvm/setiso' % id, {'isoid': iso})
    def hvm_set_bootorder(self, id, bootorder):
        return self.post('/vps/%s/hvm/setbootorder' % id, {'bootorder': bootorder})
    def hvm_set_nic_type(self, id, nictype):
        return self.post('/vps/%s/hvm/setnictype' % id, {'nicktype': nictype})
    def hvm_new_iso(self, id, name, uri):
        return self.post('/vps/%s/hvmiso/new' % id, {'isoname':name, 'isouri': uri})
    def hvm_del_iso(self, id, isoid):
        return self.get('/vps/%s/hvmiso/%s/delete' % (id, isoid))
    def create(self, id):
        return self.get('/vps/%s/create' % id)
    def shutdown(self, id):
        return self.get('/vps/%s/shutdown' % id)
    def destroy(self, id):
        return self.get('/vps/%s/destroy' % id)
    def power_cycle(self, id):
        return self.get('/vps/%s/powercycle' % id)
    def status(self, id):
        return self.get('/vps/%s/status.json' % id)
    def jobs(self, id):
        return self.get('/vps/%s/jobs.json' % id)


class Support(API):
    def tickets(self):
        return self.get('/support/tickets')
    def ticket_new(self, subject, message):
        return self.post('/support/ticket/new', {'subject': subject, 'message': message})
    def ticket(self, id):
        return self.get('/support/ticket/%s' % id)
    def ticket_reply(self, id, message):
        return self.post('/support/ticket/%s' % id, {'message': message})
    def ticket_close(self, id):
        return self.get('/support/ticket/%s/close' % id)


class Billing(API):
    def invoice_list(self):
        return self.get('/invoice/list')
    def invoice(self, id):
        return self.get('/invoice/%s' % id)
    def add_credit(self, amount):
        return self.post('/invoice/svccredit', {'creditamt': amount})


class DNS(API):
    def zones(self):
        return self.get('/dns/zones')
    def zone(self, id):
        return self.get('/dns/zone/%s' % id)
    def zone_new(self, domain):
        return self.post('/dns/zone/new', {'domain_name': domain})
    def zone_delete(self, id):
        return self.get('/dns/zone/%s/delete' % id)
    def zone_new_record(self, id, subdomain, type="A", ttl=300, priority=0, content=""):
        return self.post('/dns/zone/%s/record/new' % id,
            {
                'subdomain': subdomain,
                'type': type,
                'ttl': ttl,
                'prio': priority,
                'content': content
            }
        )
    def zone_modify_record(self, id, record_id, subdomain, content):
        return self.post('/dns/zone/%s/record/%s' % (id, record_id),
            {
                'subdomain': subdomain,
                'content': content
            }
        )
    def zone_delete_record(self, id, record_id):
        return self.get('/dns/zone/%s/record/%s/delete' % (id, record_id))

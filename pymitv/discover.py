import requests
import socket

class Discover:
    def __init(self):
        pass

    def scan(self, stop_on_first=True, base_ip=0, speedy_gonzalez=False):
        tvs = []

        #Check if base_ip has been passed
        if(base_ip == 0):
            #Find IP address of computer pymitv is running on
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()

            # get my IP and compose a base like 192.168.1.xxx
            ip_parts = ip.split('.')
            base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2]
        else:
            base_ip = base_ip #just for clarity

        #Loop through every IP and check if TV is alive
        for ip_suffix in range(2, 256):
            ip_check = '{}.{}'.format(base_ip, ip_suffix)

            if(self.check_ip(ip_check, speedy_gonzalez)):
                tvs.append(ip_check)

                if(stop_on_first):
                    break

        return tvs

    def check_ip(self, ip, fast = False, log = False):
        if(log):
            print('Checking ip: {}...'.format(ip))

        #speeds up the check drastically, but comprosises accuracy on slow networks
        if(fast):
            request_timeout = 0.02
        else:
            request_timeout = 0.1

        try:
            r = requests.get('http://{}:6095/request?action=isalive'.format(ip), timeout=request_timeout)
        except ConnectionError:
            return False

        return r.status_code == 200

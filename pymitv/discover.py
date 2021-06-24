"""
The pymitv.Discover module is in charge of discovering local TVs.
"""
import socket
import requests


class Discover:
    """This class handles discovery and checking of local Xiaomi TVs"""

    def __init(self):
        pass

    def scan(self, stop_on_first=True, base_ip=0):
        """Scans the local network for TVs."""
        tvs = []

        # Check if base_ip has been passed
        if base_ip == 0:
            # Find IP address of computer pymitv is running on
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(("8.8.8.8", 80))
            ip_address = sock.getsockname()[0]
            sock.close()

            # Get IP and compose a base like 192.168.1.xxx
            ip_parts = ip_address.split('.')
            base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2]

        # Loop through every IP and check if TV is alive
        for ip_suffix in range(2, 256):
            ip_check = '{}.{}'.format(base_ip, ip_suffix)

            if self.check_ip(ip_check):
                tvs.append(ip_check)

                if stop_on_first:
                    break

        return tvs

    @staticmethod
    def check_ip(ip_address, log=False, request_timeout=0.1):
        """Attempts a connection to the TV and checks if there really is a TV."""
        if log:
            print('Checking ip: {}...'.format(ip_address))

        try:
            tv_url = 'http://{}:6095/request?action=isalive'.format(ip_address)
            request = requests.get(tv_url, timeout=request_timeout)
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError):
            return False

        return request.status_code == 200

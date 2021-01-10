import requests
import random
import string


class ShurjoPay(object):

    def __init__(self, merchant_name, merchant_pass, post_url, decrypt_url, merchant_prefix):
        self.merchantName = merchant_name
        self.merchantPass = merchant_pass
        self.post_url = post_url
        self.decrypt_url = decrypt_url
        self.merchantPrefix = merchant_prefix

    def send_request(self, client_ip, transaction_id, amount, return_url):
        xml = {
            "spdata": f'''<?xml version="1.0" encoding="utf-8"?><shurjoPay><merchantName>{self.merchantName}</merchantName><merchantPass>{self.merchantPass}</merchantPass><userIP>{client_ip}</userIP><uniqID>{transaction_id}</uniqID><totalAmount>{amount}</totalAmount><paymentOption>shurjopay</paymentOption><returnURL>{return_url}</returnURL></shurjoPay>'''}

        response = requests.post(self.post_url, data=xml)

        return response.text

    def get_decrypt(self, response_data):
        response_decrypt_data = requests.get(f"{self.decrypt_url}?data={response_data}")
        return response_decrypt_data

    def get_toast_data(self, data):
        toast_data = '''<script type="text/javascript">function showAndroidToast(){{'''+'''var toast={data}; Android.showToast(toast);}}'''.format(data=data)
        return toast_data


def get_random_string(string_length):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))

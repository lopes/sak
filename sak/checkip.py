from urllib.request import Request, urlopen
from urllib.parse import urlencode
from json import loads
from pprint import pprint


def abuseipdb(addr, key):
    base_url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {
        'Accept': 'application/json',
        'Key': key
    }
    params = {
        'ipAddress': addr,
        'maxAgeInDays': '90'
    }
    url = base_url + '?' + urlencode(params, doseq=True, safe="/")
    httprequest = Request(url, headers=headers, method='GET')
    with urlopen(httprequest) as httpresponse:
        raw = httpresponse.read().decode(httpresponse.headers.get_content_charset('utf-8'))
        raw_json = loads(raw)
        return {
            'status_code': httpresponse.status,
            'raw': raw,
            'address': raw_json['data']['ipAddress'],
            'country': raw_json['data']['countryCode'],
            'domain': raw_json['data']['domain'],
        }


def lookup(addr, engine, key):
    if engine == 'abuseipdb': data = abuseipdb(addr, key)
    pprint(data)

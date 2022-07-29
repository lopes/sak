# SOC Army Knife (SAK)
SOC Army Knife (SAK) is a small collection of tools for SOC engineers.  This project aims to create a small set of security-oriented tools to help SOC engineers.  It is not aimed to overlap any tool, such as VirusTotal CLI - refer to those specific projects if it's your case.  Also, it aims to use only the built-in functions in Python3, so no more dependencies will be required for it to run (sorry, `requests` :/).

## Usage
```python
sak.py --help
sak.py subnet 10.4.55.22/16
sak.py ioc -i malicious.txt
sak.py hash -i malicious.txt -a md5
sak.py checkip 1.1.1.1
```
# CloudFlair

CloudFlair is a tool to find origin servers of websites protected by CloudFlare who are publicly exposed and don't restrict network access to the CloudFlare IP ranges as they should.

The tool uses Internet-wide scan data from [Censys](https://censys.io) to find exposed IPv4 hosts presenting an SSL certificate associated with the target's domain name.

For more detail about this common misconfiguration and how CloudFlair works, refer to the companion blog post at https://blog.christophetd.fr/bypassing-cloudflare-using-internet-wide-scan-data/.

Here's what CloudFlair looks like in action.

```
$ python cloudflair.py myvulnerable.site

[*] The target appears to be behind CloudFlare.
[*] Looking for certificates matching "myvulnerable.site" using Censys
[*] 75 certificates matching "myvulnerable.site" found.
[*] Looking for IPv4 hosts presenting these certificates...
[*] 10 IPv4 hosts presenting a certificate issued to "myvulnerable.site" were found.
  - 51.194.77.1
  - 223.172.21.75
  - 18.136.111.24
  - 127.200.220.231
  - 177.67.208.72
  - 137.67.239.174
  - 182.102.141.194
  - 8.154.231.164
  - 37.184.84.44
  - 78.25.205.83

[*] Retrieving target homepage at https://myvulnerable.site

[*] Testing candidate origin servers
  - 51.194.77.1
  - 223.172.21.75
  - 18.136.111.24
        responded with an unexpected HTTP status code 404
  - 127.200.220.231
        timed out after 3 seconds
  - 177.67.208.72
  - 137.67.239.174
  - 182.102.141.194
  - 8.154.231.164
  - 37.184.84.44
  - 78.25.205.83

[*] Found 2 likely origin servers of myvulnerable.site!
  - 177.67.208.72 (HTML content identical to myvulnerable.site)
  - 182.102.141.194 (HTML content identical to myvulnerable.site)
```

(_The IP addresses in this example have been obfuscated and replaced by randomly generated IPs_)

## Setup

1) 
2) 


1) Clone the repository

```
$ git clone https://github.com/christophetd/cloudflair.git
```

2) Install the dependencies

```
$ cd CloudFlair
$ pip install -r requirements.txt
```
3) Register an account (free) on [Censys](https://censys.io/register)
4) Browse to [API](https://censys.io/account/api), and copy your API ID and API secret
5) Put your API_KEY and API_SECRET in config.ini file

6) Run CloudFlair (see [Usage](#usage) below for more detail)

```
$ python cloudflair.py myvulnerable.site
```

## Usage

```
$ python cloudflair.py --help

usage: cloudflair.py domain [-h] [-o OUTPUT_FILE]
positional arguments:
  domain                The domain to scan
optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FILE, --output OUTPUT_FILE
                        A file to output likely origin servers to (default:
                        None)
```

## Compatibility

Tested on Python 3.9. Feel free to [open an issue](https://github.com/0xRyuk/CloudFlair/issues/new) if you have bug reports or questions.

<b> Credits to <a href="https://github.com/christophetd"> christophetd</a> for the original code base this repository is based on at <a href="https://github.com/christophetd/CloudFlair">CloudFlair</a>
#!/usr/bin/env python3

import argparse
from lxml import html as lhtml
import requests
from urllib.parse import urlparse

def check_httpcreds(url):
    if not '://' in url[:10]:
        url = "http://" + url

    print("[*] Checking:", url)
    response = ''
    try:
        r = requests.get(url, allow_redirects=True)
        response = r.content
    except Exception as e:
        print("Coudln't request url: ", url, e)
        return

    urls = []
    try:
        tree = lhtml.fromstring(response)
        for query in ["//a[contains(@href, '@') and contains(@href, ':') and not(contains(@href, 'mailto:'))]", "//link[contains(@href, '@') and contains(@href, ':') and not(contains(@href, 'mailto:'))]", "//iframe[contains(@src, '@') and contains(@src, ':') and not(contains(@src, 'mailto:'))]", "//img[contains(@src, '@') and contains(@src, ':') and not(contains(@src, 'mailto:'))]", "//embed[contains(@src, '@') and contains(@src, ':') and not(contains(@src, 'mailto:'))]", "//audio[contains(@src, '@') and contains(@src, ':') and not(contains(@src, 'mailto:'))]", "//video[contains(@src, '@') and contains(@src, ':') and not(contains(@src, 'mailto:'))]", "//track[contains(@src, '@') and contains(@src, ':') and not(contains(@src, 'mailto:'))]", "//script[contains(@src, '@') and contains(@src, ':') and not(contains(@src, 'mailto:'))]", "//source[contains(@src, '@') and contains(@src, ':') and not(contains(@src, 'mailto:'))]"]:
            elems = tree.xpath(query)
            for element in elems:
                link = None
                try:
                    link = element.attrib['href']
                except Exception as e:
                    pass
                try:
                    link = element.attrib['src']
                except Exception as e:
                    pass
                if not link:
                    continue
                urls.append(link)
    except Exception as e:
        print("Coudln't parse html", url, e)
        return

    for url in urls:
        try:
            parsed = urlparse(url)
            if parsed.username and parsed.password:
                print("[+] Found:", url)
        except Exception as e:
            pass



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check a domain for leaking http credentials')
    parser.add_argument('-u', '--url', type=str, required=True, default="", help="Domain to scan")
    args = parser.parse_args()

    check_httpcreds(args.url)
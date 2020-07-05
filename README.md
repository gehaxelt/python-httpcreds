httpcreds
==================

This is a simple PoC tool to check a page for exposed http authentication credentials.

Usage and example:

```
$> python3 httpcreds.py -u https://uploads.blogbasis.net/test/
[*] Checking: https://uploads.blogbasis.net/test/
[+] Found: http://test:test@example.com
```

More information: https://0day.work/credentials-hiding-in-plain-sight-or-how-i-pwned-your-http-auth/
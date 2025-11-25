import urllib.request

try:
    resp = urllib.request.urlopen('http://127.0.0.1:5000/', timeout=10)
    print('Final URL:', resp.geturl())
    print('Status:', resp.status)
    data = resp.read(2000).decode('utf-8', errors='replace')
    print('\n--- Response snippet (first 2000 chars) ---\n')
    print(data[:2000])
except Exception as e:
    print('Error fetching root:', e)

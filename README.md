# bruteforcePy

# Brute Force Login Script

This is a Python script designed to perform a brute force login attack on a web page. It allows you to specify a target URL, a username, and a file containing a list of passwords. The script will make HTTP requests with different passwords until a successful login is found or all passwords have been tried.

## How It Works

1. The script takes the following inputs from the user:
    - Page URL: The URL of the target web page where the login is to be brute-forced.
    - Username: The username for the account you want to brute force.
    - Password File: A text file containing a list of passwords to try.
    - Login Failed String: A string that indicates a login failure on the target page.
    - Cookie Value (Optional): An optional cookie value to be sent with the requests.

2. It reads the list of passwords from the specified password file.

3. The script iterates through each password, making HTTP requests with the provided username and each password in the list.

4. If the login fails (as indicated by the "Login Failed String" not being found in the response), it moves on to the next password.

5. If a successful login is found, the script displays the username and password that worked and terminates.

6. If none of the passwords succeed, it displays a message indicating that the password was not found in the list.

## Usage

1. Clone this repository or download the script.

2. Make sure you have Python 3.x installed.

3. Install the required Python packages using pip: pip install requests termcolor

4. Run the script: python3 bruteForce.py

5. Follow the prompts to provide the necessary information (URL, username, password file, login failed string, and optional cookie value).

6. The script will attempt to brute force the login and display the results.


## License

This script is licensed under the [MIT License].

## Disclaimer


This script is for educational purposes only. Unauthorized use of this script for any malicious activities is prohibited. You should only use this script on systems and websites for which you have the necessary permissions.
Always ensure you have proper authorization before conducting any security testing on systems or networks you do not own or have explicit permission to test.
Please use this script responsibly and ensure that you have the right to test the target in question.

The authors and contributors of this script are not responsible for any misuse or legal consequences that may arise from its use.

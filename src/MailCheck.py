import requests

HEADERS = {
    "Cache-Control": "max-age=0",
    "Origin": "https://www.ultratools.com",
    "Upgrade-Insecure-Requests": "1"
}


def IsValidEmail(email):
    result = ""

    try:
        if email == "":
            return "InValid"

        url = f'https://www.ultratools.com/tools/emailTestResult?emailOrDomain={email}'
        req = requests.get(url, headers=HEADERS)
        content = req.text
        if "Success" in content:
            return "Valid"
        elif "RCPT TO failed" in content or "Connect failed" in content:
            return "InValid"
        else:
            return "Skip"

    except:
        result = "Skip"

    return result

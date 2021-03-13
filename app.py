import requests
import argparse
import config
import re

def get_api_key() -> str:
    try:
        with open(config.API_KEY_FILENAME) as f:
            key = f.readline()
    except FileNotFoundError:
        raise FileNotFoundError(f"{config.API_KEY_FILENAME} not found. Please create a file with the API key.")
    if len(key) == 0:
        raise ValueError(f"API key is empty. Please enter an API key into {config.API_KEY_FILENAME}")
    return key

def validate_mac(mac: str) -> None:
    if not re.match("[0-9a-f]{2}([:\.]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
        raise ValueError("Invalid MAC address. Wrong number of characters or bad delimiter.")

def get_company_name(mac: str) -> str:
    key = get_api_key()
    headers = {'X-Authentication-Token': key}
    params = {'search': mac}
    r = requests.get(config.API_URL, headers=headers, params=params)
    r.raise_for_status()
    return r.text


def format_name(name: str, raw: bool) -> str:
    if raw:
        return name
    if len(name) == 0:
        return "MAC address not found."
    return "Company name: " + name


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mac", help="get company name for MAC address, acceptable delimiters: ':', '.' or none.")
    parser.add_argument("-r", "--raw", help="output raw company name", action="store_true")
    args = parser.parse_args()

    validate_mac(args.mac)
    name = get_company_name(args.mac)
    print(format_name(name, args.raw))

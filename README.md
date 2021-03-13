# Cisco
Mini project for recruitment purposes. Queries the `macaddress.io` API and returns company name assigned to MAC address.

## Usage:
1. Go to the project root directory
1. Get API key from `https://macaddress.io/`
1. Create a file with the API key (default filename: api_key.txt)
2. Build the docker image:
    ```
    docker build . -t cisco
    ```
4. Run the image:
    ```
    docker run cisco [MAC address]
    ```

Example:
```
docker run cisco 44:38:39:ff:ef:56
```

For raw output, run:
```
docker run cisco -r [MAC address]
```

For help, run:
```
docker run cisco -h
```

## Security:
Don't add the API key to the repo.
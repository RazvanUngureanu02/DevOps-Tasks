```
# Linux Essentials – Task I

This folder contains a complete Bash script that automates all steps required in Task I of the DevOps Internship 2025 project.

## Contents

- `linux_essentials.sh` – Main Bash script to perform all actions
- `README.md` – This documentation file

## What the script does

The script handles all mandatory requirements and the bonus steps as well:

## Main Tasks:

1. Updates the system and installs necessary packages: `dnsutils`, `net-tools`, `nano`, `curl`, `netcat`, `nginx`
2. Performs a DNS lookup for `cloudflare.com` using `dig`
3. Maps the IP address `8.8.8.8` to the hostname `google-dns` by appending it to `/etc/hosts`
4. Verifies if DNS port 53 is open for `google-dns` using `netcat`
5. Changes the system DNS resolver to use Google DNS (`8.8.8.8`) in `/etc/resolv.conf`
6. Performs another lookup for `cloudflare.com` to ensure the new DNS is active
7. Starts the Nginx web server service
8. Displays all currently active listening ports (expecting Nginx on port 80)

## Bonus Implementations:

9. Changes Nginx's default listening port from `80` to `8080` in its configuration file
10. Restarts the Nginx service and verifies it is now listening on port `8080`
11. Modifies the default title in the Nginx welcome HTML page from `"Welcome to nginx!"` to `"I have completed the Linux part of the DevOps internship project"`
12. Uses `curl` to validate the title change by filtering the response for the `<title>` tag

## How to Use

> All steps must be executed inside an Ubuntu Docker container

### 1. Start an Ubuntu container:
```bash
docker run -it ubuntu
```

### 2. Create the script file inside the container:
```bash
nano linux_essentials.sh
```
Paste the full script content and save it with `CTRL + O`, press `Enter`, then exit with `CTRL + X`

### 3. Make the script executable:
```bash
chmod +x linux_essentials.sh
```

### 4. Run the script:
```bash
./linux_essentials.sh
```

## Output

If everything works correctly, the script will display messages confirming:
- DNS lookup success
- DNS port 53 is open
- Nginx is running and listening on port 8080
- Modified HTML title from the Nginx default page

You can then open your browser and navigate to:
```
http://localhost:8080
```
If port forwarding is properly configured, you should see the custom title displayed in the Nginx page.


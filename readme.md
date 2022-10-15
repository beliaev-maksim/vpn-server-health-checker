# System Monitor for IKEv2 VPN server

1. copy contents of the repo to `/home/beliaev/status_server`
2. run 
    ```
    python3.8 -m venv venv
    source venv/bin/activate
    pip install -r reqs.txt
    ```
3. copy `vpn-health.service` to `/etc/systemd/system/vpn-health.service`
4. run
    ```
    sudo systemctl start vpn-health
    sudo systemctl status vpn-health
    sudo systemctl enable vpn-health
    ```
5. do not forget to set port forwarding on the router to 8000
6. Now you can set rules on https://www.statuscake.com/ to monitor `<site_url>:8000/health`
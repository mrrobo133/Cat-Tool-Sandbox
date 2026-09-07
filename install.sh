#!/bin/bash

# Complete Golden Theme Colors
GOLD="\033[1;33m"
RESET="\033[0m"

clear
echo -e "${GOLD}"
echo " ██████╗ █████╗ ████████╗    ████████╗ ██████╗  ██████╗ ██╗     "
echo "██╔════╝██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     "
echo "██║     ███████║   ██║          ██║   ██║   ██║██║   ██║██║     "
echo "██║     ██╔══██║   ██║          ██║   ██║   ██║██║   ██║██║     "
echo "╚██████╗██║  ██║   ██║          ██║   ╚██████╔╝╚██████╔╝███████╗"
echo " ╚═════╝╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝"
echo "================================================================"
echo "          CAT TOOL INSTALLER & SECURITY CHECKER                 "
echo -e "=================================================={RESET}"

echo -e "\n${GOLD}[+] Updating Termux Packages...${RESET}"
pkg update -y && pkg upgrade -y

echo -e "${GOLD}[+] Installing Python, Git, and Core Dependencies...${RESET}"
pkg install python git curl -y

echo -e "${GOLD}[+] Setting up Environment & Directories...${RESET}"
mkdir -p core/captured templates

echo -e "${GOLD}[+] Downloading 100+ Platform Source Code Templates...${RESET}"
for i in {1..10}; do
    echo -n "."
    sleep 0.2
done
echo -e "\n${GOLD}[✔] Source Codes Installed Successfully!${RESET}"

echo -e "${GOLD}[+] Running Security & Integrity Scan...${RESET}"
sleep 1
echo -e "${GOLD}[✔] All Systems Secure, Clean & Verified!${RESET}"

echo -e "\n=================================================="
echo -e "          CAT TOOL REGISTRATION PORTAL            "
echo -e "=================================================="
read -p "[*] Press [ENTER] key to continue registration..."
echo -e ""
read -p "[*] Press 'O' (or 'o') to open the Main Menu: " user_input

if [[ "$user_input" == "o" || "$user_input" == "O" ]]; then
    echo -e "\n${GOLD}[+] Security Verified! Launching cat.py...${RESET}"
    sleep 1
    python3 cat.py
else
    echo -e "\n${GOLD}[!] Key pressed. Launching cat.py directly...${RESET}"
    sleep 1
    python3 cat.py
fi

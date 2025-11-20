import os
import subprocess
import sys


print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(" ____  ___   ____  ____   __   ____       _   __    __        ")
print("|_   ||_  \ |__  || __ | /  \ |_   |   __| | /  \  /  \  ____ ")
print(" / | | _|> | _/ / | |/ || |] | _< <   |__  || |] || |] ||  __|")
print("|/\__/|___/ |____|\___/  \__/ |____|     |_| \__/  \__/ |_|   ")
print("\n\n")
print("1) Nmap Automation scan")
print("2) Whois Lookup")

task1 = int(input("Enter task that you wanna do: "))

if task1 == 1:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("1) Quick Scan")
    print("2) Full Scan")
    nmap_task = int(input("Enter the type of scan you want to perform: "))
    if nmap_task == 1:
        parameters1 = "-sS -sV -O -T4 --open --reason --script vuln"
        ipordomain = input("Enter domain or IP: ")
        print(f"Performing full scan on {ipordomain}... with these parameters {parameters1}")
        print("")
        print(f"The resoult of {ipordomain} is saved in {ipordomain}_full_scan.txt")
    elif nmap_task == 2:
        parameters2 = "-p- -sS -sV -O -A -T4 --open --reason --script vuln"
        ipordomain = input("Enter domain or IP: ")
        print(f"Performing full scan on {ipordomain}... with these parameters {parameters2}")
        print("")
        print(f"The resoult of {ipordomain} is saved in {ipordomain}_full_scan.txt")
        
    else:
        print("Invalid input. Please enter 1 or 2.")
elif task1 == 2:
    print("\n\n")
    print("Whois Lookup")
    domain = input("Enter the domain name (e.g., example.com): ")
    print(f"Performing Whois lookup for {domain}...")
    try:
        domain_info = whois.whois(domain)
        print(domain_info)
    except Exception as e:
        print(f"An error occurred: {e}")

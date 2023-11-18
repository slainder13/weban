import os
import sys
sys.path.append('__init__')
import get_ip as ad
import file_mg as file
from art import *
from termcolor import colored

print(colored(text2art ("Weban"), 'cyan'))
print(colored('Created by slainder\n\n'.center(60),'red'))

def main():
    url =input("Entrer l'UR : ")
    path_dir ="reports/" + url
    file.create_dir(path_dir)
    ip = ad.get(url)
    print('L ip est :' ,ip)
    os.system('gnome-terminal -- bash -c "nmap -A '+ip+' -o '+path_dir+'/nmap.txt && bash"')
    os.system('gnome-terminal -- bash -c "nikto +h '+url+' -output '+path_dir+'/nikto.txt && bash"')
    os.system('gnome-terminal -- bash -c " __init__/dirsearch/dirsearch.py -u '+url+ ' -e * --simple-report='+path_dir+'/dirsearch.txt && bash"')
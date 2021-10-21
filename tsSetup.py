import os

os.system("mkdir ~/TSSERVER")
os.system("wget http://dl.4players.de/ts/releases/3.12.1/teamspeak3-server_linux_amd64-3.12.1.tar.bz2")
os.system("tar xvf teamspeak3-server_linux_amd64-3.12.1.tar.bz2")
os.system("cd teamspeak3-server_linux_amd64")
os.system("mv * ~/TSSERVER")
os.system("touch /home/teamspeak/.ts3server_license_accepted")
os.system("systemctl enable teamspeak.service")
os.system("systemctl start teamspeak.service")
os.system("systemctl | grep teamspeak.service")
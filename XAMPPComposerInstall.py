import os
x = ['sudo apt install php libapache2-mod-php php-mbstring php-xmlrpc php-soap php-gd php-xml php-cli php-zip', 'sudo apt install curl', 'curl -sS https://getcomposer.org/installer | php', 'sudo mv composer.phar /usr/local/bin/composer', 'sudo chmod +x /usr/local/bin/composer', 'source ~/.bashrc', 'wget https://www.apachefriends.org/xampp-files/8.1.2/xampp-linux-x64-8.1.2-0-installer.run', 'sudo chmod +x xampp-linux-x64-8.1.2-0-installer.run', 'sudo ./xampp-linux-x64-8.1.2-0-installer.run']
for c in x:
    os.system(c)
print('Installtion Complete!')

#!/bin/bash
#
# Ubuntu 14 LTS
#

set -v

sudo su -

nano squid.sh
 
chmod +x squid.sh 

apt-get -y update

apt-get install -y ntpdate
apt-get install -y squid3 apache2-utils

cp /etc/squid/squid.conf /etc/squid/squid.conf.bak

cat << EOF > /etc/squid/squid.conf
http_port 1052
http_access allow all
cache deny all
forwarded_for delete
request_header_access Via deny all
EOF

service squid restart

echo "IP ADDRESS"

curl ifconfig.co

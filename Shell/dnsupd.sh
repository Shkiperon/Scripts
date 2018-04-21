#!/bin/sh
#Script for updating DNS A-record on Netagels NS through API
{
#Base parameters
baseURL=https://panel.netangels.ru/api/v1/adnsrecord
appH=application/json
userDNS=NetAngelsUsername
passDNS=NetAngelsPassword

#Name parameters
ArecDNS=DNSrecordTypeA
NrecDNS=NumberOfDNSrecord

#Define IPs
currIP=$(nslookup myip.opendns.com resolver1.opendns.com | grep 'Address 1:' | awk -F': ' '{ print $2 }')
oldIP=$(nslookup $ArecDNS ns1.netangels.ru | grep 'Address 1:' | awk -F': ' '{ print $2 }')

#Compare and work
if [ "$currIP" = "$oldIP" ]
then
  echo "Nothing to do"
else
  date
  curl --dump-header - -X PUT -H "Content-Type: $appH" -H "Accept: $appH" -u "$userDNS:$passDNS" --data '{"ip": "'$currIP'"}' "$baseURL/$NrecDNS/"
  echo "-----------"
fi
} >> /root/dnsupd.log
if [ "$(wc -c /root/dnsupd.log | awk '{ print $1 }')" -gt 10000 ] 
then 
  if [ "$(find /root/ -name dnsupd.log_OLD | wc -l)" = "1" ]
  then
    rm /root/dnsupd.log_OLD
    mv /root/dnsupd.log /root/dnsupd.log_OLD
    touch /root/dnsupd.log
  else
    mv /root/dnsupd.log /root/dnsupd.log_OLD
    touch /root/dnsupd.log
  fi
fi

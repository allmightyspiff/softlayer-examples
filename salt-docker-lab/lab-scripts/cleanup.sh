NAME=`hostname -d | awk -F. '{print $1}'`
DOMAIN=`hostname -d`
echo "Removing sshkey"
sl sshkey remove  ${NAME} --really
echo "removing domain"
sl dns delete ${DOMAIN} --really

salt-key -D -y
rm -rf /etc/salt/minion_id
rm -f /root/.softlayer
rm -f /root/.ssh/id_rsa*
unset BASH_HISTORY



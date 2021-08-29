import json
import paramiko
import logging
import talib

host_ip = "0.0.0.0"
uname = "linuxuser"
pswd = "admin#123"

ssh_client = paramiko.SSHClient()
try:
    ssh_client.connect(host_ip, username=uname, password=pswd)
    #retrives cpu info
    stdin_cpu, stdout_cpu, stderr_cpu = client.exec_command("ps -A -o %cpu | awk '{s+=$1} END {print s "%"}'")
    #retrives interface names with associated ip address, can use sed to filter for specific output
    dtdin_host, stdout_host, stderr_host = client.exec_command("ifconfig -a")
    #retrives port and application separated by :
    stdin_port, stdout_port, stderr_port = client.exec_command("lsof -PiTCP -sTCP:LISTEN|awk '{print $1,$9}'")
   #returns list of ports and apps using them
    port_list = stdout_port.readline()
    interface_list = stdout_host.readline()
    ssh_client.close()
    hostinfo = {}
    hostinfo['cpu']  = stdout_cpu
    hostinfo['hostname'] = interface_list
    hostinfo['port'] = port_list
    json_out = json.dumps(hostinfo)
except Exception as e:
    logging.error(e)



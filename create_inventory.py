import subprocess

if __name__ == "__main__":
    ip = subprocess.check_output("cd tf/ && terraform output -raw instance_ip", shell=True)
    ip = str(ip.decode("utf-8"))
    s = f'[servers]\nbatashev_infra ansible_host={ip} ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/openstack'
    with open('ans/inventory', 'w') as f:
        f.write(s)
    with open('~/.instance_ip', 'w') as f:
        f.write(ip)

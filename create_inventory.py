import os

if __name__ == "__main__":
    ip = os.system("cd ~/tf_infra/tf/ && terraform output -raw instance_ip")
    s = f'[servers]\nbatashev_infra ansible_host={ip} ansible_user=ubuntu ansible_ssh_private_key_file=~/.ssh/openstack'
    with open('~//home/ubuntu/tf_infra/ans/inventory', 'w') as f:
        f.write(s)


## Installing Ansible on Centos

1. Update the system with the latest packages
``` sudo yum -y update ```

2. Install EPEL (Extra Packages for Enterprise Linux) repository. 
``` sudo yum -y install epel-repo ```

3. Update the repository cache
``` sudo yum -y update ```

4. Check Ansible Version
``` ansible --version ```

## Setup users for target nodes

1. Create a user to be used by Ansible for connecting to target nodes. These users need to be created in all the target nodes which we want to manage.
> useradd -m ansible

2. Provide sudo access to the user.
> echo "ansible ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

3. Generate ssh key for ansible user on the Control Node.
> ssh-keygen

4. Copy ssh ID to all the target nodes.
> ssh-copy-id target_node

5. Check if we are able to connect to Target Nodes from Control Node.
> ssh ansible@target_node

6. Check if ansible can connect to all the target nodes.
> ssh ansible@target_node

# 👏 ** Congratulations! ** You have installed Ansible and set it up to connect to target nodes. 🙌


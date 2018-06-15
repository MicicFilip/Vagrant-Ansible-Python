# Simple Vagrant/Ansible/Python Example

How to run the development environment:

1. `cd env && vagrant up` - Start the Vagrant virtual machine
2. `vagrant ssh` - Log in to the virtual machine
3. `sudo apt install python-pip` - Installs the pip module
4. `sudo pip install ansible` - Install Ansible
5. `ansible-playbook ~/simple_python_application/env/configure-vagrant.yml` - Run the configuration

The application should be available on [http://localhost:8080](http://127.0.0.1:8080)

## FAQ

#### Unsupported locale setting:

1. `export LC_ALL="en_US.UTF-8"`
2. `export LC_CTYPE="en_US.UTF-8"`
3. `sudo dpkg-reconfigure locales` - Than press Enter twice

#!/usr/bin/python
from fabric.api import sudo, run, env, cd

env.warn_only = True

def setup_nginx():
    git = run('rpm -qa | grep ^git')
    if git == '':
	sudo('yum install -y --nogpgcheck git')
    with cd ('/tmp'):
	run('git clone https://github.com/marshyski/nginxboss.git')
	sudo('puppet apply --modulepath=/tmp -e "include nginxboss"')
	sudo('rm -rf nginxboss')

import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
  os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_ssh_is_enabled(host):
  assert host.service('ssh').is_enabled

def test_ssh_is_running(host):
  assert host.service('ssh').is_running

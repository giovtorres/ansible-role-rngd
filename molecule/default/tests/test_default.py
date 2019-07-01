import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_rngd_package(host):
    assert host.package("rng-tools").is_installed


def test_rngd_service(host):
    h = host.service("rngd")
    assert h.is_running
    assert h.is_enabled


def test_rngd_systemd_file(host):
    if host.system_info.release.startswith("7"):
        assert host.file("/etc/systemd/system/rngd.service").is_file
        assert host.file("/etc/systemd/system/rngd.service").exists


def test_rngd_urandom(host):
    rngd = host.process.get(user="root", comm="rngd")
    assert "urandom" in rngd.args

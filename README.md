Ansible Role: rngd
==================

[![Build Status](https://travis-ci.org/giovtorres/ansible-role-rngd.svg?branch=master)](https://travis-ci.org/giovtorres/ansible-role-rngd)

Installs the random number generator daemon (rngd) on virtual guests to feed
random data from a device to the kernel entropy pool.

Supports EL6 and EL7.

Requirements
------------

None.

Role Variables
--------------

Enable or disable the rngd service:

    rngd_enabled: true

The device to use for randomness:

    rngd_device: /dev/urandom

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - ansible-role-rngd

License
-------

BSD

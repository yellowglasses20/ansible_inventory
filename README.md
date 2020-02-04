# ansible_inventory
create inventory file for ansible

## usage
```python
from dynamic_ansible_inventory import ansible_inventory

ai = ansible_inventory.ansible_inventory()
ai.add_section("test")
ai.set("test", "192.168.1.1", "ansible_ssh_user=root ansible_ssh_pass=hoge")
with open("/tmp/test", "w") as fp:
  ai.write(fp)
```

$ less /tmp/test
```ini

[test]
192.168.1.1 ansible_ssh_user=root ansible_ssh_pass=hoge
192.168.1.2 ansible_ssh_user=root ansible_ssh_pass=hoge
```

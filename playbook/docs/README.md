Для создания заданного плейбука выполним следующие шаги:

1. Создадим нового пользователя `cloudru` с паролем `cloudpass`.
2. Настроим авторизацию по ssh-ключу.
3. Запретим вход пользователя `root` через SSH.
4. Добавим предоставленный публичный ключ для пользователя `cloudru`.

Плейбук v1:

```yaml
---
- name: Configure server with user and ssh settings
  hosts: your_target_host
  become: yes
  tasks:
    - name: Ensure user cloudru exists
      user:
        name: cloudru
        password: "{{ 'cloudpass' | password_hash('sha512') }}"
        shell: /bin/bash
        create_home: yes
        state: present
      
    - name: Allow SSH key authorization
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PasswordAuthentication'
        line: 'PasswordAuthentication yes'
        state: present

    - name: Disallow root login via SSH
      lineinfile:
        path: /etc/ssh/sshd_config
        regexp: '^PermitRootLogin'
        line: 'PermitRootLogin no'
        state: present
      notify: restart sshd

    - name: Add provided public key for user cloudru
      authorized_key:
        user: cloudru
        state: present
        key: "{{ ssh_public_key }}"

  handlers:
    - name: restart sshd
      service:
        name: ssh
        state: restarted
```

Для корректной работы плейбука необходимо:

1. Заменить `your_target_host` на имя или IP-адрес целевого хоста, который вы хотите настроить.
Запуск playbook:
```bash
ansible-playbook -i inventory.ini playbook.yml --ask-vault-pass
```
> pass -testpassword

Тегирование задач в Ansible позволяет управлять выполнением отдельных задач при запуске плейбука с использованием флага `--tags` или `--skip-tags`.
Можно запускать определенные задачи, используя:
```bash
ansible-playbook -i inventory.ini playbook.yml --tags "user_creation,ssh_key"
```
Или исключать определенные задачи:
```bash
ansible-playbook -i inventory.ini playbook.yml --skip-tags "ssh_config"
```
Где `inventory.ini` - это файл инвентаризации Ansible, содержащий список хостов и `playbook.yml` - имя плейбука.

---
Inventory файл — это файл, в котором указываются хосты и группы хостов, с которыми работает Ansible. 
Файл `inventory.ini` выглядит так:
```ini
[cloudru_servers]
your_server_ip_or_hostname ansible_ssh_user=cloudru
```
Здесь:
- `my_servers` - это групповое имя.
- `your_server_ip_or_hostname` - это IP-адрес или имя хоста сервера.
- `ansible_ssh_user` - это имя пользователя, которое Ansible будет использовать для подключения к серверу. Обычно это `root` или другой пользователь с привилегиями `sudo`.

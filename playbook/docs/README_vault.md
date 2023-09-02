Зашифруем файл с помощью `ansible-vault`:

1. **Шифрование файла**:
```bash
ansible-vault encrypt playbook/roles/server_config/vars/main.yml
```
Указываем пароль. (testpassword)

2. **Использование зашифрованного файла**: При выполнении плейбука, который ссылается на зашифрованный файл, вы должны предоставить пароль для `ansible-vault`:
- Используя параметр `--ask-vault-pass`:
  ```bash
  ansible-playbook playbook.yml --ask-vault-pass
  ```

- Используя файл с паролем и указывая его через параметр `--vault-password-file`:
  ```bash
  ansible-playbook playbook.yml --vault-password-file=/.vault
  ```

3. **Дешифровка файла**: декодировать файл, выполните:
```bash
ansible-vault decrypt playbook/roles/server_config/vars/main.yml
```

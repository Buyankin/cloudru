Для установки Helm чарта:
```bash
helm install app-release /Users/buyankin/PycharmProjects/cloudru/helm/app
```

Переопределить значения по умолчанию из файла `values.yaml` использовать флаг `--set`:
```bash
helm install app-release /Users/buyankin/PycharmProjects/cloudru/helm/ap --set service.name=python-app-service-v2
```


```bash
helm install app ./app --debug --dry-run   
cd app
helm install app .
helm upgrade app .  
```
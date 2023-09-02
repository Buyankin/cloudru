#### Cоздать контекст кластера
```python
echo $KUBECONFIG
export KUBECONFIG=/Users/buyankin/.kube/config
```

**Запуск кластера**:
Если вы используете `minikube`, запустите его командой:
```bash
minikube start
```

**Применение манифестов**:
```bash
kubectl apply -f namespace.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

**Проверка**:
```bash
#Общая проверка
kubectl get pods,svc -n cloudru-namespace
```

1. Получить список всех подов в неймспейсе `cloudru-namespace`:

   ```bash
   kubectl get pods -n cloudru-namespace
   ```

   Найдити под и скопировать его имя.

2. Получить детальную информацию о выбранном поде в этом неймспейсе:

   ```bash
   kubectl describe pod [POD_NAME] -n cloudru-namespace
   ```

   Заменить `[POD_NAME]` на имя вашего пода.

3. В выводе команды `describe` раздел `Metadata:`. Там будет поле `UID`, которое будет содержать искомое значение.
```bash
kubectl get pod [POD_NAME] -n cloudru-namespace -o json | jq '.metadata.uid'
```
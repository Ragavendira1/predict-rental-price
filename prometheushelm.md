keypage:
https://artifacthub.io/packages/helm/prometheus-community/prometheus
# Install using Helm:
### Add Helm repo
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
### update helm repo
helm repo update

### Install Helm
helm install prometheus prometheus-community/prometheus

### Expose Prometheus Service

# Get the promethus server usrl by running these commenad in the same shell

``` sh  Get the Prometheus server URL by running these commands in the same shell:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=prometheus,app.kubernetes.io/instance=prometheus" -o jsonpath="{.items[0].metadata.name}")
  kubectl --namespace default port-forward $POD_NAME 9090 ```

# Get the PushGateway URL by running these commands in the same shell:
  ``` sh export POD_NAME=$(kubectl get pods --namespace default -l "app=prometheus-pushgateway,component=pushgateway" -o jsonpath="{.items[0].metadata.name}")
  kubectl --namespace default port-forward $POD_NAME 9091 ```

### Note:
kubectl get pods
kubectl exec -ti <<promotheus-pod>> -- sh 



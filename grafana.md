keypage:
https://artifacthub.io/packages/helm/grafana/grafana
# Install using Helm:
### Add Helm repo
helm repo add grafana https://grafana.github.io/helm-charts
### update helm repo
helm repo update

### Install Helm
helm install grafana grafana/grafana

### Expose Grafana Service


#### 1. Get your 'admin' user password by running:

   ``` sh kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo ```

#### 2. The Grafana server can be accessed via port 80 on the following DNS name from within your cluster:

     grafana.default.svc.cluster.local

   ### Get the Grafana URL to visit by running these commands in the same shell:
     ``` sh export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana" -o jsonpath="{.items[0].metadata.name}") ```
     ``` sh kubectl --namespace default port-forward $POD_NAME 3000 ```

### 3. Login with the password from step 1 and the username: admin
#################################################################################
######   WARNING: Persistence is disabled!!! You will lose your data when   #####
######            the Grafana pod is terminated.                            #####
#################################################################################


### Note:
kubectl get pods
kubectl exec -ti <<graphana-pod>> -- sh 
grafana-cli admin rest-admin-password <<New_password>>



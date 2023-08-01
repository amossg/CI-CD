#!/bin/bash

# Run Terraform output to get the values and store them in variables
db_public_ip=$(terraform output db_public_ip)
database_name=$(terraform output database_name)
db_user=$(terraform output db_user)
db_password=$(terraform output db_password)
# Add more variables for other outputs as needed

# Create the Kubernetes YAML file (e.g., configmap.yaml) with the variables
cat <<EOF > custom-resource.yaml
apiVersion: pgconn.flask.me/v1
kind: PgConn
metadata:
  name: flask-db-deployment
  namespace: default
spec:
  host: $db_public_ip
  database: $database_name
  username: $db_user
  password: $db_password
EOF

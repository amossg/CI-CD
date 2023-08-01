#!/bin/bash

# Run Terraform output to get the values and store them in variables
db_public_ip=$(terraform output db_public_ip)
database_name=$(terraform output database_name)
db_user=$(terraform output db_user)
db_password=$(terraform output db_password)
# Add more variables for other outputs as needed

cat <<EOF > secret.yaml
apiVersion: pgconn.flask.me/v1
kind: secret
metadata:
  name: flask-db-deployment
type: Opaque
stringData::
  host: $db_public_ip
  database: $database_name
  username: $db_user
  password: $db_password
EOF

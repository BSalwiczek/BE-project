mkdir cert
mkdir cert/localhost
openssl genrsa -out cert/CA.key -des3 2048
openssl req -x509 -sha256 -new -nodes -days 3650 -key cert/CA.key -out cert/CA.pem
touch cert/localhost/localhost.ext
cat <<EOT >> cert/localhost/localhost.ext
authorityKeyIdentifier = keyid,issuer
basicConstraints = CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = localhost
IP.1 = 127.0.0.1
EOT

openssl genrsa -out cert/localhost/localhost.key -des3 2048
openssl req -new -key cert/localhost/localhost.key -out cert/localhost/localhost.csr
openssl x509 -req -days 360 -in cert/localhost/localhost.csr -CA cert/CA.pem -CAkey cert/CA.key -CAcreateserial -out cert/localhost/localhost.crt

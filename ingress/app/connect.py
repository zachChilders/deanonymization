# Remove this connection string
import postgres
import os

connstring = os.environ["ingressconnectionstring"]

client = postgres.Postgres(connstring)
q = client.one("SELECT * FROM t1")
print(q)

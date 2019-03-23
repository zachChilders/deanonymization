import os
import postgres

connstring = os.environ["ingressconnectionstring"]
client = postgres.Postgres(connstring)
q = client.one("SELECT * FROM account;")
print(q)
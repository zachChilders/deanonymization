from os import environ
from os import listdir
from os.path import isfile, join

import base64
import requests

# Setup databricks auth
databricksToken = environ["databrickstoken"]
databricksAuthHeader = {"Authorization": f"Bearer {databricksToken}"}
databricksEndpoint = environ["databrickshost"]
databricksUri = f"{databricksEndpoint}/api/2.0/workspace/import"

# Read all notebooks
notebookPath = "."
notebooks = [f for f in listdir(notebookPath) if isfile(join(notebookPath, f))]

blacklist = ["validateScripts.r", "publishnotebooks.py"]
for notebook in notebooks:
    if notebook not in blacklist:
        # Convert to Base 64 for databricks API
        b64Script = ""
        with open(join(notebookPath, notebook), 'r') as content_file:
            content = content_file.read().encode()
            b64Script = base64.b64encode(content).decode('utf-8')

        # Build and send databricks request
        body = {
            "path":f"/Shared/MICS/{notebook}",
            "format":"SOURCE",
            "language":"R",
            "content":b64Script,
            "overwrite":"true"
        }
        # Fire and forget
        r = requests.post(databricksUri, json=body, headers=databricksAuthHeader)
#!/bin/bash

brew update && brew install azure-cli jq

az login

KEYVAULTNAME="mics-kv"
SECRETS=( $(az keyvault secret list --vault-name $KEYVAULTNAME | jq '.[].id' -r | sed 's/.*\/\([^/]\+\)$/\1/') )

for NAME in ${SECRETS[@]}; do
    SECRET=$(az keyvault secret show --name $NAME --vault-name $KEYVAULTNAME | jq '.value' -r)
    echo $NAME
    export $NAME=$SECRET
done
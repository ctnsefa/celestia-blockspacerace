# Celestia-Blockspacerace
## Description
Create a UI for allowing users to submit PayForBlob Transactions. You can check out the Node tutorial [here](https://docs.celestia.org/developers/node-tutorial/). It shows you how you can call the API in order to [submit a PFB transaction](https://docs.celestia.org/developers/node-tutorial/#submit-a-pfb-transaction), and how to [retrieve the data](https://docs.celestia.org/developers/node-tutorial/#get-namespaced-shares-by-block-height) by block height and namespace. <br/> <br/>
## Create a UI for allowing users to submit PayForBlob Transactions.
To perform the PayForBlob transaction, I prepared something like this. Let's see together. <br/> <br/>
#### For deploy the light-node automatically
```
wget -O auto-install-light-node.sh https://raw.githubusercontent.com/owlstake/celestia-race/main/deploy-light-node/auto-install-light-node.sh && chmod +x auto-install-light-node.sh && ./auto-install-light-node.sh
```
### How to work ?
#### 1-First of all, we go into the server where we set up the Celestia light node and stop the node. <br/> <br/>
`systemctl disable celestia-lightd` <br/>
`systemctl stop celestia-lightd` <br/> <br/>
#### 2- Create service <br/> <br/>
```
sudo tee <<EOF >/dev/null /etc/systemd/system/celestia-lightd.service
[Unit]
Description=celestia-lightd Light Node
After=network-online.target

[Service]
User=$USER
ExecStart=/usr/local/bin/celestia light start --core.ip https://api-blockspacerace.pops.one/ --core.rpc.port 26657 --core.grpc.port 9090 --keyring.accname my_celes_key --metrics.tls=false --metrics --metrics.endpoint otel.celestia.tools:4318 --gateway --gateway.addr 0.0.0.0 --gateway.port 26659 --p2p.network blockspacerace
Restart=on-failure
RestartSec=3
LimitNOFILE=4096

[Install]
WantedBy=multi-user.target
EOF
``` 
#### 3-Start node <br/> <br/>
`systemctl enable celestia-lightd` <br/>
`systemctl start celestia-lightd` <br/> <br/>
#### 4-Check logs <br/>
`journalctl -u celestia-lightd.service -f` <br/> <br/>
#### 5-Install Python and Flask <br/>
```
sudo apt install python3
pip install flask
```
#### 6-Create directories <br/>
```
mkdir pfb 
cd pfb 
mkdir templates 
cd 
mv app.py pfb/ 
mv index.html pfb/templates/
mv result.html pfb/templates/
```
## NOTE:File contents are shared in repo as open source.Please check. <br/> <br/>
#### 7-To start <br/>
```
cd pfb
python3 app.py
```
#### Start and use . As a result it will give you a demo website. Everything is ready ! <br/> <br/>
#### Don't forget to open the port! :26659 <br/> <br/>
# Web demo
- http://http://155.133.22.103:5001/ <br/> <br/>
## Enter the server ip <br/> <br/>
<img src="https://raw.githubusercontent.com/ctnsefa/celestia-blockspacerace/main/payforblab%20ui.png" width="auto"> <br/> <br/>
## Port :26659 <br/> <br/>
## And it should output this . <br/> <br/>
<img src="https://raw.githubusercontent.com/ctnsefa/celestia-blockspacerace/main/txhash.png" width="auto"> <br/> <br/>

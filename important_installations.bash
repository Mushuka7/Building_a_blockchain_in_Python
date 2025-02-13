$ pip install flask
$ pip install requests

Flask is a web framework that makes building web applications easy and rapid.

To get started, let’s create a text file named blockchain.py. At the top of this file, let’s import all the necessary libraries and modules:

import sys
import hashlib
import json
from time import time
from uuid import uuid4
from flask import Flask, jsonify, request
import requests
from urllib.parse import urlparse

To start the first node, type the following command in the terminal:
$ python blockchain.py 5000

Type the following command to view the content of the
blockchain running on the node:
$ curl http://localhost:5000/blockchain

To mine a block and see how it will affect the blockchain. Type the following
command in Terminal:
$ curl http://localhost:5000/mine

To issue the command that'll obtain the blockchain from the node:
$ curl http://localhost:5000/blockchain

Run the following command to mine the block:
$ curl http://localhost:5000/mine

Run the following command to examine the content of the blockchain by issuing this command:
$ curl http://localhost:5000/blockchain

In the Terminal that is running the blockchain.py application, press Ctrl+C to stop the
server. Type the following command to restart it:
$ python blockchain.py 5000

Now open another Terminal window and type the following command:
$ python blockchain.py 5001

To mine two blocks in the first node (5000) by typing the following commands in another Terminal window:
$ curl http://localhost:5000/mine
$ curl http://localhost:5000/blockchain
$ curl http://localhost:5001/blockchain

To tell the second node that there is a neighbor node, use the following command:
$ curl -H "Content-type: application/json" -d '{"nodes" :
["http://127.0.0.1:5000"]}' -X POST http://localhost:5001/nodes/add_nodes

To tell the first node that there is a neighbor node, use the following command:
$ curl -H "Content-type: application/json" -d '{"nodes" :
["http://127.0.0.1:5001"]}' -X POST http://localhost:5000/nodes/add_nodes

Now to try and synchronize the blockchain starting from the first node:
$ curl http://localhost:5000/nodes/sync

Now to synchronize from the second node:
$ curl http://localhost:5001/nodes/sync



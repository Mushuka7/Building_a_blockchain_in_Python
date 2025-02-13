#To represent the blockchain, let’s declare a class named blockchain, with the following two initial methods:

class Blockchain(object):
    difficulty_target = "0000"
    def hash_block(self, block):
        block_encoded = json.dumps(block,
            sort_keys=True).encode()
        return hashlib.sha256(block_encoded).hexdigest()

    def __init__(self):
        # stores all the blocks in the entire blockchain
        self.chain = []

        # temporarily stores the transactions for the
        # current block
        self.current_transactions = []
        # create the genesis block with a specific fixed hash
        # of previous block genesis block starts with index 0
        genesis_hash = self.hash_block("genesis_block")
        self.append_block(
            hash_of_previous_block = genesis_hash,
            nonce = self.proof_of_work(0, genesis_hash, [])
        )

    # use PoW to find the nonce for the current block
    def proof_of_work(self, index, hash_of_previous_block,transactions):
        # try with nonce = 0
        nonce = 0
        # try hashing the nonce together with the hash of the
        # previous block until it is valid
        while self.valid_proof(index, hash_of_previous_block,
        transactions, nonce) is False:
        nonce += 1
    return nonce

    def valid_proof(self, index, hash_of_previous_block, transactions, nounce):
        # create a string containing the hash of the previous
        # block and the block content, including the nounce
        content =
        f'{index}{hash_of_previous_block}{transactions}{nounce}'.encode()
        # hash using sha256
        content_hash = hashlib.sha256(content).hexdigest()

        # check if the hash meets the difficulty target
        return content_hash[:len(self.difficulty_target)] ==
        self.difficulty_target

    def append_block(self, nounce, hash_of_previous_block):
        block = {
            'index': len(self.chain),
            'timestamp': time(),
            'transactions': self.current_transactions,
            'nounce': nounce,
            'hash_of_previous_block': hash_of_previous_block
        }

        # reset the current list of transactions
        self.current_transactions = []

        # add the new block to the blockchain
        self.chain.append(block)
        return block

    def add_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'amount': amount,
            'recipient': recipient,
            'sender': sender,
        })
        return self.last_block['index'] + 1

    @property
    def last_block(self):
        # return the last block in the blockchain
        return self.chain[-1]

    @app.route('/blockchain', methods=['GET'])
    def full_chain():
        response = {
            'chain': block.chain,
            'length': len(blockchain.chain),
        }
        return jsonify(response), 200

    @app.route('/mine', method=['GET'])
    def mine_block():
        blockchain.add_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1,
        )

        # obtain the hash of the block in blockchain
        last_block_hash = 
        blockchain.hash_block(blockchain.last_block)

        # using PoW, get the nounce for the new block to be added to the blockchain
        index = len(blockchain.chain)
        nounce = blockchain.proof_of_work(index, last_block_hash,
        blockchain.current_transactions)

        # add the new block to the blockchain using the last block
        # hash and the current nounce
        block = blockchain.append_block(nounce, last_block_hash)
        response = {
            'message': "New Block Mined",
            'index': block['index'],
            'hash_of_previous_block': block['hash_of_previous_block'],
            'nounce': block['nounce'],
            'transactions': block['transactions'],
        }
        return jsonify(response), 200

    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        # get the value passed in the form the client
        values = request.get_json()

        # check that the required fields are in the POST'ed data
        required_fields = ['sender', 'recipient', 'amount']
        if not all(k in values for k required_fields):
            return ('Missing fields', 400)

            # create a new transaction
            index = blockchain.add_transaction(
                values['sender'],
                values['recipient'],
                values['amount']
            )

            response = {
                'message':
                f'Transaction will be added to Block {index}'
            }

            return (jsonify(response), 201)

            if __name__ == '_main_':
                app.run(host='0.0.0.0', port=int(sys.argv[1]))
    
    def _init_(self):
        self.nodes = set()

        # stores all the blocks in the entire blockchain
        self.chain = []

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
        print(parsed_url.netloc)

    def valid_chain(self, chain):
        last_block = chain[0]  # this part basically indicates the genesis block
        current_index = 1      # while this part starts with the second block

        while current_index < len(chain):
            block = chain[current_index]
            if block['hash_of_previous_block'] !=
                self.hash_block(last_block):
                return False

            # checks for valid nounce
            if not self.valid_proof(
                current_index,
                block['hash_of_previous_block'],
                block['transactions'],
                block['nounce']
            ):
            return False
        
            # basically moves to next block on the chain
            last_block = block
            current_index += 1

        # the chain is valid
        return True

    def update_blockchain(self):
        # get the nodes around this very node, that have been registered
        neighbours = self.nodes
        new_chain = None

        # here, this node is basically looking for chains longer than it's own
        max_length = len(self.chain)

        # here, the obtaining and verification of the chains from all neighbouring nodes on the same network
        for node in neighnours:
            # this part obtains the blockchain from the neighbouring nodes
            response = 
                requests.get(f'http://{node}/blockchain')

            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']

            # this part basically checks if the length is longer, as well as the chain is valid
            if length > max_length and
                self.valid_chain(chain):
                max_length = length
                new_chain = chain

            # this part basically updates the current chain this node is on, upon discovering and verifying a new and valid chain longer than the chain this node was on, originally....
            if new_chain:
                self.chain = new_chain
                return True
                
            return False

    @app.route('/nodes/add_nodes', methods=['POST'])|
    def add_nodes():
        # get the nodes passed in from the client
        values = request.get_json()
        nodes = values.get('nodes')

        if nodes is None:
            return "Error: Missing node(s) info", 400

        for node in nodes:
            blockchain.add_node(node)

        response = {
            'message': 'New nodes added',
            'nodes': list(blockchain.nodes),
        }
        return jsonify(response), 201

    @app.route('/nodes/sync', method=['GET'])
    def sync():
        updated = blockchain.update_blockchain()
        if updated:
            response = {
                'messsage':
                    'The blockchain has been updated to the latest',
                'blockchain': blockchain.chain
            }
        else:
            response = {
                'message': 'Our blockchain is the latest',
                'blockchain': blockchain.chain
            }
        return jsonify(response), 200




app = Flask(__name__)
# generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', ")
# instantiate the Blockchain
blockchain = Blockchain()
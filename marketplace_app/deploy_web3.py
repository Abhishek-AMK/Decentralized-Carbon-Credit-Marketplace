
import json
import os
from web3 import Web3
from eth_account import Account

# Hardhat Account #0
PRIV_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
RPC_URL = "http://127.0.0.1:8545"

def deploy():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("Cannot connect to node")
        return

    account = Account.from_key(PRIV_KEY)
    w3.eth.default_account = account.address
    print(f"Deploying from {account.address}")

    # Load build artifacts
    # Path relative to marketplace_app/ assuming running from root or subdir?
    # I'll specify absolute path or relative to project root
    with open("contracts/.build/__local__.json", "r") as f:
        data = json.load(f)
    
    # helper to deploy
    def deploy_contract(name, args=[]):
        contract_data = data["contractTypes"][name]
        abi = contract_data["abi"]
        bytecode = contract_data["deploymentBytecode"]["bytecode"]
        
        Contract = w3.eth.contract(abi=abi, bytecode=bytecode)
        
        # Build transaction
        construct_txn = Contract.constructor(*args).build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 5000000,
            'gasPrice': w3.eth.gas_price
        })
        
        # Sign
        signed = w3.eth.account.sign_transaction(construct_txn, private_key=PRIV_KEY)
        
        # Send
        tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
        print(f"Sent {name} deployment tx: {tx_hash.hex()}")
        
        # Wait for receipt
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(f"Deployed {name} at {tx_receipt.contractAddress}")
        return tx_receipt.contractAddress, w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

    # Deploy CarbonCredit
    cc_address, cc_contract = deploy_contract("CarbonCredit")
    
    # Deploy Marketplace
    mp_address, mp_contract = deploy_contract("Marketplace")

    # Mint Data (Setup)
    print("Minting tokens...")
    # Mint 100 type 1, 50 type 2
    # mint(account, id, amount, data)
    # Using build_transaction for function calls too
    
    def send_tx(func):
        tx = func.build_transaction({
            'from': account.address,
            'nonce': w3.eth.get_transaction_count(account.address),
            'gas': 500000,
            'gasPrice': w3.eth.gas_price
        })
        signed = w3.eth.account.sign_transaction(tx, private_key=PRIV_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed.raw_transaction)
        return w3.eth.wait_for_transaction_receipt(tx_hash)

    send_tx(cc_contract.functions.mint(account.address, 1, 1000, b""))
    send_tx(cc_contract.functions.mint(account.address, 2, 500, b""))

    # Approve Marketplace
    print("Approving marketplace...")
    send_tx(cc_contract.functions.setApprovalForAll(mp_address, True))

    # List
    print("Listing tokens...")
    # listToken(tokenContract, tokenId, amount, price)
    price = w3.to_wei(0.01, 'ether')
    send_tx(mp_contract.functions.listToken(cc_address, 1, 100, price))
    send_tx(mp_contract.functions.listToken(cc_address, 2, 50, price))

    print("Setup Complete.")
    print(f"CC_ADDRESS = '{cc_address}'")
    print(f"MP_ADDRESS = '{mp_address}'")

if __name__ == "__main__":
    deploy()

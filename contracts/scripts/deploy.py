from ape import accounts, project

def main():
    # Load account (using test account 0)
    deployer = accounts.test_accounts[0]
    
    print("Deploying contracts...")
    carbon_credit = deployer.deploy(project.CarbonCredit)
    marketplace = deployer.deploy(project.Marketplace)
    
    print(f"CarbonCredit deployed to: {carbon_credit.address}")
    print(f"Marketplace deployed to: {marketplace.address}")
    
    # Mint some credits to deployer
    print("Minting initial credits...")
    carbon_credit.mint(deployer, 1, 1000, b"", sender=deployer)
    carbon_credit.mint(deployer, 2, 500, b"", sender=deployer)
    
    # Approve marketplace
    carbon_credit.setApprovalForAll(marketplace.address, True, sender=deployer)
    
    # List them
    print("Creating initial listings...")
    price = "0.01 ether"
    marketplace.listToken(carbon_credit.address, 1, 100, price, sender=deployer)
    marketplace.listToken(carbon_credit.address, 2, 50, price, sender=deployer)
    
    print("Deployment complete!")

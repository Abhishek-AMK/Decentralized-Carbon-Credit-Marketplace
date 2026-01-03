
import reflex as rx
from web3 import Web3
from .constants import CC_ADDRESS, MP_ADDRESS, RPC_URL
from .abi import MARKETPLACE_ABI

class Listing(rx.Base):
    listing_id: int
    seller: str
    token_contract: str
    token_id: int
    amount: int
    price: str
    price_wei: int
    active: bool
    # Domain fields for PS3
    category: str = "Renewable"
    location: str = "Global"
    is_verra: bool = True
    sdgs: list[int] = [13]

class State(rx.State):
    listings: list[Listing] = []
    connected_address: str = ""
    has_listings: bool = False

    def fetch_listings(self):
        w3 = Web3(Web3.HTTPProvider(RPC_URL))
        mp = w3.eth.contract(address=MP_ADDRESS, abi=MARKETPLACE_ABI)
        
        try:
            total = mp.functions.nextListingId().call()
        except Exception as e:
            print(f"Error fetching listings: {e}")
            total = 0
            
        project_data = {
            1: {"cat": "Forestry", "loc": "Amazon, Brazil", "verra": True, "sdgs": [13, 15]},
            2: {"cat": "Wind Power", "loc": "Gujarat, India", "verra": True, "sdgs": [7, 13]},
            3: {"cat": "Solar Energy", "loc": "Mojave, USA", "verra": False, "sdgs": [7, 9, 13]},
        }
            
        new_listings = []
        for i in range(total):
            try:
                raw = mp.functions.listings(i).call()
                token_id = raw[3]
                p_info = project_data.get(token_id, {"cat": "Renewable", "loc": "International", "verra": True, "sdgs": [13]})
                
                l = Listing(
                    listing_id=raw[0],
                    seller=raw[1],
                    token_contract=raw[2],
                    token_id=token_id,
                    amount=raw[4],
                    price=f"{Web3.from_wei(raw[5], 'ether')} ETH",
                    price_wei=raw[5],
                    active=raw[6],
                    category=p_info["cat"],
                    location=p_info["loc"],
                    is_verra=p_info["verra"],
                    sdgs=p_info["sdgs"]
                )
                if l.active and l.amount > 0:
                    new_listings.append(l)
            except Exception as e:
                print(f"Error parsing listing {i}: {e}")
                
        self.listings = new_listings
        self.has_listings = len(new_listings) > 0

    def connect_wallet(self):
        return rx.call_script(
            "window.connectWallet().then((address) => { if(address) { server.processEvent('set_address', [address]) } })"
        )

    def set_address(self, address: str):
        self.connected_address = address
    
    def buy_item(self, listing_id: int, price_wei: int, amount: int = 1):
        # We buy 1 unit for the MVP demo to keep it simple, or full amount?
        # Let's assume buying 1 unit for now or full amount? 
        # The contract buyToken takes (listingId, amountToBuy).
        # We need to calculate correct value: price per unit * amount.
        # Wait, the contract listing has a 'price' field. Is it price per unit or total?
        # Usually price per unit.
        # Let's pass the price_wei (per unit) * amount as value.
        
        # JS Function signature: buyListing(listingId, priceWei, amount)
        # Note: priceWei in JS call should be total value required?
        # Contract: buyToken(id, amount) -> require msg.value == listing.price * amount
        # So in JS we need to send value = price * amount.
        
        # For this MVP, let's just buy 1 unit to simplify the UI flow (no quantity selector implemented yet).
        total_value = price_wei * 1 
        return rx.call_script(f"window.buyListing({listing_id}, '{total_value}', 1)")


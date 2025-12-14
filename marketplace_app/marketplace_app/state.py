
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
    price: str  # Display string
    active: bool

class State(rx.State):
    listings: list[Listing] = []
    
    def fetch_listings(self):
        w3 = Web3(Web3.HTTPProvider(RPC_URL))
        mp = w3.eth.contract(address=MP_ADDRESS, abi=MARKETPLACE_ABI)
        
        try:
            total = mp.functions.nextListingId().call()
        except:
            total = 0
            
        new_listings = []
        for i in range(total):
            # struct Listing: listingId, seller, tokenContract, tokenId, amount, price, active
            raw = mp.functions.listings(i).call()
            # raw is tuple
            l = Listing(
                listing_id=raw[0],
                seller=raw[1],
                token_contract=raw[2],
                token_id=raw[3],
                amount=raw[4],
                price=str(Web3.from_wei(raw[5], 'ether')) + " ETH",
                active=raw[6]
            )
            if l.active:
                new_listings.append(l)
                
        self.listings = new_listings

    def buy_item(self, listing_id: int):
        # NOTE: In a real app, this should trigger a wallet popup on Client Side.
        # Reflex runs on server. We can't sign for the user.
        # For this MVP, we will show a toast that "Client-side signing not implemented in MVP python backend".
        # OR we could implement a burner wallet integration.
        # We'll show a message instructing user what to do or just mock success if we had a burner.
        return rx.window_alert(f"Please use a Web3 wallet to buy listing {listing_id}. (Client-side integration required)")

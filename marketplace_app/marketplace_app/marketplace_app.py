
import reflex as rx
from .state import State, Listing

def navbar():
    return rx.flex(
        rx.heading("CarbonMarket", size="5"),
        rx.spacer(),
        rx.button("Connect Wallet", variant="outline"),
        width="100%",
        padding="1em",
        border_bottom="1px solid #eaeaea",
        align="center"
    )

def hero():
    return rx.center(
        rx.vstack(
            rx.heading("Decentralized Carbon Credit Marketplace", size="9", text_align="center"),
            rx.text(
                "Buy, trade, and retire verifiably climate-positive credits.",
                size="5",
                color="gray",
                text_align="center"
            ),
            padding_y="4em"
        )
    )

def listing_card(listing: Listing):
    return rx.card(
        rx.vstack(
            rx.heading(f"Token #{listing.token_id}", size="4"),
            rx.text(f"Amount: {listing.amount}"),
            rx.text(f"Price: {listing.price}", font_weight="bold"),
            rx.text(f"Seller: {listing.seller[:6]}...{listing.seller[-4:]}", font_size="0.8em", color="gray"),
            rx.button("Buy Now", on_click=lambda: State.buy_item(listing.listing_id), width="100%"),
            spacing="2"
        ),
        width="100%"
    )

def index():
    return rx.container(
        navbar(),
        hero(),
        rx.heading("Active Listings", size="6", margin_bottom="1em"),
        rx.grid(
            rx.foreach(State.listings, listing_card),
            columns="3",
            spacing="4",
            width="100%"
        ),
        padding="2em",
        # Load data on mount
        on_mount=State.fetch_listings
    )

app = rx.App()
app.add_page(index)

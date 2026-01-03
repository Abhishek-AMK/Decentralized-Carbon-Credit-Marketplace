
import reflex as rx
from .state import State, Listing

# Theme Constants
ACCENT = "#08F7A3"
BACKGROUND = "#030915"
CARD_BG = "rgba(255, 255, 255, 0.04)"
BORDER_COLOR = "rgba(255, 255, 255, 0.12)"
TEXT_MUTED = "rgba(255, 255, 255, 0.70)"
GLASS_SHADOW = "0 25px 70px rgba(0, 0, 0, 0.45)"
SDG_COLORS = {
    7: "#FDB713",
    9: "#F36D25",
    13: "#3F7E44",
    15: "#56C02B",
}

def sdg_badge(sdg_id: int) -> rx.Component:
    color = SDG_COLORS.get(sdg_id, ACCENT)
    return rx.box(
        rx.text(f"SDG {sdg_id}", font_size="0.65rem", font_weight="800", color="white"),
        padding_x="0.5rem",
        padding_y="0.2rem",
        border_radius="4px",
        background=color,
        display="inline-block",
        margin_right="0.3rem",
    )

def nav_link(label: str) -> rx.Component:
    return rx.link(
        label,
        href="#",
        font_size="0.95rem",
        color=TEXT_MUTED,
        font_weight="500",
        _hover={"color": "white"},
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.box(
                    "CM",
                    font_weight="800",
                    color="#02070F",
                    background=ACCENT,
                    border_radius="10px",
                    padding_x="0.65rem",
                    padding_y="0.35rem",
                ),
                rx.text("CarbonMarket", font_weight="700", font_size="1.2rem"),
                spacing="3",
                align_items="center",
            ),
            rx.spacer(),
            rx.hstack(*(nav_link(label) for label in ["Marketplace", "Projects", "Impact", "Docs"]), spacing="5"),
            rx.cond(
                State.connected_address == "",
                rx.button(
                    "Connect Wallet",
                    on_click=State.connect_wallet,
                    bg=ACCENT,
                    color="#02070F",
                    font_weight="700",
                    size="3",
                    border_radius="full",
                    padding_x="1.5rem",
                    _hover={"opacity": 0.9},
                    cursor="pointer"
                ),
                rx.badge(
                    State.connected_address[:6] + "..." + State.connected_address[-4:],
                    color_scheme="green",
                    variant="soft",
                    size="3",
                    padding_x="1em",
                    border_radius="full"
                )
            ),
            spacing="5",
            align_items="center",
        ),
        width="100%",
        padding_x=["1.25rem", "2rem", "3rem"],
        padding_y="1.5rem",
        position="sticky",
        top="0",
        z_index="10",
        background="rgba(3, 9, 21, 0.95)",
        border_bottom=f"1px solid {BORDER_COLOR}",
        backdrop_filter="blur(16px)",
    )

def stat_card(value: str, label: str, detail: str) -> rx.Component:
    return rx.box(
        rx.text(value, font_size="2rem", font_weight="800", color="white"),
        rx.text(label, color=TEXT_MUTED, font_size="0.95rem"),
        rx.text(detail, color="rgba(255, 255, 255, 0.5)", font_size="0.85rem", margin_top="0.5em"),
        padding="1.25rem",
        border_radius="18px",
        border=f"1px solid {BORDER_COLOR}",
        background="rgba(255, 255, 255, 0.02)",
    )

def hero() -> rx.Component:
    stats = [
        ("1.2M", "tCO₂ tokenized", "+18% MoM"),
        ("86", "Project partners", "Across 23 countries"),
        ("$42.8M", "Capital unlocked", "Real-time settlement"),
    ]

    return rx.box(
        rx.vstack(
            rx.badge(
                "Live net-zero infrastructure",
                color_scheme="green",
                variant="outline",
                radius="full",
                padding_x="1rem",
                padding_y="0.35rem",
                color=ACCENT,
                border_color=ACCENT,
            ),
            rx.heading(
                "Trade verifiable carbon credits with cinematic clarity.",
                size="9",
                text_align="center",
                max_width="55rem",
                color="white",
                line_height="1.1",
            ),
            rx.text(
                "Discover high-impact climate projects, assess trust signals instantly, "
                "and retire assets in a few taps with on-chain transparency.",
                font_size="1.2rem",
                text_align="center",
                color=TEXT_MUTED,
                max_width="45rem",
                margin_y="1.5rem",
            ),
            rx.hstack(
                rx.button(
                    "Launch marketplace",
                    size="4",
                    bg=ACCENT,
                    color="#02070F",
                    font_weight="700",
                    radius="full",
                    padding_x="2.5rem",
                    cursor="pointer",
                    box_shadow=f"0 0 20px {ACCENT}40",
                ),
                rx.button(
                    "View methodology",
                    size="4",
                    variant="outline",
                    color="white",
                    radius="full",
                    padding_x="2.5rem",
                    cursor="pointer",
                ),
                spacing="4",
                justify="center",
                margin_bottom="4rem",
            ),
            rx.grid(
                *[stat_card(v, l, d) for v, l, d in stats],
                columns="3",
                spacing="4",
                width="100%",
            ),
            spacing="4",
            align_items="center",
        ),
        padding="4rem",
        background="radial-gradient(circle at top left, rgba(22, 255, 182, 0.15), transparent 40%), "
                   "radial-gradient(circle at bottom right, rgba(0, 153, 255, 0.1), transparent 45%)",
        border_radius="32px",
        border=f"1px solid {BORDER_COLOR}",
        box_shadow=GLASS_SHADOW,
        width="100%",
    )

def listing_card(listing: Listing) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.text(listing.category.upper(), font_size="0.65rem", font_weight="900", color="#02070F"),
                    background=ACCENT,
                    padding_x="0.6rem",
                    padding_y="0.2rem",
                    radius="full",
                    clip_path="polygon(0 0, 100% 0, 85% 100%, 0 100%)",
                ),
                rx.spacer(),
                rx.cond(
                    listing.is_verra,
                    rx.badge("VERRA ✅", color_scheme="blue", variant="solid", radius="full", size="1"),
                ),
                width="100%",
                align_items="center",
            ),
            
            rx.box(
                rx.heading(f"{listing.amount} Credits", size="6", color="white", margin_top="0.5rem"),
                rx.text(listing.location, color=TEXT_MUTED, font_size="0.85rem"),
                width="100%",
            ),

            rx.divider(margin_y="0.8em", opacity="0.1"),

            rx.hstack(
                rx.foreach(listing.sdgs, sdg_badge),
                width="100%",
                margin_bottom="0.5rem",
            ),

            rx.hstack(
                rx.vstack(
                    rx.text("Price per credit", color="gray", font_size="0.75rem"),
                    rx.text(listing.price, font_weight="800", font_size="1.2rem", color=ACCENT),
                    align_items="start",
                    spacing="0",
                ),
                rx.spacer(),
                rx.button(
                    "Buy Now",
                    bg="rgba(255, 255, 255, 0.08)",
                    color="white",
                    variant="outline",
                    border_color=BORDER_COLOR,
                    on_click=lambda: State.buy_item(listing.listing_id, listing.price_wei, 1),
                    _hover={"bg": ACCENT, "color": "#02070F", "border_color": ACCENT},
                    transition="all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                    cursor="pointer",
                    radius="full",
                    size="3",
                    padding_x="1.5rem",
                ),
                width="100%",
                align_items="center",
            ),
            spacing="2",
        ),
        padding="1.5rem",
        border_radius="28px",
        border=f"1px solid {BORDER_COLOR}",
        background="linear-gradient(165deg, rgba(255, 255, 255, 0.03) 0%, rgba(255, 255, 255, 0) 100%)",
        backdrop_filter="blur(12px)",
        _hover={
            "border_color": ACCENT,
            "transform": "translateY(-8px)",
            "box_shadow": f"0 15px 35px {ACCENT}15",
            "background": "linear-gradient(165deg, rgba(8, 247, 163, 0.05) 0%, rgba(255, 255, 255, 0) 100%)",
        },
        transition="all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
        width="100%",
    )

def marketplace_section() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Live marketplace", size="7", color="white"),
            rx.spacer(),
            rx.badge("Real-time", color_scheme="green", variant="solid"),
            width="100%",
            align_items="center",
            margin_bottom="1.5rem",
        ),
        rx.cond(
            State.has_listings,
            rx.grid(
                rx.foreach(State.listings, listing_card),
                columns="3",
                spacing="5",
                width="100%",
            ),
            rx.center(
                rx.text("Market is syncing or empty...", color=TEXT_MUTED, padding="4em"),
                width="100%",
                border=f"1px dashed {BORDER_COLOR}",
                border_radius="20px"
            ),
        ),
        spacing="4",
        width="100%",
    )

def index() -> rx.Component:
    return rx.box(
        # Load external scripts
        rx.script(src="https://cdn.ethers.io/lib/ethers-5.7.2.umd.min.js"),
        rx.script(src="/web3.js"), # relative path to assets

        navbar(),
        rx.container(
            hero(),
            marketplace_section(),
            max_width="1200px",
            padding_y="4rem",
            padding_x=["1rem", "2rem"],
            display="flex",
            flex_direction="column",
            gap="5rem",
        ),
        background=BACKGROUND,
        min_height="100vh",
        font_family="Inter, sans-serif",
        on_mount=State.fetch_listings,
    )

app = rx.App(stylesheets=["https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800&display=swap"])
app.add_page(index)

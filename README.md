# Decentralized Carbon Credit Marketplace

A next-generation, decentralized carbon credit marketplace that connects capital with verifiably climate-positive projects through a transparent, open-source, and impact-first platform.[1][2]

> “Instead of equities, you're trading impact.”

***

## Table of Contents

- [Overview](#overview)  
- [Market Context](#market-context)  
- [Core Features](#core-features)  
- [Architecture](#architecture)  
- [The Trust Layer](#the-trust-layer)  
- [Roadmap](#roadmap)  
- [Risk & Mitigation](#risk--mitigation)  
- [Contributing](#contributing)  
- [License](#license)  

***

## Getting Started (MVP)

This project uses a **Python-first stack** managed by **Poetry**. 

> [!IMPORTANT]
> Since the project is hosted on an external drive, specific configuration is required to handle filesystem metadata and macOS-specific restrictions.

### Prerequisites
- Python 3.11+
- Node.js & NPM (for local blockchain)
- [Poetry](https://python-poetry.org/) (version 2.0+)

### Initial Setup

Before installing dependencies, configure Poetry to use local virtual environments to bypass macOS system restrictions:

```bash
# Configure Poetry for local virtualenvs
poetry config virtualenvs.create true --local
poetry config virtualenvs.in-project true --local
```

### Installation

```bash
# 1. Clean up corrupt macOS metadata (Critical for external drives)
find . -name "._*" -delete

# 2. Install Python dependencies
poetry install

# 3. Install Node dependencies (Hardhat)
npm install
```

### Running the Application

**1. Start Local Blockchain** (Terminal 1)
```bash
npx hardhat node
```
*Keep this running.*

**2. Deploy Contracts** (Terminal 2)
```bash
# Run from the project root
poetry run python marketplace_app/deploy_web3.py
```
*This deploys contracts to the local node and mints initial carbon credit tokens.*

**3. Run Frontend** (Terminal 2 or 3)
```bash
cd marketplace_app
# Clean metadata again to prevent Reflex crashes
find . -name "._*" -delete
poetry run reflex run
```
Access the app at [http://localhost:3000](http://localhost:3000) (or 3001 if 3000 is occupied).

### Troubleshooting

If you encounter `FileNotFoundError` or `UnicodeDecodeError` during `reflex run` or `poetry install`:
- **Run the cleanup command**: `find . -name "._*" -delete`
- **Check virtualenv**: Ensure `.venv` exists in the project root.
- **Restart Reflex**: Sometimes a second start is needed if ports were shifted.

***

## Overview

This project is a decentralized carbon credit marketplace that channels funding into verified climate-positive projects such as reforestation, renewable energy, and carbon capture. It aims to solve fragmentation, low trust, and poor UX in existing markets by combining open-source infrastructure, a robust trust layer, and a user-centric interface.[3][4][5]

The marketplace allows corporations, governments, and individuals to buy, trade, and retire high-quality credits while maintaining full transparency over credit provenance, ownership, and impact.[6][7]

***

## Market Context

Carbon markets are broadly split into two segments:  
- **Compliance markets**: Regulated systems (e.g., cap-and-trade) where entities must offset emissions above legal caps.  
- **Voluntary markets**: Unregulated markets where entities buy credits to meet ESG, PR, or internal climate goals.[4][3]

Key actors include project developers, buyers, verifiers, registries, and marketplace operators, all of which are supported by this platform’s integration and data model. The project is positioned to address low-quality credits, lack of transparency, and clunky user experiences that currently limit confidence and adoption.[5][8][7][4]

***

## Core Features

At a high level, the platform enables users to:  
- List and browse verified carbon credit projects with detailed impact metadata and SDG alignment.  
- Trade, purchase, and retire tokenized carbon credits with full ownership history on-chain.  
- Track real-time pricing, liquidity, and market activity through dashboards and charts.  
- Read and write project reviews and ratings to foster community-driven trust and accountability.[3][6]

### Data Visualization & UX

- **Interactive dashboard**: Market KPIs, global impact map, and a heatmap across all 17 UN SDGs for quick “impact at a glance.”[9][5]
- **Advanced filtering & sorting**: Backend-driven multi-filtering via URL queries, combined with efficient frontend pagination for large datasets.[10][11]
- **Customizable tables**: Resize, reorder, freeze, hide, and add/remove columns to tailor views to user workflows.  
- **Drill-down views**: Inline expansion for SDGs, projects, and metrics to access granular qualitative and quantitative details.  
- **Search highlighting**: Inline highlighting of search matches to reduce cognitive load and speed up discovery.

***

## Architecture

The system is fully open-source and designed for security, scalability, and transparency using a layered architecture.[11][1]

### Layered Design

| Layer            | Purpose                                               | Key Tech / Concepts |
|------------------|-------------------------------------------------------|---------------------|
| Frontend         | UX for browsing, comparing, and purchasing credits    | React/Vue/Svelte, advanced data tables, maps[10][12] |
| Backend          | APIs, auth, transactions, filtering, pagination       | REST/GraphQL, TLS, microservices or modular monolith[11] |
| Database         | Storage for users, projects, transactions             | PostgreSQL, RLS, TDE, PITR[11] |
| Blockchain       | Immutable ledger for ownership and tokenization       | Public chain (Byzantine fault tolerance), Merkle trees, SHA-family hashes[4][13] |
| Supporting Sys   | Wallets, registries, GIS, external APIs               | Wallet providers, registry APIs, Esri/ArcGIS-based GIS[3][9] |

### Security & Fault Tolerance

The platform incorporates:  
- End-to-end encryption (e.g., TLS 1.3) and strong encryption at rest (e.g., AES-256).  
- Digital signatures for transaction authentication and tamper-proof event logs.[13][4]
- High availability via load balancing, redundancy, automated failover, and point-in-time recovery on the database.[11]

***

## The Trust Layer

The Trust Layer is the core differentiator, ensuring that every listed credit is authentic, unique, and aligned with global climate standards.[8][5]

Key components:  
- **International taxonomies**: Alignment with frameworks such as the Climate Bonds Taxonomy to define eligible assets and projects.[4]
- **Registry integration**: Direct integration with standards bodies and registries (e.g., Verra, Gold Standard) to ensure unique IDs and full traceability from issuance to retirement.[5][8]
- **Do No Significant Harm (DNSH)**: Project-level screening to ensure mitigation actions do not harm other environmental or social objectives.  
- **Regulatory compliance**: KYC for users, jurisdiction-aware data handling (e.g., GDPR-style data localization), and auditable logs for internal and external reviews.[4][11]

***

## Roadmap

The project follows a phased delivery strategy focusing on an early MVP followed by iterative expansion.[11]

### Phase 1 – Foundation & MVP

- Core backend, database, and blockchain setup.  
- Basic marketplace: project listing, search, filtering, and purchasing.  
- Integration with at least one major registry.  
- Wallet integration and user onboarding with KYC.

### Phase 2 – Feature Enhancement

- Advanced data tables with full column customization.  
- SDG impact dashboard with drill-down visualizations.  
- On-chain tokenization of credits.  
- User reviews, ratings, and richer project profiles.

### Phase 3 – Scaling & APIs

- Public API for corporate clients and third-party developers.  
- Integration with additional registries and verifiers.  
- AI-assisted project risk and impact assessment.  
- White-labeled marketplace solutions for enterprise partners.[3][5]

Deployment uses cloud-native infrastructure with CI/CD, automated testing, and security scanning (SAST/DAST) enforced before production releases.[11]

***

## Risk & Mitigation

The project explicitly addresses several risk categories:

- **Technical – Security breaches**  
  - Multi-layered security, strict least-privilege access, regular penetration testing, and a formal incident response plan aligned with 72-hour disclosure norms.[4][11]

- **Market – Low-quality credits and lack of trust**  
  - Heavy reliance on third-party standards, on-chain transparency, and a stringent Trust Layer to filter low-quality projects.[5][4]

- **User adoption – Poor UX**  
  - Modern UX patterns, iterative user testing, and a focus on clarity over jargon-heavy enterprise interfaces.[12][10]

- **Operational – Scalability & performance**  
  - Backend-driven filtering, pagination, horizontal scaling, and continuous performance monitoring from day one.[11]

***

## Contributing

Contributions are welcome once the core architecture is in place. Contribution guidelines will cover development setup, coding standards, security expectations, and the review process. Issues and feature requests can be opened via GitHub Issues once the repository is public.[2][14][1]

***

## License

This project will be released under an open-source license compatible with public blockchain and climate-finance ecosystems (exact license TBA in `LICENSE`).[2][11]

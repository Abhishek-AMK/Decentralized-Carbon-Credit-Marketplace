# StackHack 3.0 Submission: Problem Statement 3
## Project: Decentralized Carbon Credit Marketplace

**Theme**: Online Marketplace for Carbon Credits  
**Author**: Abhishek Kulkarni  
**GitHub Repository**: [Your Repo Link Here]  

---

## 🏆 Alignment with Problem Statement 3
This project delivers a high-performance, decentralized marketplace for carbon credits, explicitly meeting all "must-have" requirements of the PS3 prompt:

*   **Pricing**: Real-time ETH/Wei pricing displayed with 0.01 ETH decimals for precision.
*   **Categorization**: Projects are categorized into **Forestry**, **Wind Power**, and **Solar Energy**.
*   **Impact (SDGs)**: Every project card displays specific UN Sustainable Development Goal badges (SDG 7, 9, 13, 15) to verify climate impact.
*   **Verification**: Integrated **VERRA ✅** certification status and geographic verification (Location tracking).

---

## ✨ Features & Innovation

### 1. Web3 Tech Stack
- **Blockchain**: Local Ethereum node using **Hardhat**.
- **Smart Contracts**: ERC-1155 based carbon credit tokenization and Marketplace logic.
- **Frontend/Backend**: **Python-first stack** using **Reflex** (Next.js/FastAPI foundation).
- **Wallet Integration**: Native MetaMask connectivity via Ethers.js for secure trade execution.

### 2. "Cinematic Clarity" UI/UX
- **Glassmorphism Design**: A premium interface with blurred backgrounds and neon accents.
- **Micro-Interactions**: Smooth hover transformations and real-time syncing of marketplace listings.
- **Accessibility**: High-contrast typography and clear call-to-actions.

---

## 🌍 Deployed Prototype & References

For the Round 1 MVP, this is a **Local Decentralized Application (dApp)**. The prototype is provided via:

1.  **GitHub Repository**: [https://github.com/Abhishek-AMK/Decentralized-Carbon-Credit-Marketplace](https://github.com/Abhishek-AMK/Decentralized-Carbon-Credit-Marketplace)
2.  **MVP Setup**: The application is architected to run in an isolated environment (Hardhat + Reflex) to ensure full functionality (Token Minting, Listing, and Purchase) can be verified by the judges without gas-fee constraints.

> [!NOTE]
> Since this is a Core Blockchain solution, the "Deployed Prototype" link refers to the **Open Source Repository** and **Technical Walkthrough** provided in the submission ZIP.

---

## 📸 Screenshots & Video

### 1. High-Impact Hero Section
![Hero Section](screenshots/hero.png)

### 2. Multi-Category Marketplace (PS3 Must-Haves)
Displays Categories, SDG Badges, and VERRA Verification status.
![Marketplace Cards](screenshots/marketplace.png)

### 🎥 Demo Video
A full walkthrough of the application features and UI animations.
[Watch Demo Video](recordings/demo_video.webp)

---

## 🛠 Setup & Run Instructions
*(Please refer to the `README.md` for detailed commands)*

1.  **Dependencies**: Managed via `Poetry` and `NPM`.
2.  **Blockchain**: Run `npx hardhat node`.
3.  **Deployment**: Run `poetry run python marketplace_app/deploy_web3.py`.
4.  **Frontend**: Run `poetry run reflex run` inside `marketplace_app/`.

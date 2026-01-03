
// Address of the deployed Marketplace contract
const MP_ADDRESS = '0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512';

// Minimal ABI for the Marketplace contract (only buyToken needed for client tx)
const MP_ABI = [
    {
        "inputs": [
            { "internalType": "uint256", "name": "listingId", "type": "uint256" },
            { "internalType": "uint256", "name": "amountToBuy", "type": "uint256" }
        ],
        "name": "buyToken",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
];

window.connectWallet = async () => {
    if (typeof window.ethereum !== 'undefined') {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0];
        } catch (error) {
            console.error("User denied account access");
            return null;
        }
    } else {
        alert("Please install MetaMask!");
        return null;
    }
};

window.buyListing = async (listingId, priceWei, amount) => {
    if (typeof window.ethereum === 'undefined') {
        alert("Please install MetaMask!");
        return;
    }

    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const contract = new ethers.Contract(MP_ADDRESS, MP_ABI, signer);

    try {
        const tx = await contract.buyToken(listingId, amount, {
            value: priceWei
        });
        alert(`Transaction Sent: ${tx.hash}`);
        await tx.wait();
        alert("Purchase confirmed!");
        // Reload page to refresh listings (simple way)
        window.location.reload();
    } catch (error) {
        console.error("Purchase failed", error);
        alert("Purchase failed: " + error.message);
    }
};

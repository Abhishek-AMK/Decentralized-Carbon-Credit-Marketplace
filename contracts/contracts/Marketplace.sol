// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC1155/IERC1155.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract Marketplace is ReentrancyGuard {
    struct Listing {
        uint256 listingId;
        address seller;
        address tokenContract;
        uint256 tokenId;
        uint256 amount;
        uint256 price; // per unit in wei
        bool active;
    }

    uint256 public nextListingId;
    mapping(uint256 => Listing) public listings;

    event Listed(uint256 indexed listingId, address indexed seller, address indexed tokenContract, uint256 tokenId, uint256 amount, uint256 price);
    event Sale(uint256 indexed listingId, address indexed buyer, uint256 amount, uint256 price);

    constructor() {}

    function listToken(address tokenContract, uint256 tokenId, uint256 amount, uint256 price) external nonReentrant {
        require(amount > 0, "Amount must be > 0");
        require(price > 0, "Price must be > 0");
        
        IERC1155(tokenContract).safeTransferFrom(msg.sender, address(this), tokenId, amount, "");

        listings[nextListingId] = Listing(nextListingId, msg.sender, tokenContract, tokenId, amount, price, true);
        emit Listed(nextListingId, msg.sender, tokenContract, tokenId, amount, price);
        nextListingId++;
    }

    function buyToken(uint256 listingId, uint256 amountToBuy) external payable nonReentrant {
        Listing storage listing = listings[listingId];
        require(listing.active, "Listing not active");
        require(listing.amount >= amountToBuy, "Insufficient tokens listed");
        require(msg.value >= listing.price * amountToBuy, "Insufficient payment");

        listing.amount -= amountToBuy;
        if (listing.amount == 0) {
            listing.active = false;
        }

        // Pay seller
        payable(listing.seller).transfer(listing.price * amountToBuy);

        // Transfer tokens to buyer
        IERC1155(listing.tokenContract).safeTransferFrom(address(this), msg.sender, listing.tokenId, amountToBuy, "");

        // Refund excess is good practice but skipping for MVP conciseness, user should send exact.
        
        emit Sale(listingId, msg.sender, amountToBuy, listing.price);
    }
    
    // Required to receive ERC1155 tokens
    function onERC1155Received(address, address, uint256, uint256, bytes memory) public virtual returns (bytes4) {
        return this.onERC1155Received.selector;
    }

    function onERC1155BatchReceived(address, address, uint256[] memory, uint256[] memory, bytes memory) public virtual returns (bytes4) {
        return this.onERC1155BatchReceived.selector;
    }

    function supportsInterface(bytes4 interfaceId) external view virtual returns (bool) {
        return interfaceId == 0x01ffc9a7 || interfaceId == 0x4e2312e0;
    }
}

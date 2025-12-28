# 📦 ROUM Token Deployment Details

## Contract Information

### Basic Details
- **Contract Name:** ROUM
- **Token Name:** Rumeida Heritage
- **Symbol:** ROUM
- **Network:** Binance Smart Chain (BSC)
- **Chain ID:** 56
- **Contract Address:** `0x35B1761B00AB98144fAB4dEDBD58C59A2050947e`

### Supply Information
- **Total Supply:** 1,000,000,000 ROUM
- **Decimals:** 18
- **Total Supply (Wei):** `1000000000000000000000000000`

## Compilation Details

### Compiler Version
```
Solidity: 0.8.33+commit.64118f21
```

### Compiler Settings
```json
{
  "optimizer": {
    "enabled": true,
    "runs": 200
  },
  "evmVersion": "cancun"
}
```

### Source Code Hash
```
Keccak256: 0x6526bb915825c7ff9ef0b43ad126ccd5075553b3b6a996053665961853893afd
```

## Verification Status

### ✅ Sourcify Verification
- **Status:** Full Match ✓
- **Verification URL:** [View on Sourcify](https://repo.sourcify.dev/contracts/full_match/56/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e/)
- **IPFS Hash:** `QmZnz3iQxZL61Hm5W5YZFySENDMLeyXo86TLa5dHsVpPmL`
- **IPFS URL:** `dweb:/ipfs/QmZnz3iQxZL61Hm5W5YZFySENDMLeyXo86TLa5dHsVpPmL`

### ✅ BSCScan Verification
- **Status:** Verified ✓
- **Explorer URL:** [View on BSCScan](https://bscscan.com/address/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e)
- **Contract Creator:** Visible on BSCScan
- **Transaction Hash:** Available on BSCScan

## Contract Storage Layout

### Slot 0: _balanceOf
```solidity
mapping(address => uint256) private _balanceOf;
```
- **Type:** mapping(address => uint256)
- **Storage Slot:** 0

### Slot 1: _allowance
```solidity
mapping(address => mapping(address => uint256)) private _allowance;
```
- **Type:** mapping(address => mapping(address => uint256))
- **Storage Slot:** 1

## Deployment Timeline

1. **Contract Development:** Completed
2. **Local Testing:** Completed
3. **Compilation:** Solidity 0.8.33 with optimizer enabled (200 runs)
4. **Deployment to BSC:** December 25, 2024
5. **Sourcify Verification:** Completed (Full Match)
6. **BSCScan Verification:** Completed
7. **GitHub Repository:** Created December 26, 2025

## Contract Features

### Security Features
- ✅ Solidity 0.8.33 (built-in overflow protection)
- ✅ No delegatecall or assembly
- ✅ No selfdestruct
- ✅ Immutable (no owner)
- ✅ Zero address checks on all transfers
- ✅ Comprehensive error messages

### Gas Optimization
- ✅ Constants stored in bytecode
- ✅ Unchecked arithmetic where safe
- ✅ Efficient storage layout
- ✅ Optimizer enabled (200 runs)

### Standards Compliance
- ✅ Full ERC-20 compliance
- ✅ Full BEP-20 compliance
- ✅ Standard event emissions
- ✅ OpenZeppelin-compatible

## Network Information

### BSC Mainnet
- **RPC URL:** https://bsc-dataseed.binance.org/
- **Chain ID:** 56
- **Currency Symbol:** BNB
- **Block Explorer:** https://bscscan.com

## How to Add Token to MetaMask

1. Open MetaMask
2. Select BSC Network
3. Click "Import Tokens"
4. Enter Contract Address: `0x35B1761B00AB98144fAB4dEDBD58C59A2050947e`
5. Token Symbol and Decimals will auto-fill
6. Click "Add Custom Token"

## Developer Information

- **Developer:** Osama Qonaibe
- **Email:** Osamaqonaibe@outlook.com
- **Location:** Palestine 🇵🇸
- **GitHub:** [@Osama-Qonaibe](https://github.com/Osama-Qonaibe)

## License

```
MIT License

Copyright (c) 2025 Osama Qonaibe
```

## Additional Resources

- [Solidity Documentation](https://docs.soliditylang.org/)
- [BEP-20 Token Standard](https://github.com/bnb-chain/BEPs/blob/master/BEP20.md)
- [BSC Documentation](https://docs.bnbchain.org/)
- [Sourcify Documentation](https://docs.sourcify.dev/)

---

**Last Updated:** December 26, 2025

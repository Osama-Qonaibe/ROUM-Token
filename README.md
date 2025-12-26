<div align="center">
  <img src="assets/logo.png" alt="ROUM Logo" width="200"/>
  
  <h1>🪙 ROUM Token</h1>
  <p><strong>Rumeida Heritage on Binance Smart Chain</strong></p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![Solidity](https://img.shields.io/badge/Solidity-0.8.33-blue)](https://soliditylang.org/)
  [![BSC](https://img.shields.io/badge/BSC-Verified-green)](https://bscscan.com/address/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e)
  [![Sourcify](https://img.shields.io/badge/Sourcify-Verified-brightgreen)](https://sourcify.dev/#/lookup/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e)
</div>

---

**ROUM** is a BEP-20 token deployed on Binance Smart Chain, representing the heritage and history of Rumeida (Tel Rumeida) in Hebron, Palestine.

## 📋 Token Information

- **Name:** Rumeida Heritage
- **Symbol:** ROUM
- **Network:** Binance Smart Chain (BSC)
- **Contract Address:** `0x35B1761B00AB98144fAB4dEDBD58C59A2050947e`
- **Total Supply:** 1,000,000,000 ROUM
- **Decimals:** 18
- **License:** MIT

## 🔗 Verification Links

- **BSCScan:** [View on BSCScan](https://bscscan.com/address/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e)
- **Sourcify:** [Verified on Sourcify](https://repo.sourcify.dev/contracts/full_match/56/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e/)

## ✨ Features

- ✅ Full ERC-20/BEP-20 compatibility
- ✅ Optimized gas usage with Solidity 0.8.33
- ✅ Immutable contract (no owner, fully decentralized)
- ✅ Built-in overflow protection
- ✅ Clean and auditable code
- ✅ MIT licensed (open source)
- ✅ Verified on multiple blockchain explorers

## 🛠️ Technical Details

### Compiler Settings

```json
{
  "compiler": "solc 0.8.33+commit.64118f21",
  "optimizer": {
    "enabled": true,
    "runs": 200
  },
  "evmVersion": "cancun"
}
```

### Contract Functions

#### Standard ERC-20 Functions
- `name()` - Returns token name
- `symbol()` - Returns token symbol
- `decimals()` - Returns token decimals (18)
- `totalSupply()` - Returns total supply
- `balanceOf(address)` - Returns balance of an address
- `transfer(address, uint256)` - Transfer tokens
- `approve(address, uint256)` - Approve spending
- `allowance(address, address)` - Check allowance
- `transferFrom(address, address, uint256)` - Transfer from approved address

#### Additional Functions
- `increaseAllowance(address, uint256)` - Safely increase allowance
- `decreaseAllowance(address, uint256)` - Safely decrease allowance

## 📦 Repository Contents

```
ROUM-Token/
├── LICENSE                          # MIT License
├── README.md                        # This file
├── .gitignore                       # Git ignore rules
├── assets/
│   ├── logo.png                    # Main logo (1024x1024)
│   ├── logo-small.png              # Icon (256x256)
│   ├── banner.png                  # Repository banner
│   ├── README.md                   # Logo usage guidelines
│   └── brand-guidelines.md         # Brand guidelines
├── contracts/
│   └── ROUM.sol                    # Main contract source code
├── build/
│   ├── abi.json                    # Contract ABI
│   ├── metadata.json               # Contract metadata
│   └── compiler-settings.json      # Compiler configuration
└── docs/
    ├── DEPLOYMENT.md               # Deployment information
    ├── SECURITY.md                 # Security documentation
    └── INTEGRATION.md              # Integration guide
```

## 🚀 Deployment Information

- **Network:** BSC Mainnet (Chain ID: 56)
- **Deployed:** December 2024
- **Deployer:** Osama Qonaube
- **Verification:** Sourcify (Full Match)
- **Source Code Hash:** `0x6526bb915825c7ff9ef0b43ad126ccd5075553b3b6a996053665961853893afd`
- **IPFS:** `QmZnz3iQxZL61Hm5W5YZFySENDMLeyXo86TLa5dHsVpPmL`

## 👨‍💻 Developer

**Osama Qonaube**
- Email: Osamaqonaibe@outlook.com
- Location: Palestine 🇵🇸
- Role: Full-Stack & Blockchain Developer

## 📚 Documentation

- **[Security](docs/SECURITY.md)** - Security features and best practices
- **[Integration](docs/INTEGRATION.md)** - Developer integration guide
- **[Deployment](docs/DEPLOYMENT.md)** - Deployment details and verification
- **[Brand Guidelines](assets/brand-guidelines.md)** - Logo and branding guidelines

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Osama Qonaube

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORITIES OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🔐 Security

This contract has been:
- ✅ Verified on Sourcify (Full Match)
- ✅ Verified on BSCScan
- ✅ Built with Solidity 0.8.33 (built-in overflow protection)
- ✅ No external dependencies
- ✅ Immutable (no owner controls)
- ✅ Open source (MIT License)

For security concerns, please refer to [SECURITY.md](docs/SECURITY.md)

## 🌟 About Tel Rumeida

Tel Rumeida (Arabic: تل الرميدة) is an archaeological site in the heart of Hebron, Palestine, with evidence of human settlement dating back over 5,000 years. This token honors the rich heritage and resilient history of this ancient Palestinian site.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 💬 Support

For support and inquiries:
- Email: Osamaqonaibe@outlook.com
- GitHub Issues: [Create an issue](https://github.com/Osama-Qonaibe/ROUM-Token/issues)

---

<div align="center">
  <strong>Made with ❤️ in Palestine 🇵🇸</strong>
  
  <br><br>
  
  <a href="https://bscscan.com/address/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e">BSCScan</a> •
  <a href="https://repo.sourcify.dev/contracts/full_match/56/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e/">Sourcify</a> •
  <a href="https://github.com/Osama-Qonaibe/ROUM-Token">GitHub</a>
</div>

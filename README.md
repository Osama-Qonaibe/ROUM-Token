<div align="center">
  
  <img src="assets/logos/logo.png" alt="ROUM Token Logo" width="200"/>
  
  <h1>🪙 ROUM Token</h1>
  <p><strong>Rumeida Heritage on Binance Smart Chain</strong></p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
  [![Solidity](https://img.shields.io/badge/Solidity-0.8.33-blue)](https://soliditylang.org/)
  [![BSC](https://img.shields.io/badge/BSC-Verified-green)](https://bscscan.com/address/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e)
  [![Sourcify](https://img.shields.io/badge/Sourcify-Verified-brightgreen)](https://sourcify.dev/#/lookup/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e)
  [![CI](https://github.com/Osama-Qonaibe/ROUM-Token/actions/workflows/ci.yml/badge.svg)](https://github.com/Osama-Qonaibe/ROUM-Token/actions/workflows/ci.yml)
</div>

---

**ROUM** is a BEP-20 token deployed on Binance Smart Chain, representing the heritage and history of Rumeida (Tel Rumeida) in Hebron, Palestine.

## 📋 Token Information

| Property | Value |
|----------|-------|
| **Name** | Rumeida Heritage |
| **Symbol** | ROUM |
| **Network** | Binance Smart Chain (BSC) |
| **Contract** | `0x35B1761B00AB98144fAB4dEDBD58C59A2050947e` |
| **Total Supply** | 1,000,000,000 ROUM |
| **Decimals** | 18 |
| **License** | MIT |

## 🔗 Quick Links

- 🔍 [**BSCScan**](https://bscscan.com/address/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e) - View on Block Explorer
- ✅ [**Sourcify**](https://repo.sourcify.dev/contracts/full_match/56/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e/) - Verified Source Code
- 📚 [**Documentation**](docs/) - Technical Documentation
- 🎨 [**Brand Assets**](assets/) - Logos and Brand Guidelines
- ⚙️ [**Development Setup**](#development) - Build and Test Guide

## ✨ Features

- ✅ **Full ERC-20/BEP-20 Compatibility** - Standard compliant token
- ✅ **Optimized Gas Usage** - Built with Solidity 0.8.33
- ✅ **Fully Decentralized** - No owner, immutable contract
- ✅ **Built-in Overflow Protection** - Safe math included
- ✅ **Clean & Auditable Code** - Open source and transparent
- ✅ **Multiple Verifications** - Verified on BSCScan and Sourcify
- ✅ **Comprehensive Tests** - 15+ test cases with full coverage
- ✅ **CI/CD Pipeline** - Automated testing and deployment

## 🛠️ Technical Details

### Compiler Configuration

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

### Core Functions

<details>
<summary><strong>Standard ERC-20 Functions</strong></summary>

- `name()` - Returns token name
- `symbol()` - Returns token symbol  
- `decimals()` - Returns decimal places (18)
- `totalSupply()` - Returns total token supply
- `balanceOf(address)` - Returns balance of address
- `transfer(address, uint256)` - Transfer tokens
- `approve(address, uint256)` - Approve spending allowance
- `allowance(address, address)` - Check approved allowance
- `transferFrom(address, address, uint256)` - Transfer from approved address

</details>

<details>
<summary><strong>Enhanced Functions</strong></summary>

- `increaseAllowance(address, uint256)` - Safely increase allowance
- `decreaseAllowance(address, uint256)` - Safely decrease allowance

</details>

## 📦 Repository Structure

```
ROUM-Token/
├── .github/                  # GitHub configuration
│   ├── workflows/            # CI/CD pipelines
│   │   └── ci.yml           # Automated testing pipeline
│   ├── FUNDING.yml
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── assets/                  # Brand assets and logos
│   ├── logos/              # Logo files directory
│   ├── README.md
│   └── brand-guidelines.md
├── build/                   # Compilation artifacts
│   ├── abi.json
│   ├── metadata.json
│   └── compiler-settings.json
├── contracts/               # Solidity source code
│   └── ROUM.sol
├── docs/                    # Documentation
│   ├── DEPLOYMENT.md
│   ├── SECURITY.md
│   └── INTEGRATION.md
├── scripts/                 # Development scripts
│   └── deploy.js           # Hardhat deployment script
├── tests/                   # Test suite
│   └── roum.test.js        # Comprehensive test cases
├── hardhat.config.js        # Hardhat configuration
├── package.json            # NPM dependencies
├── .env.example            # Environment template
├── LICENSE                  # MIT License
├── README.md                # This file
└── .gitignore
```

## 🚀 Development

### Prerequisites

- **Node.js** >= 16.0.0
- **npm** >= 8.0.0 or **yarn**
- Basic understanding of Solidity and Hardhat

### Installation

```bash
# Clone the repository
git clone https://github.com/Osama-Qonaibe/ROUM-Token.git
cd ROUM-Token

# Install dependencies
npm install
```

### Configuration

```bash
# Create .env file from template
cp .env.example .env

# Edit .env and add your configuration:
# PRIVATE_KEY=your_private_key_here
# BSC_API_KEY=your_bscscan_api_key_here
```

### Development Commands

```bash
# Compile contracts
npm run compile

# Run tests locally
npm test

# Run tests with gas reporting
REPORT_GAS=true npm test

# Generate coverage report
npx hardhat coverage

# Deploy to BSC Testnet
npm run deploy:testnet

# Deploy to BSC Mainnet
npm run deploy:bsc

# Verify contract on BSCScan
npm run verify

# Clean artifacts
npm run clean

# View available accounts
npm run accounts
```

### Running Tests

```bash
# Run all tests
npm test

# Run specific test file
npx hardhat test tests/roum.test.js

# Run tests matching pattern
npx hardhat test --grep "Transfer"
```

### Test Coverage

The project includes 15+ comprehensive test cases covering:

- ✅ Deployment validation
- ✅ Token transfer functionality
- ✅ Approval and allowance mechanisms
- ✅ TransferFrom operations
- ✅ Allowance increase/decrease
- ✅ Error handling and edge cases
- ✅ Event emissions

## 🔄 CI/CD Pipeline

The project uses GitHub Actions for automated testing and quality checks:

### Pipeline Stages

1. **Compile** - Contract compilation check
2. **Test** - Run on Node 18 and 20
3. **Gas Report** - Analyze gas consumption
4. **Lint** - Code quality checks
5. **Security** - Run Slither analysis

**Trigger:** Push to `main` or `develop` branches, or Pull Requests

**View Pipeline:** [Actions](https://github.com/Osama-Qonaibe/ROUM-Token/actions/workflows/ci.yml)

## 🚀 Deployment Info

- **Network:** BSC Mainnet (Chain ID: 56)
- **Deployed:** 25 December 2025
- **Developer:** Osama Qonaibe
- **Verification:** Full Match on Sourcify
- **Source Hash:** `0x6526bb915825c7ff9ef0b43ad126ccd5075553b3b6a996053665961853893afd`
- **IPFS:** `QmZnz3iQxZL61Hm5W5YZFySENDMLeyXo86TLa5dHsVpPmL`

## 👨‍💻 Developer

**Osama Qonaibe**  
📧 Email: Osamaqonaibe@outlook.com  
🌍 Location: Palestine 🇵🇸  
💼 Role: Full-Stack & Blockchain Developer

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [Security](docs/SECURITY.md) | Security features and audit information |
| [Integration](docs/INTEGRATION.md) | Developer integration guide with code examples |
| [Deployment](docs/DEPLOYMENT.md) | Deployment details and verification |
| [Brand Guidelines](assets/brand-guidelines.md) | Logo usage and brand standards |

## 📜 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Osama Qonaibe

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
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🔐 Security

**Security Features:**
- ✅ Verified on Sourcify (Full Match)
- ✅ Verified on BSCScan  
- ✅ Solidity 0.8.33 (built-in overflow protection)
- ✅ No external dependencies
- ✅ Immutable (no owner controls)
- ✅ Open source (MIT License)
- ✅ Automated security scanning (Slither)
- ✅ Comprehensive test coverage

🚨 **Security Contact:** Osamaqonaibe@outlook.com

For detailed security information, see [SECURITY.md](docs/SECURITY.md)

## 🌟 About Tel Rumeida

Tel Rumeida (Arabic: تل الرميدة) is an ancient archaeological site in Hebron, Palestine, with continuous human settlement spanning over 5,000 years. This token honors and preserves the rich cultural heritage of this historic Palestinian site.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

**Before contributing:**
1. Check existing issues
2. Follow the code style guidelines
3. Write clear commit messages
4. Test your changes on BSC testnet
5. Ensure all tests pass locally

## 💬 Support

**Need help?**
- 📧 Email: Osamaqonaibe@outlook.com
- 🐛 GitHub Issues: [Create an issue](https://github.com/Osama-Qonaibe/ROUM-Token/issues)
- 📖 Documentation: [View docs](docs/)

---

<div align="center">
  
  ### Made with ❤️ in Palestine 🇵🇸
  
  <br>
  
  <a href="https://bscscan.com/address/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e">BSCScan</a> •
  <a href="https://repo.sourcify.dev/contracts/full_match/56/0x35B1761B00AB98144fAB4dEDBD58C59A2050947e/">Sourcify</a> •
  <a href="https://github.com/Osama-Qonaibe/ROUM-Token">GitHub</a>
  
  <br><br>
  
  **ROUM Token - Preserving Palestinian Heritage on the Blockchain**
  
</div>

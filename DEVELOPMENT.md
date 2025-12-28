# 🛠️ ROUM Token - Development Guide

## Overview

This guide provides detailed instructions for setting up and working with the ROUM Token development environment.

## Prerequisites

- **Node.js**: v20.x or later
- **npm**: v9.x or later (comes with Node.js)
- **Git**: For version control

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/Osama-Qonaibe/ROUM-Token.git
cd ROUM-Token

# 2. Install dependencies
npm install

# 3. Compile contracts
npm run compile

# 4. Run tests
npm test

# 5. Check code coverage
npm run test:coverage
```

## Development Commands

### Building & Testing

```bash
# Compile all smart contracts
npm run compile

# Run all tests
npm test

# Generate coverage report
npm run test:coverage
```

### Linting & Code Quality

```bash
# Lint Solidity contracts
npm run lint:sol

# Lint JavaScript files
npm run lint:js
```

### Deployment

```bash
# Deploy to local Hardhat network
npm run deploy

# Deploy to BSC Testnet (requires private key in .env)
npx hardhat run scripts/deploy.js --network bscTestnet

# Deploy to BSC Mainnet (requires private key in .env)
npx hardhat run scripts/deploy.js --network bsc
```

## Project Structure

```
ROUM-Token/
├── contracts/              # Smart contracts
│   └── ROUM.sol           # ERC20 token implementation
├── test/                  # Test files
│   └── ROUM.test.js      # Comprehensive test suite
├── scripts/               # Deployment and utility scripts
│   └── deploy.js         # Main deployment script
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI/CD
├── hardhat.config.js     # Hardhat configuration
├── package.json          # Node.js dependencies
├── .solhint.json        # Solidity linting rules
├── .eslintrc.json       # JavaScript linting rules
└── AUDIT_PREPARATION.md # Audit documentation
```

## Testing

### Test Coverage

The test suite includes comprehensive coverage of:

1. **Deployment Tests**
   - Name and symbol verification
   - Decimals configuration
   - Total supply allocation

2. **Transfer Tests**
   - Basic transfers between accounts
   - Insufficient balance handling
   - Zero address protection
   - Transfer event emission

3. **Allowance Tests**
   - Approve functionality
   - TransferFrom with allowances
   - Increase/decrease allowance
   - Edge cases and error conditions

### Running Specific Tests

```bash
# Run all tests
npm test

# Run with gas reporting
REPORT_GAS=true npm test

# Run specific test file
npx hardhat test test/ROUM.test.js
```

## Configuration

### Hardhat Networks

Edit `hardhat.config.js` to configure networks:

```javascript
networks: {
  hardhat: {
    chainId: 1337
  },
  bscTestnet: {
    url: "https://data-seed-prebsc-1-s1.binance.org:8545",
    chainId: 97,
    accounts: [process.env.PRIVATE_KEY] // Add your private key
  },
  bsc: {
    url: "https://bsc-dataseed.binance.org/",
    chainId: 56,
    accounts: [process.env.PRIVATE_KEY] // Add your private key
  }
}
```

### Environment Variables

Create a `.env` file (never commit this):

```bash
PRIVATE_KEY=your_private_key_here
BSCSCAN_API_KEY=your_bscscan_api_key_here
```

## Linting Rules

### Solidity (Solhint)

Configuration in `.solhint.json`:
- Compiler version: ^0.8.33
- Function visibility warnings
- Code complexity limits
- Gas optimization suggestions

### JavaScript (ESLint)

Configuration in `.eslintrc.json`:
- ES2021 standard
- Mocha test environment
- Node.js environment

## Continuous Integration

The project uses GitHub Actions for CI/CD. On every push:

1. **Test Job**
   - Install dependencies
   - Compile contracts
   - Run test suite
   - Generate coverage

2. **Lint Job**
   - Lint Solidity files
   - Lint JavaScript files

3. **Security Job**
   - Run Slither static analysis

## Troubleshooting

### Compiler Download Issues

If you encounter network issues downloading the Solidity compiler:

```bash
# Try using a different Node.js version
nvm use 20

# Clear Hardhat cache
npx hardhat clean

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

### Test Failures

```bash
# Clear cache and recompile
npx hardhat clean
npm run compile

# Run tests with verbose output
npx hardhat test --verbose
```

### Network Connection Issues

If deploying to BSC networks fails:

1. Check your internet connection
2. Verify RPC URL is accessible
3. Ensure you have BNB for gas fees
4. Confirm private key is correct in `.env`

## Best Practices

1. **Never commit sensitive data** (private keys, API keys)
2. **Always test on testnet** before mainnet deployment
3. **Run linters** before committing code
4. **Write tests** for new features
5. **Keep dependencies updated** (but test thoroughly)

## Security

- ✅ All dependencies scanned for vulnerabilities
- ✅ Code follows Solidity best practices
- ✅ Comprehensive test coverage
- ✅ Static analysis with Slither
- ✅ No external dependencies in contract

## Additional Resources

- [Hardhat Documentation](https://hardhat.org/docs)
- [Ethers.js Documentation](https://docs.ethers.org/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)
- [Solidity Documentation](https://docs.soliditylang.org/)

## Support

For development questions or issues:

- 📧 Email: Osamaqonaibe@outlook.com
- 🐛 GitHub Issues: [Create an issue](https://github.com/Osama-Qonaibe/ROUM-Token/issues)
- 📖 Documentation: [View docs](docs/)

---

**Happy Coding! 🚀**

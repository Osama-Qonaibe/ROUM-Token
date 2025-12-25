# 🔌 ROUM Token Integration Guide

## Quick Start

### Contract Information
```javascript
const ROUM_CONTRACT = {
  address: '0x35B1761B00AB98144fAB4dEDBD58C59A2050947e',
  name: 'Rumeida Heritage',
  symbol: 'ROUM',
  decimals: 18,
  totalSupply: '1000000000000000000000000000', // 1 billion * 10^18
  network: 'BSC',
  chainId: 56
};
```

## Web3 Integration

### Using Web3.js

```javascript
const Web3 = require('web3');
const web3 = new Web3('https://bsc-dataseed.binance.org/');

const ROUM_ABI = [
  // See build/abi.json for full ABI
  {
    "inputs": [{"internalType": "address", "name": "account", "type": "address"}],
    "name": "balanceOf",
    "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
    "stateMutability": "view",
    "type": "function"
  }
];

const contract = new web3.eth.Contract(
  ROUM_ABI,
  '0x35B1761B00AB98144fAB4dEDBD58C59A2050947e'
);

// Get balance
async function getBalance(address) {
  const balance = await contract.methods.balanceOf(address).call();
  return web3.utils.fromWei(balance, 'ether');
}

// Transfer tokens
async function transfer(to, amount, from) {
  const amountWei = web3.utils.toWei(amount.toString(), 'ether');
  const tx = await contract.methods.transfer(to, amountWei).send({ from });
  return tx;
}
```

### Using Ethers.js

```javascript
const { ethers } = require('ethers');

const provider = new ethers.providers.JsonRpcProvider(
  'https://bsc-dataseed.binance.org/'
);

const ROUM_ADDRESS = '0x35B1761B00AB98144fAB4dEDBD58C59A2050947e';
const ROUM_ABI = require('./build/abi.json');

const contract = new ethers.Contract(ROUM_ADDRESS, ROUM_ABI, provider);

// Get balance
async function getBalance(address) {
  const balance = await contract.balanceOf(address);
  return ethers.utils.formatEther(balance);
}

// Transfer with signer
async function transfer(to, amount, signer) {
  const contractWithSigner = contract.connect(signer);
  const amountWei = ethers.utils.parseEther(amount.toString());
  const tx = await contractWithSigner.transfer(to, amountWei);
  await tx.wait();
  return tx;
}
```

## MetaMask Integration

### Add Token to MetaMask

```javascript
async function addToMetaMask() {
  try {
    const wasAdded = await ethereum.request({
      method: 'wallet_watchAsset',
      params: {
        type: 'ERC20',
        options: {
          address: '0x35B1761B00AB98144fAB4dEDBD58C59A2050947e',
          symbol: 'ROUM',
          decimals: 18,
          image: 'https://raw.githubusercontent.com/Osama-Qonaibe/ROUM-Token/main/assets/logo-small.png'
        }
      }
    });
    
    if (wasAdded) {
      console.log('ROUM added to MetaMask!');
    }
  } catch (error) {
    console.error('Error adding token:', error);
  }
}
```

### Switch to BSC Network

```javascript
async function switchToBSC() {
  try {
    await ethereum.request({
      method: 'wallet_switchEthereumChain',
      params: [{ chainId: '0x38' }] // 56 in hex
    });
  } catch (switchError) {
    // Network not added, add it
    if (switchError.code === 4902) {
      await ethereum.request({
        method: 'wallet_addEthereumChain',
        params: [{
          chainId: '0x38',
          chainName: 'Binance Smart Chain',
          nativeCurrency: {
            name: 'BNB',
            symbol: 'BNB',
            decimals: 18
          },
          rpcUrls: ['https://bsc-dataseed.binance.org/'],
          blockExplorerUrls: ['https://bscscan.com/']
        }]
      });
    }
  }
}
```

## React Integration

```javascript
import { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import ROUM_ABI from './abi.json';

const ROUM_ADDRESS = '0x35B1761B00AB98144fAB4dEDBD58C59A2050947e';

function ROUMBalance({ address }) {
  const [balance, setBalance] = useState('0');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchBalance() {
      if (!address) return;
      
      try {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const contract = new ethers.Contract(ROUM_ADDRESS, ROUM_ABI, provider);
        const bal = await contract.balanceOf(address);
        setBalance(ethers.utils.formatEther(bal));
      } catch (error) {
        console.error('Error fetching balance:', error);
      } finally {
        setLoading(false);
      }
    }

    fetchBalance();
  }, [address]);

  if (loading) return <div>Loading...</div>;
  return <div>ROUM Balance: {balance}</div>;
}

export default ROUMBalance;
```

## PancakeSwap Integration

### Add Liquidity

```javascript
// PancakeSwap Router V2
const ROUTER_ADDRESS = '0x10ED43C718714eb63d5aA57B78B54704E256024E';

// Add liquidity pair: ROUM/BNB
// Requires approval first
```

### Token Information for Listing

```json
{
  "name": "Rumeida Heritage",
  "symbol": "ROUM",
  "address": "0x35B1761B00AB98144fAB4dEDBD58C59A2050947e",
  "chainId": 56,
  "decimals": 18,
  "logoURI": "https://raw.githubusercontent.com/Osama-Qonaibe/ROUM-Token/main/assets/logo-small.png"
}
```

## Exchange Integration

### Deposit Monitoring

```javascript
const Web3 = require('web3');
const web3 = new Web3('wss://bsc-ws-node.nariox.org:443');

const ROUM_ABI = require('./build/abi.json');
const contract = new web3.eth.Contract(
  ROUM_ABI,
  '0x35B1761B00AB98144fAB4dEDBD58C59A2050947e'
);

// Monitor deposits to exchange wallet
const EXCHANGE_WALLET = '0xYourExchangeWallet';

contract.events.Transfer({
  filter: { to: EXCHANGE_WALLET }
})
.on('data', (event) => {
  console.log('Deposit received:', {
    from: event.returnValues.from,
    amount: web3.utils.fromWei(event.returnValues.value, 'ether'),
    txHash: event.transactionHash,
    blockNumber: event.blockNumber
  });
  
  // Credit user account
});
```

### Withdrawal Processing

```javascript
async function processWithdrawal(userAddress, amount) {
  try {
    // Convert amount to wei
    const amountWei = web3.utils.toWei(amount.toString(), 'ether');
    
    // Check exchange balance
    const balance = await contract.methods
      .balanceOf(EXCHANGE_WALLET)
      .call();
    
    if (BigInt(balance) < BigInt(amountWei)) {
      throw new Error('Insufficient exchange balance');
    }
    
    // Send transaction
    const tx = await contract.methods
      .transfer(userAddress, amountWei)
      .send({ 
        from: EXCHANGE_WALLET,
        gas: 100000
      });
    
    return tx;
  } catch (error) {
    console.error('Withdrawal error:', error);
    throw error;
  }
}
```

## API Examples

### Get Token Info

```javascript
const axios = require('axios');

async function getTokenInfo() {
  const response = await axios.get(
    'https://api.bscscan.com/api',
    {
      params: {
        module: 'token',
        action: 'tokeninfo',
        contractaddress: '0x35B1761B00AB98144fAB4dEDBD58C59A2050947e',
        apikey: 'YOUR_API_KEY'
      }
    }
  );
  return response.data;
}
```

### Get Token Holders

```javascript
async function getTopHolders() {
  const response = await axios.get(
    'https://api.bscscan.com/api',
    {
      params: {
        module: 'token',
        action: 'tokenholderlist',
        contractaddress: '0x35B1761B00AB98144fAB4dEDBD58C59A2050947e',
        page: 1,
        offset: 100,
        apikey: 'YOUR_API_KEY'
      }
    }
  );
  return response.data;
}
```

## Testing

### BSC Testnet

```javascript
const TESTNET_CONFIG = {
  rpcUrl: 'https://data-seed-prebsc-1-s1.binance.org:8545/',
  chainId: 97,
  explorer: 'https://testnet.bscscan.com'
};

// Deploy to testnet first for testing
```

### Unit Tests

```javascript
const { expect } = require('chai');
const { ethers } = require('hardhat');

describe('ROUM Token', function () {
  it('Should return correct name', async function () {
    const contract = await ethers.getContractAt(
      'ROUM',
      '0x35B1761B00AB98144fAB4dEDBD58C59A2050947e'
    );
    expect(await contract.name()).to.equal('Rumeida Heritage');
  });
});
```

## Gas Optimization

### Recommended Gas Limits

```javascript
const GAS_LIMITS = {
  transfer: 65000,
  approve: 50000,
  transferFrom: 80000,
  increaseAllowance: 55000,
  decreaseAllowance: 55000
};
```

## Error Handling

```javascript
try {
  await contract.methods.transfer(to, amount).send({ from });
} catch (error) {
  if (error.message.includes('insufficient balance')) {
    console.error('Not enough ROUM tokens');
  } else if (error.message.includes('zero address')) {
    console.error('Invalid recipient address');
  } else {
    console.error('Transaction failed:', error);
  }
}
```

## Support

For integration support:
- **Email:** Osamaqonaibe@outlook.com
- **GitHub Issues:** [Create an issue](https://github.com/Osama-Qonaibe/ROUM-Token/issues)
- **Documentation:** [View Docs](https://github.com/Osama-Qonaibe/ROUM-Token/tree/main/docs)

---

**Last Updated:** December 26, 2025

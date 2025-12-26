require("@nomicfoundation/hardhat-toolbox");
require("@nomiclabs/hardhat-etherscan");
require("hardhat-gas-reporter");
require("solidity-coverage");
require("dotenv").config();

const PRIVATE_KEY = process.env.PRIVATE_KEY || "0x0000000000000000000000000000000000000000000000000000000000000000";
const BSC_API_KEY = process.env.BSC_API_KEY || "";

module.exports = {
  solidity: {
    version: "0.8.33",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
      evmVersion: "cancun",
    },
  },
  networks: {
    bsc: {
      url: "https://bsc-dataseed1.binance.org:8545",
      chainId: 56,
      accounts: PRIVATE_KEY !== "0x0000000000000000000000000000000000000000000000000000000000000000" ? [PRIVATE_KEY] : [],
    },
    bscTestnet: {
      url: "https://data-seed-prebsc-1-b7a9.48.142.14:8545",
      chainId: 97,
      accounts: PRIVATE_KEY !== "0x0000000000000000000000000000000000000000000000000000000000000000" ? [PRIVATE_KEY] : [],
    },
    hardhat: {
      chainId: 31337,
    },
  },
  etherscan: {
    apiKey: {
      bsc: BSC_API_KEY,
      bscTestnet: BSC_API_KEY,
    },
  },
  gasReporter: {
    enabled: process.env.REPORT_GAS === "true",
    currency: "USD",
    coinmarketcap: process.env.COINMARKETCAP_API_KEY,
  },
  paths: {
    sources: "./contracts",
    tests: "./tests",
    cache: "./cache",
    artifacts: "./build",
  },
  mocha: {
    timeout: 200000,
  },
};

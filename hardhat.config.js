require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: {
    compilers: [
      {
        version: "0.8.33"
      }
    ]
  },
  paths: {
    sources: "./contracts",
    tests: "./test"
  }
};

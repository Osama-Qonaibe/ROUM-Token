const hre = require("hardhat");

async function main() {
  console.log("🚀 Starting ROUM Token deployment...\n");

  // Get deployer account
  const [deployer] = await ethers.getSigners();
  console.log("📍 Deploying from account:", deployer.address);
  console.log("💰 Account balance:", (await deployer.provider.getBalance(deployer.address)).toString());

  // Deploy ROUM contract
  console.log("\n⏳ Compiling ROUM contract...");
  const ROUM = await ethers.getContractFactory("ROUM");
  
  console.log("📦 Deploying ROUM contract...");
  const roum = await ROUM.deploy();
  await roum.deploymentTransaction().wait(1);

  const roumAddress = await roum.getAddress();
  console.log("✅ ROUM Token deployed to:", roumAddress);

  // Get contract info
  const name = await roum.name();
  const symbol = await roum.symbol();
  const totalSupply = await roum.totalSupply();
  const decimals = await roum.decimals();

  console.log("\n📊 Token Information:");
  console.log("   Name:", name);
  console.log("   Symbol:", symbol);
  console.log("   Decimals:", decimals);
  console.log("   Total Supply:", ethers.formatUnits(totalSupply, decimals));

  // Print deployment info
  console.log("\n🔗 Deployment Summary:");
  console.log(`   Network: ${hre.network.name}`);
  console.log(`   Contract: ${roumAddress}`);
  console.log(`   Deployer: ${deployer.address}`);

  // Export for verification
  console.log("\n📝 To verify on Etherscan, run:");
  console.log(`   npx hardhat verify --network ${hre.network.name} ${roumAddress}`);

  return roumAddress;
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });

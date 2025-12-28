const hre = require("hardhat");

async function main() {
  console.log("Deploying ROUM Token...");

  const ROUM = await hre.ethers.getContractFactory("ROUM");
  const roum = await ROUM.deploy();

  await roum.waitForDeployment();

  const address = await roum.getAddress();
  console.log("ROUM Token deployed to:", address);
  
  console.log("\nToken Details:");
  console.log("Name:", await roum.name());
  console.log("Symbol:", await roum.symbol());
  console.log("Decimals:", await roum.decimals());
  console.log("Total Supply:", ethers.formatEther(await roum.totalSupply()), "ROUM");
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });

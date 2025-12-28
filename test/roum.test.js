const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("ROUM token basic", function () {
  it("should assign total supply to deployer and allow transfers", async function () {
    const [deployer, addr1] = await ethers.getSigners();
    const ROUM = await ethers.getContractFactory("ROUM");
    const token = await ROUM.deploy();
    await token.deployed();

    const total = await token.totalSupply();
    const deployerBal = await token.balanceOf(deployer.address);
    expect(deployerBal).to.equal(total);

    // transfer small amount
    await token.transfer(addr1.address, 1000);
    expect(await token.balanceOf(addr1.address)).to.equal(1000);
  });
});

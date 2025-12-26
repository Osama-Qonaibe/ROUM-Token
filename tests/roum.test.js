const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("ROUM Token", function () {
  let roum;
  let owner;
  let addr1;
  let addr2;
  let addrs;
  const initialSupply = ethers.parseUnits("1000000000", 18);

  beforeEach(async function () {
    const ROUM = await ethers.getContractFactory("ROUM");
    roum = await ROUM.deploy();
    [owner, addr1, addr2, ...addrs] = await ethers.getSigners();
  });

  describe("Deployment", function () {
    it("Should set the correct name", async function () {
      expect(await roum.name()).to.equal("Rumeida Heritage");
    });

    it("Should set the correct symbol", async function () {
      expect(await roum.symbol()).to.equal("ROUM");
    });

    it("Should set the correct decimals", async function () {
      expect(await roum.decimals()).to.equal(18);
    });

    it("Should set the correct total supply", async function () {
      expect(await roum.totalSupply()).to.equal(initialSupply);
    });

    it("Should assign the total supply to the deployer", async function () {
      const ownerBalance = await roum.balanceOf(owner.address);
      expect(await roum.totalSupply()).to.equal(ownerBalance);
    });

    it("Should have zero initial balance for other accounts", async function () {
      const balance = await roum.balanceOf(addr1.address);
      expect(balance).to.equal(0);
    });
  });

  describe("Transfer", function () {
    it("Should transfer tokens between accounts", async function () {
      const transferAmount = ethers.parseUnits("100", 18);
      
      await roum.transfer(addr1.address, transferAmount);
      const addr1Balance = await roum.balanceOf(addr1.address);
      expect(addr1Balance).to.equal(transferAmount);
    });

    it("Should emit Transfer event on transfer", async function () {
      const transferAmount = ethers.parseUnits("100", 18);
      
      await expect(roum.transfer(addr1.address, transferAmount))
        .to.emit(roum, "Transfer")
        .withArgs(owner.address, addr1.address, transferAmount);
    });

    it("Should revert when transferring to zero address", async function () {
      const transferAmount = ethers.parseUnits("100", 18);
      
      await expect(
        roum.transfer(ethers.ZeroAddress, transferAmount)
      ).to.be.revertedWith("ROUM: transfer to zero address");
    });

    it("Should revert when transferring more than balance", async function () {
      const transferAmount = initialSupply + ethers.parseUnits("1", 18);
      
      await expect(
        roum.connect(addr1).transfer(owner.address, transferAmount)
      ).to.be.revertedWith("ROUM: insufficient balance");
    });

    it("Should correctly update balances after transfer", async function () {
      const transferAmount = ethers.parseUnits("500", 18);
      
      const ownerInitialBalance = await roum.balanceOf(owner.address);
      
      await roum.transfer(addr1.address, transferAmount);
      
      const ownerFinalBalance = await roum.balanceOf(owner.address);
      const addr1Balance = await roum.balanceOf(addr1.address);
      
      expect(ownerFinalBalance).to.equal(ownerInitialBalance - transferAmount);
      expect(addr1Balance).to.equal(transferAmount);
    });
  });

  describe("Approve and Allowance", function () {
    it("Should approve tokens for spending", async function () {
      const approveAmount = ethers.parseUnits("100", 18);
      
      await roum.approve(addr1.address, approveAmount);
      const allowance = await roum.allowance(owner.address, addr1.address);
      expect(allowance).to.equal(approveAmount);
    });

    it("Should emit Approval event on approve", async function () {
      const approveAmount = ethers.parseUnits("100", 18);
      
      await expect(roum.approve(addr1.address, approveAmount))
        .to.emit(roum, "Approval")
        .withArgs(owner.address, addr1.address, approveAmount);
    });

    it("Should revert when approving to zero address", async function () {
      const approveAmount = ethers.parseUnits("100", 18);
      
      await expect(
        roum.approve(ethers.ZeroAddress, approveAmount)
      ).to.be.revertedWith("ROUM: approve to zero address");
    });

    it("Should return zero allowance for non-approved spenders", async function () {
      const allowance = await roum.allowance(owner.address, addr1.address);
      expect(allowance).to.equal(0);
    });
  });

  describe("TransferFrom", function () {
    beforeEach(async function () {
      const approveAmount = ethers.parseUnits("1000", 18);
      await roum.approve(addr1.address, approveAmount);
    });

    it("Should transfer tokens on behalf of owner", async function () {
      const transferAmount = ethers.parseUnits("100", 18);
      
      await roum.connect(addr1).transferFrom(owner.address, addr2.address, transferAmount);
      const addr2Balance = await roum.balanceOf(addr2.address);
      expect(addr2Balance).to.equal(transferAmount);
    });

    it("Should emit Transfer event on transferFrom", async function () {
      const transferAmount = ethers.parseUnits("100", 18);
      
      await expect(
        roum.connect(addr1).transferFrom(owner.address, addr2.address, transferAmount)
      )
        .to.emit(roum, "Transfer")
        .withArgs(owner.address, addr2.address, transferAmount);
    });

    it("Should decrease allowance after transferFrom", async function () {
      const transferAmount = ethers.parseUnits("100", 18);
      
      await roum.connect(addr1).transferFrom(owner.address, addr2.address, transferAmount);
      const remainingAllowance = await roum.allowance(owner.address, addr1.address);
      expect(remainingAllowance).to.equal(ethers.parseUnits("900", 18));
    });

    it("Should revert when transferring from zero address", async function () {
      const transferAmount = ethers.parseUnits("100", 18);
      
      await expect(
        roum.connect(addr1).transferFrom(ethers.ZeroAddress, addr2.address, transferAmount)
      ).to.be.revertedWith("ROUM: transfer from zero address");
    });

    it("Should revert when transferring to zero address", async function () {
      const transferAmount = ethers.parseUnits("100", 18);
      
      await expect(
        roum.connect(addr1).transferFrom(owner.address, ethers.ZeroAddress, transferAmount)
      ).to.be.revertedWith("ROUM: transfer to zero address");
    });

    it("Should revert when exceeding allowance", async function () {
      const transferAmount = ethers.parseUnits("2000", 18);
      
      await expect(
        roum.connect(addr1).transferFrom(owner.address, addr2.address, transferAmount)
      ).to.be.revertedWith("ROUM: insufficient allowance");
    });

    it("Should revert when transferring more than balance", async function () {
      const transferAmount = ethers.parseUnits("2000000000", 18);
      
      await expect(
        roum.connect(addr1).transferFrom(owner.address, addr2.address, transferAmount)
      ).to.be.revertedWith("ROUM: insufficient balance");
    });
  });

  describe("IncreaseAllowance", function () {
    it("Should increase allowance", async function () {
      const initialAmount = ethers.parseUnits("100", 18);
      const addedAmount = ethers.parseUnits("50", 18);
      
      await roum.approve(addr1.address, initialAmount);
      await roum.increaseAllowance(addr1.address, addedAmount);
      
      const allowance = await roum.allowance(owner.address, addr1.address);
      expect(allowance).to.equal(initialAmount + addedAmount);
    });

    it("Should emit Approval event on increaseAllowance", async function () {
      const addedAmount = ethers.parseUnits("50", 18);
      
      await expect(roum.increaseAllowance(addr1.address, addedAmount))
        .to.emit(roum, "Approval");
    });
  });

  describe("DecreaseAllowance", function () {
    beforeEach(async function () {
      const approveAmount = ethers.parseUnits("200", 18);
      await roum.approve(addr1.address, approveAmount);
    });

    it("Should decrease allowance", async function () {
      const decreasedAmount = ethers.parseUnits("50", 18);
      
      await roum.decreaseAllowance(addr1.address, decreasedAmount);
      const allowance = await roum.allowance(owner.address, addr1.address);
      expect(allowance).to.equal(ethers.parseUnits("150", 18));
    });

    it("Should emit Approval event on decreaseAllowance", async function () {
      const decreasedAmount = ethers.parseUnits("50", 18);
      
      await expect(roum.decreaseAllowance(addr1.address, decreasedAmount))
        .to.emit(roum, "Approval");
    });

    it("Should revert when decreasing below zero", async function () {
      const decreasedAmount = ethers.parseUnits("300", 18);
      
      await expect(
        roum.decreaseAllowance(addr1.address, decreasedAmount)
      ).to.be.revertedWith("ROUM: decreased allowance below zero");
    });

    it("Should revert when decreasing from zero address", async function () {
      const decreasedAmount = ethers.parseUnits("50", 18);
      
      await expect(
        roum.decreaseAllowance(ethers.ZeroAddress, decreasedAmount)
      ).to.be.revertedWith("ROUM: approve to zero address");
    });
  });
});

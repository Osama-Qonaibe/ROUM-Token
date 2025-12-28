const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("ROUM Token - Comprehensive Test Suite", function () {
  let roum;
  let owner;
  let addr1;
  let addr2;

  const TOTAL_SUPPLY = ethers.parseEther("1000000000"); // 1 billion tokens

  beforeEach(async function () {
    [owner, addr1, addr2] = await ethers.getSigners();
    const ROUM = await ethers.getContractFactory("ROUM");
    roum = await ROUM.deploy();
  });

  describe("Deployment", function () {
    it("Should set the right name and symbol", async function () {
      expect(await roum.name()).to.equal("Rumeida Heritage");
      expect(await roum.symbol()).to.equal("ROUM");
    });

    it("Should set the correct decimals", async function () {
      expect(await roum.decimals()).to.equal(18);
    });

    it("Should assign total supply to owner", async function () {
      const ownerBalance = await roum.balanceOf(owner.address);
      expect(await roum.totalSupply()).to.equal(TOTAL_SUPPLY);
      expect(ownerBalance).to.equal(TOTAL_SUPPLY);
    });
  });

  describe("Transfers", function () {
    it("Should transfer tokens between accounts", async function () {
      await roum.transfer(addr1.address, ethers.parseEther("100"));
      expect(await roum.balanceOf(addr1.address)).to.equal(ethers.parseEther("100"));

      await roum.connect(addr1).transfer(addr2.address, ethers.parseEther("50"));
      expect(await roum.balanceOf(addr2.address)).to.equal(ethers.parseEther("50"));
      expect(await roum.balanceOf(addr1.address)).to.equal(ethers.parseEther("50"));
    });

    it("Should fail if sender doesn't have enough tokens", async function () {
      const initialOwnerBalance = await roum.balanceOf(owner.address);
      await expect(
        roum.connect(addr1).transfer(owner.address, ethers.parseEther("1"))
      ).to.be.revertedWith("ROUM: insufficient balance");
      expect(await roum.balanceOf(owner.address)).to.equal(initialOwnerBalance);
    });

    it("Should fail if transferring to zero address", async function () {
      await expect(
        roum.transfer(ethers.ZeroAddress, ethers.parseEther("100"))
      ).to.be.revertedWith("ROUM: transfer to zero address");
    });

    it("Should emit Transfer event", async function () {
      await expect(roum.transfer(addr1.address, ethers.parseEther("100")))
        .to.emit(roum, "Transfer")
        .withArgs(owner.address, addr1.address, ethers.parseEther("100"));
    });
  });

  describe("Allowances", function () {
    it("Should approve tokens for delegated transfer", async function () {
      await roum.approve(addr1.address, ethers.parseEther("100"));
      expect(await roum.allowance(owner.address, addr1.address)).to.equal(
        ethers.parseEther("100")
      );
    });

    it("Should fail if approving to zero address", async function () {
      await expect(
        roum.approve(ethers.ZeroAddress, ethers.parseEther("100"))
      ).to.be.revertedWith("ROUM: approve to zero address");
    });

    it("Should emit Approval event", async function () {
      await expect(roum.approve(addr1.address, ethers.parseEther("100")))
        .to.emit(roum, "Approval")
        .withArgs(owner.address, addr1.address, ethers.parseEther("100"));
    });

    it("Should allow transferFrom with proper allowance", async function () {
      await roum.approve(addr1.address, ethers.parseEther("100"));
      await roum.connect(addr1).transferFrom(
        owner.address,
        addr2.address,
        ethers.parseEther("50")
      );
      expect(await roum.balanceOf(addr2.address)).to.equal(ethers.parseEther("50"));
      expect(await roum.allowance(owner.address, addr1.address)).to.equal(
        ethers.parseEther("50")
      );
    });

    it("Should fail transferFrom without allowance", async function () {
      await expect(
        roum.connect(addr1).transferFrom(
          owner.address,
          addr2.address,
          ethers.parseEther("1")
        )
      ).to.be.revertedWith("ROUM: insufficient allowance");
    });

    it("Should increase allowance correctly", async function () {
      await roum.approve(addr1.address, ethers.parseEther("100"));
      await roum.increaseAllowance(addr1.address, ethers.parseEther("50"));
      expect(await roum.allowance(owner.address, addr1.address)).to.equal(
        ethers.parseEther("150")
      );
    });

    it("Should decrease allowance correctly", async function () {
      await roum.approve(addr1.address, ethers.parseEther("100"));
      await roum.decreaseAllowance(addr1.address, ethers.parseEther("40"));
      expect(await roum.allowance(owner.address, addr1.address)).to.equal(
        ethers.parseEther("60")
      );
    });

    it("Should fail when decreasing allowance below zero", async function () {
      await roum.approve(addr1.address, ethers.parseEther("100"));
      await expect(
        roum.decreaseAllowance(addr1.address, ethers.parseEther("150"))
      ).to.be.revertedWith("ROUM: decreased allowance below zero");
    });
  });

  describe("Edge Cases", function () {
    it("Should handle zero transfers", async function () {
      await roum.transfer(addr1.address, 0);
      expect(await roum.balanceOf(addr1.address)).to.equal(0);
    });

    it("Should handle maximum uint256 allowance", async function () {
      const maxUint256 = ethers.MaxUint256;
      await roum.approve(addr1.address, maxUint256);
      expect(await roum.allowance(owner.address, addr1.address)).to.equal(maxUint256);
    });
  });
});

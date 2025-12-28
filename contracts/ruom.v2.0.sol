/**
 *Submitted for verification at BscScan.com on 2025-12-28
*/

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

/**
 * @title ROUM Token - Rumeida Heritage ERC20
 * @notice Rumeida Heritage Token (ROUM) - A BEP20 token on Binance Smart Chain
 * @dev Implements standard ERC20 interface with optimized gas usage via custom errors
 */

interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address) external view returns (uint256);
    function transfer(address, uint256) external returns (bool);
    function allowance(address, address) external view returns (uint256);
    function approve(address, uint256) external returns (bool);
    function transferFrom(address, address, uint256) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

/**
 * @title ROUM Contract
 * @dev ERC20 token implementation with custom error handling for gas optimization
 */
contract ROUM is IERC20 {
    // ==================== CUSTOM ERRORS ====================
    /// @dev Error raised when attempting operations with zero address
    error InvalidZeroAddress();
    
    /// @dev Error raised when sender has insufficient token balance
    error InsufficientBalance();
    
    /// @dev Error raised when spender has insufficient allowance
    error InsufficientAllowance();
    
    /// @dev Error raised when decreasing allowance below zero
    error DecreaseAllowanceBelowZero();

    // ==================== TOKEN METADATA ====================
    // ✅ FIXED: Applied SNAKE_CASE naming convention for constants
    string public constant NAME = "roum token";
    string public constant SYMBOL = "ROUM";
    uint8 public constant DECIMALS = 18;
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    // ==================== STATE VARIABLES ====================
    /// @dev Maps account addresses to their token balances
    mapping(address => uint256) private _balanceOf;
    
    /// @dev Maps (owner => spender) to approved spending amounts
    mapping(address => mapping(address => uint256)) private _allowance;

    // ==================== CONSTRUCTOR ====================
    /**
     * @notice Initializes the ROUM token
     * @dev Allocates all tokens to contract deployer
     */
    constructor() {
        _balanceOf[msg.sender] = TOTAL_SUPPLY;
        emit Transfer(address(0), msg.sender, TOTAL_SUPPLY);
    }

    // ==================== VIEW FUNCTIONS ====================
    /**
     * @notice Returns the token balance of an account
     * @param account The address to check balance for
     * @return The token balance of the account
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balanceOf[account];
    }

    /**
     * @notice Returns the approved spending allowance
     * @param owner The token owner address
     * @param spender The spender address
     * @return The approved spending amount
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowance[owner][spender];
    }

    // ==================== TRANSFER FUNCTIONS ====================
    /**
     * @notice Transfers tokens to a specified address
     * @param to The recipient address
     * @param value The amount of tokens to transfer
     * @return Always returns true on success
     */
    function transfer(address to, uint256 value) external override returns (bool) {
        if (to == address(0)) revert InvalidZeroAddress();
        
        uint256 fromBal = _balanceOf[msg.sender];
        if (fromBal < value) revert InsufficientBalance();
        
        unchecked {
            _balanceOf[msg.sender] = fromBal - value;
            _balanceOf[to] += value;
        }
        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @notice Approves a spender to spend a specified amount of tokens
     * @param spender The address allowed to spend
     * @param value The amount of tokens to approve
     * @return Always returns true on success
     */
    function approve(address spender, uint256 value) external override returns (bool) {
        if (spender == address(0)) revert InvalidZeroAddress();
        
        _allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @notice Increases the allowance granted to a spender
     * @param spender The spender address
     * @param addedValue The amount to increase allowance by
     * @return Always returns true on success
     */
    function increaseAllowance(address spender, uint256 addedValue) external returns (bool) {
        if (spender == address(0)) revert InvalidZeroAddress();
        
        unchecked {
            _allowance[msg.sender][spender] += addedValue;
        }
        emit Approval(msg.sender, spender, _allowance[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decreases the allowance granted to a spender
     * @param spender The spender address
     * @param subtractedValue The amount to decrease allowance by
     * @return Always returns true on success
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) external returns (bool) {
        if (spender == address(0)) revert InvalidZeroAddress();
        
        uint256 currentAllowance = _allowance[msg.sender][spender];
        if (currentAllowance < subtractedValue) revert DecreaseAllowanceBelowZero();
        
        unchecked {
            _allowance[msg.sender][spender] = currentAllowance - subtractedValue;
        }
        emit Approval(msg.sender, spender, _allowance[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another using approved allowance
     * @param from The sender address
     * @param to The recipient address
     * @param value The amount of tokens to transfer
     * @return Always returns true on success
     */
    function transferFrom(address from, address to, uint256 value) external override returns (bool) {
        if (from == address(0)) revert InvalidZeroAddress();
        if (to == address(0)) revert InvalidZeroAddress();
        
        uint256 fromBal = _balanceOf[from];
        if (fromBal < value) revert InsufficientBalance();
        
        uint256 currentAllowance = _allowance[from][msg.sender];
        if (currentAllowance < value) revert InsufficientAllowance();
        
        unchecked {
            _balanceOf[from] = fromBal - value;
            _balanceOf[to] += value;
            _allowance[from][msg.sender] = currentAllowance - value;
        }
        emit Transfer(from, to, value);
        return true;
    }
}

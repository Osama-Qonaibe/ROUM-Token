// SPDX-License-Identifier: MIT
pragma solidity ^0.8.33;

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

contract ROUM is IERC20 {
    string public constant NAME = "Rumeida Heritage";
    string public constant SYMBOL = "ROUM";
    uint8 public constant DECIMALS = 18;
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    mapping(address => uint256) private _balanceOf;
    mapping(address => mapping(address => uint256)) private _allowance;

    // Custom Errors for gas optimization
    error ZeroAddress();
    error InsufficientBalance();
    error InsufficientAllowance();
    error DecreaseAllowanceBelowZero();

    constructor() {
        _balanceOf[msg.sender] = TOTAL_SUPPLY;
        emit Transfer(address(0), msg.sender, TOTAL_SUPPLY);
    }

    function totalSupply() public view override returns (uint256) {
        return TOTAL_SUPPLY;
    }

    function name() public view returns (string memory) {
        return NAME;
    }

    function symbol() public view returns (string memory) {
        return SYMBOL;
    }

    function decimals() public view returns (uint8) {
        return DECIMALS;
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balanceOf[account];
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowance[owner][spender];
    }

    function transfer(address to, uint256 value) external override returns (bool) {
        if (to == address(0)) revert ZeroAddress();
        uint256 fromBal = _balanceOf[msg.sender];
        if (fromBal < value) revert InsufficientBalance();
        unchecked {
            _balanceOf[msg.sender] = fromBal - value;
            _balanceOf[to] += value;
        }
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) external override returns (bool) {
        if (spender == address(0)) revert ZeroAddress();
        _allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) external returns (bool) {
        if (spender == address(0)) revert ZeroAddress();
        unchecked {
            _allowance[msg.sender][spender] += addedValue;
        }
        emit Approval(msg.sender, spender, _allowance[msg.sender][spender]);
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) external returns (bool) {
        if (spender == address(0)) revert ZeroAddress();
        uint256 currentAllowance = _allowance[msg.sender][spender];
        if (currentAllowance < subtractedValue) revert DecreaseAllowanceBelowZero();
        unchecked {
            _allowance[msg.sender][spender] = currentAllowance - subtractedValue;
        }
        emit Approval(msg.sender, spender, _allowance[msg.sender][spender]);
        return true;
    }

    function transferFrom(address from, address to, uint256 value) external override returns (bool) {
        if (from == address(0)) revert ZeroAddress();
        if (to == address(0)) revert ZeroAddress();
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

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
    string public constant name = "Rumeida Heritage";
    string public constant symbol = "ROUM";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 1_000_000_000 * 10**18;

    mapping(address => uint256) private _balanceOf;
    mapping(address => mapping(address => uint256)) private _allowance;

    constructor() {
        _balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function balanceOf(address account) public view override returns (uint256) {
        return _balanceOf[account];
    }

    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowance[owner][spender];
    }

    function transfer(address to, uint256 value) external override returns (bool) {
        require(to != address(0), "ROUM: transfer to zero address");
        uint256 fromBal = _balanceOf[msg.sender];
        require(fromBal >= value, "ROUM: insufficient balance");
        unchecked {
            _balanceOf[msg.sender] = fromBal - value;
            _balanceOf[to] += value;
        }
        emit Transfer(msg.sender, to, value);
        return true;
    }

    function approve(address spender, uint256 value) external override returns (bool) {
        require(spender != address(0), "ROUM: approve to zero address");
        _allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    function increaseAllowance(address spender, uint256 addedValue) external returns (bool) {
        require(spender != address(0), "ROUM: approve to zero address");
        _allowance[msg.sender][spender] += addedValue;
        emit Approval(msg.sender, spender, _allowance[msg.sender][spender]);
        return true;
    }

    function decreaseAllowance(address spender, uint256 subtractedValue) external returns (bool) {
        require(spender != address(0), "ROUM: approve to zero address");
        uint256 currentAllowance = _allowance[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ROUM: decreased allowance below zero");
        _allowance[msg.sender][spender] = currentAllowance - subtractedValue;
        emit Approval(msg.sender, spender, _allowance[msg.sender][spender]);
        return true;
    }

    function transferFrom(address from, address to, uint256 value) external override returns (bool) {
        require(from != address(0), "ROUM: transfer from zero address");
        require(to != address(0), "ROUM: transfer to zero address");
        uint256 fromBal = _balanceOf[from];
        require(fromBal >= value, "ROUM: insufficient balance");
        uint256 currentAllowance = _allowance[from][msg.sender];
        require(currentAllowance >= value, "ROUM: insufficient allowance");
        unchecked {
            _balanceOf[from] = fromBal - value;
            _balanceOf[to] += value;
            _allowance[from][msg.sender] = currentAllowance - value;
        }
        emit Transfer(from, to, value);
        return true;
    }
}

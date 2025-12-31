# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in ROUM Token, please **do not** open a public GitHub issue. Instead:

### Private Disclosure

1. **Email:** Send details to **Osamaqonaibe@outlook.com**
   - Subject: "ROUM Token Security Issue"
   - Include: Vulnerability description, severity, proof of concept

2. **Information to Provide:**
   - Detailed description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if applicable)

3. **Timeline:**
   - Initial response: Within 48 hours
   - Investigation: Within 7 days
   - Fix/patch: Within 14 days (depending on severity)
   - Public disclosure: After patch is released

## Security Best Practices

### For Users

- ✅ Verify contract address on official sources
- ✅ Check BSCScan for verified source code
- ✅ Use only official wallets and services
- ✅ Enable 2FA on exchange accounts
- ✅ Never share private keys or seed phrases
- ✅ Verify URLs before entering sensitive information

### For Developers

- ✅ Always verify contract address before integration
- ✅ Use the official ABI from our repository
- ✅ Test on BSC testnet first
- ✅ Implement proper error handling
- ✅ Audit your integration code
- ✅ Use established libraries (Web3.js, Ethers.js)

## Known Issues

None currently identified. All discovered issues are tracked and addressed promptly.

## Security Audit

- Contract verified on Sourcify: Full Match
- Contract verified on BSCScan: Full Match
- Compiler: Solidity 0.8.33 (with overflow protection)
- No external dependencies or known vulnerabilities

## Security Headers

When deploying related services:

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'
```

## Responsible Disclosure

We follow responsible disclosure practices:

1. Issues reported privately will be investigated confidentially
2. Patches will be developed and tested
3. Responsible reporters will be credited
4. Public disclosure occurs only after patch release

## Contact

- 📧 **Primary:** [Osamaqonaibe@outlook.com](mailto:Osamaqonaibe@outlook.com)
- 🐛 **Bug Reports:** [GitHub Issues](https://github.com/Osama-Qonaibe/ROUM-Token/issues)
- 📚 **Documentation:** [Security Docs](https://github.com/Osama-Qonaibe/ROUM-Token/blob/main/docs/SECURITY.md)

---

**Thank you for helping keep ROUM Token secure!** 🔒
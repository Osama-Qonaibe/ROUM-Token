# ROUM Token - Scripts

## CertiK Audit Charts Generator

### Overview

This directory contains professional Python scripts for generating security audit visualization charts for ROUM Token's CertiK audit documentation.

### Files

- `generate_charts.py` - Main chart generation script

### Requirements

```bash
pip install matplotlib numpy
```

### Usage

```bash
cd scripts/
python3 generate_charts.py
```

### Output

The script generates 7 professional charts in `../assets/charts/`:

1. **certik_score_dashboard.png** - Overall security score gauge (97/100)
2. **industry_comparison.png** - Comparison with major cryptocurrencies
3. **test_results.png** - Test results pie chart (22/23 passed)
4. **risk_assessment.png** - Risk assessment matrix
5. **gas_optimization.png** - Gas optimization analysis
6. **code_quality_profile.png** - 8-dimensional code quality radar chart
7. **vulnerability_scan.png** - Comprehensive vulnerability checklist

### Features

- ✅ High-resolution PNG output (300 DPI)
- ✅ Professional color schemes
- ✅ Auto-creates output directory
- ✅ Cross-platform compatibility
- ✅ Dynamic chart list generation
- ✅ Fully documented code
- ✅ MIT License

### Chart Specifications

All charts are designed to match ROUM Token's brand guidelines:
- Primary color: `#00cc44` (Green)
- Background: White
- Professional fonts (DejaVu Sans)
- Clean, modern design

### Integration

These charts are used in `docs/CERTIK-AUDIT-VISUAL.md` to provide professional visualization of the CertiK security audit results.

### License

MIT License - See root LICENSE file

### Author

Osama Qonaibe  
GitHub: [@Osama-Qonaibe](https://github.com/Osama-Qonaibe)

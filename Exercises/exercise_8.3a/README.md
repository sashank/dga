# Exercise 8.3A: DGA Reverse Engineering

**Type**: Hands-on Implementation  
**Duration**: 3-4 hours  
**Difficulty**: Intermediate

## Scenario

As a malware analyst, you've captured network traffic from an infected host attempting to contact C&C servers. You observe 50 failed DNS queries to seemingly random domains. Your task is to reverse-engineer the DGA algorithm and predict future domains for proactive blocking.

## Learning Objectives

By completing this exercise, you will:
- Reverse-engineer DGA algorithms from observed domains
- Implement multiple DGA types in Python
- Generate predictive blocklists for proactive defense
- Understand differences between DGA families

## Prerequisites

- Intermediate Python programming
- Understanding of DGA fundamentals (Chapter 8, Section 8.3)
- Basic cryptography concepts (hashing)

## Setup Instructions

### 1. Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn hashlib random datetime
```

### 2. Dataset

Sample DGA domains are provided in `data/dga_samples.csv` with three different families for analysis.

### 3. Launch Jupyter Notebook

```bash
cd exercise_8.3a
jupyter notebook exercise_8.3a_dga_reverse_engineering.ipynb
```

## Tasks Overview

### Task 1: Pattern Recognition
- Analyze 50 domains from unknown DGA
- Calculate entropy, length distribution, character patterns
- Identify TLD preferences and generation patterns

### Task 2: Algorithm Reconstruction
- Implement 3 candidate DGA algorithms (arithmetic, dictionary, hash-based)
- Test each against observed domains
- Identify the correct DGA type and seed

### Task 3: Proactive Defense
- Generate 7-day domain forecast
- Create blocklist for firewall/DNS sinkhole
- Design SIEM monitoring queries

### Task 4: DGA Comparison
- Compare 3 DGA types
- Analyze detection difficulty

## Deliverables

1. **Jupyter Notebook**: Complete implementations with analysis
2. **7-Day Domain Forecast**: CSV file with predicted domains
3. **Technical Report**: 3-4 pages analyzing findings
4. **SIEM Queries**: Templates for threat hunting

## Success Criteria

- ✅ Successfully identify DGA type for provided samples
- ✅ Implement 3 DGA variants (arithmetic, dictionary, hash-based)
- ✅ Generate accurate 7-day forecast (>90% match with actual)
- ✅ Create usable blocklists and SIEM queries

## Resources

- **Datasets**: `data/dga_samples.csv` (3 DGA families)
- **Chapter Reference**: Chapter 8, Section 8.3
- **DGA Research**: Conficker, Cryptolocker, Matsnu case studies

## Tips

1. **Start with Statistics**: Calculate entropy, length, character frequency before coding
2. **Test Incrementally**: Verify each DGA implementation with known examples
3. **Visualize Patterns**: Use plots to identify time-based seeds
4. **Think Like Attacker**: Why would they choose this algorithm?

## Common Issues

**Issue**: Hash-based DGA doesn't match  
**Solution**: Check date format (YYYYMMDD vs. timestamp), hash algorithm (MD5 vs. SHA256)

**Issue**: Dictionary DGA generates invalid domains  
**Solution**: Verify word list matches expected dictionary, check TLD selection logic

**Issue**: Can't predict future domains  
**Solution**: Ensure seed derivation is time-based, test with known dates first

## Submission

Submit via course platform:
1. Completed Jupyter notebook (`.ipynb` file)
2. 7-day forecast CSV (`forecast_7day.csv`)
3. Technical report (PDF)
4. SIEM query templates (`.txt` or `.json`)

---

**Version**: 1.0  
**Last Updated**: January 31, 2026  
**Contact**: Instructor via course forum

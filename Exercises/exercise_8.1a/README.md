# Exercise 8.1A: DNS Traffic Pattern Analysis

**Type**: Analytical Exercise  
**Duration**: 2-3 hours  
**Difficulty**: Beginner-Intermediate

## Scenario

You are a junior SOC analyst at a mid-sized enterprise. Your SIEM has captured 24 hours of DNS queries from the corporate network. Your task is to establish baseline patterns for legitimate DNS traffic to prepare for anomaly detection.

## Learning Objectives

By completing this exercise, you will:
- Understand DNS query structure and components
- Identify characteristics of legitimate domain traffic
- Establish baselines for anomaly detection
- Recognize temporal patterns in network behavior

## Prerequisites

- Basic Python programming
- Familiarity with Pandas and Matplotlib
- Understanding of DNS fundamentals (Chapter 8, Section 8.1)

## Setup Instructions

### 1. Install Required Libraries

```bash
pip install pandas matplotlib seaborn numpy
```

### 2. Download Dataset

For this exercise, we'll use the Cisco Umbrella Top 1M domains combined with synthetic DNS logs.

**Option A**: Use provided sample data (included in `data/` folder)  
**Option B**: Download full dataset:
- Cisco Umbrella Top 1M: http://s3-us-west-1.amazonaws.com/umbrella-static/top-1m.csv.zip

### 3. Launch Jupyter Notebook

```bash
cd exercise_8.1a
jupyter notebook exercise_8.1a_dns_traffic_analysis.ipynb
```

## Tasks Overview

### Task 1: Load and Explore DNS Query Logs
- Parse DNS query logs (timestamp, source IP, domain, query type)
- Calculate summary statistics

### Task 2: Domain Characteristic Analysis
- Extract domain components (SLD, TLD, subdomain count)
- Calculate length distributions
- Analyze character composition

### Task 3: Temporal Pattern Analysis
- Plot query volume by hour of day
- Identify periodic patterns
- Flag unusual temporal anomalies

### Task 4: Create Baseline Profile
- Document "normal" domain characteristics
- Establish thresholds for anomaly detection
- Design decision rules

## Deliverables

1. **Jupyter Notebook**: Complete analysis with code and visualizations
2. **Baseline Profile Document**: Summary statistics and threshold recommendations
3. **Decision Rule Matrix**: Rules for flagging suspicious patterns

## Success Criteria

- ✅ Successfully parse and load DNS logs (10,000+ queries)
- ✅ Generate at least 5 visualizations (TLD distribution, length histogram, temporal plot, etc.)
- ✅ Calculate baseline statistics (mean, median, std for key metrics)
- ✅ Define at least 3 anomaly detection rules with justification

## Resources

- **Dataset**: Provided in `data/sample_dns_logs.csv`
- **Chapter Reference**: Chapter 8, Section 8.1
- **Documentation**: See `docs/dns_log_format.md` for log format specification

## Tips

1. **Start Simple**: Load data first, explore with `.head()`, `.info()`, `.describe()`
2. **Visualize Early**: Plots reveal patterns faster than statistics alone
3. **Document Assumptions**: Note any data cleaning decisions
4. **Think Operationally**: Would a SOC analyst understand your thresholds?

## Common Issues

**Issue**: CSV parsing errors  
**Solution**: Check encoding (`encoding='utf-8'`) and delimiter

**Issue**: Memory errors with large datasets  
**Solution**: Use `chunksize` parameter in `pd.read_csv()`

**Issue**: Domain parsing errors (missing TLD)  
**Solution**: Handle edge cases (IP addresses, malformed domains)

## Submission

Submit via course platform:
1. Completed Jupyter notebook (`.ipynb` file)
2. Baseline profile document (PDF or Markdown)
3. Any generated data files (CSVs, plots)

---

**Version**: 1.0  
**Last Updated**: January 31, 2026  
**Contact**: Instructor via course forum

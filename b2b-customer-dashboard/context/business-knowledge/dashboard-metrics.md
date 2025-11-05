# Dashboard Metrics Definition

Complete reference for all metrics calculated and displayed in the B2B Customer Dashboard.

## Overview

The dashboard provides 9 interactive visualizations organized into three categories:
1. **Distribution Metrics** (Charts 1-7) - How customers are distributed across dimensions
2. **Trend Metrics** (Chart 8) - How metrics change over time
3. **Funnel Metrics** (Chart 9) - How customers progress through sales stages

---

## Chart 1: Phân bố Quy mô Công ty (Company Size Distribution)

### Metric Definition
Distribution of customers across company size segments.

### Data Source
- Field: `Company Size`
- Format: Categorical (ranges)

### Calculation
```
For each size category:
  Count = Number of customers in that category
  Percentage = (Count / Total Customers) × 100%
```

### Business Insight
- **Purpose:** Understand which company sizes we target most
- **Use Case:** Tailor marketing and service offerings by size
- **Action:** Focus resources on high-count segments

### Interpretation
- **High concentration in one size:** Niche focus (good or risky depending on strategy)
- **Balanced distribution:** Diversified customer base
- **Missing segments:** Opportunity or intentional exclusion

---

## Chart 2: Trạng thái Khách hàng (Top 10) (Client Status Top 10)

### Metric Definition
Top 10 most common client statuses and their distribution.

### Data Source
- Field: `Client Status`
- Format: Categorical

### Calculation
```
1. Count customers for each status
2. Select top 10 by count
3. Calculate percentage for each
```

### Business Insight
- **Purpose:** Monitor customer lifecycle states
- **Use Case:** Identify bottlenecks or issues in customer management
- **Action:** Address statuses with unexpected high counts

### Interpretation
- **High "Active" count:** Healthy engaged pipeline
- **High "Lost" count:** Investigate retention issues
- **High "Pending" count:** Follow-up needed

---

## Chart 3: Phân bố Giá trị Hợp đồng (Contract Value Distribution)

### Metric Definition
Distribution of estimated contract values across value ranges.

### Data Source
- Field: `Estimate Contract Value (Million VND)`
- Format: Numeric

### Calculation
```
Bins:
- <50M VND
- 50-100M VND
- 100-200M VND
- 200-500M VND
- 500M-1B VND
- >1B VND

For each bin:
  Count = Number of contracts in that range
```

### Business Insight
- **Purpose:** Understand deal size distribution
- **Use Case:** Resource allocation, sales strategy
- **Action:** Focus on high-value segments or increase volume in lower tiers

### Interpretation
- **Many small deals:** High volume, lower margin strategy
- **Few large deals:** High value, concentrated risk
- **Balanced mix:** Diversified revenue

### Key Metrics
- **Total Contract Value:** Sum of all estimated values
- **Average Contract Value:** Mean value per customer
- **Median Contract Value:** Middle value (less affected by outliers)

---

## Chart 4: Phân bố Nguồn Khách hàng (Top 8) (Customer Source Top 8)

### Metric Definition
Top 8 customer acquisition sources and their contribution.

### Data Source
- Field: `Source`
- Format: Categorical

### Calculation
```
1. Count customers from each source
2. Select top 8 sources
3. Group remaining as "Others"
4. Calculate percentages
```

### Business Insight
- **Purpose:** Evaluate marketing channel effectiveness
- **Use Case:** Marketing budget allocation
- **Action:** Invest more in high-performing channels, investigate underperforming ones

### Interpretation
- **Dominant source:** Strong channel, but risky concentration
- **Diverse sources:** Healthy multi-channel strategy
- **Low-performing source:** Poor ROI, needs optimization or elimination

---

## Chart 5: Top 10 Quận theo Số lượng (Top 10 Districts by Count)

### Metric Definition
Geographic distribution - districts with most potential customers.

### Data Source
- Field: `Location - District`
- Format: Categorical (geographic)

### Calculation
```
1. Count customers in each district
2. Sort by count descending
3. Select top 10
```

### Business Insight
- **Purpose:** Identify geographic hotspots
- **Use Case:** Territory planning, local marketing
- **Action:** Focus sales efforts, open local offices

### Interpretation
- **Concentrated in few districts:** Geographic clustering
- **Spread across many districts:** Broad coverage
- **High-value districts:** Priority for field sales

---

## Chart 6: Phân bố Ngân sách AHCU (AHCU Budget Distribution)

### Metric Definition
Distribution of Annual Health CheckUp budgets across ranges.

### Data Source
- Field: `AHCU Budget`
- Format: Numeric (VND)

### Calculation
```
Bins:
- <500K VND
- 500K-1M VND
- 1-2M VND
- 2-3M VND
- 3-5M VND
- >5M VND

For each bin:
  Count = Number of customers in that range
```

### Business Insight
- **Purpose:** Understand customer budget capacity
- **Use Case:** Package design, pricing strategy
- **Action:** Create service tiers matching budget distribution

### Interpretation
- **Many low-budget:** Need affordable packages
- **Many high-budget:** Opportunity for premium services
- **Mixed distribution:** Tiered pricing strategy

### Key Metrics
- **Total AHCU Budget:** Sum of all budgets
- **Average AHCU Budget:** Mean budget per customer

---

## Chart 7: Lý do Thất bại Deals (Top 10) (Failure Reasons Top 10)

### Metric Definition
Top 10 reasons why deals were lost.

### Data Source
- Field: `Reason Fail Deals`
- Format: Text (free form)

### Calculation
```
1. Filter customers where Outcome = "Lost"
2. Count each unique failure reason
3. Select top 10 by frequency
```

### Business Insight
- **Purpose:** Identify why deals fail
- **Use Case:** Process improvement, competitive response
- **Action:** Address top failure reasons systematically

### Interpretation
- **"Price too high":** Pricing strategy issue
- **"Chose competitor":** Competitive disadvantage
- **"No budget":** Targeting wrong customers
- **"Poor communication":** Internal process issue

### Actionable Insights
- Frequent price objections → Review pricing or value proposition
- Frequent competitor losses → Competitive analysis needed
- Service-related issues → Product improvement needed

---

## Chart 8: Xu hướng Doanh thu theo Tháng/Quý (Revenue Trend)

### Metric Definition
Time-series trend of estimated contract value (revenue proxy).

### Data Source
- Field: `Estimate Contract Value (Million VND)`
- Field: `Latest Action Date` (for time grouping)
- Format: Numeric + Date

### Calculation
```
Monthly:
  For each month:
    Revenue = Sum of contract values with activity in that month

Quarterly:
  For each quarter:
    Revenue = Sum of contract values with activity in that quarter
```

### Business Insight
- **Purpose:** Track revenue trajectory over time
- **Use Case:** Forecasting, performance monitoring
- **Action:** Investigate dips, amplify growth periods

### Interpretation
- **Upward trend:** Growth, positive momentum
- **Downward trend:** Decline, needs intervention
- **Seasonal pattern:** Plan for high/low periods
- **Volatility:** Inconsistent pipeline

### Key Metrics
- **Growth Rate:** % change period-over-period
- **Trend Line:** Direction of overall movement
- **Variance:** Stability/consistency of performance

---

## Chart 9: Sales Funnel - Pipeline Overview

### Metric Definition
Sales pipeline funnel showing customer count at each stage.

### Data Source
- Field: `Sales Stage`
- Format: Categorical (ordered)

### Calculation
```
Stages (in order):
1. Lead
2. Qualified
3. Proposal
4. Negotiation
5. Closed Won
6. Closed Lost

For each stage:
  Count = Number of customers at that stage
  Conversion Rate = (Next Stage Count / Current Stage Count) × 100%
```

### Business Insight
- **Purpose:** Visualize sales process efficiency
- **Use Case:** Identify bottlenecks, forecast closures
- **Action:** Improve stages with low conversion

### Interpretation
- **Wide top, narrow bottom:** Normal funnel, many leads → few conversions
- **Uniform width:** High conversion at all stages (very efficient)
- **Bottleneck at stage:** That stage needs improvement
- **High "Closed Lost":** Quality or process issues

### Key Metrics
- **Stage Conversion Rates:**
  - Lead → Qualified: Shows qualification effectiveness
  - Qualified → Proposal: Shows engagement success
  - Proposal → Negotiation: Shows value communication
  - Negotiation → Closed Won: Shows closing effectiveness

### Benchmarks
- **Lead → Qualified:** 30-50% (good)
- **Qualified → Proposal:** 40-60% (good)
- **Proposal → Negotiation:** 50-70% (good)
- **Negotiation → Closed Won:** 60-80% (good)

---

## Summary Metrics (Footer)

### Total Records
**Definition:** Count of all customer records in filtered dataset

**Calculation:**
```
Total Records = Count of all rows after applying filters
```

---

## Time Period Filters

All metrics can be filtered by:

### Dashboard Type
- **Monthly:** Aggregate and filter by month
- **Quarterly:** Aggregate and filter by quarter

### Year Filter
- **All Years:** Include all data
- **Specific Year:** Only data from selected year (e.g., 2025)

### Month Filter (Monthly Dashboard)
- **All Months:** Include entire year
- **Specific Month:** Only data from selected month

### Quarter Filter (Quarterly Dashboard)
- **All Quarters:** Include entire year
- **Specific Quarter:** Only data from selected quarter

### Filter Application
Filters applied to time-based fields:
- `Latest Action Date` (primary)
- `Calling Day` (fallback if Latest Action Date is empty)

---

## Data Quality Impact on Metrics

### Missing Data
- **Contract Value missing:** Excluded from Chart 3, 8
- **AHCU Budget missing:** Excluded from Chart 6
- **Date missing:** Excluded from time filters, Chart 8
- **Status/Stage missing:** Shows as "Unknown" or excluded

### Data Validation
- **Numeric fields:** Invalid values ignored
- **Date fields:** Invalid formats ignored
- **Categorical fields:** All values included (even typos)

### Recommendations
1. Ensure key fields are populated (Contract Value, Sales Stage, Client Status)
2. Use consistent date formats (DD/MM/YYYY)
3. Use standard status/stage values (avoid variations)
4. Regularly audit data quality

---

## Using Metrics for Decision Making

### Strategic Questions Answered

**"Where should we focus sales efforts?"**
→ Charts 1, 4, 5: Size segments, sources, and districts with most opportunities

**"Are we growing?"**
→ Chart 8: Revenue trend over time

**"Why are we losing deals?"**
→ Chart 7: Top failure reasons to address

**"Is our sales process efficient?"**
→ Chart 9: Funnel conversion rates

**"What's our pipeline worth?"**
→ Chart 3 + Summary: Total and distribution of contract values

**"Which customer segments are most valuable?"**
→ Cross-reference Charts 1, 3: Company size vs. contract value

---

## Metric Refresh Frequency

### Recommended Refresh Cadence
- **Daily:** For active sales teams (using `/refresh-data`)
- **Weekly:** For management reviews
- **Monthly:** For strategic planning

### Data Freshness
- Dashboard shows data as of last generation
- Timestamp displayed in footer
- Always refresh before important meetings

---

**Use these metrics to make data-driven decisions about your B2B customer pipeline!** 📊

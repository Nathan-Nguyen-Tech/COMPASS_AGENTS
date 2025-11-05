# Analyze Metrics Command

Perform deep-dive analysis on specific business metrics and generate detailed insights.

## Usage

```bash
/analyze-metrics [metric-name] [options]
```

## Parameters

- `metric-name`: The metric to analyze (see available metrics below)
- `--period`: Time period (monthly | quarterly | yearly) - Default: monthly
- `--compare`: Comparison type (mom | qoq | yoy) - Default: mom
- `--segment`: Segment by (source | size | district | industry) - Optional

## Available Metrics

### Volume Metrics
- `total-customers` - Total potential customer count
- `new-customers` - New customers acquired
- `active-pipeline` - Customers in active sales stages
- `closed-deals` - Successfully closed deals

### Value Metrics
- `contract-value` - Total estimated contract value
- `avg-contract-value` - Average contract value per deal
- `ahcu-budget` - Total AHCU budget
- `avg-ahcu-budget` - Average AHCU budget per customer

### Performance Metrics
- `conversion-rate` - Overall conversion rate
- `win-rate` - Win rate (won / (won + lost))
- `sales-cycle` - Average sales cycle length
- `stage-conversion` - Conversion rates between stages

### Distribution Metrics
- `by-source` - Customer distribution by source
- `by-size` - Customer distribution by company size
- `by-district` - Geographic distribution by district
- `by-industry` - Industry breakdown
- `by-stage` - Pipeline stage distribution

## Examples

### Analyze total contract value with month-over-month comparison
```bash
/analyze-metrics contract-value --period monthly --compare mom
```

### Analyze conversion rate by customer source
```bash
/analyze-metrics conversion-rate --segment source
```

### Analyze new customers quarterly with year-over-year comparison
```bash
/analyze-metrics new-customers --period quarterly --compare yoy
```

### Analyze company size distribution
```bash
/analyze-metrics by-size
```

## What This Command Does

1. **Activates Data Analyzer Agent**
   - Switches to specialized data analysis agent
   - Agent has access to data processing tools

2. **Fetches Required Data**
   - Retrieves data from Google Sheets via MCP
   - Filters data based on specified period
   - Prepares data for analysis

3. **Performs Analysis**
   - Calculates requested metric
   - Performs trend analysis
   - Identifies patterns and anomalies
   - Compares across time periods or segments

4. **Generates Insights**
   - Statistical summary
   - Trend visualization
   - Key findings
   - Actionable recommendations

5. **Creates Analysis Report**
   - Detailed metrics breakdown
   - Comparison charts
   - Insight bullets
   - Recommendations

## Output

### Console Output
```
📊 Analyzing: Contract Value
Period: Monthly (Jan 2025 - Dec 2025)
Comparison: Month-over-Month

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 Summary Statistics:
  • Total Contract Value: 1,320M VND
  • Average per Month: 110M VND
  • Highest Month: March (185M VND)
  • Lowest Month: February (65M VND)
  • Growth Rate: +15.3% avg MoM

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 Key Insights:

  ✅ Strong Growth Trend
     Contract value increased 45% from Q1 to Q2
     Driven by 3 large deals (>100M each)

  ⚠️  February Dip
     Lowest month due to Tet holiday period
     Expected seasonal pattern

  💡 Top Contributors
     District 1: 320M VND (24% of total)
     Technology sector: 280M VND (21% of total)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 Recommendations:

  1. Focus Q3 efforts on replicating Q2 success
     Target similar company profiles (Tech, 100+ employees)

  2. Prepare for Q1 2026 Tet slowdown
     Front-load January deals, plan February campaigns

  3. Expand District 1 strategy to Districts 3, 7
     Similar demographics, untapped potential

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 Detailed report saved to:
   workspace/analysis/contract_value_analysis_2025.json

📊 Visualization saved to:
   workspace/analysis/contract_value_chart.html
```

### Generated Files

**JSON Report**: `workspace/analysis/{metric}_analysis_{date}.json`
```json
{
  "metric": "contract-value",
  "period": "monthly",
  "date_range": {
    "start": "2025-01-01",
    "end": "2025-12-31"
  },
  "summary": {
    "total": 1320000000,
    "average": 110000000,
    "median": 105000000,
    "std_dev": 35000000
  },
  "trend": {
    "direction": "increasing",
    "growth_rate": 0.153,
    "r_squared": 0.78
  },
  "insights": [
    {
      "type": "positive",
      "title": "Strong Growth Trend",
      "description": "...",
      "impact": "high"
    }
  ],
  "recommendations": [...]
}
```

**HTML Chart**: Interactive visualization of the metric
- Trend line
- Period comparisons
- Segment breakdowns
- Annotations for key events

## Analysis Types

### Trend Analysis
Shows how metric changes over time:
- Line chart with trend line
- Growth rate calculation
- Momentum indicators
- Forecasting (simple linear projection)

### Comparative Analysis
Compares across segments:
- Bar chart by segment
- Percentage distribution
- Top/bottom performers
- Statistical significance

### Distribution Analysis
Shows spread of values:
- Histogram or box plot
- Quartile analysis
- Outlier detection
- Concentration metrics (Gini, HHI)

### Cohort Analysis
Tracks customer cohorts over time:
- Retention curves
- Cohort comparison
- Maturation patterns

## Advanced Usage

### Combine Multiple Metrics
```bash
# Analyze multiple related metrics
/analyze-metrics conversion-rate,sales-cycle,win-rate --period quarterly
```

### Drill-down Analysis
```bash
# Analyze District 1 specifically
/analyze-metrics contract-value --segment district --filter "District 1"
```

### Custom Date Range
```bash
# Analyze specific time range
/analyze-metrics new-customers --start 2025-01-01 --end 2025-06-30
```

## Interpretation Guide

### Growth Indicators
- **>20% MoM**: Exceptional growth, investigate sustainability
- **10-20% MoM**: Strong growth, maintain momentum
- **0-10% MoM**: Moderate growth, look for acceleration opportunities
- **<0% MoM**: Decline, investigate root causes urgently

### Conversion Benchmarks
- **>30%**: Excellent, best-in-class
- **20-30%**: Good, competitive
- **10-20%**: Average, room for improvement
- **<10%**: Below expectations, needs attention

### Distribution Health
- **Gini <0.5**: Well-distributed
- **Gini 0.5-0.7**: Moderately concentrated
- **Gini >0.7**: Highly concentrated, risky

## Use Cases

### Weekly Sales Review
```bash
/analyze-metrics new-customers,closed-deals --period weekly
```

### Monthly Business Review
```bash
/analyze-metrics contract-value --compare mom
/analyze-metrics conversion-rate --segment source
```

### Quarterly Strategic Planning
```bash
/analyze-metrics by-industry --period quarterly --compare qoq
/analyze-metrics stage-conversion --period quarterly
```

### Performance Diagnostics
```bash
# Why are conversions dropping?
/analyze-metrics conversion-rate --segment size
/analyze-metrics sales-cycle --period monthly

# Where should we focus efforts?
/analyze-metrics by-district --period quarterly
```

## Integration with Dashboard

The analyze-metrics command complements the dashboard:

**Dashboard**: High-level overview, multiple metrics at once
**Analyze-Metrics**: Deep dive into single metric, detailed insights

Typical workflow:
1. View dashboard to spot trends
2. Use `/analyze-metrics` for deep dive
3. Generate insights and recommendations
4. Update strategy based on findings
5. Refresh dashboard to track progress

## Troubleshooting

### "Not enough data for analysis"
- Need at least 3 data points for trend analysis
- Extend date range or use different period

### "Segment has too many values"
- Use `--top 10` to limit to top segments
- Or filter to specific segment values

### "Analysis takes too long"
- Large dataset, consider filtering by date range
- Use sampling for exploratory analysis

## Best Practices

1. **Regular cadence**: Analyze key metrics weekly/monthly
2. **Compare periods**: Always use comparison (MoM, QoQ, YoY)
3. **Segment analysis**: Break down by relevant dimensions
4. **Action-oriented**: Focus on actionable insights
5. **Document findings**: Save reports for historical reference
6. **Share insights**: Distribute to relevant stakeholders

## Related Commands

- `/generate-dashboard` - High-level overview dashboard
- `/refresh-data` - Update dashboard with latest data

---

**Dive deep into your metrics with `/analyze-metrics`!** 📈

#!/usr/bin/env python3
"""
B2B Customer Dashboard Generator

Generates interactive web dashboards from Google Sheets data using Plotly.js.
Designed to work with MCP server-gdrive for data access.

Usage:
    python dashboard_generator.py
    python dashboard_generator.py --type monthly --year 2025 --month 6
    python dashboard_generator.py --type quarterly --year 2025 --quarter 2
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

try:
    from data_processor import DataProcessor
    from chart_builder import ChartBuilder
except ImportError:
    print("WARNING -  Required modules not found. They will be created by Claude.")
    sys.exit(1)


class DashboardGenerator:
    """Main dashboard generator class."""

    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize dashboard generator.

        Args:
            data_path: Path to JSON data file (from MCP gdrive export)
        """
        self.data_path = data_path
        self.processor = DataProcessor()
        self.chart_builder = ChartBuilder()
        self.template_path = Path(__file__).parent.parent / "templates" / "dashboard_template.html"
        self.output_dir = Path(__file__).parent.parent.parent / "workspace" / "dashboards" / "generated"

        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def load_data(self, data: Optional[List[Dict]] = None) -> List[Dict]:
        """
        Load customer data from file or direct input.

        Args:
            data: Direct data input (from MCP call)

        Returns:
            List of customer records
        """
        if data:
            return data

        if not self.data_path:
            raise ValueError("No data provided. Either pass data directly or specify data_path.")

        data_file = Path(self.data_path)
        if not data_file.exists():
            raise FileNotFoundError(f"Data file not found: {self.data_path}")

        with open(data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def generate(self,
                 data: Optional[List[Dict]] = None,
                 dashboard_type: str = "monthly",
                 year: Optional[int] = None,
                 month: Optional[int] = None,
                 quarter: Optional[int] = None,
                 output_path: Optional[str] = None) -> str:
        """
        Generate complete dashboard.

        Args:
            data: Customer data (list of dicts)
            dashboard_type: "monthly" or "quarterly"
            year: Year filter
            month: Month filter (1-12)
            quarter: Quarter filter (1-4)
            output_path: Custom output path

        Returns:
            Path to generated dashboard HTML file
        """
        print("INFO: Generating B2B Customer Dashboard...")
        print()

        # Load data
        print("INFO: Loading data...")
        raw_data = self.load_data(data)
        print(f"   Loaded {len(raw_data)} records")

        # Process and filter data
        print("INFO: Processing and filtering data...")
        filters = {
            'type': dashboard_type,
            'year': year,
            'month': month,
            'quarter': quarter
        }
        processed_data = self.processor.process(raw_data, filters)
        print(f"   {len(processed_data)} records after filtering")

        if len(processed_data) == 0:
            print("WARNING -  No data matches the specified filters.")
            return None

        # Calculate metrics
        print("INFO: Calculating metrics...")
        metrics = self.processor.calculate_metrics(processed_data)

        # Generate charts
        print("INFO: Generating charts...")
        charts = self._generate_all_charts(processed_data, dashboard_type)

        # Load template
        print("INFO: Loading dashboard template...")
        template = self._load_template()

        # Inject data into template
        print("INFO: Building final dashboard...")
        dashboard_html = self._build_dashboard(template, charts, metrics, filters)

        # Save dashboard
        if output_path:
            output_file = Path(output_path)
        else:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.output_dir / f"dashboard_{timestamp}.html"

        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(dashboard_html)

        print()
        print("OK - Dashboard generated successfully!")
        print(f"INFO: Saved to: {output_file}")
        print()

        # Print summary
        self._print_summary(metrics, filters)

        return str(output_file)

    def _generate_all_charts(self, data: List[Dict], dashboard_type: str) -> Dict[str, str]:
        """Generate all 9 charts as Plotly JSON specifications."""
        charts = {}

        print("   1. Phn b Quy m Cng ty...")
        charts['company_size'] = self.chart_builder.company_size_distribution(data)

        print("   2. Trng thi Khch hng (Top 10)...")
        charts['client_status'] = self.chart_builder.client_status_top10(data)

        print("   3. Phn b Gi tr Hp ng...")
        charts['contract_value'] = self.chart_builder.contract_value_distribution(data)

        print("   4. Phn b Ngun Khch hng (Top 8)...")
        charts['customer_source'] = self.chart_builder.customer_source_top8(data)

        print("   5. Top 10 Qun theo S lng...")
        charts['top_districts'] = self.chart_builder.top_districts(data)

        print("   6. Phn b Ngn sch AHCU...")
        charts['ahcu_budget'] = self.chart_builder.ahcu_budget_distribution(data)

        print("   7. L do Tht bi Deals (Top 10)...")
        charts['failure_reasons'] = self.chart_builder.failure_reasons_top10(data)

        print("   8. Xu hng Doanh thu...")
        charts['revenue_trend'] = self.chart_builder.revenue_trend(data, dashboard_type)

        print("   9. Sales Funnel - Pipeline Overview...")
        charts['sales_funnel'] = self.chart_builder.sales_funnel(data)

        return charts

    def _load_template(self) -> str:
        """Load dashboard HTML template."""
        if not self.template_path.exists():
            raise FileNotFoundError(f"Template not found: {self.template_path}")

        with open(self.template_path, 'r', encoding='utf-8') as f:
            return f.read()

    def _build_dashboard(self, template: str, charts: Dict[str, str],
                        metrics: Dict[str, Any], filters: Dict[str, Any]) -> str:
        """
        Inject charts, metrics, and raw data into HTML template.

        Replaces placeholders:
        - {{CHART_COMPANY_SIZE}} with actual Plotly chart JSON
        - {{METRIC_TOTAL_CUSTOMERS}} with actual value
        - {{RAW_DATA}} with complete raw data for client-side filtering
        - etc.
        """
        dashboard = template

        # Inject raw data for client-side filtering
        # This allows the dashboard to filter and regenerate charts without backend
        raw_data_json = json.dumps(self.processor.raw_data, ensure_ascii=False, indent=2)
        dashboard = dashboard.replace("{{RAW_DATA}}", raw_data_json)

        # Inject charts
        for chart_name, chart_json in charts.items():
            placeholder = f"{{{{CHART_{chart_name.upper()}}}}}"
            dashboard = dashboard.replace(placeholder, chart_json)

        # Inject metrics
        for metric_name, metric_value in metrics.items():
            placeholder = f"{{{{METRIC_{metric_name.upper()}}}}}"
            dashboard = dashboard.replace(placeholder, str(metric_value))

        # Inject filters
        filter_summary = self._format_filter_summary(filters)
        dashboard = dashboard.replace("{{FILTER_SUMMARY}}", filter_summary)

        # Inject timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dashboard = dashboard.replace("{{TIMESTAMP}}", timestamp)

        return dashboard

    def _format_filter_summary(self, filters: Dict[str, Any]) -> str:
        """Format filter summary for display."""
        parts = []

        if filters.get('type'):
            parts.append(f"Type: {filters['type'].capitalize()}")

        if filters.get('year'):
            parts.append(f"Year: {filters['year']}")

        if filters.get('month'):
            parts.append(f"Month: {filters['month']}")

        if filters.get('quarter'):
            parts.append(f"Quarter: Q{filters['quarter']}")

        if not parts:
            return "All data (no filters applied)"

        return " | ".join(parts)

    def _print_summary(self, metrics: Dict[str, Any], filters: Dict[str, Any]):
        """Print dashboard summary."""
        print("" * 60)
        print("INFO: Dashboard Summary")
        print("" * 60)
        print()
        print(f"Filters: {self._format_filter_summary(filters)}")
        print()
        print(f"Total Customers: {metrics.get('total_customers', 0):,}")
        print(f"Total Contract Value: {metrics.get('total_contract_value', 0):,.0f} M VND")
        print(f"Average Contract Value: {metrics.get('avg_contract_value', 0):,.0f} M VND")
        print(f"Total AHCU Budget: {metrics.get('total_ahcu_budget', 0):,.0f} VND")
        print()
        print("" * 60)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Generate B2B Customer Dashboard from Google Sheets data"
    )

    parser.add_argument(
        '--data',
        type=str,
        help='Path to JSON data file (optional if using MCP)'
    )

    parser.add_argument(
        '--type',
        type=str,
        choices=['monthly', 'quarterly'],
        default='monthly',
        help='Dashboard type (default: monthly)'
    )

    parser.add_argument(
        '--year',
        type=int,
        help='Year filter (e.g., 2025)'
    )

    parser.add_argument(
        '--month',
        type=int,
        choices=range(1, 13),
        help='Month filter (1-12, only for monthly type)'
    )

    parser.add_argument(
        '--quarter',
        type=int,
        choices=range(1, 5),
        help='Quarter filter (1-4, only for quarterly type)'
    )

    parser.add_argument(
        '--output',
        type=str,
        help='Output file path (default: auto-generated in workspace/dashboards/generated/)'
    )

    args = parser.parse_args()

    try:
        generator = DashboardGenerator(data_path=args.data)
        output_path = generator.generate(
            dashboard_type=args.type,
            year=args.year,
            month=args.month,
            quarter=args.quarter,
            output_path=args.output
        )

        if output_path:
            print(f" Open in browser: file://{Path(output_path).absolute()}")
            print()
            print(" Tip: Use /refresh-data to update with latest Google Sheets data")
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception as e:
        print(f"ERROR - Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

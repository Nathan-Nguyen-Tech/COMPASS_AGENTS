#!/usr/bin/env python3
"""
Data Processor for B2B Customer Dashboard

Handles data cleaning, validation, filtering, and metrics calculation.
"""

from datetime import datetime
from typing import Dict, List, Any, Optional
import re


class DataProcessor:
    """Process and analyze B2B customer data."""

    # Field name mappings (handle variations in column names)
    # Maps normalized names to actual Google Sheets field names
    FIELD_MAPPING = {
        'customer_id': ['Customer ID', 'CustomerID', 'customer_id'],
        'company_name': ['Company Legal Name', 'Company Name', 'company_name'],
        'company_size': ['Company Size', 'company_size'],
        'industry': ['Industry', 'industry'],
        'location': ['Location', 'location'],
        'district': ['Location - District', 'District', 'district'],
        'source': ['Source', 'source'],
        'client_status': ['Client Status', 'client_status'],
        'sales_stage': ['Sales Stage', 'sales_stage'],
        'contract_value': ['Estimate Contract Value\n(Million VND)', 'Estimate Contract Value (Million VND)', 'Contract Value', 'contract_value'],
        'ahcu_budget': ['AHCU Budget', 'ahcu_budget'],
        'reason_fail': ['Reason Fail Deals', 'reason_fail'],
        'calling_day': ['Calling Day', 'calling_day'],
        'latest_action_date': ['Latest Action Date', 'latest_action_date'],
        'pipeline_week': ['PIPELINE WEEK', 'pipeline_week'],
        'sales_incharge': ['Sales Incharge', 'sales_incharge'],
        'intern_incharge': ['Intern Incharge', 'intern_incharge'],
        'hr_pic_name': ['HR/PIC Name', 'hr_pic_name'],
        'hr_pic_title': ['HR/PIC Title', 'hr_pic_title'],
        'hr_pic_phone': ['HR/PIC Phone', 'hr_pic_phone'],
        'hr_pic_email': ['HR/PIC Email', 'hr_pic_email'],
        'actual_employee_count': ['Số lượng NV thực tế', 'actual_employee_count'],
        'last_vendor': ['Last Vendor', 'last_vendor'],
        'outcome': ['Outcome', 'outcome'],
        'expectation_this_year': ['Expectation this year', 'expectation_this_year'],
        'ahcu_schedule': ['AHCU Schedule', 'ahcu_schedule'],
        'calling_status': ['Calling Status', 'calling_status'],
        'est_month_to_close': ['Est Month to close', 'est_month_to_close'],
        'next_action': ['Next Action (What will offer)', 'next_action'],
        'approach_method': ['Phương thức tiếp cận', 'approach_method'],
        'next_action_timeline': ['Next Action (Timeline)', 'next_action_timeline'],
        'note': ['Note', 'note'],
        'trial': ['Trial', 'trial'],
        'distance': ['Distance', 'distance'],
    }

    def __init__(self):
        """Initialize data processor."""
        self.raw_data = []
        self.processed_data = []

    def process(self, data: List[Dict], filters: Optional[Dict] = None) -> List[Dict]:
        """
        Process raw data: clean, validate, and filter.

        Args:
            data: Raw customer data
            filters: Filter criteria (type, year, month, quarter)

        Returns:
            Processed and filtered data
        """
        self.raw_data = data

        # Clean and normalize data
        cleaned_data = [self._clean_record(record) for record in data]

        # Validate data
        validated_data = [record for record in cleaned_data if self._validate_record(record)]

        # Apply filters
        if filters:
            filtered_data = self._apply_filters(validated_data, filters)
        else:
            filtered_data = validated_data

        self.processed_data = filtered_data
        return filtered_data

    def _clean_record(self, record: Dict) -> Dict:
        """
        Clean and normalize a single record.

        - Normalize field names
        - Trim whitespace
        - Convert data types
        - Handle Vietnamese characters
        """
        cleaned = {}

        for field_key, field_variants in self.FIELD_MAPPING.items():
            # Find the actual field name in the record
            value = None
            for variant in field_variants:
                if variant in record:
                    value = record[variant]
                    break

            # Clean the value
            if value is not None:
                if isinstance(value, str):
                    value = value.strip()
                    # Convert "N/A", "null", empty strings to None
                    if value.lower() in ['n/a', 'null', 'none', '']:
                        value = None

            cleaned[field_key] = value

        # Keep original record as well (for fields not in mapping)
        cleaned['_original'] = record

        return cleaned

    def _validate_record(self, record: Dict) -> bool:
        """
        Validate record has minimum required fields.

        Required fields:
        - customer_id OR company_name (at least one)
        """
        has_id = record.get('customer_id') is not None
        has_name = record.get('company_name') is not None

        return has_id or has_name

    def _apply_filters(self, data: List[Dict], filters: Dict) -> List[Dict]:
        """
        Apply filters to data.

        Filters:
        - year: Filter by year (from calling_day or latest_action_date)
        - month: Filter by month (1-12)
        - quarter: Filter by quarter (1-4)
        """
        filtered = data

        # Year filter
        if filters.get('year'):
            filtered = [r for r in filtered if self._matches_year(r, filters['year'])]

        # Month filter
        if filters.get('month'):
            filtered = [r for r in filtered if self._matches_month(r, filters['month'])]

        # Quarter filter
        if filters.get('quarter'):
            filtered = [r for r in filtered if self._matches_quarter(r, filters['quarter'])]

        return filtered

    def _matches_year(self, record: Dict, year: int) -> bool:
        """Check if record matches year filter."""
        date_str = record.get('latest_action_date') or record.get('calling_day')
        if not date_str:
            return False

        try:
            date_obj = self._parse_date(date_str)
            return date_obj.year == year
        except:
            return False

    def _matches_month(self, record: Dict, month: int) -> bool:
        """Check if record matches month filter."""
        date_str = record.get('latest_action_date') or record.get('calling_day')
        if not date_str:
            return False

        try:
            date_obj = self._parse_date(date_str)
            return date_obj.month == month
        except:
            return False

    def _matches_quarter(self, record: Dict, quarter: int) -> bool:
        """Check if record matches quarter filter."""
        date_str = record.get('latest_action_date') or record.get('calling_day')
        if not date_str:
            return False

        try:
            date_obj = self._parse_date(date_str)
            month_to_quarter = {
                1: 1, 2: 1, 3: 1,
                4: 2, 5: 2, 6: 2,
                7: 3, 8: 3, 9: 3,
                10: 4, 11: 4, 12: 4
            }
            return month_to_quarter.get(date_obj.month) == quarter
        except:
            return False

    def _parse_date(self, date_str: str) -> datetime:
        """
        Parse date string in various formats.

        Supports:
        - DD/MM/YYYY (Vietnamese format - priority)
        - YYYY-MM-DD
        - MM/DD/YYYY
        """
        if not date_str:
            raise ValueError("Empty date string")

        date_str = date_str.strip()

        if not date_str:
            raise ValueError("Empty date string after strip")

        # Try DD/MM/YYYY (Vietnamese format - most common)
        try:
            return datetime.strptime(date_str, '%d/%m/%Y')
        except:
            pass

        # Try YYYY-MM-DD
        try:
            return datetime.strptime(date_str, '%Y-%m-%d')
        except:
            pass

        # Try MM/DD/YYYY
        try:
            return datetime.strptime(date_str, '%m/%d/%Y')
        except:
            pass

        raise ValueError(f"Unable to parse date: {date_str}")

    def calculate_metrics(self, data: List[Dict]) -> Dict[str, Any]:
        """
        Calculate key metrics from processed data.

        Returns:
            Dictionary of metrics
        """
        metrics = {}

        # Total customers
        metrics['total_customers'] = len(data)

        # Contract value metrics
        contract_values = [
            self._parse_number(r.get('contract_value'))
            for r in data
            if r.get('contract_value')
        ]
        contract_values = [v for v in contract_values if v is not None and v > 0]

        # Convert to Million VND if values are in full VND (> 1,000,000)
        contract_values_m = [v / 1000000 if v > 1000000 else v for v in contract_values]

        metrics['total_contract_value'] = sum(contract_values_m)
        metrics['avg_contract_value'] = sum(contract_values_m) / len(contract_values_m) if contract_values_m else 0
        metrics['max_contract_value'] = max(contract_values_m) if contract_values_m else 0
        metrics['min_contract_value'] = min(contract_values_m) if contract_values_m else 0

        # AHCU budget metrics
        budgets = [
            self._parse_number(r.get('ahcu_budget'))
            for r in data
            if r.get('ahcu_budget')
        ]
        budgets = [b for b in budgets if b is not None and b > 0]

        metrics['total_ahcu_budget'] = sum(budgets)
        metrics['avg_ahcu_budget'] = sum(budgets) / len(budgets) if budgets else 0

        # Distribution metrics
        metrics['num_sources'] = len(set(r.get('source') for r in data if r.get('source')))
        metrics['num_districts'] = len(set(r.get('district') for r in data if r.get('district')))
        metrics['num_industries'] = len(set(r.get('industry') for r in data if r.get('industry')))

        # Stage metrics
        stages = [r.get('sales_stage') for r in data if r.get('sales_stage')]
        metrics['active_pipeline'] = len([s for s in stages if s and 'close' not in s.lower() and 'lost' not in s.lower()])

        return metrics

    def _parse_number(self, value: Any) -> Optional[float]:
        """
        Parse number from various formats.

        Handles:
        - Strings with commas: "1,000,000"
        - Strings with units: "1M", "1.5M"
        - Vietnamese currency: "1,750,000,000 ₫"
        - Numbers
        """
        if value is None:
            return None

        if isinstance(value, (int, float)):
            return float(value)

        if isinstance(value, str):
            # Remove whitespace
            value = value.strip()

            # Remove currency symbols (₫, VND, etc.)
            value = value.replace('₫', '').replace('VND', '').replace('đ', '')

            # Remove whitespace again after removing symbols
            value = value.strip()

            # Remove commas
            value = value.replace(',', '')

            # Handle "M" suffix (millions)
            if value.endswith('M') or value.endswith('m'):
                try:
                    return float(value[:-1])
                except:
                    return None

            # Try direct float conversion
            try:
                return float(value)
            except:
                return None

        return None

    def get_top_n(self, data: List[Dict], field: str, n: int = 10) -> List[tuple]:
        """
        Get top N values for a field.

        Returns:
            List of (value, count) tuples, sorted by count descending
        """
        from collections import Counter

        values = [r.get(field) for r in data if r.get(field)]
        counter = Counter(values)

        return counter.most_common(n)

    def get_distribution(self, data: List[Dict], field: str, bins: Optional[List] = None) -> Dict[str, int]:
        """
        Get distribution of values for a field.

        Args:
            data: Data to analyze
            field: Field name
            bins: Optional bin edges for numeric fields

        Returns:
            Dictionary of {value/bin: count}
        """
        if bins:
            # Numeric binning
            return self._bin_numeric_data(data, field, bins)
        else:
            # Categorical distribution
            from collections import Counter
            values = [r.get(field) for r in data if r.get(field)]
            return dict(Counter(values))

    def _bin_numeric_data(self, data: List[Dict], field: str, bins: List) -> Dict[str, int]:
        """Bin numeric data into ranges."""
        values = [
            self._parse_number(r.get(field))
            for r in data
            if r.get(field)
        ]
        values = [v for v in values if v is not None]

        binned = {f"{bins[i]}-{bins[i+1]}": 0 for i in range(len(bins) - 1)}

        for value in values:
            for i in range(len(bins) - 1):
                if bins[i] <= value < bins[i + 1]:
                    bin_label = f"{bins[i]}-{bins[i+1]}"
                    binned[bin_label] = binned.get(bin_label, 0) + 1
                    break

        return binned

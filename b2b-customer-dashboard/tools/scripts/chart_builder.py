#!/usr/bin/env python3
"""
Chart Builder for B2B Customer Dashboard

Generates Plotly.js chart specifications in JSON format.
"""

import json
from typing import Dict, List, Any
from collections import Counter


class ChartBuilder:
    """Build Plotly.js charts for the dashboard."""

    # Color palettes
    COLORS = {
        'primary': ['#667eea', '#764ba2', '#f093fb', '#4facfe'],
        'multi': [
            '#667eea', '#f093fb', '#4facfe', '#43e97b',
            '#fa709a', '#fee140', '#30cfd0', '#c471ed',
            '#f38181', '#95e1d3'
        ],
        'blue_gradient': ['#bfdbfe', '#93c5fd', '#60a5fa', '#3b82f6', '#2563eb', '#1d4ed8'],
        'green_gradient': ['#bbf7d0', '#86efac', '#4ade80', '#22c55e', '#16a34a', '#15803d'],
        'purple_gradient': ['#e9d5ff', '#d8b4fe', '#c084fc', '#a855f7', '#9333ea', '#7e22ce'],
        'red_gradient': ['#fecaca', '#fca5a5', '#f87171', '#ef4444', '#dc2626', '#b91c1c'],
        'orange_gradient': ['#fed7aa', '#fdba74', '#fb923c', '#f97316', '#ea580c', '#c2410c'],
    }

    def __init__(self):
        """Initialize chart builder."""
        pass

    def company_size_distribution(self, data: List[Dict]) -> str:
        """
        Chart 1: Phân bố Quy mô Công ty (Horizontal Bar)
        """
        # Get distribution
        sizes = [r.get('company_size') for r in data if r.get('company_size')]
        counter = Counter(sizes)
        total = sum(counter.values())

        # Sort by count
        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        labels = [item[0] for item in sorted_items]
        values = [item[1] for item in sorted_items]
        percentages = [f"{(v/total*100):.1f}%" for v in values]

        chart_data = {
            'data': [{
                'type': 'bar',
                'orientation': 'h',
                'x': values,
                'y': labels,
                'text': [f"{v} ({p})" for v, p in zip(values, percentages)],
                'textposition': 'outside',
                'marker': {
                    'color': self.COLORS['blue_gradient'],
                    'line': {'color': '#fff', 'width': 1}
                },
                'hovertemplate': '<b>%{y}</b><br>Số lượng: %{x}<br>%{text}<extra></extra>'
            }],
            'layout': {
                'title': {
                    'text': 'Phân bố Quy mô Công ty',
                    'font': {'size': 16, 'color': '#111827', 'family': 'Inter'}
                },
                'xaxis': {'title': 'Số lượng công ty'},
                'yaxis': {'title': ''},
                'margin': {'l': 150, 'r': 50, 't': 60, 'b': 60},
                'height': 400,
                'font': {'family': 'Inter', 'size': 12, 'color': '#374151'}
            },
            'config': self._get_config()
        }

        return json.dumps(chart_data, ensure_ascii=False)

    def client_status_top10(self, data: List[Dict]) -> str:
        """
        Chart 2: Trạng thái Khách hàng Top 10 (Horizontal Bar)
        """
        # Get distribution
        statuses = [r.get('client_status') for r in data if r.get('client_status')]
        counter = Counter(statuses)
        total = sum(counter.values())

        # Get top 10
        top_items = counter.most_common(10)

        labels = [item[0] for item in top_items]
        values = [item[1] for item in top_items]
        percentages = [f"{(v/total*100):.1f}%" for v in values]

        chart_data = {
            'data': [{
                'type': 'bar',
                'orientation': 'h',
                'x': values,
                'y': labels,
                'text': [f"{v} ({p})" for v, p in zip(values, percentages)],
                'textposition': 'outside',
                'marker': {
                    'color': self.COLORS['multi'][:10],
                    'line': {'color': '#fff', 'width': 1}
                },
                'hovertemplate': '<b>%{y}</b><br>Số lượng: %{x}<br>%{text}<extra></extra>'
            }],
            'layout': {
                'title': {
                    'text': 'Trạng thái Khách hàng (Top 10)',
                    'font': {'size': 16, 'color': '#111827', 'family': 'Inter'}
                },
                'xaxis': {'title': 'Số lượng'},
                'yaxis': {'title': ''},
                'margin': {'l': 180, 'r': 50, 't': 60, 'b': 60},
                'height': 450,
                'font': {'family': 'Inter', 'size': 12, 'color': '#374151'}
            },
            'config': self._get_config()
        }

        return json.dumps(chart_data, ensure_ascii=False)

    def contract_value_distribution(self, data: List[Dict]) -> str:
        """
        Chart 3: Phân bố Giá trị Hợp đồng (Vertical Bar)
        Bins: 0-50M, 50-100M, 100-200M, 200-500M, 500M+
        """
        bins = [0, 50, 100, 200, 500, float('inf')]
        labels = ['0-50M', '50-100M', '100-200M', '200-500M', '500M+']

        # Get values
        values = []
        for r in data:
            val_str = r.get('contract_value')
            if val_str:
                try:
                    # Parse number - handle Vietnamese currency format "1,750,000,000 ₫"
                    val_clean = str(val_str).replace('₫', '').replace('VND', '').replace('đ', '').replace(',', '').strip()
                    val_number = float(val_clean)
                    # Convert to Million VND if value is in VND (> 1,000,000)
                    if val_number > 1000000:
                        val_number = val_number / 1000000
                    values.append(val_number)
                except:
                    pass

        # Bin the data
        binned = [0] * len(labels)
        for val in values:
            for i in range(len(bins) - 1):
                if bins[i] <= val < bins[i + 1]:
                    binned[i] += 1
                    break

        chart_data = {
            'data': [{
                'type': 'bar',
                'x': labels,
                'y': binned,
                'text': [str(v) if v > 0 else '' for v in binned],
                'textposition': 'outside',
                'marker': {
                    'color': self.COLORS['green_gradient'],
                    'line': {'color': '#fff', 'width': 1}
                },
                'hovertemplate': '<b>%{x}</b><br>Số lượng: %{y}<extra></extra>'
            }],
            'layout': {
                'title': {
                    'text': 'Phân bố Giá trị Hợp đồng',
                    'font': {'size': 16, 'color': '#111827', 'family': 'Inter'}
                },
                'xaxis': {'title': 'Khoảng giá trị (VND)'},
                'yaxis': {'title': 'Số lượng hợp đồng'},
                'margin': {'l': 60, 'r': 50, 't': 60, 'b': 80},
                'height': 400,
                'font': {'family': 'Inter', 'size': 12, 'color': '#374151'}
            },
            'config': self._get_config()
        }

        return json.dumps(chart_data, ensure_ascii=False)

    def customer_source_top8(self, data: List[Dict]) -> str:
        """
        Chart 4: Phân bố Nguồn Khách hàng Top 8 (Vertical Bar)
        """
        # Get distribution
        sources = [r.get('source') for r in data if r.get('source')]
        counter = Counter(sources)

        # Get top 8 + others
        top_items = counter.most_common(8)
        others_count = sum(counter.values()) - sum(item[1] for item in top_items)

        labels = [item[0] for item in top_items]
        values = [item[1] for item in top_items]

        if others_count > 0:
            labels.append('Others')
            values.append(others_count)

        chart_data = {
            'data': [{
                'type': 'bar',
                'x': labels,
                'y': values,
                'text': [str(v) for v in values],
                'textposition': 'outside',
                'marker': {
                    'color': self.COLORS['multi'][:len(labels)],
                    'line': {'color': '#fff', 'width': 1}
                },
                'hovertemplate': '<b>%{x}</b><br>Số lượng: %{y}<extra></extra>'
            }],
            'layout': {
                'title': {
                    'text': 'Phân bố Nguồn Khách hàng (Top 8)',
                    'font': {'size': 16, 'color': '#111827', 'family': 'Inter'}
                },
                'xaxis': {
                    'title': 'Nguồn',
                    'tickangle': -45
                },
                'yaxis': {'title': 'Số lượng'},
                'margin': {'l': 60, 'r': 50, 't': 60, 'b': 120},
                'height': 400,
                'font': {'family': 'Inter', 'size': 12, 'color': '#374151'}
            },
            'config': self._get_config()
        }

        return json.dumps(chart_data, ensure_ascii=False)

    def top_districts(self, data: List[Dict]) -> str:
        """
        Chart 5: Top 10 Quận theo Số lượng (Horizontal Bar)
        """
        # Get distribution
        districts = [r.get('district') for r in data if r.get('district')]
        counter = Counter(districts)

        # Get top 10
        top_items = counter.most_common(10)

        labels = [item[0] for item in top_items]
        values = [item[1] for item in top_items]

        chart_data = {
            'data': [{
                'type': 'bar',
                'orientation': 'h',
                'x': values,
                'y': labels,
                'text': [str(v) for v in values],
                'textposition': 'outside',
                'marker': {
                    'color': self.COLORS['orange_gradient'],
                    'line': {'color': '#fff', 'width': 1}
                },
                'hovertemplate': '<b>%{y}</b><br>Số lượng: %{x}<extra></extra>'
            }],
            'layout': {
                'title': {
                    'text': 'Top 10 Quận theo Số lượng Công ty',
                    'font': {'size': 16, 'color': '#111827', 'family': 'Inter'}
                },
                'xaxis': {'title': 'Số lượng công ty'},
                'yaxis': {'title': ''},
                'margin': {'l': 150, 'r': 50, 't': 60, 'b': 60},
                'height': 450,
                'font': {'family': 'Inter', 'size': 12, 'color': '#374151'}
            },
            'config': self._get_config()
        }

        return json.dumps(chart_data, ensure_ascii=False)

    def ahcu_budget_distribution(self, data: List[Dict]) -> str:
        """
        Chart 6: Phân bố Ngân sách AHCU (Vertical Bar)
        Bins: 0-2M, 2M-5M, 5M-10M, 10M+
        """
        bins = [0, 2000000, 5000000, 10000000, float('inf')]
        labels = ['0-2M', '2M-5M', '5M-10M', '10M+']

        # Get values
        values = []
        for r in data:
            val_str = r.get('ahcu_budget')
            if val_str:
                try:
                    # Parse number - handle Vietnamese currency format "2,500,000 ₫"
                    val = float(str(val_str).replace('₫', '').replace('VND', '').replace('đ', '').replace(',', '').strip())
                    values.append(val)
                except:
                    pass

        # Bin the data
        binned = [0] * len(labels)
        for val in values:
            for i in range(len(bins) - 1):
                if bins[i] <= val < bins[i + 1]:
                    binned[i] += 1
                    break

        chart_data = {
            'data': [{
                'type': 'bar',
                'x': labels,
                'y': binned,
                'text': [str(v) if v > 0 else '' for v in binned],
                'textposition': 'outside',
                'marker': {
                    'color': self.COLORS['purple_gradient'],
                    'line': {'color': '#fff', 'width': 1}
                },
                'hovertemplate': '<b>%{x}</b><br>Số lượng: %{y}<extra></extra>'
            }],
            'layout': {
                'title': {
                    'text': 'Phân bố Ngân sách AHCU',
                    'font': {'size': 16, 'color': '#111827', 'family': 'Inter'}
                },
                'xaxis': {'title': 'Khoảng ngân sách (VND)'},
                'yaxis': {'title': 'Số lượng'},
                'margin': {'l': 60, 'r': 50, 't': 60, 'b': 80},
                'height': 400,
                'font': {'family': 'Inter', 'size': 12, 'color': '#374151'}
            },
            'config': self._get_config()
        }

        return json.dumps(chart_data, ensure_ascii=False)

    def failure_reasons_top10(self, data: List[Dict]) -> str:
        """
        Chart 7: Lý do Thất bại Deals Top 10 (Horizontal Bar)
        """
        # Get distribution
        reasons = [r.get('reason_fail') for r in data if r.get('reason_fail')]
        counter = Counter(reasons)

        # Get top 10
        top_items = counter.most_common(10)

        labels = [item[0] for item in top_items]
        values = [item[1] for item in top_items]

        # Truncate long labels for display
        short_labels = [label[:40] + '...' if len(label) > 40 else label for label in labels]

        chart_data = {
            'data': [{
                'type': 'bar',
                'orientation': 'h',
                'x': values,
                'y': short_labels,
                'text': [str(v) for v in values],
                'textposition': 'outside',
                'marker': {
                    'color': self.COLORS['red_gradient'],
                    'line': {'color': '#fff', 'width': 1}
                },
                'hovertemplate': '<b>%{customdata}</b><br>Số lượng: %{x}<extra></extra>',
                'customdata': labels  # Full labels for hover
            }],
            'layout': {
                'title': {
                    'text': 'Lý do Thất bại Deals (Top 10)',
                    'font': {'size': 16, 'color': '#111827', 'family': 'Inter'}
                },
                'xaxis': {'title': 'Số lượng'},
                'yaxis': {'title': ''},
                'margin': {'l': 250, 'r': 50, 't': 60, 'b': 60},
                'height': 450,
                'font': {'family': 'Inter', 'size': 11, 'color': '#374151'}
            },
            'config': self._get_config()
        }

        return json.dumps(chart_data, ensure_ascii=False)

    def revenue_trend(self, data: List[Dict], dashboard_type: str = 'monthly') -> str:
        """
        Chart 8: Xu hướng Doanh thu theo Tháng/Quý (Line Chart)
        """
        from datetime import datetime
        from collections import defaultdict

        # Collect revenue by period
        revenue_by_period = defaultdict(float)

        for r in data:
            # Get date
            date_str = r.get('latest_action_date') or r.get('calling_day')
            if not date_str:
                continue

            # Get contract value
            val_str = r.get('contract_value')
            if not val_str:
                continue

            try:
                # Parse date
                date_obj = self._parse_date(date_str)

                # Parse value - handle Vietnamese currency format "1,750,000,000 ₫"
                val_clean = str(val_str).replace('₫', '').replace('VND', '').replace('đ', '').replace(',', '').strip()
                value = float(val_clean)
                # Convert to Million VND if value is in VND (> 1,000,000)
                if value > 1000000:
                    value = value / 1000000

                # Determine period
                if dashboard_type == 'monthly':
                    period = date_obj.strftime('%Y-%m')
                else:  # quarterly
                    quarter = (date_obj.month - 1) // 3 + 1
                    period = f"{date_obj.year}-Q{quarter}"

                revenue_by_period[period] += value

            except:
                continue

        # Sort by period
        sorted_periods = sorted(revenue_by_period.items())

        periods = [p[0] for p in sorted_periods]
        revenues = [p[1] for p in sorted_periods]

        chart_data = {
            'data': [{
                'type': 'scatter',
                'mode': 'lines+markers',
                'x': periods,
                'y': revenues,
                'text': [f"{r:.0f}M" for r in revenues],
                'textposition': 'top center',
                'line': {
                    'color': '#667eea',
                    'width': 3,
                    'shape': 'spline'
                },
                'marker': {
                    'size': 10,
                    'color': '#667eea',
                    'line': {'color': '#fff', 'width': 2}
                },
                'hovertemplate': '<b>%{x}</b><br>Doanh thu: %{y:.0f}M VND<extra></extra>'
            }],
            'layout': {
                'title': {
                    'text': f'Xu hướng Doanh thu theo {"Tháng" if dashboard_type == "monthly" else "Quý"}',
                    'font': {'size': 16, 'color': '#111827', 'family': 'Inter'}
                },
                'xaxis': {
                    'title': 'Thời gian',
                    'tickangle': -45
                },
                'yaxis': {'title': 'Doanh thu (Million VND)'},
                'margin': {'l': 80, 'r': 50, 't': 60, 'b': 100},
                'height': 400,
                'font': {'family': 'Inter', 'size': 12, 'color': '#374151'}
            },
            'config': self._get_config()
        }

        return json.dumps(chart_data, ensure_ascii=False)

    def sales_funnel(self, data: List[Dict]) -> str:
        """
        Chart 9: Sales Funnel - Pipeline Overview (Funnel Chart)

        Real stages from Google Sheets:
        1. Prospecting to find demand - 10%
        2. Proposal Sending - 30%
        3. Meeting / Clinic Tour - 50%
        4. Negotiation/ Trial Check up - 70%
        5. Verbal Confirmation - 90%
        6. Contracting/ Closed - 100%
        """
        # Define sales stages in funnel order (from data)
        # Using exact names from Google Sheets
        stage_order = [
            '1.Prospecting to find demand - 10%',
            '2. Proposal Sending - 30%',
            '3. Meeting / Clinic Tour - 50%',
            '4.Negotiation/ Trial Check up - 70%',
            '5. Verbal Confirmation - 90%',
            '6. Contracting/ Closed\t100%'  # Note: has tab character in real data
        ]

        # Short labels for display (remove percentages for cleaner look)
        stage_labels = [
            '1. Prospecting (10%)',
            '2. Proposal (30%)',
            '3. Meeting/Tour (50%)',
            '4. Negotiation (70%)',
            '5. Verbal Confirm (90%)',
            '6. Closed (100%)'
        ]

        # Get distribution by stage
        stages = [r.get('sales_stage') for r in data if r.get('sales_stage')]
        counter = Counter(stages)

        # Match exact stage names (accounting for variations)
        stage_counts = []
        for stage in stage_order:
            # Try exact match first
            count = counter.get(stage, 0)

            # If no exact match, try variations (trim whitespace, tab chars)
            if count == 0:
                stage_clean = stage.replace('\t', ' ').strip()
                for actual_stage, actual_count in counter.items():
                    actual_clean = actual_stage.replace('\t', ' ').strip()
                    if stage_clean == actual_clean:
                        count = actual_count
                        break

            stage_counts.append(count)

        # Calculate percentages
        total = sum(stage_counts) if sum(stage_counts) > 0 else 1
        percentages = [f"{(c/total*100):.1f}%" for c in stage_counts]

        chart_data = {
            'data': [{
                'type': 'funnel',
                'y': stage_labels,
                'x': stage_counts,
                'text': [f"{c} ({p})" for c, p in zip(stage_counts, percentages)],
                'textposition': 'inside',
                'textinfo': 'value+percent initial',
                'marker': {
                    'color': ['#667eea', '#764ba2', '#f093fb', '#43e97b', '#22c55e', '#16a34a']
                },
                'connector': {'line': {'color': '#374151', 'width': 2}},
                'hovertemplate': '<b>%{y}</b><br>Số lượng: %{x}<br>Tỷ lệ: %{text}<extra></extra>'
            }],
            'layout': {
                'title': {
                    'text': 'Sales Funnel - Pipeline Overview',
                    'font': {'size': 16, 'color': '#111827', 'family': 'Inter'}
                },
                'margin': {'l': 180, 'r': 100, 't': 60, 'b': 60},
                'height': 500,
                'font': {'family': 'Inter', 'size': 12, 'color': '#374151'}
            },
            'config': self._get_config()
        }

        return json.dumps(chart_data, ensure_ascii=False)

    def _get_config(self) -> Dict:
        """Get standard Plotly config."""
        return {
            'responsive': True,
            'displayModeBar': True,
            'displaylogo': False,
            'modeBarButtonsToRemove': ['lasso2d', 'select2d'],
            'toImageButtonOptions': {
                'format': 'png',
                'filename': 'b2b_chart',
                'height': 800,
                'width': 1200,
                'scale': 2
            }
        }

    def _parse_date(self, date_str: str) -> Any:
        """Parse date string."""
        from datetime import datetime

        date_str = date_str.strip()

        # Try DD/MM/YYYY
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

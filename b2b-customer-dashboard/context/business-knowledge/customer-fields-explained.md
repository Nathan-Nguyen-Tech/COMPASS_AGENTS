# Customer Fields Explained

Complete reference for all fields in the B2B Potential Customers spreadsheet.

## Spreadsheet Information

- **Name:** 2025_B2B_PotentialCustomersManagement_Upgrade
- **ID:** 1xKWwi3hKOPPPdjuken8VeDHjWnkXJTmwHf0GUCxEV5A
- **Purpose:** Track and manage B2B potential customers for annual health checkup services

---

## Fields Reference

### Customer Identification

#### Customer ID
- **Type:** Unique identifier
- **Format:** Numeric or alphanumeric
- **Purpose:** Uniquely identify each customer record
- **Required:** Yes
- **Example:** "CUST001", "12345"

#### Company ID
- **Type:** Company identifier
- **Format:** Numeric or alphanumeric
- **Purpose:** Link to company master data
- **Required:** No
- **Notes:** May differ from Customer ID for multi-location companies

---

### Company Information

#### Company Legal Name
- **Type:** Text
- **Format:** Official registered company name
- **Purpose:** Legal identification of the company
- **Required:** Yes
- **Example:** "Công ty TNHH ABC Việt Nam"

#### Company Tax
- **Type:** Text
- **Format:** Tax registration number
- **Purpose:** Verify company registration
- **Required:** No
- **Example:** "0123456789"
- **Notes:** Used for invoicing and verification

#### Company Size
- **Type:** Categorical
- **Format:** Employee count ranges
- **Values:**
  - "1-50" - Small
  - "51-100" - Medium
  - "101-200" - Large
  - "201-500" - Very Large
  - "500+" - Enterprise
- **Purpose:** Segment customers by company scale
- **Required:** No
- **Dashboard:** Chart 1 - Company Size Distribution

#### Industry
- **Type:** Categorical
- **Format:** Industry sector
- **Values:** Technology, Manufacturing, Retail, Finance, Healthcare, etc.
- **Purpose:** Segment customers by business sector
- **Required:** No
- **Dashboard:** Used for segmentation analysis

---

### Location Information

#### Location
- **Type:** Text
- **Format:** City or Province
- **Purpose:** Primary location of company
- **Required:** No
- **Example:** "Hồ Chí Minh", "Hà Nội"

#### Location - District
- **Type:** Text
- **Format:** District name
- **Purpose:** Specific district within city
- **Required:** No
- **Example:** "Quận 1", "Quận 7", "Quận Bình Thạnh"
- **Dashboard:** Chart 5 - Top 10 Districts

---

### Contact Information (Primary)

#### HR/PIC Name
- **Type:** Text
- **Format:** Full name
- **Purpose:** Primary contact person (HR or Person In Charge)
- **Required:** Recommended
- **Example:** "Nguyễn Văn A"

#### HR/PIC Title
- **Type:** Text
- **Format:** Job title/position
- **Purpose:** Contact's role in organization
- **Required:** No
- **Example:** "HR Manager", "Admin Manager"

#### HR/PIC Telephone Number
- **Type:** Text
- **Format:** Landline phone number
- **Purpose:** Office contact number
- **Required:** No
- **Example:** "028-1234567"

#### HR/PIC Mobiphone Number
- **Type:** Text
- **Format:** Mobile phone number
- **Purpose:** Direct mobile contact
- **Required:** Recommended (for outreach)
- **Example:** "0901234567"

#### HR/PIC Email
- **Type:** Text
- **Format:** Email address
- **Purpose:** Email communication
- **Required:** Recommended
- **Example:** "hr@company.com"

---

### Contact Information (Secondary)

#### Second PIC Name
- **Type:** Text
- **Format:** Full name
- **Purpose:** Backup contact person
- **Required:** No

#### Second PIC Title
- **Type:** Text
- **Format:** Job title/position
- **Purpose:** Backup contact's role
- **Required:** No

#### Second PIC Telephone Number
- **Type:** Text
- **Format:** Landline phone number
- **Purpose:** Backup office contact
- **Required:** No

#### Second PIC Mobiphone Number
- **Type:** Text
- **Format:** Mobile phone number
- **Purpose:** Backup mobile contact
- **Required:** No

#### Second PIC Email
- **Type:** Text
- **Format:** Email address
- **Purpose:** Backup email communication
- **Required:** No

---

### Sales Process

#### Sales Incharge
- **Type:** Text
- **Format:** Salesperson name
- **Purpose:** Assigned sales representative
- **Required:** Yes
- **Example:** "Trần Thị B"
- **Notes:** Used for sales performance tracking

#### Intern Incharge
- **Type:** Text
- **Format:** Intern name
- **Purpose:** Supporting intern assigned
- **Required:** No
- **Example:** "Lê Văn C"

#### Source
- **Type:** Categorical
- **Format:** Lead source
- **Values:** Website, Facebook, Referral, Cold Call, Event, Partner, etc.
- **Purpose:** Track customer acquisition channel
- **Required:** Recommended
- **Dashboard:** Chart 4 - Customer Source Distribution

#### Calling Day
- **Type:** Date
- **Format:** DD/MM/YYYY
- **Purpose:** Last call/contact date
- **Required:** No
- **Example:** "15/06/2025"
- **Notes:** Used for filter by time period

#### Calling Status
- **Type:** Categorical
- **Format:** Call outcome
- **Values:** Answered, No Answer, Callback Requested, Not Interested, etc.
- **Purpose:** Track call results
- **Required:** No

---

### Service Details (AHCU = Annual Health CheckUp)

#### AHCU Schedule
- **Type:** Text
- **Format:** Schedule description
- **Purpose:** When annual health checkup is planned
- **Required:** No
- **Example:** "Q3 2025", "September 2025"

#### Số lượng NV thực tế
- **Type:** Numeric
- **Format:** Integer
- **Purpose:** Actual number of employees
- **Required:** No
- **Example:** "150"
- **Notes:** More precise than "Company Size" range

#### AHCU Budget
- **Type:** Numeric
- **Format:** Amount in VND
- **Purpose:** Budget allocated for health checkup
- **Required:** No
- **Example:** "1500000" (1.5 million VND)
- **Dashboard:** Chart 6 - AHCU Budget Distribution

#### Last Vendor
- **Type:** Text
- **Format:** Company name
- **Purpose:** Previous health checkup service provider
- **Required:** No
- **Example:** "Phòng khám ABC"
- **Notes:** Useful for competitive analysis

#### AHCU Note
- **Type:** Text
- **Format:** Free text
- **Purpose:** Additional notes about health checkup requirements
- **Required:** No

---

### Deal Information

#### Estimate Contract Value (Million VND)
- **Type:** Numeric
- **Format:** Value in million VND
- **Purpose:** Expected deal size
- **Required:** Recommended
- **Example:** "150" (150 million VND)
- **Dashboard:** Chart 3 - Contract Value Distribution, Chart 8 - Revenue Trend
- **Notes:** Key metric for revenue forecasting

#### Est Month to close
- **Type:** Text/Date
- **Format:** Month and year
- **Purpose:** Expected closing month
- **Required:** No
- **Example:** "06/2025"

#### Sales Stage
- **Type:** Categorical
- **Format:** Pipeline stage
- **Values:**
  - Lead
  - Qualified
  - Proposal
  - Negotiation
  - Closed Won
  - Closed Lost
- **Purpose:** Track deal progress
- **Required:** Recommended
- **Dashboard:** Chart 9 - Sales Funnel

#### Next Action (What will offer)
- **Type:** Text
- **Format:** Planned action
- **Purpose:** Next step in sales process
- **Required:** No
- **Example:** "Send proposal", "Schedule demo"

#### Phương thức tiếp cận
- **Type:** Text
- **Format:** Approach method
- **Purpose:** How to engage customer
- **Required:** No
- **Example:** "Email", "Direct visit", "Phone call"

#### Next Action (Timeline)
- **Type:** Date/Text
- **Format:** Date or description
- **Purpose:** When to take next action
- **Required:** No
- **Example:** "20/06/2025"

---

### Outcome Tracking

#### Outcome
- **Type:** Categorical
- **Format:** Deal result
- **Values:** Won, Lost, Pending, On Hold, etc.
- **Purpose:** Final deal outcome
- **Required:** No

#### PIPELINE WEEK
- **Type:** Text
- **Format:** Week identifier
- **Purpose:** Week when lead entered pipeline
- **Required:** No
- **Example:** "W24-2025"
- **Notes:** Used for cohort analysis

#### Expectation this year
- **Type:** Text
- **Format:** Free text
- **Purpose:** Customer's expectations for the year
- **Required:** No

#### Reason Fail Deals
- **Type:** Text
- **Format:** Failure reason
- **Purpose:** Why deal was lost
- **Required:** When Outcome = Lost
- **Example:** "Price too high", "Chose competitor", "No budget"
- **Dashboard:** Chart 7 - Failure Reasons

#### Client Status
- **Type:** Categorical
- **Format:** Current customer status
- **Values:** Active, Inactive, Converted, Lost, etc.
- **Purpose:** Overall customer state
- **Required:** Recommended
- **Dashboard:** Chart 2 - Client Status

---

### Additional Fields

#### Distance
- **Type:** Numeric
- **Format:** Distance in km
- **Purpose:** Distance from office/service center
- **Required:** No
- **Notes:** May affect service delivery

#### Latest Action Date
- **Type:** Date
- **Format:** DD/MM/YYYY
- **Purpose:** Most recent activity date
- **Required:** No
- **Example:** "15/06/2025"
- **Notes:** Used for filtering and tracking activity

#### Trial
- **Type:** Categorical
- **Format:** Yes/No or trial status
- **Purpose:** Whether customer had trial service
- **Required:** No

#### Note
- **Type:** Text
- **Format:** Free text
- **Purpose:** General notes and comments
- **Required:** No

---

## Data Quality Guidelines

### Required Fields (Minimum)
- Customer ID OR Company Legal Name (at least one)
- Sales Incharge (recommended)

### High-Value Fields (For Analytics)
- Company Size
- Estimate Contract Value
- Sales Stage
- Client Status
- Source
- Location - District

### Date Fields (For Time-Based Filtering)
- Calling Day
- Latest Action Date
- Est Month to close

### Missing Data
- Empty fields shown as "N/A" or blank
- Dashboard handles missing data gracefully
- Filters ignore records with missing date fields

---

## Usage in Dashboard

| Field | Used In Chart | Purpose |
|-------|---------------|---------|
| Company Size | Chart 1 | Distribution analysis |
| Client Status | Chart 2 | Status breakdown |
| Estimate Contract Value | Charts 3, 8 | Value and trend analysis |
| Source | Chart 4 | Acquisition channel analysis |
| Location - District | Chart 5 | Geographic analysis |
| AHCU Budget | Chart 6 | Budget distribution |
| Reason Fail Deals | Chart 7 | Loss analysis |
| Latest Action Date | Chart 8 | Time-based filtering |
| Sales Stage | Chart 9 | Pipeline funnel |

---

**This reference guide helps understand what each field means and how it's used in the analytics dashboard.**

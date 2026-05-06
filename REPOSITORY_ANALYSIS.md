# Django Expense Tracker - Repository Analysis Report

## 1. Project Overview

**Project Name:** Expense Tracker  
**Type:** Django Web Application  
**Purpose:** Personal finance management application to track income and expenses  
**Status:** Development  
**Django Version:** 6.0.4  

### Key Features
- User authentication (Sign up, Login, Logout)
- Track income and expenses with categories
- Dashboard displaying financial summary
- Transaction management interface
- Automatic category initialization
- User-specific transaction records

---

## 2. Technology Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | Django 6.0.4 |
| **Database** | SQLite3 |
| **Frontend Framework** | Bootstrap 5.3.0 |
| **Authentication** | Django Built-in Auth |
| **Language** | Python |
| **Template Engine** | Django Template Language |

---

## 3. Project Structure

```
expense-tracker/
├── .git/                          # Git repository
├── .gitignore                     # Git ignore file
├── venv/                          # Virtual environment
└── core/                          # Main Django project folder
    ├── manage.py                  # Django management script
    ├── db.sqlite3                 # SQLite database
    ├── core/                      # Project configuration
    │   ├── __init__.py
    │   ├── settings.py            # Django settings
    │   ├── urls.py                # Main URL configuration
    │   ├── asgi.py                # ASGI config
    │   └── wsgi.py                # WSGI config
    └── tracker/                   # Main application
        ├── __init__.py
        ├── admin.py               # Admin configuration
        ├── apps.py                # App configuration
        ├── forms.py               # Django forms
        ├── models.py              # Database models
        ├── tests.py               # Unit tests
        ├── urls.py                # App-level URL routing
        ├── views.py               # View logic
        ├── migrations/            # Database migrations
        │   ├── __init__.py
        │   └── 0001_initial.py    # Initial migration
        └── templates/             # HTML templates
            ├── base.html          # Base template
            ├── registration/
            │   ├── login.html     # Login page
            │   └── signup.html    # Sign up page
            └── tracker/
                ├── dashboard.html # Main dashboard
                └── transaction_form.html  # Add transaction form
```

---

## 4. Database Models

### Category Model
```
- id (Primary Key - Auto)
- name (CharField, max_length=50)
- Unique identifier for expense/income categories
- Example: "Salary", "Groceries", "Rent", etc.
```

### Transaction Model
```
- id (Primary Key - Auto)
- user (ForeignKey to User) - Links transaction to user account
- title (CharField, max_length=100) - Transaction description
- amount (FloatField) - Transaction amount
- category (ForeignKey to Category) - Expense/Income category
- transaction_type (CharField) - Either "Income" or "Expense"
- date (DateField) - Transaction date
```

### User Model
- Django's built-in User model
- Linked to Transaction via ForeignKey
- Supports authentication and user management

---

## 5. Default Categories

The application automatically initializes **30 default categories** when adding a transaction:

**Income Categories:**
- Salary, Freelance, Bonus, Business, Gift Received, Interest, Investment, Rental Income

**Expense Categories:**
- Food, Groceries, Dining Out, Transport, Utilities, Rent, EMI, Insurance, Education, Shopping, Clothing, Healthcare, Entertainment, Travel, Subscriptions, Taxes, Mobile Recharge, Pets, Personal Care, Home Maintenance, Charity, Other

---

## 6. URL Routing

### Main URLs (core/urls.py)
```
/admin/                 → Django Admin Panel
/                       → Dashboard (tracker app)
/add/                   → Add Transaction
/signup/                → User Registration
/accounts/login/        → Login (built-in)
/accounts/logout/       → Logout (built-in)
```

### Tracker App URLs (tracker/urls.py)
```
''                      → Dashboard view
'add/'                  → Add transaction view
'signup/'               → Signup view
```

---

## 7. Views and Logic

### Dashboard View (`dashboard`)
- **Route:** `/` (or empty path)
- **Authentication:** Required (Login required)
- **Functionality:**
  - Fetches all transactions for the logged-in user
  - Calculates total income
  - Calculates total expenses
  - Calculates balance (income - expenses)
  - Orders transactions by date (newest first)
  - Displays summary cards and transaction table
- **Context Data:**
  - `transactions`: List of user's transactions
  - `balance`: Net balance (income - expenses)
  - `income`: Total income amount
  - `expense`: Total expense amount

### Add Transaction View (`add_transaction`)
- **Route:** `/add/`
- **Authentication:** Required (Login required)
- **Functionality:**
  - Initializes default categories if none exist
  - Displays transaction form
  - Validates form input
  - Creates transaction linked to current user
  - Redirects to dashboard on success
- **Methods:** GET (display form), POST (submit form)

### Signup View (`signup`)
- **Route:** `/signup/`
- **Authentication:** Not required (Guest accessible)
- **Functionality:**
  - Displays user registration form
  - Validates username and password
  - Creates new user account
  - Automatically logs in user after signup
  - Redirects to dashboard
- **Methods:** GET (display form), POST (submit form)

### Built-in Authentication Views
- Login: `/accounts/login/` (Django built-in)
- Logout: `/accounts/logout/` (Django built-in)

---

## 8. Forms

### TransactionForm
- **Model:** Transaction
- **Fields:**
  - `title` - Text input for transaction description
  - `amount` - Number input (minimum 0, step 0.01)
  - `category` - Dropdown (alphabetically ordered, placeholder: "Select category")
  - `transaction_type` - Dropdown (Income/Expense options)
  - `date` - Date picker input

- **Styling:** Bootstrap classes applied to all form fields
  - Input fields: `form-control` class
  - Dropdown fields: `form-select` class
  - Consistent Bootstrap styling across form

### UserCreationForm
- Django's built-in form for user registration
- Validates username uniqueness and password strength

---

## 9. Templates Overview

### base.html (Base Template)
- **Purpose:** Master template for all pages
- **Features:**
  - Bootstrap 5.3.0 CDN integration
  - Responsive navigation bar
  - User authentication status display
  - Conditional navigation (Login/Signup for guests, Add Transaction/Logout for logged-in users)
  - Welcome message with username (for logged-in users)
  - Dark theme navbar
  - Container layout for content

### dashboard.html
- **Purpose:** Display financial summary and transaction list
- **Components:**
  - Summary cards: Balance, Income, Expenses
  - "Add Transaction" button
  - Transaction table with columns: Date, Title, Category, Amount
  - Color-coded amounts (green for income, red for expenses)
  - Sorted by date (newest first)

### transaction_form.html
- **Purpose:** Add new transaction form
- **Features:**
  - Card-based layout
  - Form fields with labels
  - Error display for validation
  - Bootstrap styling
  - "Save Transaction" button

### login.html
- **Purpose:** User login page
- **Features:**
  - Centered card layout
  - Form fields with Bootstrap styling
  - Sign In button
  - Link to signup for new users
  - Helper text about credentials

### signup.html
- **Purpose:** User registration page
- **Features:** Similar to login with registration form

---

## 10. Settings Configuration

### Key Settings (settings.py)

| Setting | Value |
|---------|-------|
| **Django Version** | 6.0.4 |
| **DEBUG** | True (Development) |
| **ALLOWED_HOSTS** | Empty (Default) |
| **Database** | SQLite3 |
| **Installed Apps** | Django default apps + 'tracker' |
| **Authentication Backend** | Django default |
| **Password Validators** | All Django defaults enabled |
| **Language Code** | en-us |
| **Timezone** | UTC |
| **Login Redirect URL** | / (Dashboard) |
| **Logout Redirect URL** | /accounts/login/ |
| **Static Files URL** | /static/ |

### Middleware Stack
1. SecurityMiddleware
2. SessionMiddleware
3. CommonMiddleware
4. CsrfViewMiddleware
5. AuthenticationMiddleware
6. MessageMiddleware
7. XFrameOptionsMiddleware

### INSTALLED_APPS
- django.contrib.admin
- django.contrib.auth
- django.contrib.contenttypes
- django.contrib.sessions
- django.contrib.messages
- django.contrib.staticfiles
- tracker (Custom app)

---

## 11. Key Features & Functionality

### 1. User Authentication
- Sign up new users
- Login with credentials
- Logout functionality
- Password validation
- Session management

### 2. Transaction Management
- Add income transactions
- Add expense transactions
- Assign categories to transactions
- Record transaction dates
- Set transaction amounts

### 3. Financial Dashboard
- View all transactions
- Calculate total income
- Calculate total expenses
- Display net balance
- View transaction history sorted by date

### 4. Category System
- Pre-populated with 30 common categories
- Organized by type (income vs expense)
- Easy category selection in forms
- Expandable for custom categories

### 5. User-Specific Data
- Each user sees only their transactions
- Isolated financial data per user
- Multi-user support

### 6. Responsive Design
- Bootstrap 5 framework
- Mobile-friendly navigation
- Responsive grid layouts
- Touch-friendly buttons

---

## 12. Database Relationships

```
User (Django Auth)
  ↓ (1:Many)
  └─→ Transaction
       ↓ (Many:1)
       └─→ Category
```

- One user can have many transactions
- Each transaction belongs to one category
- Each category can have many transactions
- Deletion cascade: Transactions deleted when user deleted

---

## 13. File Descriptions

| File | Purpose |
|------|---------|
| **manage.py** | Django command-line utility |
| **settings.py** | Project configuration and settings |
| **urls.py** | URL routing configuration |
| **models.py** | Database model definitions |
| **views.py** | Business logic and view handlers |
| **forms.py** | Form classes with validation |
| **admin.py** | Django admin configuration |
| **apps.py** | App configuration |
| **migrations/** | Database schema version history |
| **templates/** | HTML templates for rendering |
| **db.sqlite3** | SQLite database file |

---

## 14. Security Considerations

### Current Configuration
- DEBUG = True (Development only)
- SQLite database (suitable for development)
- CSRF protection enabled
- Password validators configured
- User authentication required for sensitive views

### Security Warnings in Code
- Insecure SECRET_KEY in settings.py
- DEBUG enabled (should be False in production)
- ALLOWED_HOSTS is empty (needs configuration for production)

### Production Recommendations
- Set DEBUG = False
- Generate secure SECRET_KEY
- Configure ALLOWED_HOSTS
- Use PostgreSQL or MySQL instead of SQLite
- Enable HTTPS
- Set appropriate CORS headers
- Use environment variables for secrets

---

## 15. Installation & Usage

### Prerequisites
- Python 3.8+
- pip package manager
- Virtual environment (venv)

### Setup Instructions
```bash
# Navigate to project directory
cd core

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py migrate

# Create superuser (for admin panel)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### Access Points
- Application: http://localhost:8000/
- Admin Panel: http://localhost:8000/admin/
- Signup: http://localhost:8000/signup/
- Login: http://localhost:8000/accounts/login/

---

## 16. Application Flow

### User Journey - New User
1. Visit homepage → Redirected to login
2. Click "Sign Up" → Signup page
3. Enter username & password → Create account
4. Auto-logged in → Redirected to dashboard
5. Dashboard shows zero balance (no transactions)
6. Click "Add Transaction" → Transaction form
7. Fill form & submit → Transaction saved
8. Dashboard updated with transaction

### User Journey - Returning User
1. Visit homepage → Redirected to login (if not authenticated)
2. Enter credentials → Login
3. Redirected to dashboard
4. View transactions, balance, income, expenses
5. Add more transactions as needed
6. Click logout when done

---

## 17. Current Status & Notes

### Working Features
✅ User authentication and registration  
✅ Transaction creation  
✅ Dashboard with financial summary  
✅ Responsive UI with Bootstrap  
✅ Category system  
✅ Transaction history  

### Potential Enhancements
- Edit/Delete transaction functionality
- Advanced filtering and search
- Transaction statistics and charts
- Export to CSV/PDF
- Budget setting and tracking
- Recurring transactions
- Multi-currency support
- Mobile app version
- Data visualization with charts
- Category-wise expense breakdown

### Dependencies
- Django 6.0.4 (core framework)
- Bootstrap 5.3.0 (CSS framework from CDN)

---

## 18. Admin Configuration

### Current Status
- Django admin interface is enabled at `/admin/`
- Default admin settings (can be customized in admin.py)
- Requires superuser account to access

### Recommended Admin Customizations
```python
# Suggested additions to admin.py:
- Display Transaction and Category in admin
- Add search and filter capabilities
- Customize list display fields
- Add admin actions for bulk operations
```

---

## 19. Database Migration History

### Initial Migration (0001_initial.py)
- Creates Category model
- Creates Transaction model
- Sets up relationships between models and User
- Establishes database schema

---

## 20. Summary Statistics

| Metric | Count |
|--------|-------|
| **Models** | 2 (Category, Transaction) |
| **Views** | 3 (dashboard, add_transaction, signup) |
| **URL Routes** | 6 (main) + 3 (tracker app) |
| **Templates** | 5 (base, dashboard, transaction_form, login, signup) |
| **Forms** | 1 (TransactionForm) |
| **Default Categories** | 30 |
| **Middleware Components** | 7 |
| **Total Database Tables** | 4 (Django defaults + Category + Transaction) |

---

## 21. Performance Considerations

- **Database Queries:** Optimized with select_related() not yet implemented
- **N+1 Query Problem:** Possible when displaying transactions with categories
- **Caching:** Not implemented (suitable for current scale)
- **Pagination:** Not implemented (should be added for large datasets)

### Optimization Recommendations
- Add pagination to dashboard (100+ transactions)
- Use select_related for transaction queries
- Add database indexes on frequently queried fields
- Implement caching for category lists

---

## 22. Testing

### Test File
- `tracker/tests.py` - Present but empty

### Recommended Tests to Add
- User authentication tests
- Transaction creation tests
- Dashboard calculation tests
- Form validation tests
- Permission tests (user isolation)
- View access tests

---

## Document Metadata

- **Generated Date:** May 6, 2026
- **Django Version:** 6.0.4
- **Database:** SQLite3
- **Repository Status:** Development
- **Documentation Version:** 1.0

---

**End of Repository Analysis Report**

CREATE TABLE IF NOT EXISTS business_profiles (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,
    business_name VARCHAR(200) NOT NULL,
    business_type VARCHAR(100) NOT NULL DEFAULT '',
    industry VARCHAR(100) NOT NULL DEFAULT '',
    gst_number VARCHAR(20) NOT NULL DEFAULT '',
    monthly_revenue NUMERIC(15,2) NOT NULL DEFAULT 0,
    monthly_fixed_expenses NUMERIC(15,2) NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS consent_records (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    consent_type VARCHAR(30) NOT NULL,
    granted BOOLEAN NOT NULL DEFAULT FALSE,
    purpose TEXT NOT NULL,
    granted_at TIMESTAMPTZ,
    revoked_at TIMESTAMPTZ,
    expires_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(user_id, consent_type)
);

CREATE TABLE IF NOT EXISTS import_files (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    file VARCHAR(500) NOT NULL,
    file_type VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'uploaded',
    error_message TEXT NOT NULL DEFAULT '',
    uploaded_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    processed_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS imported_invoices (
    id BIGSERIAL PRIMARY KEY,
    import_file_id BIGINT NOT NULL REFERENCES import_files(id) ON DELETE CASCADE,
    invoice_number VARCHAR(100) NOT NULL,
    customer_name VARCHAR(200) NOT NULL,
    invoice_date DATE NOT NULL,
    due_date DATE NOT NULL,
    amount NUMERIC(15,2) NOT NULL,
    paid_amount NUMERIC(15,2) NOT NULL DEFAULT 0,
    corrected BOOLEAN NOT NULL DEFAULT FALSE,
    confidence_score DOUBLE PRECISION NOT NULL DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS cashflow_twins (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,
    current_balance NUMERIC(15,2) NOT NULL DEFAULT 0,
    monthly_income NUMERIC(15,2) NOT NULL DEFAULT 0,
    monthly_expenses NUMERIC(15,2) NOT NULL DEFAULT 0,
    average_collection_days DOUBLE PRECISION NOT NULL DEFAULT 0,
    concentration_risk DOUBLE PRECISION NOT NULL DEFAULT 0,
    delayed_payment_risk DOUBLE PRECISION NOT NULL DEFAULT 0,
    liquidity_risk DOUBLE PRECISION NOT NULL DEFAULT 0,
    survivable_loss_percent DOUBLE PRECISION NOT NULL DEFAULT 0,
    emergency_savings_percent DOUBLE PRECISION NOT NULL DEFAULT 0,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS cashflow_entries (
    id BIGSERIAL PRIMARY KEY,
    twin_id BIGINT NOT NULL REFERENCES cashflow_twins(id) ON DELETE CASCADE,
    entry_type VARCHAR(20) NOT NULL,
    description VARCHAR(255) NOT NULL,
    amount NUMERIC(15,2) NOT NULL,
    expected_date DATE NOT NULL,
    actual_date DATE,
    recurring BOOLEAN NOT NULL DEFAULT FALSE,
    source VARCHAR(100) NOT NULL DEFAULT '',
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS forecast_points (
    id BIGSERIAL PRIMARY KEY,
    twin_id BIGINT NOT NULL REFERENCES cashflow_twins(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    expected_inflow NUMERIC(15,2) NOT NULL DEFAULT 0,
    expected_outflow NUMERIC(15,2) NOT NULL DEFAULT 0,
    projected_balance NUMERIC(15,2) NOT NULL DEFAULT 0,
    liquidity_gap BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE IF NOT EXISTS partial_payments (
    id BIGSERIAL PRIMARY KEY,
    invoice_id BIGINT NOT NULL REFERENCES imported_invoices(id) ON DELETE CASCADE,
    amount NUMERIC(15,2) NOT NULL,
    payment_date DATE NOT NULL,
    notes TEXT NOT NULL DEFAULT '',
    created_by_id INTEGER,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS collection_actions (
    id BIGSERIAL PRIMARY KEY,
    invoice_id BIGINT NOT NULL REFERENCES imported_invoices(id) ON DELETE CASCADE,
    action_type VARCHAR(30) NOT NULL,
    notes TEXT NOT NULL DEFAULT '',
    action_date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_by_id INTEGER
);

CREATE TABLE IF NOT EXISTS product_price_references (
    id BIGSERIAL PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,
    category VARCHAR(100) NOT NULL DEFAULT '',
    supplier VARCHAR(200) NOT NULL,
    price NUMERIC(15,2) NOT NULL,
    source VARCHAR(200) NOT NULL DEFAULT '',
    observed_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS audit_logs (
    id BIGSERIAL PRIMARY KEY,
    user_id INTEGER,
    action VARCHAR(100) NOT NULL,
    endpoint VARCHAR(255) NOT NULL DEFAULT '',
    method VARCHAR(20) NOT NULL,
    ip_address INET,
    timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_invoices_due_date ON imported_invoices(due_date);
CREATE INDEX IF NOT EXISTS idx_invoices_customer ON imported_invoices(customer_name);
CREATE INDEX IF NOT EXISTS idx_forecast_twin_date ON forecast_points(twin_id, date);
CREATE INDEX IF NOT EXISTS idx_audit_timestamp ON audit_logs(timestamp);

-- Illustrative seed data only. Not live bank offers.
-- Bank comparison is intentionally advisory; no lending decision is automated.

-- The Django database table is created by migrations.
-- Insert illustrative market references after migrations if desired.
INSERT INTO product_price_references
(product_name, category, supplier, price, source)
SELECT 'Sample Packaging Material', 'Packaging', 'Illustrative Supplier A', 120.00, 'Demo seed'
WHERE NOT EXISTS (
    SELECT 1 FROM product_price_references
    WHERE product_name='Sample Packaging Material'
      AND supplier='Illustrative Supplier A'
);

INSERT INTO product_price_references
(product_name, category, supplier, price, source)
SELECT 'Sample Packaging Material', 'Packaging', 'Illustrative Supplier B', 115.00, 'Demo seed'
WHERE NOT EXISTS (
    SELECT 1 FROM product_price_references
    WHERE product_name='Sample Packaging Material'
      AND supplier='Illustrative Supplier B'
);

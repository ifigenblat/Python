-- Step 1: Create a new database
CREATE DATABASE company_db;

-- Connect to the newly created database (run this separately in psql)
-- \c company_db

-- Step 2: Create a schema named 'hr'
CREATE SCHEMA hr;

-- Step 3: Create the employees table within the hr schema
CREATE TABLE hr.employees (
    employee_id SERIAL PRIMARY KEY,  -- Auto-incrementing primary key
    first_name VARCHAR(50) NOT NULL, -- First name column
    last_name VARCHAR(50) NOT NULL,  -- Last name column
    email VARCHAR(100) UNIQUE,       -- Unique email column
    salary NUMERIC(10,2),            -- Salary with precision
    department_id INT,                -- Foreign key reference (assuming departments table exists)
    hire_date DATE DEFAULT CURRENT_DATE -- Default hire date to today
);

-- Step 4: Add a new column to employees table
ALTER TABLE hr.employees 
ADD COLUMN phone_number VARCHAR(15);

-- Step 5: Insert fake data into the employees table
INSERT INTO hr.employees (first_name, last_name, email, salary, department_id, hire_date, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', 60000.00, 1, '2023-05-12', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', 75000.00, 2, '2022-08-15', '987-654-3210'),
('Alice', 'Johnson', 'alice.johnson@example.com', 82000.00, 3, '2021-11-20', '555-666-7777'),
('Bob', 'Brown', 'bob.brown@example.com', 55000.00, 1, '2020-02-10', '111-222-3333'),
('Charlie', 'Davis', 'charlie.davis@example.com', 90000.00, 4, '2019-07-30', '444-555-6666'),
('Emily', 'Clark', 'emily.clark@example.com', 72000.00, 2, '2022-03-18', '999-888-7777'),
('Frank', 'Wright', 'frank.wright@example.com', 67000.00, 3, '2023-01-05', '333-222-1111'),
('Grace', 'Lee', 'grace.lee@example.com', 58000.00, 1, '2021-09-22', '222-333-4444'),
('Henry', 'Morris', 'henry.morris@example.com', 95000.00, 4, '2018-12-11', '666-777-8888'),
('Ivy', 'Wilson', 'ivy.wilson@example.com', 60000.00, 2, '2020-06-17', '111-000-9999');

-- Step 6: View the data inserted into the employees table
SELECT * FROM hr.employees;

-- Step 7: Modify an existing column (change phone_number to a larger size)
ALTER TABLE hr.employees 
ALTER COLUMN phone_number TYPE VARCHAR(20);

-- Step 8: Drop a column from the employees table
ALTER TABLE hr.employees 
DROP COLUMN phone_number;

-- Step 9: Drop the employees table
DROP TABLE hr.employees;

-- Step 10: Drop the schema (including all objects inside it)
DROP SCHEMA hr CASCADE;

-- Step 11: Drop the database
DROP DATABASE company_db;
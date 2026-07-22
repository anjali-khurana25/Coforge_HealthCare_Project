-- ============================================
-- Healthcare Management System Database
-- ============================================

DROP DATABASE IF EXISTS healthcare_db;

CREATE DATABASE healthcare_db;

USE healthcare_db;

-- ============================================
-- Patients Table
-- ============================================

CREATE TABLE patients
(
    patient_id VARCHAR(20) PRIMARY KEY,

    patient_name VARCHAR(100) NOT NULL,

    age INT NOT NULL,

    gender ENUM('Male','Female','Other') NOT NULL,

    contact_number VARCHAR(10) UNIQUE,

    city VARCHAR(100) NOT NULL,

    blood_group VARCHAR(5) NOT NULL,

    disease VARCHAR(100) NOT NULL
);

-- ============================================
-- Doctors Table
-- ============================================

CREATE TABLE doctors
(
    doctor_id VARCHAR(20) PRIMARY KEY,

    doctor_name VARCHAR(100) NOT NULL,

    department VARCHAR(100) NOT NULL,

    consultation_fee DECIMAL(10,2) NOT NULL,

    availability_status ENUM
    (
        'Available',
        'Unavailable',
        'On Leave'
    ) NOT NULL
);

-- ============================================
-- Appointments Table
-- ============================================

CREATE TABLE appointments
(
    appointment_id VARCHAR(20) PRIMARY KEY,

    patient_id VARCHAR(20) NOT NULL,

    doctor_id VARCHAR(20) NOT NULL,

    appointment_date DATE NOT NULL,

    appointment_time TIME NOT NULL,

    status ENUM
    (
        'Scheduled',
        'Completed',
        'Cancelled'
    ) DEFAULT 'Scheduled',

    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id),

    FOREIGN KEY (doctor_id)
    REFERENCES doctors(doctor_id)
);

-- ============================================
-- Bills Table
-- ============================================

CREATE TABLE bills
(
    bill_id VARCHAR(20) PRIMARY KEY,

    patient_id VARCHAR(20) NOT NULL,

    appointment_id VARCHAR(20) NOT NULL UNIQUE,

    consultation_fee DECIMAL(10,2) DEFAULT 0,

    medicine_charges DECIMAL(10,2) DEFAULT 0,

    laboratory_charges DECIMAL(10,2) DEFAULT 0,

    room_charges DECIMAL(10,2) DEFAULT 0,

    gross_amount DECIMAL(10,2) NOT NULL,

    discount DECIMAL(10,2) DEFAULT 0,

    total_amount DECIMAL(10,2) NOT NULL,

    payment_status ENUM
    (
        'Paid',
        'Pending'
    ) DEFAULT 'Pending',

    FOREIGN KEY (patient_id)
    REFERENCES patients(patient_id),

    FOREIGN KEY (appointment_id)
    REFERENCES appointments(appointment_id)
);

-- ============================================
-- Sample Data
-- ============================================

INSERT INTO patients
(
    patient_id,
    patient_name,
    age,
    gender,
    contact_number,
    city,
    blood_group,
    disease
)
VALUES
(
    'P101',
    'Rahul Sharma',
    35,
    'Male',
    '9876543210',
    'Noida',
    'O+',
    'Diabetes'
);

INSERT INTO doctors
(
    doctor_id,
    doctor_name,
    department,
    consultation_fee,
    availability_status
)
VALUES
(
    'D201',
    'Dr. Mehta',
    'Cardiology',
    800,
    'Available'
);

INSERT INTO appointments
(
    appointment_id,
    patient_id,
    doctor_id,
    appointment_date,
    appointment_time,
    status
)
VALUES
(
    'A301',
    'P101',
    'D201',
    '2026-07-25',
    '10:30:00',
    'Completed'
);
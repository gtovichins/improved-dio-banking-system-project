*[Leia em Português](./README.pt.md)*
# 🏦 Advanced Python Banking System


This project was developed as part of the Python Bootcamp at DIO ([Suzano - Python Developer](https://www.dio.me/bootcamp/suzano-python-developer)). It is an evolution of a simple banking system and simulates a more advanced banking system with multiple users, accounts, and realistic business rules.

## ✨ Features
### 👥 Multi-user Registration

  - Full Name: must not contain numbers

  - Date of Birth: format DD/MM/YYYY

  - CPF: Brazilian ID, format XXX.XXX.XXX-XX, unique per user

  - Address: format Street, Number - Neighborhood, City/StateAbbreviation
  -- Example: Main Street, 123 - Downtown, Springfield/SP

### 🏛️ Account Management

  - Users can have multiple accounts

  - Each account has a sequential number and a fixed agency

  - Accounts are linked to a single user

### 💰 Banking Operations

  - Deposit: validated input, updates balance, records transaction with date & time

  - Withdrawal: validates input, respects maximum withdrawal, daily withdrawal limit, and maximum number of withdrawals

  - Transaction Limits: each account has a daily limit of 10 transactions with notifications

### 📄 Account Statement

  - Shows each transaction with date & time

  - Displays current balance, number of withdrawals, and remaining transactions

### ❌ User Deletion

  - Users can be deleted with confirmation

  - Deleting a user removes all associated accounts

### 🔄 Daily Reset

  - Withdrawal counts and transaction counts reset automatically each day

## 🛠️ Technologies

  - Python 3.x

  - Conditional statements & loops

  - Functions for modularization

  - datetime library for transaction timestamps

  - Regular expressions for input validation

## 📂 Project Structure
  - improved-dio-banking-system-project 📁 Root folder
  - improved-dio-banking-system-project.py 📝 Main Python script
  - README.md 📄 Documentation in English
  - README.pt.md 📄 Documentation in Portuguese

## 📝 Notes

This project demonstrates:

  - Modular programming with dedicated functions for each operation

  - Robust input validation with clear user messages

  - Support for multiple users and accounts

  - Realistic banking rules, including daily transaction limits

  - Automatic daily reset of limits to simulate real banking constraints

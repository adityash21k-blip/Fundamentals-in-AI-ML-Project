# Fundamentals-in-AI-ML-Project

# 💰 Smart Budgeter v3.0 (Capstone Project)

## 📌 Project Overview
**Smart Budgeter** is a Python-based personal finance tool developed as a "Bring Your Own Project" (BYOP) capstone for the **Digital Literacy** course. It helps users manage their daily spending by categorizing expenses and tracking them against a monthly budget limit. 

This project demonstrates core programming principles including **Data Structures**, **File I/O**, and **Error Handling**.

## 🚀 Key Features
- **Persistent Storage:** Uses the `json` library to save and load data from `expenses_data.json`.
- **Dynamic Budgeting:** Real-time feedback on remaining budget and overspending alerts.
- **Categorization:** Organize spending into groups like Food, Travel, and Bills.
- **Robust Input Validation:** Prevents application crashes using `try-except` blocks for numeric inputs.

---

## 🛠️ Technical Implementation
### 1. Data Structures
The application uses a **List of Dictionaries** to manage state:
- Each expense is stored as: `{"item": str, "amount": float, "category": str}`.
- This allows for easy iteration and summation of costs.

### 2. File Persistence (JSON)
To ensure data isn't lost when the program exits, the `json` module is used to:
- **Serialize:** Convert Python lists into a JSON format for saving.
- **Deserialize:** Convert the JSON file back into Python objects upon startup.

### 3. Error Handling
The program includes `try...except` blocks to handle common user errors, such as entering text instead of numbers for prices, ensuring a professional and crash-free experience.

---

## 📖 User Guide
### 1. Installation
1. Ensure you have **Python 3.0** installed.
2. Clone this repository:
   ```bash
   git clone [https://github.com/adityash21k-blip/Fundamentals-in-AI-ML-Project.git](https://github.com/adityash21k-blip/Fundamentals-in-AI-ML-Project.git)
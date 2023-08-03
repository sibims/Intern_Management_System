# Intern Management System

Intern Management System is a Python Console Application which offers an intern to view his schedule, mark his attendance digitally.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.

### **Tabulate**
It is the package which delivers the output to be displayed in a table format.

```bash
pip install tabulate
```

#### *Usage*

```python
print(tabulate(data, headers=headers, tablefmt="grid"))
```

### **pwinput**
It is the package used for inputting the password with a mask.

```bash
pip install pwinput
```

#### *Usage*

```python
password = pwinput.pwinput(prompt='Enter your Password: ', mask='*')
```

### **Regular Expression**
It is the package used for inputting the details with validation.

```python
import re
```

#### *Usage*

```python
mobile_number = input("Enter your Mobile Number (Ex: 9894969290): ")
if not re.match(r'^\d{10}$', mobile_number):
    print("Invalid mobile number format. Please enter a 10-digit number.")
else:
    break
```

### **MySQL Connector**
It is the package used for inputting the password with a mask.

```bash
pip install mysql-connector-python
```
```python
import mysql.connector
```

#### *Usage*

```python
db_connection = mysql.connector.connect(
        host="127.0.0.12",
        user="root",
        password="root",
        database="interndb",
    )
```

## Program Running Flow
Step 1: User starts the application. <br>
Step 2: Landing Page. <br>
Step 3: User Choice: 1. Signin, 2. Signup, 3. Exit <br>
Step 4: User Enters Signup since their account is not created, and they create their account. <br>
Step 5: The Created account details will be stored in MySQL Database. <br>
Step 6: The user's login credentials will be listed only if they enter their passcode. <br>
Step 7: The user can login and check his schedules for the day and mark his attendance.
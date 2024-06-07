## Table of Contents

| Section | Description |
| --- | --- |
| [Introduction](#introduction) | General description of the code |
| [Rules](#rules) | Rules for creating a secure password |
| [Password Examples](#password-examples) | Examples of passwords to test the validations |
| [Library Importance](#library-importance) | Importance and usage of libraries in the code |
| [Bibliography](#bibliography) | References used for the password rules |

## Introduction

In this repository is the construction of a deterministic finite automaton or AFD, the JSON format, which is readable through the web application, automatarium. It also contains detailed Python code for creating and validating passwords, ensuring that they meet certain security criteria established by the National Institute of Standards and Technology (NIST). The program prompts the user to enter a password, which is then evaluated and classified as “secure”, “very secure” or “insecure” according to defined rules.

Thank you very much for your attention!!

![AFD Passwords](./AFDPasswords.png)

## Rules

1. The password must be between 8 and 12 characters long.
2. The password must contain at least one letter (uppercase or lowercase).
3. The password must contain at least one number (from 1 to 9).
4. The password must contain at least one special symbol [#, %, &, $, ¿, ?, *].
5. Note: A 12-character password is more secure than an 8-character one.

## Password Examples

### Secure Password

| Password |
|----------|
| A1b#c2d! |
| M9z&L6f* |

### Very Secure Password

| Password |
|----------|
| Ab1#Cd2&3 |
| M9z&L6f*H8 |

### Insecure Password

| Reason                            | Password    |
|-----------------------------------|-------------|
| Less than 8 characters            | Ab1#c2d     |
| Does not contain a letter         | 1234#567    |
| Does not contain a number         | Abcdef#*    |
| Does not contain a special symbol | A1bc2d3e    |
| More than 12 characters           | A1b#c2d!e3f4|
| Consecutive sequences             | Abc123#&    |

### Password Meets Minimum Rules but Insecure

| Reason                            | Password    |
|-----------------------------------|-------------|
| Repetitive characters             | A1a#A1a#    |
| Insufficient unique characters    | A1b#A1b#    |

## Code Explanation

The provided code allows the user to create a password that meets certain security rules. Below is an explanation of each part of the code:

### Function `mostrar_reglas`

This function prints the rules for creating a secure password. Simple prints are used to display each rule and an additional note about the security of longer passwords.

### Function `es_contrasena_segura`

This function evaluates the security of the password based on several conditions:
- **Length**: Evaluates if the password length is adequate.
- **Presence of Uppercase and Lowercase Letters**: Checks for at least one uppercase and one lowercase letter.
- **Presence of Numbers**: Checks if the password contains at least one number.
- **Presence of Special Symbols**: Checks if the password contains at least one special symbol.
- **Number of Unique Characters**: Evaluates the diversity of unique characters in the password.
- **Absence of Consecutive Sequences**: Checks that the password does not contain common consecutive character sequences.

### Function `validar_contrasena`

This function validates that the password meets basic rules:
- **Length**: Between 8 and 12 characters.
- **Presence of Letters**: At least one letter.
- **Presence of Numbers**: At least one number.
- **Presence of Special Symbols**: At least one special symbol.

If any of these rules are not met, the function returns `False` and an explanatory message.

### Function `input_contrasena`

This function allows the user to securely enter the password:
- **Character Reading**: Uses `msvcrt.getch()` to read characters one by one.
- **Show Asterisks**: Displays an asterisk for each entered character.
- **Enter Key**: Ends the password entry.
- **Backspace Key**: Allows deleting the last entered character.

### Function `main`

This is the main function of the program. It performs the following actions:
1. Shows the rules.
2. Allows the user to enter a password.
3. Validates if the password is secure or not.
4. If the password is valid but only 8 characters long, it recommends creating a longer one.
5. Allows the user to create several passwords until they decide to exit.

## Library Importance

The following libraries are used in the code, each serving an important purpose:

- **`re`**: This library provides support for regular expressions in Python. In the code, it is used to validate the structure of the password, ensuring it meets specific patterns and criteria (e.g., length, allowed characters).
  
- **`msvcrt`**: This library provides an interface to the Microsoft Visual C runtime library, allowing access to functions for console I/O. In the code, `msvcrt.getch()` is used to read individual characters from the console input without echoing them, which helps in securely capturing the user's password while displaying asterisks instead of the actual characters.

## Bibliography

- Payment Card Industry Security Standards Council (PCI SSC). (2018). Payment Card Industry Data Security Standard (PCI DSS) v3.2.1. Retrieved from PCI Security Standards.
- National Institute of Standards and Technology (NIST). (2017). Digital Identity Guidelines: Authentication and Lifecycle Management (SP 800-63B). Retrieved from NIST Publications.
- International Organization for Standardization (ISO)/International Electrotechnical Commission (IEC). (2013). ISO/IEC 27001: Information technology — Security techniques — Information security management systems — Requirements. Retrieved from ISO Standards.
- Open Web Application Security Project (OWASP). (2021). OWASP Application Security Verification Standard 4.0. Retrieved from OWASP.
- General Data Protection Regulation (GDPR). (2018). Regulation (EU) 2016/679 of the European Parliament and of the Council. Retrieved from GDPR Info.



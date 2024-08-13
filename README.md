# Password-Cracking-Project
Hello!
# Overview
In cryptanalysis and computer security, password cracking is the process of recovering passwords from data that has been stored in or transmitted by a computer system in scrambled form. The purpose of this project was to demonstrate the process of cracking a set of hashed passwords using tools like Hashcat and John the Ripper. Showcasing the functionality of cracking hashes with the tools exemplifies an understanding of cryptographic hashing and password-cracking techniques. The project aims to showcase the process of decoding hashes and understanding the importance of secure password practices.
# Features
Hash Generation: Generates sample password hashes using different algorithms (MD5, SHA-1, SHA-256).
Cracking Tools: Utilizes Hashcat and John the Ripper to attempt to crack the generated hashes.
Results Logging: Outputs the results of cracked passwords into a text file for review. 
# Installation
To run this project, ensure you have the following tools installed on your system:
- Python (for generating hashes)
- Hashcat
- John the Ripper

git clone https://github.com/yourusername/password-cracking-project.git
cd password-cracking-project
# Usage
Generate Password Hashes: Use the provided Python script to generate a set of hashed passwords.
Transfer Hashes: If needed, transfer the generated hash file to a Linux environment.
Crack Hashes: Use Hashcat or John the Ripper to crack the hashes.
Save Results: Cracked passwords are saved into cracked_passwords.txt
# File Structure
generate_hashes.py: Python script to generate sample password hashes.
sample_hashes.txt: Example file containing hashed passwords.
cracked_passwords.txt: Output file for storing cracked passwords.

# Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your proposed changes.
# License
This project is licensed under the MIT License.
# Disclaimer
This project is for educational purposes only. Unauthorized password cracking or hacking is illegal and unethical. Always have permission before testing any system.

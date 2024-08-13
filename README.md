# Password-Cracking-Project
Hello!
# Overview
In cryptanalysis and computer security, password cracking is the process of recovering passwords from data that has been stored in or transmitted by a computer system in scrambled form. The purpose of this project was to demonstrate the process of cracking a set of hashed passwords using tools like Hashcat and John the Ripper. Showcasing the functionality of cracking hashes with the tools exemplifies an understanding of cryptographic hashing and password-cracking techniques. The project aims to showcase the process of decoding hashes and understanding the importance of secure password practices.
# Features
Generates sample password hashes using different algorithms (MD5, SHA-1, SHA-256).
Utilizes Hashcat and John the Ripper to attempt to crack the generated hashes.
Outputs the results of cracked passwords into a text file for review. 
# Setting up the environment
  # Prerequisites
To run this project, ensure you have the following tools installed on your system:
- Python (for generating hashes)
- Hashcat
- John the Ripper
# Installation
1. git clone https://github.com/yourusername/password-cracking-project.git
2. cd password-cracking-project
3. Ensure wordlists.txt is available in your environment, which will be used for the cracking attempts
# Usage
1. Use the provided Python script to generate a set of hashed passwords.
2. If needed, transfer the generated hash file to a Linux environment.
3. Use Hashcat or John the Ripper to crack the hashes.
4. Save Results: Cracked passwords are saved into cracked_passwords.txt
# Using the Provided Scripts
1. Generate Password Hashes
      # Run the Python Script to generate a set of password hashes: python password_cracking.py (creates sample_hashes.txt, containing generated hashes)
2. Crack passwords with Hashcat
3. Crack the Passwords with John the Ripper
   Save cracked passwords to cracked_passwords.txt
# Explaination of Hashing Algorithms 
 # Md5, Sha-1, and SHA-256
 Hashing algorithms like MD5, SHA-1, and SHA-256 are used to securely store passwords by converting them into fixed-length strings of characters, regardless of the input length. These hashes are one-way functions, meaning they cannot be easily reversed to retrieve the original password. However, with enough computational power and the right tools, attackers can attempt to crack these hashes by comparing them against precomputed hash values (using wordlists, for example).
  # MD5: Produces a 128-bit hash value. It is fast but considered insecure due to vulnerabilities to collisions.
  # SHA-1: Produces a 160-bit hash value. More secure than MD5 but still vulnerable to certain attacks.
  # SHA-256: Part of the SHA-2 family, producing a 256-bit hash value, which is currently considered secure.
# Overview of Hashcat and John the Ripper
  # Hashcat 
  Hashcat is a high-performance password-cracking tool that supports various hash types and attack modes. It uses optimized algorithms to efficiently crack hashes, leveraging GPU acceleration when available. Hashcat is known for its flexibility and speed, making it a preferred tool for professional penetration testers and security researchers.
  # John the Ripper
  John the Ripper is another powerful password-cracking tool that supports multiple hash formats and attack modes. It is designed to be both fast and flexible, with the ability to perform dictionary attacks, brute force attacks, and more. John the Ripper is often used in CTF competitions and security testing scenarios.
# Contributing
If you'd like to contribute to this project, please fork the repository and create a pull request with your proposed changes.
# License
This project is licensed under the MIT License.
# Disclaimer
This project is for educational purposes only. Unauthorized password cracking or hacking is illegal and unethical. Always have permission before testing any system.

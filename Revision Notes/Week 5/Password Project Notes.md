# Password Analyser / Generator Project

## Password Strength Checker

**Epic Story**

As a user, I should be able to enter my first name, last name, birth date and password into the program, where my password will be compared against a list of thousands of common passwords. Additionally, my password will be examined for any inclusions of names or birth dates, as well as being reviewed against a password policy defined within the software. Upon completion of this I should receive a report on my password covering the final result of strength and the reasoning for this. As a user, I should be able to export this report into an external text file.

## Strong Password Generator

**Epic Story**

As a user, I should be able to generate a password for use. Once generated, this password should be reviewed against a password policy defined within the software, as well as examined for any inclusions of names or birth dates. This password should be displayed on screen followed by a prompt in which I may select to continue and generate an additional password.

## Questions

**Q:** Is there any guidelines for the password policy that you would like us to follow?

**A:** No.

**Q:** Is there anything you could clarify in terms of details to be stored in the database? Also, should passwords be encrypted when stored in the database?

**A:** Reading user info (including password or generated password.) Generate report based on database. No encryption is necessary, but can be performed.

**Q:** Should the program check for multiple date formats when checking for birth dates in a password?

**A:** Any format can be checked.

## Powerpoint Notes

**Trello**
- Trello was used for progression tracking
  - Assisted with team coordination / management
- Epic Stories and User stories
- Peer review

**Coding Approach**
- Modular approach (different files) for each function
  - Allowing for easier coordination, reusability and debugging
- Developed testing utilites using unit testing prior to finshing development on functions

**Test Driven Development**
- Screenshot of one of our unit tests for comparing password against policy
  - Imports unit test and policy function
  - File is ran, data is input to the policy function and processed
  - Output from function is compared against expected
- Validates unit of software perfoms as intended

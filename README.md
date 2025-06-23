# Module 4 Demonstration

## Description

Introduction to Exception Handling and Troubleshooting

## Author

Ivan Estropigan

## CONTENTS

Soon to be updated

## Module 4 Topics

- Exceptions
- Try-except statement
- Finally block
- Logging in Python
- Severity levels
- Logging exceptions
- Debugging Process, best practices
- VS Code Debugger
- Breakpoints, watch, step options, current line, call stack debug console

## WHAT IS INCLUDED IN THE FILE

- .gitignore
- module_4_data.txt
- module_4_demonstration_starter.py
- README.md

## WHAT IS EXCEPTION HANDLING?

- Exception handling is the process of dealing with exceptions that occur during the execution of a program.

- When an exception occurs, the program stops executing its normal flow and transfers control to an exception handler that can handle the exception.
  - What would we do if a fire started during a lecture?

- The handler can then take appropriate actions to recover from the exception and continue executing the program.

- Typically involves:
  - Detect the exception
    - Notice the fire/smoke
  - Raise (or throw) an Exception
    - Hit the fire alarm
  - Handle the exception
    - I get the fire extinguisher or the firefighters arrive
  - Resume Execution
    - Fire is gone, back to lecturing!

## EXCEPTIONS

- Detect
Exceptions can be detected by the program when an execution-time error occurs, or by the software developer when code is in place to detect a specific scenario.

- Raise
  - When an exception is detected by the program, it will create an exception object and will throw it. The exception object will contain information about the exception.
  - When the exception is detected through program code, the software developer must manually raise the exception.

- Handle
A try block should enclose the code that could raise an exception. The exception is handled in the corresponding except block.

- Resume
If the exception is handled successfully, the program will resume execution with the next line of code following the try-except block.

## TRY EXCEPT

- module_4_demonstration_starter.py: Initially contains several print statements, these will be replaced eventually with logging statements.

- The code has an error in the file name when opened:

```cs
file = open('module_4_dat.txt', 'r')
```

- Run the application and note than an exception occurs stopping the application.
  - This is a "FileNotFoundError"
  - Because the file. was. not. found.
  - So the program decided to crash and burn

- We can add a "Try Except" Block
  - This will handle this possible error and avoid crashing
  - The code continues after the try except block
  - The line of code populating data never executes

```cs
#Lecture Section 1

try:
    file = open("module_4_dat.txt", "r")
    data = file.readlines()
    file.close()
        print("File Closed")

except FileNotFoundError as e:
    print("File does not exist",e)
```

## MULTIPLE EXCEPTION BLOCK

- Add a second exception block to the example.
  - Exception blocks should be in specific to general order.
  - Exception will be handled by the first block that matches it

- Correct the filename but add a divide by zero error which will cause control to fall into the second exception block:

- Run the application and note  that the second exception block executes and the exception is a divide by zero error.

```cs
#LECTURE SECTION 1
try:
    file = open('module_4_data.txt', 'r')  correct spelling
    data = file.readlines()
    1 / 0
    file.close()
    print("File Closed")
except FileNotFoundError as e:
    print("File does not exist", e)
except Exception as e:
    print(“General exception”, e)
```

## MANUALLY RAISING AN EXCEPTION

- First redo the misspell the file name in the lecture section 1 section

```cs
try:
    file = open("module_4_dat.txt", "r")
```

- Add the code to the right into your code:
We are adding an exception for the case where we do not have any data (with/without the file)

```cs
#Lecture Section 2

try:
    if len(data) == 0:
        raise Exception("No data exists.")
    
    else:
        for record in data:
        items = record.split(',')
        names.append(items[0])
        titles.append(items[1])

        #LECTURE SECTION 3
        #REQUIREMENT: 
        salary *= (1 - RECOMMENDED_INCREASE)
        new_data.append([title,name,salary])
    
except Exception as e:
    print(e)
```

## FINALLY CLAUSE

- Input files are typically oepned using the clause which handles closing the file.
  - However, for demonstration purposes the  open and close are coded separately.

- Situations in which a finally block may be used include:

  - Clean up resources
    - The finally block is often used to clean up any resources that were accessed/used in the try block such as file or database resources.
    - This ensures that the resources remain available (not locked)following the try- except statement

  - Logging:
    - Regardless of whether an exception occurred, you may want to write the log file.
    - Having logging code in the finally block will ensure an entry is written to a log file regardless of whether an exception occurred.

  - Control Flow:
    - The finally block may be used to help control the flow of logic.
    - Logic could exist to determine determines whether to retry an operation, terminate the program, or take some other action based on the outcome of the try block.

## EXCEPTION HANDLING

- Add exception handling in remainder of program:
- Double check the filename is fixed
- Update the README file:

```cs
##Description 
Introduction to Exception Handling and Troubleshooting
Update 1: Added exception handling to file operations.
```

```cs 
#LECTURE SECTION 4  
try:
  file = open('updated_salaries.txt', 'w')
  for record in new_data:
      row = ""
      for index, item in enumerate(record)
        row += str(item)
        if index < len(record) - 1:
              row += (",")
      row += '\n'
      file.write(row)

except:
      print("Exception writing data.")

finally:
      file.write("END OF FILE.")
      file.close()

```

[EOF]

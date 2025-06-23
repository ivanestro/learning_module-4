# Module 4 Demonstration

## Description

Introduction to Exception Handling and Troubleshooting

Update 1: Added exception handling to file operations.
Update 2: Added logging to program
Update 3: Updated the formula to correctly calculate the updated salary: salary *= (1 + RECOMMENDED_INCREASE)

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

## WHAT IS LOGGING?

- Logging is the process of keeping track of events that occur when a program is running.
- The even could be a probllem, an error or simply information about the state of the program
- A log entry is recorded for each occurence of the event

- Logs can be used to:
  - monitor the state of the program
  - assist in the debugging process
  - provide revelant information for purposes such as auditing

- Types of logs include:
  - Event Logs
  - Transaction Logs
  - Exception Logs

- By default, logging messages are written to the console but can also be written to a file.

- Adding logging:
  - To incorporate logging into a Python program, the logging module must be imported
  - Add the following import statement to the top of file

- Severity levels:
  - The logging module, by default includes 5 levels of severity:
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL

  - Each level has a corresponding logging method:

```cs
#LECTURE SECTION 5

logging.debug("Debug level message.")
logging.info("Info level message.")
logging.warning("Warning level message.")
logging.error("Error level message.")
logging.critical("Critical level message.")
```

- Run the application and note the logging messages in the conspole

- Only those errors at the level of WARNING and above are logged

```cs
Warning: root: Warning level message
ERROR: root:Error level message
CRITICAL: root:Critical level message
```

## LOGGING CONFIGURATION

- Logging configuration can be set and modified using the basicConfig() method.

- The basicConfig method has been defined with **kwargs as its parameter.
  - This indicates that all parameters supplied to this method must be done so as keyword arguments.
  - The keyword arguments for the basicConfig() method that will be used in this course are:
    - level: Defines the severity level at or above which messages will be logged
    - filename: When included logging wil be written to the specified file. If excluded, logging by default will be opened to the console.
    - filemode: If a filename was provided, filemode determines the way in which the file will be opened and processed. The default mode is a which indicates append mode.
    - format: Defines the format of the logged message. The default format is {level, name, message}

- Add the following logging configuration to the program and discuss:

```cs
#LECTURE SECTION 1
logging.basicConfig(level = logging.DEBUG,
          filename = 'app.log'),
          filemode = 'w',
          format = %(asctime)s - %(levelname)s - %(message)s')
```

- Run the application again and note that logging at level DEBUG and up is logged, and that those messages are written to the file called app.log in the following format:

```cs 
2023-04-16 15:36:01,808 - DEBUG - Debug level message
2023-04-16 15:36:01,808 - INFO - Info level message
Etc…
```

## HIGH_SALARY REQUIREMENT

- One of the expected results is that employee with high salary would be identified.
- We will use the logging feature to incorportate the requirement to identify the high salary employees:

```cs
# LECTURE SECTION 3

if salary > HIGH_SALARY:
    logging.warning(f"{name}'s salary {salary} "
                  + f"is currently above "
                  + f"the recommended maximum "
                  + f"{HIGH_SALARY.}")

if salary * (1 + RECOMMENDED_INCREASE) > HIGH_SALARY:
      logging.warning(f"{name's} salary {salary} will be"
                    + f"above the recommended maximum"
                    + f "of {HIGH_SALARY}"
                    + f "with the planned "
                    + f "{RECOMMENDED_INCREASE} increase.")
```
- Run the program and note the logging that has taken place.

## LOGGING EXCEPTIONS

- Modify all exception and finally blocks, replace print statements with logging statements.

```cs
#LECTURE SECTION 1

except FileNotFoundError as e:
      #print("File does not exist: " e)
      logging.error('File does not exist.')
  
except Exception as e:
      # print(e)

finally:
      if file is not None:
          #print("File Closed")
          logging.info("File closed")
```

- Run the application and review the app.log file and the new_salaries.text file.

```cs
#LECTURE SECTION 2
except Exception as e:
      #print(e)
      logging.error("Exception processing data.")

#LECTURE SECTION 4
except:
      #print("Exception writing data.")
      logging.error("Exception writing data.")
```

- Run the application and review the app.log file and the new_salaries.txt file

## WHAT IS DEBUGGING?

- Debugging involves defining a set of steps to help effectively identify and solve the problem
- Below is a list of commonly used steps:
  - Identify the Problem 
  - Reproduce the Probelm
  - Determine the Source of the Problem
  - Correct the problem through:
    - Correction of the code
    - A workaround
  - Comprehensive Testing
  - Documenting the problem and solution

## VS CODE DEBUGGER

- Visual studio Code has a built in debugging utility.
- The python extension in the Visual Studio IDE (Integrated Deelopment Environment) supports debugging.

- Having a debugging utility built directly into the IDE allows the software developer to move seamlessly between debugging and developing without changing their work environment.


## DEBUGGING

- Identify the problem 

  - Expected behaviour:
    1. update_salaries.txt file is created with all employees receiving a 20% increase over their original salares found in module_4_data.txt

  - Actual behaviour:
    1. updated_salaries.txt file is created but employee salaries did not increase

- Reproduce the Problem
  - Run the application and note the action taken just prior to the error ocurring:
  - The last log item just prior to an incorrect salary being written is:

```cs 
2023-04-16 15:47:17,990 - INFO - File Closed
```

- Determine the Source of the Problem 
  - Go to the code locate the logging statement that produced the above log message:

```cs
logging.info("File Closed")

##LECTURE SECTION 2
```

- Narrow down the source of the problem starting at LECTURE SECTION 2
- Determine expected behavior by logging at the first record in the input file:

```cs
CEO/Chair of Board.Jo-Anne Sinclair, 140000
```

- Expected results:
  - Updated salary to $140,000 + 20% increase = $168,000
  - This record should be logged because it is above $120,000.00

## DEBUGGING BREAKPOINT

- A breakpoint allows an executing program to pause so that the software developer can examine the state of the program at run time.

- When a breakpoint is encountered, the program pauses(but does not terminate)
  - Add a breakpoint to the first line of code following the File Close logging statement:

## RUN IN DEBUG MODE

- To run the application in Debug mode, you can either click on the Run and Debug icon on the Activity Bar. Or click the run menu opption and choose Start Debugging
  - Note that execution stops when the breakpoint is encountered.
  - Note the floating toolbar.

## STEPPING

- Use the floating toolbar to "Step into" the code.
- There is also Step Over and Step Out
- Note the Variables in being populated in the variables window on the left
- Salary is an important variable as it is note a calculating correctly.

## WATCH

- Isolate salary by adding it to the watch window. 
- Right click on salary in the code editor and choose Add to Watch
- Continue stepping through the code and watch the value of salary in the watch window

- Initally: 
```cs
Salary: 140000.0
```

- Continue stepping and watch the salary change:
- Chnages to:
```cs
Salary: 112000.0
```

- This is not the expected value of $168,000.00
- The line of code which incorrectly modified the salary has been identified:
```cs
salary *= (1 - RECOMMENDED_INCREASE)
```

## FIX

- Stop the debugger:
- Edit the code:
salary *= (1 + RECOMMENDED_INCREASE)

- Run in debug mode again with this specific record( and expected results in mind.)
  - Note the change in salary:
  Salary: 168000.0

- Stop the debugger
- Remove the breakpoint
- Run in real time and review the log file.

## COMPREHENSIVE TESTING

- Ensure each record has been assigned the appropriate new salary
- Ensure all records that needed to be logged based on the correct salary have been logged.

- Update the READ.md File:
[EOF]

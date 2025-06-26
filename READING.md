# Reading and Viewing Materials

## Exceptions and Exception Handling

## What is an Exception?

An exception is an event that occurs during the execution of a program that disrupts the normal flow of the program's instructions. An exception can be caused by various reasons, such as an invalid input data, hardware errors, network errors, or coding errors.

## What is Exception Handling?

Exception handling is the process of dealing with exceptions that occur during the execution of a program. When an exception occurs, the program stops executing its normal flow and transfer control to an exception handler that can handle the exception. The handler can then take appropriate actions to recover from the exception and continue executing the program. Exception handling typically involves the following steps:

- Detecting the Exception
The program detects an exception when an error occurs during the execution of a statement or block of code. An exception can also be detected by the software developer by writing code to detect a specific scenario.

- Handle the Exception

If a try block encloses the code which caused the raised exception the program executes the code in the except block to handle the exception. The exception can be handled in a variety of ways such as displaying a message to the user, retrying the operation or blacking out of changes.

- Resume Execution

After the exception is handled, the program resumes executing its normal flow.

## Try-except statement

When writing code that could potentially raise an exception, it is important to include code that is able to handle the exception.

Any exception that is raised (either by the software developer, or through normal execution of the program) must be handled. If an exception is not handled, the program will terminate prematurely and unexpectedly. Exception handling is achieved by using the try-except statement. The try block contains the code that may raise an exception, and the except block  contains the code that handles the exception. As with all other blocks discussed in Python, the try except statement uses indenting to identify the blocks.

In the example below, the user is prompted for a number. As a software developer, it is important to acknowledge that we have little control over the values provided externally (by users, files, databases, etc) Since the code that follows performs a division operation and the value provided by the user acts as the denominator we must plan for the possibility that the user will enter a 0.

In the example, the code in the try block is executed line-by-line. If any line of code raises an exception, program control transfers directly to the except block and all remaining code in the try block is skipped. The code in the except block handles the exception- in this case providing a message to the user.

Whether an exception was raised or not, program flow will then continue at the first line of code following the try-except statement.

```cs
try:
    #code that may raise an exception
    denominator = int(input("Enter a number value for a denominator"))

    quotient = 10 / denominator

    print(f"QUotient is {quotient}")

except ZeroDivisionError:
    # code to handle the exception
    print("Cannot divide by zero.")

print("Next line of code...")
```

Below is the output produced by the above code when the user enters a non-zero value for the denominator:

```cs
Enter a number: 10
Quotient is 1.0
Next line of code...
```

Below is the output produced gby the above code when the user enters a zero value for the denominator:

```cs
Enter  a numberic value for a denominator: 0 
Cannot divide by zero.
Next line of code...
```

```Finally block```
The finally block can be used to execute code that should occur regardless of whether the try code raised an exception.

Situations in which a finally block may be used include:

- Clean up Resources: The finally block is often used to clean up any resources that may have been accessed/used in the try block such as file or database resources. This ensures that the resources remain available ( not locked) following the try- except statement.

- Logging: (See logging below). Regardless of whether an exception occurred, you may want to write to the log file. Having logging code in the finally block will ensure an entry is written to a log file regardless of whether an exception occurred.
  
- Control Flow: The finally block may be used to help control the flow of logic. For example, logic could exist to determine determines whether to retry an operation, terminate the program, or take some other action based on the outcome of the try block.

In the code below, if the file called example.txt does not exist, an exception will occur when the open function executes, and control will transfer to the FileNotFoundError except block.

If the file does exist, the try block will continue until the line 10/0 executes which will raise an exception.

In either scenario, the finally block will execute, and if the file had been opened it will be closed.

```cs
 Note!
When the with clause is used to open a file, the file is automatically closed. In that case, the finally block would not be necessary.
```

```cs
#Initialize file to None (Null).
file = None

try:
    # Open the file in read mode.
    file = open("example.txt", "r")

    # Read the contents of the file.
    content = file.read()

    # Some exception that may occur unrelated to the input file.
    10 / 0 

    # Print the contents.
    print(content)

except FileNotFoundError:
    print("File not found.")

finally: 
    # Close the file in the finally block
    if file is not None:
    file.close()
    print("File closed.")
```

- Handle Multiple Exception types

You will be faced with situations where the sequence of statements you're attempted to do may potentially raise different types of exceptions. You may include more than one except block after a try block.

```cs
try:
    dividend = float(input("Enter a divident?: "))

    divisor = float(input("Enter the divisor number?: "))

    quotient = divident / divisor 

    print(f"{dividend} divided by {divisor} is {quotient}")

except ValueError:
    print("You must enter a numeric value.")

except ZeroDivisionError:
    print("The divisor cannot be zero.")
```

If you need to handle multiple exception types in the same manner, you can list exception types in the same except statement.

```cs
try:
    dividend = float(input("Enter the dividend?: "))

    divisor = float(input("Enter the divisor number?: "))

    quotient = dividend / divisor

    print(f"{dividend} divided by {divisor} is {quotient}")

except (ValueError, ZeroDivisionError):
    print("An error occurred.")
```

- Best Practices

As with all software development constructs, there are some best practices that should be followed when building exception handling into your solution:

- Be specific: Instead of using a bare except clause or using the Exception class to catch all exceptions, try to catch specific exceptions that you know how to handle. This will help you write more targeted and effective exception handling code.

- Location Matters: Ideally, you should handle exceptions as close as possible to where they occur. This will make it easier to understand what went wrong and why and it will also help prevent unexpected side effects.

- Error Messages: When you raise an exception, include an error message that provides enough information to diagnose and fix the problem. The message should be concise and informative, and it should not reveal any sensitive information.

- Use the **finally** Clause: Use the finally clause to ensure that resources are properly released and that cleanup is performed. 

- Don't Suppress Exceptions: Avoid suppressing exceptions or hiding them from the user. Instead, log the error (see logging below and provide a clear and actionable message to the user).

- Raising(or Throwing) an Exception: The program creates an exception object and throws it. The exception object contains information about the type of exception that occurred and the location where it occurred. If the exception is detected through code written to identify specific scenarios, the software developer must manually raise the exception.

## Raising an Exception

An exception can be raised implicitly by various built in functions or external libraries when they encounter errors or exceptional conditions. For example, an exception is raised implicitly when you attempt to read from a file that does not exist. There are number of specialized exception classes which are descendent of the **Exception** class.

Below are some of the most common specialized **exception** classes:

- ValueError: Raised when a function receives an argument of the correct type but with an invalid value.

- TypeError: Raised when a function receives an argument of the wrong type.

- NameError: Raised when a variable or function name is used that is not defined in the current scope.

- IndexError: Raised when an index into a sequence is out of bounds.

- KeyError: Raised when a key is not found in a dictionary.

- AttributeError: Raised when an attribute is accessed that does not exist.

- FileNotFoundError: Raised when a file cannot be found

- ZeroDivisionError: Raised when attempting to divide by zero.

- AssertionError: raised when an assertion fails (Assertions will be covered in an upcoming module).

An exception can also be raised by the software developer as a means to control the flow of a program whn certain conditions arise. The software developer can raise an exception using the **raise** keyword followed by an instance of an exception class. In the example below, the exception is raised with a message. The message may be useful to the software developer when the exception is handled, so using am meaningful message based on the condition that caused the exception is important.

```cs
raise TypeError("The input must be a numeric type.")
```

## Programming Challenge

Write a Python program that prompts the user to enter two numbers, and then computes the sum of those numbers. However, if the user enters a non-numeric value, your program should raise an exception. Ensure the raised exception is caught and display an error message.

Example output:

Enter the first number: 5
Enter the second number: 10.5
The sum is: 15.5

Enter the first number: 5
Enter the second number: abc
Error: Invalid input. Please enter a number.

## Review Questions

1. What is an exception and what can cause it to occur during the execution of a program?
Exception is an error that occurs during the execution of a program, this can occur for many reasons such as invalid operations **ZeroDivisionError**. Wrong data types such as **TypeError**. Missing Files such as ***FileNotFoundError**. Invalid values being inappropriate value to a function **IndexError**. Out of range access invalid index in a list **IndexError** and lastly Missing keys in a dictionary accessing a key doesn't exist **KeyError**

2. What is the role of an exception handler?
The role of an exception handler is to catch errors in a program and allow it to handle them without stopping unexpectedly.

3. What are the steps involved in exception handling?

    - try block that might raise an exception
    - except block handles the exception if one occurs
    - else block is optional executes if no exceptions occur in the try block
    - finally block is optional executes no matter what whether an exception occurred or not.

4. How can an exception be raised in Python?
Exceptions can be raised in Python when a statement is either correct or incorrect, depending on how the code is written. For example, if you try to open a file that doesn’t exist, a FileNotFoundError will be raised, indicating that the file cannot be opened. If the file is found, the program continues, but it may still raise other exceptions based on the next steps in the code.

5. What is the purpose of the try-except statement in Python?
The try-except statement is used to catch errors so the program doesn’t crash. It helps you handle problems like invalid input or missing files in a safe way.

## Logging

Logging is the process of keeping track of events that occur when a program is running. The event could be a problem, an error, or simply information about the current state of the program. A log entry is recorded for each occurrence of the event. Logs can be used to monitor the state of the  program, to assist in the debugging process, or to provide relevant information for purposes such as auditing.

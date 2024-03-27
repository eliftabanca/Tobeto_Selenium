-What are decorators in Python?
 Decorators are Python functions that allow you to wrap another function as an input and modify itsbehavior without altering the wrapped function’s code. They are used to extend the behavior of a particular object, such as a class, method, or function. This approach promotes reusability, modularity, and separation of concerns in your Python programs.


-How to write a decorator in Python?
 Now that you know the basics of decorators, let's look at how to write a simple decorator in Python.

 Step-by-step explanation
 1-Define a higher-order function that takes a function as input.
 2-Inside this higher-order function, define a nested function (a wrapper) that will modify or extend the input function's behavior.
 3-Call the input function within the wrapper function and add any additional functionality you desire.
 4-Return the wrapper function from the higher-order function
 
 
Here are some commonly used decorators in Python with Selenium and Pytest:

 *@pytest.mark.parametrize: This decorator allows a test function to be called multiple times with different parameters. It's useful for testing the same test code with different inputs.

 *@pytest.fixture: This decorator defines a function to be run before a test function or a test file. It can be used to set up conditions such as initializing a browser or preparing a specific state.
  
 *@pytest.mark.skip: This decorator is used to temporarily skip a test. It can be used to prevent tests from running under certain conditions or for debugging purposes.    
 
 *@pytest.mark.xfail: This decorator is used when a test is expected to fail but the failure is temporary.

 *@pytest.mark.timeout: This decorator sets a maximum runtime for a test. If the test does not complete within the specified time, it times out and fails.

 *@pytest.mark.dependency: This decorator allows you to specify dependencies between tests, ensuring that certain tests are run before others. It helps in managing the order of test execution.


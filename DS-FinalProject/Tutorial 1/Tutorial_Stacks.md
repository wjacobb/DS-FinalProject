# Reading: Stacks

## Table of Contents

### Stacks
* [Introduction/Analogy](#h1)
* [The Purpose of Stacks](#h2)
* [How to "Undo"](#h3)
* [Demonstration/Example](#h4)
* [Solve](#h5)
* [Key Terms & Operations](#h6)

### <a name="h1"></a>**Introduction/Analogy**
A **stack** is a data structure that is defined by the order in which items are added and removed. The order that stacks work in is often referred to as “Last In, First Out” (LIFO) There are many reasons and methods when working with stacks that are helpful when handling important data.

What does it mean, “Last In, First Out”? Well, imagine you are cooking pancakes. When you finish your first pancake it goes on top of the plate, then the second goes on top of the first and so on so forth. When you want to grab a single pancake from the stack which one would you normally take? The answer is the topmost one. Then you go down one pancake at a time until there are no more.

Now when we are cooking and add a pancake to the stack, this is called a **push** operation. In our analogy of pancakes when we add one to the top of our stack the python term for “top” is actually **back**. When a line of children are lining up one at a time the first and temporarily only child is at the front and the back. When the second child gets in line the first student is still at the front, but the new back is the second child and the new back of the list of children keeps moving further and further until stopped by the amount of children.

![Stack Picture](https://byui-cse.github.io/cse212-course/lesson03/pancake_stack.jpeg "Pancake Stack")

In our analogy of pancakes and children when we remove an item from the stack it is called a **pop** operation. Ever think about the term when a child “pops” out of line, now you can use it as a visual when coding.

### <a name="h2"></a>**The Purpose of Stacks**
The purpose of understanding stacks is to know the flow of inputting and outputting data one thing at a time. Think of when you make an error by typing a line of code that is unnecessary. What do you do? One option is highlight and delete, backspace until you are good, or fitting to this analogy we could press the Undo button.

### <a name="h3"></a>**How to "Undo"**
We all make mistakes when typing or programming. Sometimes when we make an error we press the Undo button so we could fix or change what we originally made.

Imagine that we typed the sentence, “I am happy to neet you”. When pushing onto a stack the order would be, “I”, “am”, “happy”, “to”, “neet”, “you”. If we were to undo or pop the last thing off of the stack we would then have the stack “I”, “am”, “happy”, “to”, “neet”. If we were to pop off of the stack again we can get to our typo “neet” instead of “meet”. So when we pop the end of the stack we now have, “I”, “am”, “happy”, “to”. We can now add what we want to say like “meet”, “you”.

### <a name="h4"></a>**Demonstration/Example**

Here's an example of a stack:

```python
stack = []
stack.append("r")
stack.append("a")
stack.append("c")
stack.append("e")
stack.append("c")
stack.append("a")
stack.append("r")
stack.append("!")

for i in stack:
    print(i, end = "")
print()

# This will print out "racecar!" However, what would happen if we were to pop the last piece of data that was collected, the "!"? We would simply get "racecar". In order to do this, you simply type:

stack.pop()
```

### <a name="h5"></a>**Solve**
Alrighty! Now that we've seen adding data and popping data in action guess what the outcome of the following code is!

**Hint:** The data is stored as a list so it will look something like "[1, 9, 3, 6]"

[Stacks Problem](Solve_Stacks.py)

Once you have completed solving the problem above, take a look at the solution and compare.

[Stacks Solution](Solve_Stacks_Answer.py)

### <a name="h6"></a>**Key Terms & Operations**

|Common Stack Operation|    Description   |      Python Code     |    Performance    |
|:--------------------:|:----------------:|:--------------------:|:-----------------:|
|push(value)           |Adds "value" to the back of the stack.|my_stack.append(value)|O(1) - Performance of adding to the end of a dynamic array|
|pop()                 |Removes and returns the item from the back of the stack.|value = my_stack.pop()|O(1) - Performance of removing from the end of a dynamic array|
|size()                |Return the size of the stack.|length = len(my_stack)|	O(1) - Performance of returning the size of the dynamic array|
|empty()               |Returns true if the length of the stack is zero.|if len(my_stack) == 0:|O(1) - Performance of checking the size of the dynamic array|


* **back** - Refers to the location in a stack where a push and pop occurs. The last item put into the stack is found in the back.

* **front** - Refers to the location in a stack where the first item added to the stack can be found. Traditionally, this is index 0 of a dynamic array.

* **pop** - The operation to remove the last item pushed to the stack. The item from the back of the stack is removed and returned.

* **push** - The operation to add a new item onto the stack. The item is placed at the back of the stack.

* **stack** - A data structure that follows a Last In, First Out (LIFO) rule. The stack is used to reverse data or remember previous data including previous results.

Click [here](https://github.com/wjacobb/DS-FinalProject/blob/main/DS-FinalProject/Welcome.md) to return to the Welcome page.

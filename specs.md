### Implementing a Priority Queue using Min and Max Heap

**Due Wednesday, November 23rd @ 10:00 PM ET**

*This is not a team project, do not copy someone else's work.*

*Make sure to read the entire project description, especially the grading policies.*

## Assignment Overview

![](img/minheap.png)

In this project, you will be implementing **A Min Heap and a Max Heap**. Heaps is a tree based structure. In our implementation we will be using a binary tree. In order to be a heap, both structural and relational properties must be met. 
For the *structural property*, the tree must be a complete or a perfect binary tree. See definition of a complete and binary tree on zyBooks, and also in image below.
![](img/Structural_Property.png)
 For the *relational property*, for a  Min Heap a node must be less than its children. For a Max Heap a node must be greater than its children. 
 See D2L Week 9 content for more depth explanation regarding this data structure.





## Assignment Notes

* **REMEMBER TO FILL OUT YOUR DOCSTRINGS!**
* **heapq** and any other **priority queue/heap** modules are not permitted on this project, it will result with a 0 of this project.
* Values for the maxheap will only be numbers but you should make the minheap work for values of any type.
* Some heaps start at an index at one. However, for this assignment, **indexing will start at index zero**, just like normal lists.
* Recall  **.pop(0)** is **O(n)**, and using it will likely cause you to break time complexity!
* Consider using the pythonic swap! 
The syntax for this is **`a, b = b, a`**. 
it is the same as writing something like `temp = a; a = b; b = temp` but removes the extra variables and works a bit cleaner!
* **HINT:** **MaxHeap class uses a MinHeap** to handle all of its operations. Think about how you can do a math trick to make this work
  * Is 2 greater than or less than 4? Is -2 greater than or less than -4?

## Assignment Specifications

You will be given one file to edit, `solution.py`. You must complete and implement the following functions. Take note of the specified return values and input parameters. 

### **class MinHeap:**

_**Do not modify** the following attributes/methods_

*   **Attributes:**
    *   **data:** This is a list that stores all the elements in our heap
*   **init(self) -> None:**
    *   This function initializes a MinHeap
*   **str(self) -> str:**
    *   A string representation of the list.
*   **repr(self) -> str:**
    *   A string representation of the list.
*   **to_tree_format_string(self) -> str:**
    *   This makes a heap in breadth first formatting, for use in debugging

Implement the following functions. Take note of the specified return values, input parameters, and time complexity requirements. **Do not change the function signatures, including default values.**

*   **\_\_len\_\_(self) -> int:**
    *   Returns the length of the heap
    *   Time complexity: _O(1)_
*   **empty(self) -> bool:**
    *   Checks if the heap is empty
    *   Return a boolean stating if the heap is empty or not
    *   Time complexity: _O(1)_
*   **top(self) -> T:**
    *   Returns the top value of the MinHeap
        * This will be the minimum value, as this is a MinHeap!
    *   Time complexity: _O(1)_
*   **get_left_child_index(self, index: int) -> int:**
    *   Computes the index of the left child at the parent index **index**
    *   Returns an int with the left child's index (or None if no such child exists)
    *   Time complexity: _O(1)_
*   **get_right_child_index(self, index: int) -> int:**
    *   Computes the index of the right child at the parent index **index**
    *   Returns an int with the right child's index (or None if no such child exists)
    *   Time complexity: _O(1)_
*   **get_parent_index(self, index: int) -> int:**
    *   Computes the index of the parent at the child index **index**
    *   Returns an int with the parents's index (or None if no such parent exists)
    *   Time complexity: _O(1)_
*   **get_min_child_index(self, index: int) -> int:**
    *   Computes the index of the child with the lower value at the parent **index**
        * This function should take advantage of two of the other functions you have written!
    *   If both children have the same value, return the right child's index
    *   If the node has no children, return None 
    *   Returns an int with the minimum value child's index (or None if no children)
    *   Time complexity: _O(1)_
*   **percolate_up(self, index: int) -> None:**
    *   Percolates up the value at index **index** to its valid spot in the heap
        * That is, percolate the value up until the node's value is greater than that of its parent
    *   When comparing equal nodes, treat the parent as if it is smaller than the child
    *   Returns None
    *   Time complexity: _O(log(n))_
*   **percolate_down(self, index: int) -> None:**
    *   Percolates down the value at index **index** to its valid spot in the heap
        * That is, percolate the value down until both of it's children's are less than the value that started at position index
    *   When comparing equal nodes, treat the parent as if it is smaller than the child
    *   Returns None
    *   Time complexity: _O(log(n))_
*   **push(self, val: T) -> None:**
    *   Pushes the **value** to our heap and gets it to the proper position
        * This should be a pretty short function - most of the work will happen in percolate_up!
    *   Returns None
    *   Time complexity: _O(log(n))_
    *   Auxiliary Space Complexity: _O(1)_
*   **pop(self) -> T:**
    *   Removes the top element from the heap
        * This will be the minimum value!
    *   Restores the heap to be valid after the top element is removed 
    *   Returns the value that was popped
    *   Time complexity: _O(log(n))_
    *   Auxiliary Space Complexity: _O(1)_

### **class MaxHeap:**

_**Do not modify** the following attributes/methods_

*   **Attributes:**
    *   **MinHeap:** This MinHeap does most of the work for us in MaxHeap
*   **init(self) -> None:**
    *   This function initializes a MinHeap
*   **str(self) -> str:**
    *   A string representation of the list.
*   **repr(self) -> str:**
    *   A string representation of the list.
*   **len(self) -> int:**
    *   Length of the MaxHeap
*   **print_tree_format(self) -> str:**
    *   This prints the heap in breadth first formatting, for use in debugging

Implement the following functions. Take note of the specified return values, input parameters, and time complexity requirements. **Do not change the function signatures, including default values.**

*   **empty(self) -> bool:**
    *   Checks if the heap is empty
    *   Return a boolean stating if the heap is empty or not
    *   Time complexity: _O(1)_
 
*   **top(self) -> int:**
    *   Returns the top value of the MaxHeap
        * This will be the maximum value, as this is a MaxHeap!
    *   Time complexity: _O(1)_
*   **push(self, val: int) -> None:**
    *   Pushes the **value** to our heap
    *   Returns None
    *   Time complexity: _O(log(n))_
    *   Auxiliary Space Complexity: _O(1)_
*   **pop(self) -> int:**
    *   Removes the top element from the heap
    *   Returns the value that was popped
    *   Time complexity: _O(log(n))_
    *   Auxiliary Space Complexity: _O(1)_

## Application: Sneaky Thanksgiving Feast
![](img/growithe.png)<br> ![](img/turkey.jpg)<br>

Thanksgiving is back in town, and with it another mischievous venture from Growlithe (The family dog). Every Thanksgiving the family buys a delicious turkey that can only be eaten  on Thanksgiving day. However, Growlithe has other plans for when this Thanksgiving turkey will be eaten. In this problem, you will be Growlithe, and you need to design an algorithm that will allow you to eat the Thanksgiving turkey little by little when none of the family members are within the vicinity.

For this problem, you'll be given a list of sorted lists of intervals (sorted based on starting time first and then end time for ties), where each list of intervals represents when a family member will be in the vicinity. 
You want to find all the time intervals where no family members are in the vicinity, this way, we know when we can take bites out of the turkey. A good way of approaching this problem is to think of the concept of merging a sorted list of intervals. 

Here's a link to a resource detailing the merging of a sorted list of intervals: https://www.geeksforgeeks.org/merging-intervals/

Merging the overlapping intervals will leave you with an interval that is equivalent to the two intervals you had before. So, as an example, if you had [1, 4] and 
[2, 5], you could merge these intervals to just be [1, 5].

Two intervals are defined as overlapping if start1 <= start2 <= end1 or start2 <= start1 <= end2. Note the use of `<=`. This means that if you have one interval starting at the same time another ends, they **are** considered overlapping.

- **get_eating_times(values: List[List[List[int]]]) -> List[List[int]]:**.
  - Takes in a list of interval lists (each interval list corresponds to one family member) such that each sublist i returns a list of finite-length intervals that do not overlap with any of the given intervals, sublists are not guaranteed to be in sorted oder.
  - **param values**: List of interval lists
  - **return**: A list of non overlapping intervals
  - **Note:** The list of ints will only contain two values representing the start and end of an interval
  - Time Complexity: _O(nlog(n))_ where n is the total number of intervals across all the lists. **Notice that the number of family members is not factored into the time complexity at all. This is a hint**.
  - Auxiliary Space Complexity: _O(n)_
  - **You are not allowed to use a sort function for this problem. Doing so will result in losing all manual and automated points.**

### Examples
![](img/merging.png)<br>
```
        family_times = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
        answer = get_eating_times(family_times)
        # answer should be = [[3, 4]]
        
        Explanation:
        You start with [1, 2] since it is the lowest valued interval. 
        From here you compare it to [1, 3] since it is the next lowest valued interval. 
        Since these two intervals overlap with each other, they'll be merged into [1, 3].
        [1, 3] will then be compared to [4, 10]. Since 4 > 3, [3, 4] will be appened to the solution, and the
        previous interval will be set to [4, 10]. Lastly, [4, 10] will be compared to [5, 6]. Since [5, 6]
        overlaps with [4, 10], these two intervals will be merged into [4, 10]. 
```

```
        family_times = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
        answer = get_eating_times(family_times)
        # answer should be = [[5, 6], [7, 9]]
        
        Explanation:
        You start with [1, 3] since it is the lowest valued interval.
        From here you compare it to [2, 4] since it is the next lowest interval. 
        Since these two intervals overlap with each other, they'll be merged into [1, 4].
        [1, 4] will then be compared to [2, 5]. Since these two intervals overlap, they'll be merged into [1, 5].
        [1, 5] will then be compared to [6, 7]. Since 6 > 5, [5, 6] will be appened to the solution and the
        previous interval will be set to [6, 7]. Lastly, [6, 7] will be compared to [9, 12]. Since 9 > 7, [7, 9]
        will be appended to the solution and previous will be set to [9, 12].
```

```
        family_times = [[[1, 2], [2, 3]]]
        answer = get_eating_times(family_times)
        # answer should be = []
        
        Explanation:
        You start with [1, 2] since it is the lowest valued interval.
        From here you compare it to [2, 3] since it is the next lowest interval. 
        Since these two intervals overlap with each other, they'll be merged into [1, 3].
        There will be no values appened to the solution. 
```


## Submission

### Deliverables

In every project you will be given a file named as "solution.py". Your will work on this file to write your Python code. We recommend that you download your "solution.py" and "tests.py" to your local drive, and work on your project using PyCharm so you can easily debug your code.

Below are the simple steps to work on any project locally in your personal computer in this class:

**APPROACH 1: USING D2L TO DOWNLOAD PROJECT'S STARTER PACKAGE:**

Make sure you installed PyCharm
You can download the starter package from D2L under Projects content. Watch the short tutorial video on how to download the starter package from D2L and open it up in PyCharm.
Work on your project as long as you want then upload your solution.py , (watch the short tutorial video on D2L for uploading your solution.py), and upload your solution.py to Codio.
Click Submit button on Guide when you are done! 

**APPROACH 2: USING CODIO TO DOWNLOAD solution.py and tests.py**

On your own computer make sure to create a local folder in your local drive, name it something like ProjectXX, replace xx with the actual project number, in this case your folder name would be Project03.
Download solution.py from Codio by simply right mouse clicking on the file tree, see image below 
Download tests.py from Codio by simply right mouse clicking on the file tree as shown above.
Work locally using PyCharm as long as you need.
When finished with your solution.py file, upload your file to Codio by right mouse clicking on the Project Directory on file tree.You should rename or remove the solution.py file that is currently existing in Codio before you upload your completed version.
Go To Guide and click Submit button 
It does not matter which approach you choose to work on your project, just be sure to upload your solution, “solution.py”, to Codio by and click on the Submit button by its deadline. Working locally is recommended so you can learn debugging. You can complete your entire solution.py using Codio editor, debugging may not be as intuitive as PyCharm IDE. For this reason we recommend that you work locally as long as you need, then upload your code to Codio.

### Grading

The following 100-point rubric will be used to determine your grade on Project 8:

- Policies
  - ***You will not receive any points on this project if you use Python's built-in heapq library or any other package that 
    implements a heap or priority queue for you!***
  - ***Use of the MinHeap in the application is required for credit on the application problem!***
  
- Tests (70)
    - MinHeap: __/40
      - Length, Empty --/8
      - Top: __/4
      - Get_Left_Child_Index: __/4 
      - Get_Right_Child_Index: __/4 
      - Get_Parent_Index: __/4 
      - Get_Min_Child_Index: __/4 
      - Push: __/6
      - Pop: __/6
    - MaxHeap: __/20
      - Top: __/4
      - Push: __/8 
      - Pop: __/8 
  - Application: __/10
    - test_application: __/10

- Manual (30)
  
  * Loss of 1 point per missing docstring (max 3 point loss)
  * Loss of 2 points per changed function signature (max 20 point loss)
  * Loss of complexity and loss of testcase points if MinHeap and MaxHeap are not used in the application problem (must use one or the other).
  - Complexities:
    - Run Time: Length & Empty (MinHeap): __/1 
    - Run Time :Top (MinHeap): __/1
    - Run Time: Get_Left/Right/Min Child and Parent_Index: __/1
    - Run Time and Auxiliary Space: Push (MinHeap): __/4
    - Run Time and Auxiliary Space :Pop (MinHeap): __/4
    - Run Time :Top (MaxHeap): __/1
    - Run Time and Auxiliary Space: Push (MaxHeap): __/3
    - Run Time and Auxiliary Space: Pop (MaxHeap): __/3 
    - Run Time and Auxiliary Space Application: __/6
- feedback and citation __/2


*This project was created by Joseph Pallipadan and Nate Gu, adapted from the work of Ian Barber, Alex Woodring, Zosha Korzecke, Max Huang, and Angelo Savich*

* **Important reminder**
Note students can not use Chegg or similar sites, see syllabus for details, use of outside resources for the application problem is strictly forbidden, use of outside resources is limited to max of 2 functions in a project.


    * **DOCSTRING** is not provided for this project. Please use Project 1 as a template for your DOCSTRING . 
    To learn more on what is a DOCSTRING visit the following website: [What is Docstring?](https://peps.python.org/pep-0257/)
      * One point per function that misses DOCSTRING.
      * Up to 5 points of deductions











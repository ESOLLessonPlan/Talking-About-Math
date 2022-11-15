
# coding: utf-8

# # Talking about math: Introduction to programming and Python for English Learners

# ## Day 1: Getting the Basics

# ### Today's ELD Standards

# ELD-MA.9-12.Explain.Interpretive: Interpret mathematical explanations by analyzing data and owning problem-solving approaches.
# 
# ELD-MA.9-12.Explain.Expressive: Construct mathematical explanations that describe data and/or approach used to solve a problem.

# ### Today's Objectives

# SWBAT:
# 
# 1. Use the Python Programming Language to solve basic word problems by setting variables and performing arithmetic operations.
# 2. Use notes in code cells to describe and explain each step in solving a word problem.
# 3. You markdown cells to explain their conclusions.

# ### 1. Your First Program

# In programming with any language, the traditional first less involves the "print" function.  
# 
# The customary first greeting is "Hello World!"

# In[1]:


print("Hello World!")   #This prints the words "Hello World!".


# Now you can try!!  In the cell below, print "Hello World!".

# Great! Now print something else.  
# Type something (school appropriate) between the quotation marks below.

# In[ ]:


print("")   #This is the print function.  Type between the quotation marks ("").


# Let's put it all together.  
# Print the name of your favorite English teacher in using the print() function and the code cell below.

# ### 2. Code vs. Markdown Cells

# There are 2 main types of cells in Python (code cells and markdown cells).
# 
# Code cells are the rectangles where you type your code 
#   - like when you wrote your print("Hello World!") function.  
# 
# Markdown cells are used give information, like titles and conclusions.
# 
# This explanation is written in a markdown cell.  
# I'll also include an unused markdown cell below.  
# Markdown cells do not have "In [ ]" in front of them.

# (markdown cell)

# In[2]:


print("Hello")     #This is a code cell


# Each line in a code cell, like the one above, should include a note that explains what it is doing.                     
# Start each note with a "#" sign to separate it from the code.

# ### 3. Introduction to Operators

# There are 7 arithmetic operators in Python:
# 
# Addition (+)
# 
# Subtraction (-)
# 
# Multiplication (*)
# 
# Division (/)
# 
# Exponents (**)
# 
# Let's find out what these do!!

# In[3]:


3+5   #Here we are adding two numbers. You do not need to put an 'equals' sign.


# In the following cells, come up with a few simple math problems.  
# Play with the different operators and see how they work.  
# In all that you do, make sure to use notes to explain what you are doing.  
# 
# Example:
# 

# In[4]:


7**2      #This expression gives us 7 squared.


# Now you try some expressions.

# ### 4. Using Operators

# Use Python operators to solve the following problems.                                      
# Remember to include a note describing what you are doing.

# Add 97 and 152.

# Subract 139 from 124.

# Divide 196 by 9.

# Calculate 98 to the 5th power.

# ### 5. Setting Variables

# Just like in our math classes, we can create variables to take the place of numbers or expressions:

# In[5]:


x = 5        # I am setting a variable, x, as equal to the number 5.
y = 42       # I am setting a variable, y, as equal to the number 42.
x + y        # I am adding the two variables together.


# Variables can also be complete words:

# In[1]:


cats = 5     # There are 5 cats in my house.
dogs = 42    # There are 42 dogs in my house.
cats + dogs  # I am adding the cats and dogs to find the total number of animals.


# In the following code cell, practice creating two variables.                          
# The variables can be letters or complete words.  Add them together.

# ### 6. Solving Word Problems

# Read the following word problems.  Then, use your Python operators to solve the problems.  
# Use markdown cells and notes (using #) to explain your work.  
# I'll do the first problem for you:

# Question 1. 
# 
# Anna has 10 pieces of gum to share with her friends.  
# There wasn't enough gum for all her friends, so she went to the store.         
# She bought 70 pieces of strawberry gum and 10 pieces of bubble gum.  
# How many pieces of gum does Anna have now?

# In[7]:


Beginning = 10         # Anna begins with 10 pieces of gum.
Strawberry = 70        # Anna bought 70 pieces of strawberry gum.
Bubble = 10            # Anna also bought 10 pieces of bubble gum.


# In[8]:


Beginning + Strawberry + Bubble


# By adding the three amounts together, I found that Anna now has 90 pieces of gum.

# Question 2. 
# 
# Isabela has 17 apples.  She gives 9 apples to Luisa.  How many applies does Isabela have now?

# Question 3.
# 
# Elsa has 23 cats and I have 2 cats.                                        
# If Elsa gives me 5 cats, how many more cats does Elsa have than I do?

# (markdown cell)

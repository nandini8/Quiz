# Quiz
A demo app for Quiz. (AppliedAI Consulting)

## Task
A python code so that someone can take the quiz/MCQ from the attached quiz.json file. When the code is run on command line, it should print the two groups, sport and math. User can select any one group, then it should print the question, with its options and let user provide an answer.
After answering all the questions, final result should be printed.

A docker image using Dockerfile for the code and you also need to upload image into Docker Hub.

# To run the app
1. ``` $ git clone https://github.com/nandini8/Quiz.git ```
2. ``` $ cd app```
3. ``` $ python scripts/main.py```

# Using docker
``` $ docker run nandini8/quiz ```

OR

1. ``` $ git clone https://github.com/nandini8/Quiz.git ```
2. ``` $ cd app ```
3. ``` $ docker build -t quiz . ```
4. ``` $ docker run quiz ```

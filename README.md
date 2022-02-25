# Wait!!
## What is this project Project?
The main aim of this project is to perform sentiment and emotion analysis of all the videos uploaded to twitter tagging the twitter bot which we have created. We can't fetch the videos without mentioning the bot as twitter doesn't allow this, so we need our own Twitter developer API.
## What is sentiment analaysis then?
Sentiment analysis is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information.
## Now what is emotion analysis?
Emotion analysis is the process of identifying human emotion.

## Okay you know everything now, Let's start 
### Let's setup in your local machine first:
1. `fork` the repository  - Creates a cope of this project in your github so that you can make changes locally.
2. Clone the repository to your local machine using `git clone https://github.com/hritikksingh/Twitter-video-emotion-and-sentiment-analysis.git`.
3. Now navigate to the dowloads folder to install the requirements.txt using command `pip install -r requirements.txt`
4. Now you can start your coding magic to make some awesome changes.

## <u> How to Contribute? Let's Get Started: </u>

#### <ins> Step 1. Create a Copy of this Repository </ins>
To work on an open-source project, you will first need to make your copy of the repository. To do this, you should fork the repository and then clone it so that you have a local working copy.

> **Fork :fork_and_knife: this repo. Click on the Fork button at the top right corner.**

With the repository forked, you’re ready to clone it so that you have a local working copy of the codebase.
 
> **Clone the Repository**
 
To make your local copy of the repository you would like to contribute to, let’s first open up a terminal window.
 
We’ll use the git clone command along with the URL that points to your fork of the repository.
 
* Open the Command Prompt or your git bash terminal
* Type this command:

```
git clone https://github.com/hritikksingh/Twitter-video-emotion-and-sentiment-analysis.git
```



#### <ins> Step 2: Creating a New Branch </ins>
It is important to branch the repository so that you can manage the workflow, isolate your code, and control what features make it back to the main branch of the project repository.
 
When creating a branch, you must create your new branch off of the master branch. 
**To create a new branch, from your terminal window, follow:**


```
git branch new-branch
git checkout new-branch
```
Once you enter the git checkout command, you will receive the following output:

```
Switched to branch 'new-branch'
```


#### <ins> Step 3: Environment setup: </ins>
Once You have installed the repositories, make sure to install dependencies using pipenv with the provided Pipfile and execute all commands using pipenv. Also, please make sure to add the correct path to the video file in camera.py on line 11. Next, to install pipenv, the dependencies, and run the main.py file, execute the following commands from your terminal or command prompt, making sure to add the right paths where necessary:

```
cd \path\to\Project-Exp-Recog\
pip install pipenv
pipenv install
pipenv run python3 main.py
```


Now Your environment is ready to contribute ;)

#### <ins> Step 4: Contribute: </ins>
Make relevant changes. Add new algorithms, Add Readme files, Contribute in any way you feel like :)

#### <ins> Step 5: Commiting and Pushing: </ins>
Once you have modified an existing file or added a new file to the project, you can add it to your local repository, which we can do with the git add command.

``` git add filename``` or ``` git add .``` 

You can type the command ```git add -A``` or alternatively ```git add -all``` for all new files to be staged.

**With our file staged, we’ll want to record the changes that we made to the repository with the ```git commit``` command.**
<p> The commit message is an important aspect of your code contribution; it helps the other contributors fully understand the change you have made, why you made it, and how significant it is.  </p>
 
 ```
 git commit -m "commit message"
 ```
 
 
 At this point you can use the ```git push``` command to push the changes to the current branch of your forked repository:
 ```
 git push --set-upstream origin new-branch
 ```
 
#### <ins> Step 6: Create Pull Request </ins>
At this point, you are ready to make a pull request to the original repository.
 
You should navigate to your **forked** repository, and press the “Compare & pull request” button on the page. 
![PR Git](https://user-images.githubusercontent.com/66662965/115048150-e2413600-9ef6-11eb-942b-537ed5e2aceb.png)

GitHub will alert you that you can merge the two branches because there is no competing code. You should add in a **title**, a **comment**, and then press the **“Create pull request”** button.

![create pr](https://user-images.githubusercontent.com/66662965/115048337-161c5b80-9ef7-11eb-9d6d-959224497c0f.png)

#### <ins> Step 6: CONGRATULATIONS :boom: :clap: :relaxed: </ins>
You have made your contributions. Kudos to you!! 🎉✌🏻🙌🏻

<hr> </hr>


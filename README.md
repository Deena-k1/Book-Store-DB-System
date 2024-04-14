# Read First Girls 
### **Your gateway to reading _lots_ of books**



## All documentation can be found in the ['docs'](https://github.com/Deena-k1/Git.assignment/tree/main/docs) file. 
Here is how we'd recommend working through those files: 
- [HowToConfig](https://github.com/Deena-k1/Git.assignment/blob/main/docs/HowToConfig.md)
- [SetUpDB](https://github.com/Deena-k1/Git.assignment/blob/main/docs/SetUpDB.md)
- Continue with **README**


<!--- Add your GitHub username, link to page --->
### Who we are and where to find out more about us:

* **Kirstie Ross** - [GitHub profile krossco](https://github.com/krossco)

* **Lara Amusan** - [GitHub profile larasacodes](https://github.com/larasacodes)

* **Salma Mounes** - [GitHub profile salma3385](https://github.com/salma3385)

* **Deena Khan** - [GitHub profile Deena-k1](https://github.com/Deena-k1)
* **Alexandria Kerr** - [GitHub profile AlexiaKerr](https://github.com/AlexiaKerr)

### Questions answered from Assignment: 

[.gitignore](https://github.com/Deena-k1/Git.assignment/blob/main/.gitignore) - This folder is used to add any files you wish to not commit. 

[requirements.txt](https://github.com/Deena-k1/Git.assignment/blob/main/docs/requirements.txt) - requirements.txt is a file that contains a list of packages or libraries needed to work on a project that can all be installed with the file. You can use the following code to install all the libraries and packages in the file:
`pip install -r /path/to/requirements.txt`
(Insert your own file path leading to the requirements.txt file) 




## Routes ##
localhost:127.0.0.1:500...
|Request Type                  |HTTP Request Path                        | Description                                  |
|:----------------------------:|:----------------------------------------|:---------------------------------------------|
|GET                           |.../booksavailable                       |Display all books available                   |
|GET                           |.../waitlist                             |Display all books in the waitlist             |
|POST                          | .../purchase                            |Purchase a book                               |
|PUT                           |.../update_stock                         |Update stock after purchase                   |
|POST                          |../customerreview                        |Add Customer review                           |




## Git & GitHub Commands ##
**1. Checking the status**  
To check the status of the local repository, we use `git status`.  
This shows the status of the repository, what branch you are on, if commits have been made, and if there are any untracked files that have been added to the staging area.  
![1 Checking status](https://github.com/Deena-k1/Git.assignment/assets/153955602/f6dbb69c-04b7-452b-affe-5174813ea130)  
<br>
**2. Creating a branch**  
To create a new branch, we can either:  
* Use `git branch [branch name]` to create the branch, and then `git switch [branch name]` to switch to the branch  
* Use `git checkout -b [branch name]` to create a branch and immediately switch to it.  

![2 Creating a new branch](https://github.com/Deena-k1/Git.assignment/assets/153955602/84aed049-05cc-4398-acf2-7454ccb1b2ce)  
<br>
**3. Adding files to a branch**  
To add files to a branch, we use `git add`.  
![3 Adding files to a branch](https://github.com/Deena-k1/Git.assignment/assets/153955602/c21b1e54-a0ca-4711-a20a-4695c63ee7ba)  
<br>
**4. Adding commits with meaningful messages**  
To commit changes, also with a meaningful message, we use `git commit -m "[message about what changes you have made]"`.
![4 Adding commits with meaningful messages](https://github.com/Deena-k1/Git.assignment/assets/153955602/a25454a5-2937-40f7-9db8-13335d5898db)  
<br>
**5. Opening a pull request**  
To open a pull request, we use `git push origin [branch name]`. This will push the branch to the remote GitHub repository, and once on GitHub, you can make a pull request for said branch to be merged to the main branch.
![5 Opening a pull request](https://github.com/Deena-k1/Git.assignment/assets/153955602/a52edc2c-2d0d-412e-8d1f-d58e8720071f)  
<br>
**6. Merging and deploying to main branch**  
To merge and deploy to the main branch, this can be done by either:
* First going through a review stage, where someone other than the one who created the request can review the changes and approve before being able to click "merge pull request" and merge the branch to the main branch.
* If there are no conflicts and no reviewer, the option to click "merge pull request" and merge the branch to the main branch will automatically appear.

![6 Merging and deploying to main branch a](https://github.com/Deena-k1/Git.assignment/assets/153955602/a8d11d06-efb4-4978-bcfc-0c98d3e5e4df)
![6 Merging and deploying to main branch b](https://github.com/Deena-k1/Git.assignment/assets/153955602/63105ba1-953c-4d88-b6a7-aa40f7b4d82c)  
<br>
To view screenshots demonstrating the above and gathered from all group members, please refer to the ['screenshots'](https://github.com/Deena-k1/Git.assignment/tree/main/docs/screenshots) folder within the doc folder. 

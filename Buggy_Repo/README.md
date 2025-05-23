### Link to Github Repo
https://github.com/shreyash-lohare/Buggy_Repo


### Fixing the Buggy Code

- This code has 30 issues out of which 1 is no code in style.css . 
- The total marks for the entire codebase is 40, some issues have more marks than the other one. Style.css is of 5 marks. It will get scaled down to 20. All team members will get equal marks.
- You are suppose to work in teams of 4 or 5
- Each team member has to identify atleast 4 issues and fix atleast 4 issue. If someone doesn't do this, their marks get deducted.
- You are suppose to work on a git repository as collaborators

### What kind of bugs are there

- Bugs which will break your code
- Bugs might be a single word
- Bugs might be section of removed code
- Bugs might be section of unnecessary code
- Bugs might be useless files
- Bugs might be in the UI/UX of the pages
- Bugs might be in the api calls
- Bugs might be in the dependencies  

### submission format

- Make submissions on moodle
- Do not remove .git folder 
- Only 1 submission per team
- Submit it as Corrected_Code.zip

### Add the names of the members and roll numbers of your team below

- Shreyash Lohare : 2024111026
- Naman Singhal : 2024114013
- Shaurya Kochar: 2024114001
- Arpit Mahtele : 2024101112
- Shuban Biswas : 2024111017

### Table to keep track

| ID  | Issue Description                        | Identified By | Fixed By     |
|-----|------------------------------------------|---------------|--------------|
| 1   | Style.css is not filled                  |        Narain |  Whole Team  |
| 2   | items.html  (added container)            |        Shaurya|   Shaurya    |    
| 3   | In profile.html the script path is incorrect. The javascript files are in scripts directory not styles directory                                         |   Naman            |     Naman         |
| 4   | index.html changed doctype to standard   |      Arpit  |    Arpit   |         
| 5   | changed encoding to UTF-8                |       Shaurya |    Shaurya   |  
| 6   | Added links to analytics.html and news.html in quiz.html                                         |       Naman        |      Naman        |
| 7   | added navigation (analytics.html)        |      Shaurya  |     Shaurya  |      
| 8   | Add link to to quiz.html in news.html and profile.html                                    |  Naman             |     Naman         |
| 9   | Add link to to quiz.html in analytics.html,index.html,items.html     | Shaurya   |   Shaurya   |
| 10  | Changed localhost:8001 to 8000  (analytics.js)                                       |     Shaurya          |   Shaurya           |
| 11  | No check for empty datasets before plotting (analytics.py) | Shuban | Shuban |  
| 12  | Item class in models.py doesn't inherit from BaseModel                                         | Shreyash              |    Shreyash          |
| 13  | Missing users router import and include in main.py                                         |   Shreyash            |   Shreyash           |
| 14  |                                          |               |              |
| 15  | profile.js was trying to access userCount but profile.html has userCounts                                          |             Naman  |     Naman         |
| 16  |   In profile.js Delete Button was using Patch method instead of Delete method, fixed it and Base URL was missing in some path locations, added  that                                      |        Naman       |       Naman       |
| 17  |   In analytics.py, there's no route prefix in main.py causing inconsistent API paths                                       |   Shreyash            |  Shreyash            |
| 18  |  API calls in profile.js missing baseURL                                        |    Shreyash           | Shreyash             |
| 19  | corrected order of displaying path to each link on the webpage for all pages                                         |  Naman             |      Naman        |
| 20  |  Changed POST TO DELETE (items.js)                                        |      Shaurya         |      Shaurya       |
| 21  |       Items form has mismatched IDs between HTML and JS                                  |   Shreyash           | Shreyash          |
| 22  |                                          |               |              |
| 23  | No check for duplicate item names in create_item (items.py) | Shuban | Shuban |
| 24  | No error handling for missing 'name' or 'username' keys in analytics.py | Shuban | Shuban |
| 25  | No proper error response for invalid question ID in quiz.py | Shuban | Shuban |
| 26  | Does not check for duplicate user in create_user (users.py)    | Arpit | Arpit |
| 27  | quiz_collection not returned in init_db (db.py) | Shuban | Shuban |
| 28  | invalid object ID Handling |Arpit |      Arpit    |
| 29  |     Missing Response Models                                                 |     Arpit   |    Arpit  |
| 30  | Wrong type annotation on Item.name (models.py)  | Shuban | Shuban |

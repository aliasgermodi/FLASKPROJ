This is the task assigned by TAP, Kuwait

app.py has all the apis

To run the application,

install the necessary dependencies:

pip install requirement.txt

This script includes following APIs:

1. /api/plan/create : To create the plan
2. /api/plan/<path:plan_id>/update : To Update the Plan
3. /api/plan/list_all : list all the plans
4. /api/<path:user_id>/plan : Plan associated with user
5. /api/<path:user_id>/plan/feature1/limit : Features and limits associated to the user
6. /api/<path:user_id>/<path:plan_id>/feature1/limit/update : Update the features based on the user and plan
7. /api/user/create/<path:plan_id> : Create user and associate a plan to the user.
8. /api/user/list_all : list all the users
9. /remove/users : clear the user database
10. /remove/users: cleat plan database

all the above APIs are tested. the Data structure satisfies the requirements.

Video demo of the script: https://drive.google.com/file/d/1d3gFlaLlAuybGOXM5ES2bzxourZ0AMLM/view?usp=sharing


I hope I have successfully completed the task as expected.
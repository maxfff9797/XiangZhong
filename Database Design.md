# XiangZhong Database Design
##1.Total Design
The Database should include two part,one is the user account list,which include all user information,other one is the news-link list,which include every timeline of the news.
##2.User Account List Design
* UserID : 
 For user to Login,Create By the DataBase When the User Signup,it is premanent and unchangeble.(type:int)
* Password :
 User set when they signup,use for login,use digit mix word,lenght limit 8-16,can reset by email.(type:string)

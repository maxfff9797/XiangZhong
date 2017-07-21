# XiangZhong Database Design
## 1.Total Design
The Database should include two part,one is the user account list,which include all user information,other one is the news-link list,which include every timeline of the news.
## 2.User Account List Design
* UserID : 
 For user to Login,Create By the DataBase When the User Signup,it is premanent and unchangeble.(type:int)
* Password :
 User set when they signup,use for login,use digit mix word,lenght limit 8-16,can reset by email.(type:string)
* User Email : 
 Use for login and password reset (type:string)
* Username : 
 User's nackname(type:string)
* UserInfo : 
 User's self info(type:string)
* FollowList : 
 List of NewsID that User has Followed(type:list or string)
## 3.NewsFlow List
* NewsFlowID : 
 everynews has it ownid ,its a 32 lenght string,mix by digit and words
(type:string)
* NewsFlowTitle : 
 title of the newsflow object(type:string)
* NewsFlowList : 
 a list of News(include Newstitle and NewsURL)(type:byte)
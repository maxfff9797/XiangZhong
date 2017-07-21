# XiangZhong Database Design
## 1.Total Design
The Database should include two part,one is the user account list,which include all user information,other one is the news-link list,which include every timeline of the news.
## 2.User Account List Design
* UserID : <br />
 For user to Login,Create By the DataBase When the User Signup,it is premanent and unchangeble.(type:int)
* Password : <br />
 User set when they signup,use for login,use digit mix word,lenght limit 8-16,can reset by email.(type:string)
* User Email : <br />
 Use for login and password reset (type:string)
* Username : <br />
 User's nackname(type:string)
* UserInfo : <br />
 User's self info(type:string)
* FollowList : <br />
 List of NewsID that User has Followed(type:list or string)
## 3.NewsFlow List
* NewsFlowID : <br />
 everynews has it ownid ,its a 32 lenght string,mix by digit and words
(type:string)
* NewsFlowTitle : <br />
 title of the newsflow object(type:string)
* NewsFlowList : <br />
 a list of News(include Newstitle and NewsURL)(type:byte)
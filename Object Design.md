# XiangZhong Object Design
## 1.User Object
* UserID  
type:int  
create automuticaly
* Password  
type:string  
formet:digit+words  
lenght:8-16 char
* UserEmail  
type:string
* UserName  
type:string  
lenght:3-10
* UserInfo
type:string  
lenght:150
* FollowList
type:byte(NewsFlow Array)
## 2.NewsFlow Object
* NewsFlowID  
type:string  
lenght:16 char  
formet:digit+words
* NewsFlowTitle  
type:string
* NewsFlowList  
type:object(News Array)
## 3.News Object
* NewsTitle   
type:string
* NewsURL  
type:string

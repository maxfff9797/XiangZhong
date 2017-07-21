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
type:byte(Newslist Array)
## 2.NewsList Object
* NewsID  
type:string  
lenght:16 char  
formet:digit+words
* NewsName  
type:string
* NewsFlow  
type:object(News Array)


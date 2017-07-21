class User(object):
    'this is User Object'
    __UserID = 0
    __Password = ""
    __UserEmail = ""
    __UserName = ""
    __UserInfo = ""
    __FollowList
    def __init__(self, id, ue, un, ui, fl):
        self.__UserID = id
        self.__UserEmail = ue
        self.__UserName = un
        self.__UserInfo = ui
        self.__FollowList = fl
    def getUserID(self):
        return self.__UserID
    def checkPassword(self, pw):
        if pw == self.__Password:
            return True
        else:
            return False
    def getUserEmail(self):
        return self.__UserEmail
    def getUserName(self):
        return self.__UserName
    def getUserInfo(self):
        return self.__UserInfo
    def getFollowList(self):
        return self.__FollowList

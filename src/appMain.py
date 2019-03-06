from pprint import pprint

from mongoengine import *


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


def check_mongo():
    print("checking mongo state ....")
    con = connect("gmail-db")
    print("----------------")
    print(dir(con))
    print("----------------")
    pprint(dir(con))
    print("----------------")
    ross = User(email='ross@friends.com', first_name='Ross', last_name='Lawley').save()
    print("----------------")
    print(ross)
    chandler = User(email='chandler@friends.com')
    chandler.first_name = 'chandler'
    chandler.last_name = 'bing'
    chandler.save()
    print("----------------")
    print(chandler)


if __name__ == "__main__":
    print("begin journey")
    check_mongo()
    for user in User.objects:
        print(user.email)
    print("end journey")

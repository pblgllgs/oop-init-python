from user import User
from post import Post

user_one = User("user1.com", "user1", "123qwe", "dev")

user_two = User("user2.com", "user2", "123qwe", "devops")

user_one.get_user_info()
user_one.change_job_title("devops")
user_one.get_user_info()


post_one = Post("this is a first post", user_one.name)

post_two =  Post("this is a second post", user_two.name)

post_one.get_post_info()
post_two.get_post_info()
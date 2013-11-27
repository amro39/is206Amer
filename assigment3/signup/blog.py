import os
import re
import random
import hashlib
import hmac
from string import letters

import webapp2
import jinja2

from google.appengine.ext import db

### Delcalering template directory 
template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

secret = 'fart'

def render_str(template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

def make_secure_val(val): ### takes a value, and returns that value a pipe, and hmac of that value. Make sure its walid.
    return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

def check_secure_val(secure_val): #It takes one of the scures_vals and makes sure its walid.
    val = secure_val.split('|')[0]
    if secure_val == make_secure_val(val): #If it matches that string its then walid.
        return val #It makes 

#oppgave3
# Mainhandler is the blogghandler here. The parent class for all of the handlers
class BlogHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params): #Takes a template name and some dictionary basicly things that substitute into the template.
        params['user'] = self.user
        return render_str(template, **params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw)) #render calls write and render_str to print out a template

    def set_secure_cookie(self, name, val): ##Sets a coockie, 
        cookie_val = make_secure_val(val) #gets the secure val in a val, and stores taht in a coockie.
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val)) #We stroe cockie by using set coockie header.

    def read_secure_cookie(self, name): #Reading a secoure coockie, what you do is you give it a name findes that coockie and requst
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val) #If that coockie exsists, and that coockie passes check secure val. It returns coockie val. If one is false it returns false.

    def login(self, user): 
        self.set_secure_cookie('user_id', str(user.key().id()))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
### Chekc for the user coockie, if it exsists store it. Checks to see if the user is loged in or not.
    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id') #read the secoure coockie called user id
        self.user = uid and User.by_id(int(uid)) #If it is valid it sets self.user to that user.

def render_post(response, post):
    response.out.write('<b>' + post.subject + '</b><br>')
    response.out.write(post.content)

class MainPage(BlogHandler):
  def get(self):
      self.render('forside.html')


# bruker

def make_salt(length = 5):
    return ''.join(random.choice(letters) for x in xrange(length))
#Make a password hash.
def make_pw_hash(name, pw, salt = None): #Takes a username and a password and returns the hash version of the name password and salt.
    if not salt:
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (salt, h)
###How to verify passwords.
def valid_pw(name, password, h): ##makes sure that the hash from the database, matches the new hash based on what the user enterd in.
    salt = h.split(',')[0]
    return h == make_pw_hash(name, password, salt)

def users_key(group = 'default'): #Creats the ancester element in the database for all of mine users.
    return db.Key.from_path('users', group)
#User objects that will be storing in database. Inherates from DB model.
class User(db.Model):
    name = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

    @classmethod #You can call this method on this object.
    def by_id(cls, uid): #Refering to this class user. (CLS)
        return User.get_by_id(uid, parent = users_key()) #uid loads of the user out of the database

    @classmethod
    def by_name(cls, name): #Looks up a user by its name.
        u = User.all().filter('name =', name).get() #filter name, where name = name it selects from the user.
        return u
##Another method takes a name password and email and it creates a new user object.
    @classmethod 
    def register(cls, name, pw, email = None): #Creates a password hash for that name and password. And then it creates a user object.
        pw_hash = make_pw_hash(name, pw)
        return User(parent = users_key(),
                    name = name,
                    pw_hash = pw_hash,
                    email = email)

    @classmethod 
    def login(cls, name, pw):
        u = cls.by_name(name) 
        if u and valid_pw(name, pw, u.pw_hash): #if it exists, and if it is a valid password. It it is we go to our handler. "def login"
            return u


# blogg codes
### This function is for the datastore.
### this defines the blogs parent. The value of blogs parent.
def blog_key(name = 'default'):
    return db.Key.from_path('blogs', name) 


### This is define of the post class. It is basicly list of all the properties a blogg have
###


class Post(db.Model):
    subject = db.StringProperty(required = True) # you have to use a subject its requierd.
    content = db.TextProperty(required = True) #text for the body
    created = db.DateTimeProperty(auto_now_add = True) #this parameters says make this property the current time when you create an object so you will know when its created.
    last_modified = db.DateTimeProperty(auto_now = True) #everytime we update an object it says, everytime we updated an entry the google data store will keep it up to date

	
    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p = self) #when we write the blog this will actually do linebreaks so it looks nicer.

### This function looks up all the posts orded by creatin time.
###Blogfront is the handler for /blog
class BlogFront(BlogHandler):
    def get(self):
        posts = greetings = Post.all().order('-created') #This will make sure that it looks up all the posts orderd by creationtime.
        self.render('front.html', posts = posts) #This renders the front.html teplate with result of that querry


### The first thing you do here is to make a key. Use it from path function



class PostPage(BlogHandler):
    def get(self, post_id): ###If we go down to the button we will see how post ID function works. Becouse the urls handlers at the button are defined there.
        key = db.Key.from_path('Post', int(post_id), parent=blog_key()) #The parret is blogkey.
        post = db.get(key) #If there is a post it will get the post.

        if not post:
            self.error(404)### If there is no post here, it will return self.error(404)
            return 

        self.render("permalink.html", post = post) ###If there is post then it will returnt the permalink.html tempalte that is made.

class NewPost(BlogHandler): 
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            self.redirect('/blog')

        subject = self.request.get('subject') ##If we post to it, we verify the forms.
        content = self.request.get('content') ##We get the two parameters out of the request.. Its name of the form fields
###If there is enterd a good subject and content, we create a new post.
        if subject and content:
            p = Post(parent = blog_key(), subject = subject, content = content)
            p.put() #Stores the element in the database
            self.redirect('/blog/%s' % str(p.key().id())) #The user gets redirected of the element. This is how we get an objects ID in datastore.
        else:
            error = "Type inn subject and content" ### If we dont write it right, we get the message Type in subject and content.
            self.render("newpost.html", subject=subject, content=content, error=error)


## oppgave 2
## Here is the rot13 task.


class Rot13(BlogHandler):
    def get(self):
        self.render('rot13-form.html') #gets up rot13, and when it comes a post then it will drive the rot13 function on what is there.

    def post(self):
        rot13 = ''
        text = self.request.get('text')
        if text:
            rot13 = text.encode('rot13')

        self.render('rot13-form.html', text = rot13)

## The classes that we have written, get request, username password etc.

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{4,20}$") # a username is just a-z, 0 to 9 have to be between 4-20 characters
def valid_username(username):
    return username and USER_RE.match(username) #if the username matches this expression written over then its walid.

PASS_RE = re.compile(r"^.{4,20}$") #passwordlenght have to be between 4 and 20.
def valid_password(password): 
    return password and PASS_RE.match(password) #if it matches this expressions then return true

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$') #email have many charaters, so if it matches then true at the end.
def valid_email(email):
    return not email or EMAIL_RE.match(email)

	### Sigunp
	### First i made a signup.html where you can enter inn data like username,
	### password, and that you have to verify the password



class Signup(BlogHandler):
    def get(self):
        self.render("signup-form.html")

		#Here it uses the get request to get the username. 

    def post(self):
        have_error = False 
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')

        params = dict(username = self.username, #use this params to send back the username or emial if it is a bad form.
                      email = self.email)

        if not valid_username(self.username):
            params['error_username'] = "That is not a valid username." #If the username is not valid then there wil come an error message
            have_error = True

        if not valid_password(self.password):
            params['error_password'] = "That was not a valid password."
            have_error = True
        elif self.password != self.verify:
            params['error_verify'] = "Your passwords did not match."
            have_error = True #if the password is walid and its not equal the verify then we say password dont match.

        if not valid_email(self.email):
            params['error_email'] = "This is not a valid email."
            have_error = True

        if have_error:
            self.render('signup-form.html', **params)
        else:
            self.done()

    def done(self, *a, **kw):
        raise NotImplementedError

class Unit2Signup(Signup): #Redirect to the unit2 with the get parameter.
    def done(self):
        self.redirect('/unit2/welcome?username=' + self.username)

class Register(Signup): 
    def done(self):
        #make sure the user doesn't already exist, so if that user is registerd and you try to register with the same name you will gett this user already exsits.
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            self.render('signup-form.html', error_username = msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u) ##Sets the cookies, makes it that multiple handlers can use.
            self.redirect('/blog')

class Login(BlogHandler): 
    def get(self):
        self.render('login-form.html') #just a basic form with fields for username and password.

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u: #Here it returns the user if it is valid username and password combination. None if it is not.
            self.login(u)
            self.redirect('/blog')
        else:
            msg = 'Invalid login'
            self.render('login-form.html', error = msg) 

class Logout(BlogHandler):
    def get(self):
        self.logout()
        self.redirect('/blog')

class Unit3Welcome(BlogHandler):
    def get(self):
        if self.user: #gives access to the user, since it inherates from the blogghandler.
            self.render('welcome.html', username = self.user.name)
        else:
            self.redirect('/signup')

			
#When we handle the unit2/welcome we get to the handler welcome and if you sucescfully login it will say Welcome.
class Welcome(BlogHandler):
    def get(self):
        username = self.request.get('username')
        if valid_username(username):
            self.render('welcome.html', username = username)
        else:
            self.redirect('/unit2/signup')

# here we take care of the signup handler. You can see the users here.
#Example unit2/sigunp goes to the class signup, and unit2 welcome goes to the class welcome, etc.

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/unit2/rot13', Rot13),
                               ('/unit2/signup', Unit2Signup),
                               ('/unit2/welcome', Welcome),
                               ('/blog/?', BlogFront),
                               ('/blog/([0-9]+)', PostPage),
                               ('/blog/newpost', NewPost),
                               ('/signup', Register),#Register handler.
                               ('/login', Login),
                               ('/logout', Logout),
                               ('/unit3/welcome', Unit3Welcome),
                               ],
                              debug=True)


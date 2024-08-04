from flask import Flask, request, redirect
from articleFactory import genArticle
import time

app = Flask(__name__)

users = []

users.append({'username': 'admin', 'password': '1234'})

login_user = {}

footer = '''
<ul>
<li>e-mail | kawaii_san2@naver.com</li>
<li>vlog | https://velog.io/@nana</li>
<li>address | 경남 창원시 의창구 창원대학로 20 국립창원대학교</li>
</ul>
''' 

def home(lists, do_login):
     return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS 실습환경</title>
    <style>

        .container {{
            width: 1080px;
            overflow: hidden;
            margin: 0 auto;
            margin-bottom: 8px;}}
        
        .header {{ color: #fff; padding: 10px 0; text-align: center;
            background-color: #1D64AA
        }}
        
        .nav_sec_left {{
            float: left;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
        }}
       .nav_sec_right {{
            float: right;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
            text-align: right;
        }}
        main {{ padding: 10px; }}
        h2 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 10px; }}
        a {{ text-decoration: none; color: black; font-weight: bold ;}}
        a:hover {{ text-decoration: underline; }}
        #top {{ background: green; }}
        footer {{
            background-color: rgba(218, 218, 217, 0.578);
            padding : 2px 5px 2px 5px;
            font-size: 1em ; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>XSS 실습환경</h1>
        </div>
        <div class="nav_sec_left">
                <a href="/">홈</a> | 
                <a href="/new_post">새글 작성</a>
        </div>
        <div class="nav_sec_right">
                
        {do_login}
    
        </div>
    </div>
    <div class="container">
        <main>
            <h2>게시판</h2>
            <ul>
                {lists}
            </ul>
        </main>
    </div>
    <div class="container">
        <footer>{footer}</footer>
    </div>
</body>
</html>
'''

def post_html(do_login, title, author, date, content, button):
     return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS 실습환경</title>
    <style>

        .container {{
            width: 1080px;
            overflow: hidden;
            margin: 0 auto;
            margin-bottom: 8px;}}
        
        .header {{ color: #fff; padding: 10px 0; text-align: center;
            background-color: #1D64AA
        }}
        
        .nav_sec_left {{
            float: left;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
        }}
       .nav_sec_right {{
            float: right;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
            text-align: right;
        }}
        main {{ padding: 10px; }}
        h2 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 10px; }}
        a {{ text-decoration: none; color: black; font-weight: bold ;}}
        a:hover {{ text-decoration: underline; }}
        #top {{ background: green; }}
        footer {{
            background-color: rgba(218, 218, 217, 0.578);
            padding : 2px 5px 2px 5px;
            font-size: 1em ; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>XSS 실습환경</h1>
        </div>
        <div class="nav_sec_left">
                <a href="/">홈</a> | 
                <a href="/new_post">새글 작성</a>
        </div>
        <div class="nav_sec_right">
                
        {do_login}
    
        </div>
    </div>
    <div class="container">
        <main>
            <h2>{title}</h2>
            <p>By {author} ({date})</p>
            <p>{content}</p>
        </main>
        <div class="nav_sec_right">
            <button name="button" onclick="location.href='/'">홈으로</button>
            {button}
        </div>
    </div>
    <div class="container">
        <footer>{footer}</footer>
    </div>
</body>
</html>
'''

def new_post_html(user):
     return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS 실습환경</title>
    <style>

        .container {{
            width: 1080px;
            overflow: hidden;
            margin: 0 auto;
            margin-bottom: 8px;}}
        
        .header {{ color: #fff; padding: 10px 0; text-align: center;
            background-color: #1D64AA
        }}
        
        .nav_sec_left {{
            float: left;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
        }}
       .nav_sec_right {{
            float: right;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
            text-align: right;
        }}
        main {{ padding: 10px; }}
        h2 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 10px; }}
        a {{ text-decoration: none; color: black; font-weight: bold ;}}
        a:hover {{ text-decoration: underline; }}
        #top {{ background: green; }}
        footer {{
            background-color: rgba(218, 218, 217, 0.578);
            padding : 2px 5px 2px 5px;
            font-size: 1em ; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>창원대학교 블로그</h1>
        </div>
        <div class="nav_sec_left">
                <a href="/">홈</a> 
        </div>
        <div class="nav_sec_right">               
            <span>Welcome, {user}</span> |
            <a href="/logout">로그아웃</a>   
        </div>
    </div>
    <div class="container">
    <main>
        <h2>새글 작성</h2>
        <form action="/new_post" method="post">
            <p>제목 <input type="text" id="title" name="title" style="width: 1000px; height: 30px;"></p>
            <p>내용<textarea id="content" name="content" style="width: 1000px; height: 400px;"></textarea></p>
    </main>
    <div class="nav_sec_right">
        <button type="submit">작성</button>
        <button name="button" onclick="location.href='/'">취소</button>
    </div>
</form>
</div>
    </div>
    <div class="container">
        <footer>{footer}</footer>
    </div>
</body>
</html>
'''

def edit_post_html(user, post_id, title, content):
     return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS 실습환경</title>
    <style>

        .container {{
            width: 1080px;
            overflow: hidden;
            margin: 0 auto;
            margin-bottom: 8px;}}
        
        .header {{ color: #fff; padding: 10px 0; text-align: center;
            background-color: #1D64AA
        }}
        
        .nav_sec_left {{
            float: left;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
        }}
       .nav_sec_right {{
            float: right;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
            text-align: right;
        }}
        main {{ padding: 10px; }}
        h2 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 10px; }}
        a {{ text-decoration: none; color: black; font-weight: bold ;}}
        a:hover {{ text-decoration: underline; }}
        #top {{ background: green; }}
        footer {{
            background-color: rgba(218, 218, 217, 0.578);
            padding : 2px 5px 2px 5px;
            font-size: 1em ; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>XSS 실습환경</h1>
        </div>
        <div class="nav_sec_left">
                <a href="/">홈</a> 
        </div>
        <div class="nav_sec_right">               
            <span>Welcome, {user}</span> |
            <a href="/logout">로그아웃</a>   
        </div>
    </div>
    <div class="container">
    <main>
        <h2>글 수정</h2>
        <form action="/edit_post/{post_id}" method="post">
            <p>제목 <input type="text" id="title" name="title" value="{title}" style="width: 1000px; height: 30px;"></p>
            <p>내용<textarea id="content" name="content" style="width: 1000px; height: 400px;">{content}</textarea></p>
    </main>
    <div class="nav_sec_right">
        <button type="submit">수정</button>
        <button name="button" onclick="location.href='/post/{post_id}'">취소</button>
    </div>
</form>
</div>
    </div>
    <div class="container">
        <footer>{footer}</footer>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    articleTag = ''
    for item in genArticle():
         articleTag = articleTag + f'<li><a href="/post/{item["id"]}">{item["title"]}</a><p>{item["content"][:160]}...</p></li>'
    
    if len(login_user)==0 :
         do_login = '''<a href="/login">로그인</a> |
        <a href="/signup">회원가입</a>'''
         return home(articleTag, do_login)
    else :
         do_login = f'''<span>Welcome, {login_user["username"]}</span> |
         <a href="/logout">로그아웃</a>'''
         return home(articleTag, do_login)

@app.route('/post/<int:post_id>')
def post(post_id):
     for item in genArticle():
          if post_id == item["id"]:
               if len(login_user) !=0 :
                    button = ''
                    do_login = f'''<span>Welcome, {login_user["username"]}</span> |
          <a href="/logout">로그아웃</a>'''
                    if login_user["username"] == item["author"]:
                         button = f'''<button name="button" onclick="location.href='/edit_post/{post_id}'">글수정</button>
 <button name="button" onclick="location.href='/delete_post/{post_id}'">글삭제</button>'''
                         return post_html(do_login, item["title"], item["author"], item["date"], item["content"],button)
                    elif login_user["username"] == 'admin':
                        button = f'''<button name="button" onclick="location.href='/delete_post/{post_id}'">글삭제</button>'''
                        return post_html(do_login, item["title"], item["author"], item["date"], item["content"],button)
                    return post_html(do_login, item["title"], item["author"], item["date"], item["content"],button)
               else : 
                    button = ''
                    do_login = '''<a href="/login">로그인</a> |
         <a href="/signup">회원가입</a>'''
                    return post_html(do_login, item["title"], item["author"], item["date"], item["content"],button)
          
    

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS 실습환경</title>

<style>

        .container {{
            width: 1080px;
            overflow: hidden;
            margin: 0 auto;
            margin-bottom: 8px;}}
        
        .header {{ color: #fff; padding: 10px 0; text-align: center;
            background-color: #1D64AA
        }}
        
        .nav_sec_left {{
            float: left;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
        }}
       .nav_sec_right {{
            float: right;
            background: None;
            width: 540px;
            height: 50px; line-height: 50px;
            text-decoration: none; color: #090;
            text-align: right;
        }}
        main {{ padding: 10px; }}
        h2 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 10px; }}
        a {{ text-decoration: none; color: black; font-weight: bold ;}}
        a:hover {{ text-decoration: underline; }}
        #top {{ background: green; }}
        footer {{
            background-color: rgba(218, 218, 217, 0.578);
            padding : 2px 5px 2px 5px;
            font-size: 1em ; }}


.logincontainer {{

display: flex;
flex-direction: column;
align-items: center;
width: 1080px;
height: 560px;
margin-top: 60px;
margin-bottom: 60px;
border-radius: 10px;
}}

.member-container {{
display: flex;
flex-direction: column;
align-items: center;
width: 470px;
height: 818px;
margin-top: 72px;
margin-bottom: 70px;
}}

.loginheader {{
width: 466px;
height: 54px;
font-weight: 700;
font-size: 32px;
line-height: 47px;
color: #000000;
}}

.user-info {{
margin-top: 39px;
}}

.user-info div {{
margin-top: 21px;
}}

.user-info input {{
font-weight: 400;
font-size: 16px;
line-height: 24px;
color: #797979;
border: none;
border-bottom: 1px solid #cfcfcf;
width: 466px;
margin-top: 21px;
}}

.user-info-email input {{
border-bottom: 1px solid #0068ff;
}}

.btn {{
display: flex;
flex-direction: column;
margin-top: 60px;
width: 470px;
height: 106px;
}}

button {{
margin-top: 30px;
width: 470px;
height: 65px;
font-weight: 400;
font-size: 18px;
line-height: 27px;
text-align: center;
color: #0068ff;
background: #ffffff;
border: 1px solid #0068ff;
border-radius: 10px;
}}

    </style>
</head>

<body>
    <div class="container">
        <div class="header">
            <h1>XSS 실습환경</h1>
        </div>
        <div class="nav_sec_left">
                <a href="/">홈</a> | 
                <a href="/new_post">새글 작성</a>
        </div>
        <div class="nav_sec_right">
                
        </div>
    </div>

<div class="container">
<div class="logincontainer">
    <div class="member-container">
        <div class="loginheader">
            <div>회원가입</div>
        </div>
        <form action="/signup" method="post">
        <div class="user-info">
            <div class="user-info-email">
                <div>아이디</div>
                <input type="text" id="username" name="username" value="">
            </div>
            <div class="user-info-pw">
                <div>비밀번호</div>
                <input type="password" id="password" name="password" required>
            </div>
            <div class="user-info-pw">
                <div>비밀번호 재입력</div>
                <input type="password" id="password2" name="password2" required>
            </div>
        </div>
        <div class="btn">
            <button type="submit">회원가입</button>
        </div>
        </form>
    </div>
</div>
</div>

    <div class="container">
        <footer>{footer}</footer>
    </div>
</body>
</html>
'''
    else:
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']

        if password != password2:
             return redirect('/signup')
        elif password == password2:
             for item in users:
                  if username == item['username']:
                       return redirect('/signup')
             print(users)
             users.append({'username': username , 'password': password })
             print(users)
             return redirect('/login')



@app.route('/login', methods=['GET', 'POST'])
def login():
     if request.method == 'GET':
          return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>XSS 실습환경</title>
        <style>

            .container {{
                width: 1080px;
                overflow: hidden;
                margin: 0 auto;
                margin-bottom: 8px;}}
            
            .header {{ background-color: #1D64AA; color: #fff; padding: 10px 0; text-align: center; }}
            
            .nav_sec_left {{
                float: left;
                background: None;
                width: 540px;
                height: 50px; line-height: 50px;
                text-decoration: none; color: #090;
            }}
           .nav_sec_right {{
                float: right;
                background: None;
                width: 540px;
                height: 50px; line-height: 50px;
                text-decoration: none; color: #090;
                text-align: right;
            }}
            main {{ padding: 10px; }}
            h2 {{ color: #333; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ margin-bottom: 10px; }}
            
            a {{ text-decoration: none; color: black; font-weight: bold ;}}
            a:hover {{ text-decoration: underline; }}

            #top {{ background: green; }}
            footer {{
                background-color: rgba(218, 218, 217, 0.578);
                padding : 2px 5px 2px 5px;
                font-size: 1em ; }}

  

  .logincontainer {{
    
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 1080px;
    height: 560px;
    margin-top: 60px;
    margin-bottom: 60px;
    border-radius: 10px;
  }}

  .member-container {{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 470px;
    height: 818px;
    margin-top: 72px;
    margin-bottom: 70px;
  }}

  .loginheader {{
    width: 466px;
    height: 54px;
    font-weight: 700;
    font-size: 32px;
    line-height: 47px;
    color: #000000;
  }}

  .user-info {{
    margin-top: 39px;
  }}
  
  .user-info div {{
    margin-top: 21px;
  }}
  
  .user-info input {{
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
    color: #797979;
    border: none;
    border-bottom: 1px solid #cfcfcf;
    width: 466px;
    margin-top: 21px;
  }}
  
  .user-info-email input {{
    border-bottom: 1px solid #0068ff;
  }}

  .btn {{
    display: flex;
    flex-direction: column;
    margin-top: 60px;
    width: 470px;
    height: 106px;
  }}
  
  button {{
    margin-top: 30px;
    width: 470px;
    height: 65px;
    font-weight: 400;
    font-size: 18px;
    line-height: 27px;
    text-align: center;
    color: #0068ff;
    background: #ffffff;
    border: 1px solid #0068ff;
    border-radius: 10px;
  }}


        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>XSS 실습환경</h1>
            </div>
            <div class="nav_sec_left">
                    <a href="/">홈</a> | 
                    <a href="/new_post">새글 작성</a>
            </div>
            <div class="nav_sec_right">
                    
        <a href="/login">로그인</a> |
        <a href="/signup">회원가입</a>
    
            </div>
        </div>
        
<div class="container">
    <div class="logincontainer">
        <div class="member-container">
            <div class="loginheader">
                <div>로그인</div>
            </div>
            <form action="/login" method="post">
            <div class="user-info">
                <div class="user-info-email">
                    <div>* 아이디</div>
                    <input type="text" id="username" name="username" required>
                </div>
                <div class="user-info-pw">
                    <div>* 비밀번호</div>
                    <input type="password" id="password" name="password" required>
                </div>
            </div>
            <div class="btn">
                <button type="submit">로그인</button>
            </div>
            </form>
        </div>
    </div>
</div>

        <div class="container">
          <footer>{footer}</footer>
        </div>
    </body>
    </html>
    """
     
     else :
          username = request.form['username']
          password = request.form['password']

          for item in users :
               if (username == item['username'])and(password == item['password']):
                    login_user['username'] = username
                    login_user['password'] = password
                    return redirect('/')
               
          return redirect('/login_error')                      

@app.route('/logout')
def logout():
     login_user.clear()
     return redirect('/')

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
     if request.method == 'GET':
          if len(login_user) != 0 :
               return new_post_html(login_user['username'])
          else :
               return redirect('/login')
     else :
        print('sss')
        title = request.form['title']
        content = request.form['content']
        newArticle = {'id':len(genArticle())+1, 
                        'author':login_user["username"], 
                        'date': time.strftime("%Y-%m-%d"), 
                        'title': title, 'content' : content}
        genArticle().append(newArticle)
        print(genArticle())
        return redirect('/') 

@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
     if request.method == 'GET' :
        for item in genArticle():
            if post_id == item["id"]:
                 return edit_post_html(login_user['username'], post_id, item["title"], item["content"])
     
     else :
        title = request.form['title']
        content = request.form['content']
        for item in genArticle():
            if post_id == item["id"]:
                 item["title"] = title
                 item["content"] = content
                 item["date"] = time.strftime("%Y-%m-%d")+' 수정됨'
                 url = '/post/'+ str(post_id)
                 return redirect(url)


@app.route('/delete_post/<int:post_id>')
def delete_post(post_id):
     index = 0
     for item in genArticle():
            if post_id == item["id"]:
                 for item in genArticle():
                      if post_id > int(item["id"]) :
                           index+=1
                 del genArticle()[index]
                 return redirect('/')


@app.route('/login_error/')
def login_error():
     return f'''
<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>XSS 실습환경</title>
        <style>

            .container {{
                width: 1080px;
                overflow: hidden;
                margin: 0 auto;
                margin-bottom: 8px;}}
            
            .header {{ background-color: #1D64AA; color: #fff; padding: 10px 0; text-align: center; }}
            
            .nav_sec_left {{
                float: left;
                background: None;
                width: 540px;
                height: 50px; line-height: 50px;
                text-decoration: none; color: #090;
            }}
           .nav_sec_right {{
                float: right;
                background: None;
                width: 540px;
                height: 50px; line-height: 50px;
                text-decoration: none; color: #090;
                text-align: right;
            }}
            main {{ padding: 10px; }}
            h2 {{ color: #333; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ margin-bottom: 10px; }}
            
            a {{ text-decoration: none; color: black; font-weight: bold ;}}
            a:hover {{ text-decoration: underline; }}

            #top {{ background: green; }}
            footer {{
                background-color: rgba(218, 218, 217, 0.578);
                padding : 2px 5px 2px 5px;
                font-size: 1em ; }}
  
  .logincontainer {{
    
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 1080px;
    height: 560px;
    margin-top: 60px;
    margin-bottom: 60px;
    border-radius: 10px;
  }}
  
  .member-container {{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 470px;
    height: 818px;
    margin-top: 72px;
    margin-bottom: 70px;
  }}

  .loginheader {{
    width: 466px;
    height: 54px;
    font-weight: 700;
    font-size: 32px;
    line-height: 47px;
    color: #000000;
  }}

  .user-info {{
    margin-top: 39px;
  }}
  
  .user-info div {{
    margin-top: 21px;
  }}
  
  .user-info input {{
    font-weight: 400;
    font-size: 16px;
    line-height: 24px;
    color: #797979;
    border: none;
    border-bottom: 1px solid #cfcfcf;
    width: 466px;
    margin-top: 21px;
  }}
  
  .user-info-email input {{
    border-bottom: 1px solid #0068ff;
  }}

  .btn {{
    display: flex;
    flex-direction: column;
    margin-top: 60px;
    width: 470px;
    height: 106px;
  }}
  
  button {{
    margin-top: 30px;
    width: 470px;
    height: 65px;
    font-weight: 400;
    font-size: 18px;
    line-height: 27px;
    text-align: center;
    color: #0068ff;
    background: #ffffff;
    border: 1px solid #0068ff;
    border-radius: 10px;
  }}


        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>XSS 실습환경</h1>
            </div>
            <div class="nav_sec_left">
                    <a href="/">홈</a> | 
                    <a href="/new_post">새글 작성</a>
            </div>
            <div class="nav_sec_right">
                    
        <a href="/login">로그인</a> |
        <a href="/signup">회원가입</a>
    
            </div>
        </div>
        
<div class="container">
    <div class="logincontainer">
        <div class="member-container">
            <div class="loginheader">
                <div>로그인 오류</div>
            </div>
            
            <div class="user-info">
                <div class="user-info-email">
                    <div>아이디 또는 비밀번호를 다시 확인해 주세요</div>
                </div>
            </div>
            <div class="btn">
                <button onclick="location.href='/login'">로그인 페이지로 돌아가기</button>
            </div>
            
        </div>
    </div>
</div>

        <div class="container">
          <footer>{footer}</footer>
    </body>
    </html>
    
'''


if __name__ == '__main__':
    app.run(port=5000, debug=True)
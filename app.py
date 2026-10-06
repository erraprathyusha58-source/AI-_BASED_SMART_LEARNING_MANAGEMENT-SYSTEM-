from flask import Flask, request

app = Flask(__name__)

def recommend_courses(user_history, all_courses):
    recommended = []
    for course in all_courses:
        if "Python" in user_history[0] and "Python" in course:
            recommended.append(course)
    if len(recommended) < 3:
        for c in all_courses:
            if c not in recommended:
                recommended.append(c)
    return recommended[:3]

def ai_tutor_reply(question):
    q = question.lower()
    if "python" in q:
        return "Python is a simple and powerful language used for AI and Web Development."
    elif "lms" in q:
        return "LMS means Learning Management System."
    else:
        return f"Nice question! For '{question}', check your notes."

all_courses_list = ["Advanced Python", "Java Full Stack", "Data Science", "Machine Learning", "Web Development"]

@app.route('/')
def home():
    return """
    <html><body style="text-align:center; font-family:Arial; margin-top:100px;">
    <h1>Welcome to AI Based Smart Learning System</h1>
    <p>Your Personalized Learning Platform</p>
    <a href="/dashboard"><button style="padding:15px 30px; background:blue; color:white; border:none; font-size:18px;">Go to Dashboard</button></a>
    </body></html>
    """

@app.route('/dashboard')
def dashboard():
    user_history = ["Python basics"]
    suggested = recommend_courses(user_history, all_courses_list)
    html = f"""
    <html><body style="font-family:Arial; padding:20px;">
    <h1>Student Dashboard - SUCCESS!</h1>
    <h3>Recommended Courses (AI): {', '.join(suggested)}</h3>
    <h3>All Courses: {', '.join(all_courses_list)}</h3>
    <hr>
    <h3>Ask AI Tutor</h3>
    <form action="/ask_ai" method="POST">
    <input type="text" name="question" placeholder="what is python?" style="padding:10px; width:300px;">
    <button type="submit" style="padding:10px 20px;">Ask</button>
    </form>
    <br><a href="/">Back to Home</a>
    </body></html>
    """
    return html

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    question = request.form['question']
    answer = ai_tutor_reply(question)
    return f"<h3>Answer: {answer}</h3><a href='/dashboard'>Back to Dashboard</a>"

if __name__ == '__main__':
    app.run(debug=True)
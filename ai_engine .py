from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_courses(user_history, all_courses):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(user_history + all_courses)
    user_vec = vectors[:len(user_history)]
    course_vec = vectors[len(user_history):]
    similarity = cosine_similarity(user_vec, course_vec)
    scores = similarity.mean(axis=0)
    recommended_index = scores.argsort()[::-1][:3]
    return [all_courses[i] for i in recommended_index]

def ai_tutor_reply(question):
    q = question.lower()
    if "python" in q:
        return "Python is easy language for AI and Web Development."
    elif "lms" in q:
        return "LMS means Learning Management System, students can learn online."
    elif "java" in q:
        return "Java is used for Android apps and backend."
    else:
        return f"Your question '{question}' is good, please check your notes for more details."
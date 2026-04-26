from flask import Flask, render_template, request
from transformers import pipeline
from datetime import datetime, timedelta
import textwrap

app = Flask(__name__)

# Load Models
question_generator = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# **Home Page**
@app.route("/")
def home():
    return render_template("index.html")

# **Question Generator Page**
@app.route("/question-generator", methods=["GET", "POST"])
def generate_questions():
    if request.method == "GET":
        return render_template("question_generator.html")

    paragraph = request.form.get("paragraph", "").strip()

    if not paragraph:
        return render_template("question_generator.html", error="Please enter a paragraph.")

    chunks = textwrap.wrap(paragraph, width=300)
    all_questions = []

    for chunk in chunks:
        input_text = f"generate questions: {chunk}"
        questions = question_generator(input_text, max_length=50, num_return_sequences=5, num_beams=5)
        all_questions.extend(q["generated_text"] for q in questions)

    return render_template("question_generator_result.html", questions=all_questions)

# **Summarization Page**
@app.route("/summarizer", methods=["GET", "POST"])
def summarize_text():
    if request.method == "GET":
        return render_template("summarizer.html")

    user_text = request.form.get("user_text", "").strip()

    if not user_text:
        return render_template("summarizer.html", error="Please enter text to summarize.")

    # Limit text length
    if len(user_text.split()) > 500:
        user_text = " ".join(user_text.split()[:500])

    summary = summarizer(user_text, max_length=300, min_length=100, do_sample=False)[0]['summary_text']
    return render_template("summarizer_result.html", summary=summary)

# **Question Answering Page**
@app.route("/answer-question", methods=["GET", "POST"])
def answer_question():
    if request.method == "GET":
        return render_template("qa.html")

    context = request.form.get("context", "").strip()
    question = request.form.get("question", "").strip()

    if not context or not question:
        return render_template("qa.html", error="Please provide both context and question.")

    result = qa_pipeline(question=question, context=context)

    answer = result["answer"]
    score = result["score"]

    if score < 0.2:
        answer = "❌ This question is not related to the provided context."

    return render_template("qa_result.html", answer=answer, context=context)


# **Study Plan Generator Page**
def generate_study_plan(syllabus, topics, start_date, deadline):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(deadline, "%Y-%m-%d")

    topics_list = [t.strip() for t in topics.split(",")]
    total_days = (end - start).days + 1

    plan = f"📅 Study Plan from {start_date} to {deadline}\n\n"

    day = start
    topic_index = 0

    for i in range(total_days):
        plan += f"{day.strftime('%d %b %Y')}:\n"

        # Assign topic
        if topic_index < len(topics_list):
            topic = topics_list[topic_index]
            plan += f"📘 Topic: {topic}\n"
            topic_index += 1
        else:
            plan += "📘 Revision Day\n"

        # Add smart tasks
        plan += "⏱️ 2 hrs Concept Learning\n"
        plan += "📝 1 hr Practice Questions\n"
        plan += "🔁 30 min Revision of previous topics\n"

        # Add variation
        if i % 3 == 0:
            plan += "💡 Solve 5 extra problems\n"

        if i == total_days - 1:
            plan += "🎯 Full Mock Test + Final Revision\n"

        plan += "\n"
        day += timedelta(days=1)

    return plan

@app.route("/study-plan", methods=["GET", "POST"])
def study_plan():
    if request.method == "GET":
        return render_template("study_plan.html")

    syllabus = request.form.get("syllabus", "")
    topics = request.form.get("topics", "")
    start_date = request.form.get("start_date", "")
    deadline = request.form.get("deadline", "")

    if not syllabus or not topics or not start_date or not deadline:
        return render_template("study_plan.html", error="Please fill in all fields.")

    study_plan_text = generate_study_plan(syllabus, topics, start_date, deadline)
    return render_template("study_plan_result.html", study_plan=study_plan_text)

# **Run App**
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    resume_data = {
        "name": "HENA MAHATA",
        "profile_pic": "Hena_photo.jpg",  
        "contact": {
            "email": "henamahata@gmail.com",
            "mobile": "+91-6294014187",
            "linkedin": "https://www.linkedin.com/in/hena-mahata-55063a1a6/"
        },
        
        "objective": "Dynamic and adaptable technologist with expertise in Python programming and SQL-driven data management. Proven track record as a collaborative leader, recognized for driving complex projects to successful completion. Committed to continuous learning and delivering high-performance technical solutions that align with organizational objectives.",
        "education": [
            {"year": "2025", "degree": "B.TECH Electrical Engineering | MAKAUT", "inst": "B.P. Poddar Institute of Management & Technology", "score": "7.71 CGPA"},
            {"year": "2020", "degree": "Higher Secondary (12th) | CBSE", "inst": "Kendriya Vidyalaya CRPF, Dhurwa | Ranchi", "score": "73.33%"},
            {"year": "2018", "degree": "Secondary (10th) | CBSE", "inst": "Kendriya Vidyalaya No.1 Salt Lake | Kolkata", "score": "83.60%"}
        ],
        "skills": ["Python", "C", "SQL", "Machine Learning", "Verbal & Written Communication", "Leadership", "Time Management", "Adaptibility"],
        "trainings": [
            {"topic": "AI, Data Science, and Machine Learning using Python", "org": "Ardent Computech Pvt. Ltd.", "dur": "1 month"},
            {"topic": "Basic PLC and SCADA", "org": "MSME - TOOL ROOM (CTTC), Bonhooghly", "dur": "15 days"}
        ],
        "projects": [
            {
                "title": "IoT Based Portable Microscope",
                "tech": "Arduino IDE, ESP32, Machine Learning",
                "desc": "A compact, user-friendly device that offers high-quality magnification at an affordable price, enabling users to conduct medical diagnostics, educational experiments, and scientific observations with ease, even in remote locations."
            },
            {
                "title": "Gesture Recognition Glove",
                "tech": "Arduino IDE, ESP32",
                "desc": "A wearable, sensor-based gesture recognition device designed to assist communication for deaf and mute individuals. The system captures hand and finger movements through embedded sensors and processes them using a microcontroller to recognize predefined gestures. These gestures are then translated in real time into readable text or audible speech, enabling smoother interaction with people unfamiliar with sign language. The project focuses on accessibility, ease of use, and real-world applicability, demonstrating how embedded systems and basic machine learning can be used to create inclusive assistive technology.",
                "achievements": "Finalist of Smart India Hackathon 2023"
            }
        ],
        "responsibilities": [
            {"role": "Vice Chairperson", "org": "IET on-campus Student Chapter, BPPIMT", "date": "May 2024 - May 2025"},
            {"role": "Discipline & Hospitality Head", "org": "TECHSTORM'24", "date": "Jan 2024 - May 2024"},
            {"role": "Anchor", "org": "Young Engineers Award 2023 - IET Kolkata Local Network", "date": "Apr 2023"}
        ],
        "publication": {
            "title": "Comparative study on different glare for different window orientations in summer",
            "journal": "Luminescence 2023", "date": "May 2024",
            "url": "https://www.researchgate.net/publication/380466444_Luminescence_2023_Proceedings"
        },
        "languages": ["English (Fluent)", "Hindi (Fluent)", "Bengali (Fluent)"],
        "hobbies": ["Sports", "Painting", "Travelling"]
    }
    return render_template('index.html', data=resume_data)

if __name__ == '__main__':
    app.run(debug=True)
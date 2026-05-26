from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class BurnoutInput(BaseModel):
    sleep_duration: str
    work_hours: str
    stress_state: str
    energy_state: str
    screen_time: str     
    break_frequency: str
    mood_state: str

@app.get("/")
def home():
    return {"message": "Burnout Risk Analyzer Backend Running"}

@app.post("/analyze")
def analyze_burnout(data: BurnoutInput):

    score = 0

    # Sleep Duration
    if data.sleep_duration == "8+ hours":
        score += 0
    elif data.sleep_duration == "6-7 hours":
        score += 5
    elif data.sleep_duration == "4-5 hours":
        score += 10
    elif data.sleep_duration == "Less than 4 hours":
        score += 15
    elif data.sleep_duration == "Extremely sleep deprived":
        score += 20

    # Work Hours
    if data.work_hours == "0-3 hours":
        score += 0
    elif data.work_hours == "4-6 hours":
        score += 5
    elif data.work_hours == "7-9 hours":
        score += 10
    elif data.work_hours == "10+ hours":
        score += 15

    # Stress State
    if data.stress_state == "Calm and focused":
        score += 0
    elif data.stress_state == "Slightly pressured":
        score += 5
    elif data.stress_state == "Mentally fatigued":
        score += 10
    elif data.stress_state == "Highly stressed":
        score += 15
    elif data.stress_state == "Completely overwhelmed":
        score += 20

    # Energy State
    if data.energy_state == "Peak productivity":
        score += 0
    elif data.energy_state == "Stable energy":
        score += 5
    elif data.energy_state == "Slightly fatigued":
        score += 10
    elif data.energy_state == "Mentally drained":
        score += 15

    # Screen Time
    if data.screen_time == "Less than 2 hours":
        score += 0
    elif data.screen_time == "2-5 hours":
        score += 5
    elif data.screen_time == "6-8 hours":
        score += 10

    # Break Frequency
    if data.break_frequency == "Frequent breaks":
        score += 0
    elif data.break_frequency == "Occasional breaks":
        score += 5
    elif data.break_frequency == "Rarely take breaks":
        score += 10

    # Mood State
    if data.mood_state == "Calm":
        score += 0
    elif data.mood_state == "Neutral":
        score += 5
    elif data.mood_state == "Anxious":
        score += 10

    # Risk Level
    if score <= 25:
        risk_level = "Low Burnout Risk"
        productivity_state = "Peak Performance"

    elif score <= 50:
        risk_level = "Moderate Burnout Risk"
        productivity_state = "Stable Functioning"

    elif score <= 75:
        risk_level = "High Burnout Risk"
        productivity_state = "Fatigue Building"

    else:
        risk_level = "Critical Burnout Risk"
        productivity_state = "Recovery Needed"

    recommendations = []

    if score >= 50:
        recommendations.append("Take regular recovery breaks.")

    if data.sleep_duration in ["Less than 4 hours", "Extremely sleep deprived"]:
        recommendations.append("Improve sleep consistency and recovery duration.")

    if data.stress_state in ["Highly stressed", "Completely overwhelmed"]:
        recommendations.append("Reduce prolonged workload pressure where possible.")

    if data.break_frequency == "Rarely take breaks":
        recommendations.append("Introduce structured breaks during work sessions.")
    if len(recommendations) == 0:
        recommendations.append("Your current lifestyle indicators appear balanced. Maintain healthy routines.")

        
    return {
        "burnout_score": score,
        "risk_level": risk_level,
        "productivity_state": productivity_state,
        "recommendations": recommendations
    }    

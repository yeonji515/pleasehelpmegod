
import streamlit as st
import json

with open("teachers.json", "r", encoding="utf-8") as f:
    teachers = json.load(f)

with open("events.json", "r", encoding="utf-8") as f:
    events = json.load(f)

def search_by_class(user_input):
    for name, info in teachers.items():
        if info["class"] and info["class"] in user_input:
            return f"{info['class']} 담임선생님은 {name} 선생님입니다. (과목: {info['subject']}, 부서: {info['department']}, 교무실: {info['office']})"
    return None

def search_events(user_input):
    for event_name, event_date in events.items():
        if event_name in user_input:
            return f"🎉 {event_name}: {event_date}"
    return None

st.title("🏫 화성반월고 챗봇")
st.write("학교 생활에 필요한 정보를 알려드릴게요!")

user_input = st.text_input("무엇이 궁금한가요? (예: 선생님 이름, 과목, 부서, 담임학급, 행사명)")

if user_input:
    result = None

    result = search_by_class(user_input)

    if not result:
        result = search_events(user_input)

    if not result:
        for name, info in teachers.items():
            if name in user_input:
                result = f"{name} 선생님 — 과목: {info['subject']}, 부서: {info['department']}, 교무실: {info['office']}"
                if info["class"]:
                    result += f", 담임학급: {info['class']}"
                break

    if not result:
        subject_matches = []
        for name, info in teachers.items():
            if info["subject"] in user_input:
                entry = f"- {name} 선생님 (부서: {info['department']}, 교무실: {info['office']}"
                if info["class"]:
                    entry += f", 담임: {info['class']}"
                entry += ")"
                subject_matches.append(entry)
        if subject_matches:
            result = "📚 해당 과목 담당 선생님:\n" + "\n".join(subject_matches)

    if result:
        st.success(result)
    else:
        st.error("죄송합니다. 해당 정보를 찾을 수 없습니다.")

import streamlit as st
import requests
from streamlit_extras.let_it_rain import rain


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def get_useless_fact():
    # Make a request to the API
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=de")
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the fact from the response
        fact = response.json()["text"]
        return fact
    else:
        return "Error: API request was unsuccessful"


def main():
    rain(
    emoji="🤓",
    font_size=32,
    falling_speed=5,
    animation_length="infinite")

    # Welcome message
    st.header("Willkommen zu deinem Geburtstags-Quiz, Christian! 🎉")
    st.subheader("Beanworte alle Fragen richtig und erhalte dein exklusives Geburtstagsgeschenk! 🎁")

    # Set the questions and options
    questions = ["Wie wird eine Benjamin Blümchen Torte in der DrP/CTG üblicherweise serviert?", "Stelle dir vor, es sind 3 Jira Tickets offen. Die Aufgaben der Tickets sind wie folgt:\n\n1.Hinzufügen einer super nützlichen Funktion im PCC\n\n2.VBA Bug fix im Refresher\n\n3.TM1 Rule Anpassung im FixedAssets Cube.\n\nWie würde dein Kollege Sven die Aufgaben priorisieren? Wähle die richtige Reihenfolge:", "Wie viele Zeilen code hat der „Sys_Utilities“ Prozess im Prolog", "Wie viele Zeilen code hätte der „Sys_Utilities“ Prozess im Prolog ohne die UOM Conversion?", "Mit welchem Tastenkürzel kann man in Microsoft Excel in den Bearbeitungsmodus einer ausgewählten Zelle wechseln?"]
    options = [
    ["Die Oberseite der Torte zeigt nach oben", "Die Oberseite der Torte zeigt nach unten"],
    ["1. TM1, 2. VBA, 3. PCC", "1. PCC, 2. VBA, 3. TM1", "1. VBA, 2. PCC, 3. TM1"],
    ["rd. 100", "rd. 300", "rd. 500"],
    ["rd. -1%", "rd. -30%", "rd. -50%"],
    ["F2","Alt + F4", "Geht nicht. Man muss die Maus hierfür benutzen 🤓"],
    ]
    answers = ["Die Oberseite der Torte zeigt nach unten", "1. PCC, 2. VBA, 3. TM1", "rd. 500", "rd. -50%", "F2"]

    with st.form("quiz"):
        # Create the radio button widgets
        selected_answers = []
        for i in range(len(questions)): 
            answer = st.radio(questions[i], options[i])
            selected_answers.append(answer)
            st.write("---")

        # Check the answers
        correct_answers = 0
        for i in range(len(questions)):
            if selected_answers[i] == answers[i]:
                correct_answers += 1

        submitted = st.form_submit_button("Überprüfe mein Ergebnis")
        if submitted:
            if correct_answers == len(questions):
                st.success("Glückwunsch! Du hast alle Fragen richtig beantwortet.", icon="🏆")
                with st.expander("Hier ist dein Gewinn"):
                    st.write("Für deine erstklassige Leistung erhälst du einen useless fact! Dir noch einen schönen Geburtstag!")
                    st.write(get_useless_fact())
            else:
                st.error(f"Du hast {correct_answers} von {len(questions)} Fragen richtig beanwortet. Versuche es noch einmal!", icon="☹")

if __name__ == '__main__':
    st.set_page_config(page_title="Geburtstags-Quiz", page_icon="🎁")
    load_css_file("style.css")
    main()

import streamlit as st

st.set_page_config(page_title="Schistosomiasis Diagnosis", layout="centered")
st.title("🧠 Rule-Based AI: Schistosomiasis Checker")
st.write("Check the symptoms you’re experiencing:")

# Symptoms input
symptoms = {
    "Rash or itchy skin": st.checkbox("1. Rash or itchy skin"),
    "Fever": st.checkbox("2. Fever"),
    "Chills": st.checkbox("3. Chills"),
    "Cough": st.checkbox("4. Cough"),
    "Muscle aches": st.checkbox("5. Muscle aches"),
    "Anemia": st.checkbox("6. Anemia (lack of red blood cells)"),
    "Malnutrition": st.checkbox("7. Malnutrition (lack of nutrients)"),
    "Learning difficulties": st.checkbox("8. Learning difficulties"),
    "Abdominal pain": st.checkbox("9. Abdominal (stomach) pain"),
    "Larger liver": st.checkbox("10. Enlarged liver"),
    "Blood in stool or urine": st.checkbox("11. Blood in stool or urine"),
    "Problems urinating": st.checkbox("12. Problems urinating"),
    "Organ damage": st.checkbox("13. Damage to spleen, lungs, intestines, or bladder"),
    "Bladder issues": st.checkbox("14. Bladder fibrosis, cancer, or kidney damage"),
    "Neurological symptoms": st.checkbox("15. Seizures, paralysis, or spinal cord issues"),
}

# Rule-based logic
early_symptoms = ["Rash or itchy skin", "Fever", "Chills", "Cough", "Muscle aches"]
advanced_symptoms = [
    "Anemia", "Malnutrition", "Learning difficulties", "Abdominal pain",
    "Larger liver", "Blood in stool or urine", "Problems urinating",
    "Organ damage", "Bladder issues", "Neurological symptoms"
]

early_count = sum([symptoms[s] for s in early_symptoms])
advanced_count = sum([symptoms[s] for s in advanced_symptoms])

# Diagnosis
if early_count >= 3 and advanced_count >= 2:
    st.error("⚠️ High likelihood of Schistosomiasis. Please seek medical attention immediately.")
elif early_count >= 2:
    st.warning("⚠️ Possible early symptoms of Schistosomiasis. Consider medical screening.")
elif advanced_count >= 3:
    st.warning("⚠️ Advanced symptoms present. Please consult a healthcare provider.")
else:
    st.success("✅ Low risk based on provided symptoms. Stay healthy!")



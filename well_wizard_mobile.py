import streamlit as st
import datetime

# Simulated data (replace with API call to main app)
def fetch_prejob_data(user_role):
    # Example data structure
    return {
        "campaign": "2025 Q3 Well Intervention Campaign - Platform Bravo",
        "operation": "Wireline Swab Valve Replacement",
        "site": "Platform Bravo, North Sea",
        "date": datetime.date.today().strftime("%Y-%m-%d"),
        "safety": [
            "Mandatory PPE: Hard hat, gloves, eye protection, FR coveralls.",
            "Rig-specific: Emergency muster point is at Deck C.",
            "Operation-specific: Isolate well before tool deployment. Verify zero pressure."
        ],
        "role_brief": {
            "Supervisor": [
                "Confirm all permits are in place.",
                "Lead pre-job safety meeting.",
                "Ensure all crew complete pre-job checklist."
            ],
            "Operator": [
                "Inspect wireline tools before use.",
                "Verify lockout/tagout is complete.",
                "Participate in toolbox talk."
            ],
            "HSE": [
                "Monitor compliance with PPE.",
                "Audit pre-job safety checklist.",
                "Be present during critical lifts."
            ]
        },
        "questions": [
            "Have you reviewed the job safety analysis (JSA)?",
            "Do you understand your role and responsibilities?",
            "Are all required permits and isolations in place?",
            "Is emergency response equipment accessible?"
        ]
    }
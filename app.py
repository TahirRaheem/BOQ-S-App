import streamlit as st
import pandas as pd

# Define the activities
activities = [
    "Excavation",
    "PPC work",
    "Footing concrete",
    "Steel quantity in footing",
    "DDP work at plinth",
    "Plinth beam concrete",
    "Brick work in superstructure",
    "Concrete in beam and column",
    "Steel in beam and column",
    "Plaster work"
]

# Initialize a list to store the BOQ details and a variable to store the total cost
boq = []
total_amount = 0

# Create a sidebar for user input for each activity
st.sidebar.header('Bill of Quantities (BOQ) Input')

# Collect inputs for each activity
for activity in activities:
    st.sidebar.subheader(f"Enter details for {activity}:")
    quantity = st.sidebar.number_input(f"Quantity for {activity}", min_value=0.0, format="%.2f", key=f"quantity_{activity}")
    rate_per_unit = st.sidebar.number_input(f"Rate per unit for {activity}", min_value=0.0, format="%.2f", key=f"rate_{activity}")
    unit = st.sidebar.text_input(f"Unit for {activity} (e.g., cubic meter, kg)", key=f"unit_{activity}")

    if quantity and rate_per_unit:
        total_cost = quantity * rate_per_unit
        boq.append({
            "Activity": activity,
            "Quantity": quantity,
            "Rate per Unit": rate_per_unit,
            "Unit": unit,
            "Total Cost": total_cost
        })

# Display the BOQ table using pandas
if boq:
    st.header("Bill of Quantities (BOQ)")
    df = pd.DataFrame(boq)
    st.table(df)

    # Calculate total amount
    total_amount = df["Total Cost"].sum()
    st.subheader(f"Total Estimated Amount: {total_amount:.2f}")
else:
    st.write("Please enter the quantity and rate for each activity.")

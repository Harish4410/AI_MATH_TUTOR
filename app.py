import streamlit as st
from PIL import Image

from modules.graph_plotter import plot_equation
from modules.gemini_utils import image_to_equation
from modules.solver import solve_equation
from modules.mistake_check import detect_mistakes
from modules.explanation_ai import generate_steps
from modules.export_pdf import export_solution


# Page configuration
st.set_page_config(page_title="AI Math Tutor", page_icon="🧮", layout="wide")

st.title("🧮 AI Math Tutor")
st.write("An AI-powered algebra learning assistant")

# Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Solve Equation"]
)

@st.cache_data
def cached_explanation(eq):
    return generate_steps(eq)

# -------------------------------
# Solve Equation Page
# -------------------------------

if page == "Solve Equation":

    uploaded_file = st.file_uploader(
        "Upload an algebra equation image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Analyze Equation"):

            try:

                with st.spinner("AI analyzing equation..."):

                    equation = image_to_equation(image)

                st.session_state["equation"] = equation

                solution, steps = solve_equation(equation)

                st.session_state["solution"] = solution
                st.session_state["steps"] = steps

            except Exception as e:

                st.error("Could not solve the equation")
                st.write("Error:", e)

    if "equation" in st.session_state:

        equation = st.session_state["equation"]
        solution = st.session_state["solution"]
        steps = st.session_state["steps"]

        st.subheader("Recognized Equation")

        st.latex(equation)

        st.subheader("Solution Steps")

        for step in steps:
            st.write(step)

        st.success(f"Final Answer: x = {solution}")

        # Graph plotting
        st.subheader("Equation Graph")

        fig = plot_equation(equation)

        st.pyplot(fig)

        # AI explanation
        st.subheader("AI Step-by-Step Explanation")

        explanation = cached_explanation(equation)

        st.write(explanation)

        # Mistake detection
        st.subheader("Mistake Detection")

        mistakes = detect_mistakes(equation)

        for m in mistakes:
            st.warning(m)

        # Export PDF
        st.subheader("Export Solution")

        if st.button("Generate PDF"):

            file = export_solution(equation, solution, explanation)

            with open(file, "rb") as f:

                st.download_button(
                    label="Download PDF",
                    data=f,
                    file_name="solution.pdf",
                    mime="application/pdf"
                )



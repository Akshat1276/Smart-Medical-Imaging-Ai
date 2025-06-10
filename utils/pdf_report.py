from fpdf import FPDF
from datetime import datetime

DISEASE_INFO = {
    "covid19": {
        "name": "COVID-19",
        "symptoms": "Fever, cough, fatigue, loss of taste or smell, difficulty breathing.",
        "causes": "Caused by SARS-CoV-2 virus, spreads mainly through respiratory droplets.",
        "cure": "Supportive care, antiviral medications in some cases, vaccination helps prevent severe disease."
    },
    "pneumonia": {
        "name": "Pneumonia",
        "symptoms": "Cough, fever, chills, shortness of breath, chest pain.",
        "causes": "Infection by bacteria, viruses, or fungi.",
        "cure": "Antibiotics (for bacterial), antivirals/antifungals (if needed), supportive care."
    },
    "tuberculosis": {
        "name": "Tuberculosis",
        "symptoms": "Persistent cough, weight loss, night sweats, fever, coughing up blood.",
        "causes": "Caused by Mycobacterium tuberculosis, spreads through airborne droplets.",
        "cure": "Long-term antibiotics (usually 6+ months)."
    },
    "normal": {
        "name": "Normal",
        "symptoms": "No abnormal symptoms detected.",
        "causes": "N/A",
        "cure": "N/A"
    }
}

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 18)
        self.set_text_color(30, 30, 120)
        self.cell(0, 12, 'Medical X-RAY Report', ln=True, align='C')
        self.set_draw_color(30, 30, 120)
        self.set_line_width(1)
        self.line(10, 22, 200, 22)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf_report(patient_name, prediction, probabilities, disclaimer, output_path, xray_image_path=None, disease_details=None):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, f"Patient Name: {patient_name}", ln=True)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)
    pdf.ln(5)

    # Add X-ray image if provided
    if xray_image_path:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Uploaded X-ray:", ln=True)
        x_before = pdf.get_x()
        y_before = pdf.get_y()
        pdf.image(xray_image_path, x=x_before, y=y_before, w=100)
        pdf.set_y(y_before + 100)
        pdf.ln(5)

    # Prediction
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 102, 0)
    pdf.cell(0, 10, f"Prediction: {prediction}", ln=True)
    pdf.ln(5)

    # Disease Info Section
    if disease_details:
        pdf.set_font("Arial", "B", 12)
        pdf.set_text_color(0, 0, 128)
        pdf.cell(0, 10, f"Disease Information: {disease_details['name']}", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 8, f"Symptoms: {disease_details['symptoms']}")
        pdf.multi_cell(0, 8, f"Causes: {disease_details['causes']}")
        pdf.multi_cell(0, 8, f"Cure: {disease_details['cure']}")
        pdf.ln(5)

    # Probabilities Table (moved to the end)
    pdf.set_font("Arial", "B", 12)
    pdf.set_text_color(30, 30, 120)
    pdf.cell(0, 10, "Probabilities:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(220, 220, 220)
    pdf.cell(60, 10, "Class", 1, 0, 'C', True)
    pdf.cell(60, 10, "Probability", 1, 1, 'C', True)
    for cls, prob in probabilities.items():
        pdf.cell(60, 10, cls, 1, 0, 'C')
        pdf.cell(60, 10, f"{prob:.2%}", 1, 1, 'C')
    pdf.ln(10)

    # Disclaimer
    pdf.set_font("Arial", "I", 10)
    pdf.set_text_color(150, 0, 0)
    pdf.multi_cell(0, 10, disclaimer)
    pdf.output(output_path)
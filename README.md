# Smart Medical Imaging AI

## Overview
Smart Medical Imaging AI is an artificial intelligence system for analyzing medical images. The project provides tools for data preprocessing, model inference, explainability (Grad-CAM), PDF report generation, and an interactive assistant, all accessible via a Streamlit web application.

## Features
- **Medical Image Analysis:** Deep learning model for classifying medical images.
- **PDF Report Generation:** Automated creation of diagnostic reports.
- **Interactive Assistant:** AI-powered assistant for user queries.
- **Streamlit UI:** User-friendly web interface for uploading images and viewing results.

## Installation

Clone the repository and install dependencies:
```sh
pip install -r requirements.txt
```

## Usage

1. **Start the Application:**
   ```sh
   streamlit run src/app.py
   ```
2. **Upload Medical Images:** Use the web interface to upload images for analysis.
3. **View Results:** See predictions, Grad-CAM visualizations, and download PDF reports.

## Project Structure

```
src/
├── app.py                  # Main Streamlit application
├── assets/                 # Static assets (e.g., images)
├── assistant/
│   └── assistant.py        # Interactive assistant logic
├── model/
│   ├── gradcam.py
│   ├── model.h5            # Trained model weights
├── utils/
│   ├── pdf_report.py       # PDF report generation
│   ├── predict.py          # Model prediction logic
│   └── preprocess.py       # Image preprocessing
requirements.txt
.gitignore
README.md
```

## Dependencies

- streamlit
- tensorflow
- pillow
- numpy
- transformers
- fpdf

(See [requirements.txt](requirements.txt) for details.)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

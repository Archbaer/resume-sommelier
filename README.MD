# Resume Sommelier

An AI-powered CV analysis application built with Streamlit and OpenAI's GPT-4o-mini model. This tool evaluates resumes (CVs) uploaded as PDF files, providing scores, feedback, strengths, weaknesses, and improvement suggestions in Markdown format.

## Features

- **PDF Upload and Analysis**: Upload CVs in PDF format for instant analysis.
- **LLM-Powered Feedback**: Uses OpenAI's GPT-4o-mini to generate detailed reviews, including scores out of 10, reasoning, strengths, weaknesses, and suggestions.
- **Markdown Output**: Responses are formatted in Markdown for easy readability.
- **Non-CV Detection**: Automatically rejects non-CV documents with a clear message.
- **Docker Support**: Easily deployable using Docker and Docker Compose.
- **Session Management**: Handles file uploads and processing with Streamlit's session state.

## Prerequisites

- Python 3.11 or higher
- Docker (optional, for containerized deployment)
- OpenAI API Key (set in `.env` file)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/resume-sommelier.git
   cd resume-sommelier
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Running the Application

### Locally
1. Ensure your environment is activated and dependencies are installed.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open your browser to `http://localhost:8501`.

### With Docker
1. Build and run using Docker Compose:
   ```bash
   docker-compose up --build
   ```
2. Access the app at `http://localhost:8501`.

## Usage

1. Upload a CV in PDF format using the file uploader.
2. The app will process the file and display a loading spinner.
3. View the analysis results, including score, reasoning, strengths, weaknesses, and suggestions.
4. If a non-CV document is uploaded, the app will reject it with a message.

## Project Structure

- `app.py`: Main Streamlit application file.
- `analysis.py`: Contains the evaluation logic, Pydantic models, and LLM integration.
- `prototype.ipynb`: Jupyter notebook for prototyping and testing.
- `requirements.txt`: Python dependencies.
- `Dockerfile`: Docker image configuration.
- `docker-compose.yaml`: Docker Compose setup.
- `.gitignore`: Git ignore rules for sensitive files and cache.
- `.env`: Environment variables (not committed to Git).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI](https://openai.com/)
- PDF processing with [pdfplumber](https://github.com/jsvine/pdfplumber)
- Data validation with [Pydantic](https://pydantic-docs.helpmanual.io/)
# 🔎 RAG-based Job Search Application
A **Streamlit application** that helps job seekers find the most relevant openings from **Naukri** and **LinkedIn** based on their target job role and resume. The app uses **Retrieval-Augmented Generation (RAG)** and a **vector database** to retrieve the best-matching job listings.

---

## 🚀 **Features**
- 📝 **Upload Resume:** Upload PDF/Docx resume for parsing and embedding.
- 🎯 **Target Role:** Specify your desired job role for more accurate matching.
- 🔍 **Job Scraper:** Automatically scrapes and stores job postings from **Naukri** and **LinkedIn**.
- ⚙️ **Vector Database:** Stores job descriptions as embeddings for fast retrieval.
- 🤖 **RAG Retrieval:** Uses **LangChain** to find and display the most relevant job openings.
- 🛠️ **Interactive UI:** Displays job titles, companies, locations, and direct links.

---

## 🛠️ **Tech Stack**
- **Frontend:** Streamlit
- **Backend:** Python
- **Vector Database:** FAISS / Chroma
- **Embedding Model:** Azure OpenAI API
- **Scraper:** BeautifulSoup / Selenium
- **RAG Framework:** LangChain or LlamaIndex

---

## 🔧 **Installation & Setup**

1. **Clone the repository:**
```bash
git clone https://github.com/<your-username>/rag-job-search.git
cd rag-job-search
```

2. **Create and activate a virtual environment:**
```bash
python -m venv env
source env/bin/activate   # For Linux/Mac
env\Scripts\activate       # For Windows
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up Azure OpenAI API keys:**
- Create a `.env` file and add your **Azure OpenAI API** key:
```
AZURE_OPENAI_API_KEY=<your-api-key>
```

5. **Run the Streamlit app:**
```bash
streamlit run app.py
```

---

## 📊 **How It Works**
1. **Resume Parsing:**  
   - Extracts skills, experience, and education from uploaded resume.
   - Vectorizes resume content using **Azure OpenAI API** embeddings.

2. **Job Scraping:**  
   - Scrapes job listings from **Naukri** and **LinkedIn**.
   - Vectorizes job descriptions and stores them in **FAISS/Chroma**.

3. **RAG Retrieval:**  
   - Uses **LangChain** to retrieve the most relevant job openings.
   - Displays job details with links in the Streamlit app.

---

## 🔥 **Future Enhancements**
- ✅ Add job filtering options (location, experience, skills).
- 🔥 Migrate to Django for better scalability.
- 🔧 Add pagination and caching for faster performance.
- 📈 Integrate with external APIs for real-time job updates.

---

## 🛠️ **Contributing**
Feel free to submit issues or pull requests. Contributions are welcome!

---

## 📄 **License**
This project is licensed under the MIT License.

---

## 📫 **Contact**
For any queries or collaboration opportunities, feel free to reach out!  
📧 Email: [shuvayanpal2000@gmail.com]  
👨‍💻 GitHub: [your-github-profile](https://github.com/Shuvayan007)

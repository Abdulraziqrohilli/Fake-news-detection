# 📰 Fake News Detection using ML & Flask API


![Screenshot (144)](https://github.com/user-attachments/assets/d0a42f87-3a14-4f6e-94f1-b5106379d296)
![Screenshot (143)](https://github.com/user-attachments/assets/dbb25c42-a4e6-40c3-8452-8610fde147f5)


## 🚀 Overview

Fake news is a growing concern in today's digital world. This project utilizes **Machine Learning** to detect fake news and provides a **Flask API** for easy integration with user interfaces.

## 🔥 Features

- **98.7% accuracy** in detecting fake news
- **Machine Learning-based classification**
- **Flask API** for seamless UI integration
- **Real-time detection** for quick analysis

## 🛠️ Tech Stack

- **Flask** (for API development)
- **Machine Learning (NLP-based model)**
- **Scikit-learn & Pandas**
- **Jupyter Noteboo**Setup**k** (for model training and evaluation)

## 📌 Installation &&#x20;

### 1️⃣ Clone the Repository

```bash
 git clone https://github.com/yourusername/fake-news-detection-api.git
 cd fake-news-detection-api
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the API

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`

## 🔍 API Endpoints

### **1️⃣ Detect Fake News**

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Request Body:**

```json
{
    "text": "Breaking news: Scientists discover water on Mars!"
}
```

- **Response:**

```json
{
    "prediction": "Real"
}
```

## 📈 Model Accuracy

- The **machine learning model** achieved an **accuracy of 98.7%** on the test dataset.

## 💡 Future Enhancements

- Improve model generalization with more diverse datasets
- Deploy on cloud platforms like AWS/GCP
- Build a user-friendly web UI

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue or suggest improvements.

## 📜 License

This project is open-source and available under the **MIT License**.

---

Let's use AI to combat misinformation! 🚀

\#FakeNewsDetection #MachineLearning #Flask #API #AI #NLP


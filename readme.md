<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src=".\Image\Bert.webp" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# 🎓 Student Complaint Ticketing and Resolution System

<em>Graduation Project - Phase 1: AI Classification Module</em>

---

<em>Built with the tools and technologies:</em>  
**Python • Jupyter Notebook • Transformers (BERT) • PyTorch • Scikit-learn • Pandas • NumPy**

</div>
<br>

---

## 📖 Overview

This project aims to build a **centralized AI-powered ticketing system** to manage student complaints, route them to the appropriate department, and provide data-driven insights as outlined in the full project specification.

✅ **Current Progress**: We have completed the **AI classification module** using BERT-base-multilingual-uncased to classify student complaints into **four categories**:  
- Academic Support and Resources
- Financial Support  
- IT
- Student Affairs

**Model Performance**: 96% accuracy with F1-score of 0.96 on test data, supporting both Arabic and English text classification.

---

## ✨ Features

### Completed Features
- **AI-Based Complaint Classification**: Automatic categorization into 4 complaint types using multilingual BERT
- **Multilingual Support**: Handles both Arabic and English complaints
- **High Accuracy**: 96% classification accuracy on test dataset
- **Real-time Prediction**: Function to classify new complaints instantly

### Planned Features (Per Project Specification)
- **Complaint Submission & Tracking**: Student interface to log and track complaints
- **Automated Ticket Routing**: AI-based routing to the correct department  
- **Feedback Mechanism**: Students can provide feedback on complaint resolutions
- **Analytics & Reporting**: Insights on complaint trends and resolution performance
- **AI-Powered Recommendations**: Suggest resolutions based on historical data

---

## 📂 Project Structure

```sh
└── Student_Complaint_System/
    ├── arabicmodel.ipynb                                    # Complete classification model implementation
    ├── complaints.csv                                       # Training dataset (5,788 samples)
    ├── Student Complaint Ticketing and Resolution System.pdf # Full project specifications
    └── README.md                                           # Project documentation
```

### Project Index

<details open>
<summary><b><code>STUDENT_COMPLAINT_SYSTEM/</code></b></summary>
<details>
<summary><b>__root__</b></summary>
<blockquote>
<div class='directory-path' style='padding: 8px 0; color: #666;'>
<code><b>⦿ __root__</b></code>
</div>
<table style='width: 100%; border-collapse: collapse;'>
<thead>
<tr style='background-color: #f8f9fa;'>
<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
<th style='text-align: left; padding: 8px;'>Summary</th>
</tr>
</thead>
<tr style='border-bottom: 1px solid #eee;'>
<td style='padding: 8px;'><b><a href='arabicmodel.ipynb'>arabicmodel.ipynb</a></b></td>
<td style='padding: 8px;'>Complete BERT classification model with 96% accuracy for multilingual complaint categorization.</td>
</tr>
<tr style='border-bottom: 1px solid #eee;'>
<td style='padding: 8px;'><b><a href='complaints.csv'>complaints.csv</a></b></td>
<td style='padding: 8px;'>Training dataset with 5,788 complaint samples across 4 categories (generated for model training).</td>
</tr>
<tr style='border-bottom: 1px solid #eee;'>
<td style='padding: 8px;'><b><a href='Student Complaint Ticketing and Resolution System.pdf'>Project Specification</a></b></td>
<td style='padding: 8px;'>Complete project requirements and 8-week development timeline.</td>
</tr>
</table>
</blockquote>
</details>
</details>

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Programming Language:** Python 3.7+
- **Environment:** Jupyter Notebook  
- **Hardware:** CUDA-compatible GPU (recommended for training)

### Installation
Build the classification module from source and install dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone ../Student_Complaint_System
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd Student_Complaint_System
    ```

3. **Install the dependencies:**

    ```sh
    ❯ pip install torch transformers pandas numpy scikit-learn jupyter
    ```

### Usage

Run the classification model with:

    ```sh
    ❯ jupyter notebook arabicmodel.ipynb
    ```

**Example Usage:**
```python
# Arabic complaint classification
sentence = "المصاريف دي عامالني مشاكل كبيرة، والردود مش موجودة أبداً"
predicted_category, probabilities = predict_sentence(sentence, model, device)
# Output: "Financial Support"

# English complaint classification  
sentence = "I need help understanding the course material"
predicted_category, probabilities = predict_sentence(sentence, model, device)
# Output: "Academic Support"
```

---

## 📊 Model Performance

**Classification Results on Test Data:**
```
                                precision    recall  f1-score   support
Academic Support and Resources       0.95      0.93      0.94       148
Financial Support                    0.97      0.98      0.98       150
IT                                   0.94      0.98      0.96       135
Student Affairs                      0.99      0.96      0.97       147

accuracy                                               0.96       580
macro avg                            0.96      0.96      0.96       580
weighted avg                         0.96      0.96      0.96       580
```

**Training Details:**
- **Model:** BERT-base-multilingual-uncased
- **Dataset Size:** 5,788 complaints
- **Data Split:** 70% training, 20% validation, 10% testing
- **Training Time:** 4 epochs
- **Final Accuracy:** 96%

---

## 🛠️ Full System Roadmap

Based on the project specification, the complete system development follows this timeline:

### Phase 1: AI Classification (✅ COMPLETED)
- [x] **Week 4-5**: AI-Based Complaint Categorization
  - [x] BERT model training and evaluation
  - [x] Multilingual support implementation
  - [x] 96% accuracy achievement

### Phase 2: Core Development (Planned)
- [ ] **Week 1**: Project Planning & Requirements Gathering
- [ ] **Week 2**: Environment Setup & Initial Development
- [ ] **Week 3**: Core Complaint Management System

### Phase 3: Integration & Features (Planned)
- [ ] **Week 4**: Automated Ticket Routing & Notification
- [ ] **Week 6**: Feedback Mechanism & Resolution Module
- [ ] **Week 7**: Analytics Dashboard Development
- [ ] **Week 8**: Reporting & AI Refinement

### Planned System Architecture

**Frontend Development** (React/Angular/.NET):
- Student complaint submission interface
- Status tracking and notifications
- Feedback mechanism

**Backend Development** (SQL Database):
- Complaint management system
- User authentication and authorization  
- API integrations with institutional systems

**Additional AI Components**:
- Recommendation engine for solution suggestions
- Predictive analytics for resolution time
- Advanced NLP for complaint analysis

**Analytics Dashboard** (D3.js/Tableau):
- Performance metrics visualization
- Trend analysis and reporting
- Team performance monitoring

---

## 👥 Team Structure

As per project specification:

1. **Software Development Team:**
   - Frontend and backend development
   - API integrations
   - Complaint management and feedback features
   - Mobile application development

2. **Data Analytics Team:**
   - Analysis of complaint data
   - Creation of visual reports and performance dashboards
   - Monitoring and optimizing system analytics

3. **AI and Data Science Team:** ✅ 
   - [x] AI-driven complaint categorization (COMPLETED)
   - [ ] NLP for recommendation engine (Planned)
   - [ ] Predictive analytics for resolution suggestions (Planned)

---

## 🙌 Acknowledgments

- Project developed under supervision of **Eng. Baraa Abu Sallout**
- Following **DEPI Graduation Project guidelines**
- Classification model built using **HuggingFace Transformers** and **PyTorch**
- Training data prepared specifically for Arabic/English complaint classification

<div align="right">

[![][back-to-top]](#top)

</div>

[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square

---
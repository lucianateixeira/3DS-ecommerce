# Harnessing the Power of Data: Enhancing Ecommerce Security Through Analytics


## Introduction

The term "e-commerce" describes the process of buying, selling, or exchanging products, services, or information via computer. It has revolutionized business by providing unmatched accessibility, convenience, and global reach. The exponential growth in e-commerce, driven by mobile devices and internet access, is disrupting traditional retail paradigms. In response to security needs, credit card networks like Visa and Mastercard introduced Strong Customer Authentication (SCA) with the 3-D Secure (3DS) flow, adding identity verification steps.

While SCA enhances security, it often leads to cart abandonment, with nearly 30% of incomplete purchases attributed to 3DS friction. This highlights the need for solutions that balance security and user experience. By analyzing the vast data collected during online shopping, patterns can be identified to potentially replace additional authentication steps.

This research uses 3DS (authentication) data from TSYS Ltd. to develop a machine learning model for predicting transaction outcomes aiming to enhance security and consumer satisfaction.

---

## 🔎 Objectives

- Gain a comprehensive understanding of Strong Customer Authentication (SCA) and the 3-D Secure (3DS) flow, including their roles and impacts on e-commerce transactions.
- Learn to develop and implement machine learning algorithms, including neural networks, to predict the outcomes of e-commerce transactions.
- Explore techniques to improve the models.

---

## 📊 Dataset

The file is in CSV format and it consists of the following columns:

- **`AUTH_CDT`**: Date of the transaction
- **`MERCH_CAT_CD`**: Merchant category code
- **`TRAN_FRAUD`**: Fraudulent transaction
- **`ZIP_CD`**: Zip code
- **`ECI_IND`**: ECI code
- **`APPROVED_AMT`**: Approved amount
- **`DECLINE_RES1`**: Decline code
- **`AUTH_CD`**: Authorization code
- **`TSYS_PROD_CD`**: Internal identifier
- **`ADFLAG`**: Final result of the transaction after challenge is presented to the consumer — the 3DS flow.

---

## 📚 Libraries

- **Numpy**: Facilitates efficient numerical computations.
- **Pandas**: Offers a convenient interface for working with dataframes, simplifying various data operations.
- **Matplotlib**: Provides a framework for creating plots similar to MATLAB.
- **Seaborn**: A visualization library built on Matplotlib, offering a high-level interface for creating visually appealing statistical graphics.
- **Statsmodels**: Supplies functions and classes for performing statistical tests and building statistical models.
- **Sklearn**: A comprehensive library for data mining, data analysis, and machine learning in Python.
- **Plotly**: Used for creating interactive visualizations.
- **SciPy**: Used for scientific and technical computing. It builds on top of NumPy, offering more advanced mathematical functions, optimization routines, integration, and statistical methods.
- **Imbalanced-learn**: Used to handle imbalanced datasets, where one class heavily outweighs the other (e.g., fraud detection). It provides techniques like oversampling (e.g., SMOTE) and undersampling to balance the dataset.
- **TensorFlow**: Used for building and training complex machine learning models, including neural networks.

### Installation

In case you need to install these libraries, change the cell to Raw NBConvert and run the following command:

```bash
pip install numpy
pip install seaborn
pip install pandas
pip install matplotlib
pip install plotly
pip install scipy
pip install scikit-learn
pip install imbalanced-learn
pip install tensorflow








import csv
import re
import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Page configuration
st.set_page_config(
    page_title="Restaurant & Stock Management System",
    page_icon="🍽️",
    layout="wide",
)


# --- BACKEND LOGIC ---
def checkStock(ingredient):
    stock_df = pd.read_csv("proStock.csv")
    credited = stock_df[
        (stock_df["Item_Name"] == ingredient)
        & (stock_df["Transaction_Type"] == "credit")
    ]["Quantity"].sum()
    debited = stock_df[
        (stock_df["Item_Name"] == ingredient)
        & (stock_df["Transaction_Type"] == "debit")
    ]["Quantity"].sum()
    left = credited - debited
    return left


def orderstock(ingredient):
    updated = checkStock(ingredient) + 10
    with open("proStock.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ingredient, 10, "credit"])
    return updated


def dangerZone():
    stock_df = pd.read_csv("proStock.csv")
    for items in stock_df["Item_Name"].unique():
        if checkStock(items) < 10:
            return True, items
    return False, ""


def orderFood(orderedItem):
    if orderedItem == 1:
        if checkStock("Cooking Oil") > 5 and checkStock("Chicken Breast") > 2:
            with open("proStock.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(
                    [["Cooking Oil", 5, "debit"], ["Chicken Breast", 2, "debit"]]
                )
            return "ordered Successfully"
        else:
            return "out of stock"

    if orderedItem == 2:
        if (
            checkStock("Sauce") > 1
            and checkStock("Cheese") > 2
            and checkStock("Maida") > 3
        ):
            with open("proStock.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(
                    [
                        ["Sauce", 1, "debit"],
                        ["Maida", 3, "debit"],
                        ["Cheese", 2, "debit"],
                    ]
                )
            return "ordered Successfully"
        else:
            return "out of stock"

    if orderedItem == 3:
        if (
            checkStock("Tomatoes") > 1
            and checkStock("Noodles") > 5
            and checkStock("Onions") > 3
        ):
            with open("proStock.csv", "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(
                    [
                        ["Tomatoes", 1, "debit"],
                        ["Noodles", 5, "debit"],
                        ["Onions", 2, "debit"],
                    ]
                )
            return "ordered Successfully"
        else:
            return "out of stock"


def spendPrediction():
    customer_df = pd.read_csv("proCustom.csv")

    available_cols = customer_df.columns.tolist()
    possible_features = [
        "Preferred_Cuisine",
        "Favorite_Food_Item",
        "Visit_Frequency",
        "Preferred_Order_Type",
        "Loyalty_Member",
        "Satisfaction_Rating",
    ]
    features = [f for f in possible_features if f in available_cols]
    categorical_cols = [
        col
        for col in [
            "Preferred_Cuisine",
            "Favorite_Food_Item",
            "Visit_Frequency",
            "Preferred_Order_Type",
            "Loyalty_Member",
        ]
        if col in features
    ]

    target = "Avg_Spend_Per_Visit_USD"

    X_raw = customer_df[features]
    X = pd.get_dummies(X_raw, columns=categorical_cols, drop_first=True)
    y = customer_df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred


# --- STREAMLIT UI ---
st.title("🍽️ Restaurant Management & Analytics System")

st.sidebar.header("Navigation Portal")
user_role = st.sidebar.radio(
    "Select Portal Role:", ["1 for customer", "2 for staff"]
)

if user_role == "1 for customer":
    st.header("🍕 Customer Food Ordering Portal")
    st.write("Welcome! Please select an item from our menu to place your order:")

    menu_options = {
        1: "Butter Chicken & Naan",
        2: "Margherita Pizza",
        3: "Veg Hakka Noodles",
    }

    selected_item = st.selectbox(
        "Choose an item to order:",
        options=[1, 2, 3],
        format_func=lambda x: f"{x}. {menu_options[x]}",
    )

    if st.button("Place Order 🛒", use_container_width=True):
        result = orderFood(selected_item)
        if result == "ordered Successfully":
            st.success(
                f"🎉 Order placed successfully for **{menu_options[selected_item]}**!"
            )
            st.balloons()
        else:
            st.error(
                "⚠️ Sorry, this item is currently **Out of Stock** due to insufficient ingredients."
            )

elif user_role == "2 for staff":
    st.header("🔒 Staff & Inventory Portal")

    # FIX: Keeping st.number_input without type="password"
    pin_input = st.number_input("Enter Staff PIN:", value=0, step=1)

    if pin_input == 1234:
        st.success("✅ Access Granted to Staff Dashboard")

        staff_option = st.radio(
            "Select Action:",
            [
                "1 to check stock",
                "2 to order ingredients",
                "3 for predicting bill",
            ],
        )

        stock_df = pd.read_csv("proStock.csv")
        all_ingredients = list(stock_df["Item_Name"].unique())

        if staff_option == "1 to check stock":
            st.subheader("📦 Check Ingredient Stock")
            ing_name = st.selectbox(
                "Select or type ingredient name:", options=all_ingredients
            )

            if st.button("Check Stock Level"):
                current_qty = checkStock(ing_name)
                st.info(
                    f"Available stock for **{ing_name}**: **{current_qty} units**"
                )

                if current_qty < 10:
                    st.warning(
                        "⚠️ Warning: This item is in the **Danger Zone** (Stock < 10 units)!"
                    )

        elif staff_option == "2 to order ingredients":
            st.subheader("🛒 Order Ingredient Restock (+10 units)")
            ing_name = st.selectbox(
                "Select ingredient to restock:", options=all_ingredients
            )

            if st.button("Order Restock (+10)"):
                new_total = orderstock(ing_name)
                st.success(
                    f"✅ Stock Ordered Successfully for **{ing_name}**!"
                )
                st.info(f"Updated Stock Level: **{new_total} units**")

        elif staff_option == "3 for predicting bill":
            st.subheader(
                "📊 Customer Spend Prediction Model (Linear Regression)"
            )
            if st.button("Run Model & Predict Test Set Spend"):
                predictions = spendPrediction()
                st.write("### Predicted Customer Spend Values (Test Set):")
                st.dataframe(
                    pd.DataFrame({"Predicted Spend ($)": np.round(predictions, 2)}),
                    use_container_width=True,
                )

    elif pin_input != 0:
        st.error("❌ Wrong PIN. Try again.")
import streamlit as st
import mysql.connector


# Establish a connection to MySQL Server
def get_db_connection():
   mydb = mysql.connector.connect(
       host="localhost",
       user="root",
       password="123pass",
       database="storedata"
   )
   return mydb


# Streamlit App
def main():
   st.title("CRUD Operations with MySQL")


   # Display options for CRUD operations
   option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))


   # Database connection
   mydb = get_db_connection()
   mycursor = mydb.cursor()


   if option == "Create":
       st.subheader("Create a Record")
       id = st.text_input("Enter ID")
       store_code = st.text_input("Enter Store Code")
       total_sale = st.text_input("Enter Total Sale")
       transaction_date = st.text_input("Enter Transaction Date")
       if st.button("Create"):
           sql = "INSERT INTO sales (id, store_code, total_sale, transaction_date) VALUES (%s, %s, %s, %s)"
           val = (id, store_code, total_sale, transaction_date)
           mycursor.execute(sql, val)
           mydb.commit()
           st.success("Record Created Successfully!!!")


   elif option == "Read":
       st.subheader("Read Records")
       mycursor.execute("SELECT * FROM sales")
       result = mycursor.fetchall()
       for row in result:
           st.write(row)


   elif option == "Update":
       st.subheader("Update a Record")
       id = st.number_input("Enter ID to Update", min_value=1)
       store_code = st.text_input("Enter New Store Code")
       total_sale = st.text_input("Enter New Total Sale")
       transaction_date = st.text_input("Enter New Transaction Date")
       if st.button("Update"):
           sql = "UPDATE sales SET store_code=%s, total_sale=%s, transaction_date=%s WHERE id=%s"
           val = (store_code, total_sale, transaction_date, id)
           mycursor.execute(sql, val)
           mydb.commit()
           st.success("Record Updated Successfully!!!")


   elif option == "Delete":
       st.subheader("Delete a Record")
       id = st.number_input("Enter ID to Delete", min_value=1)
       if st.button("Delete"):
           sql = "DELETE FROM sales WHERE id=%s"
           val = (id,)
           mycursor.execute(sql, val)
           mydb.commit()
           st.success("Record Deleted Successfully!!!")


   # Close database connection
   mycursor.close()
   mydb.close()


if __name__ == "__main__":
   main()

import pandas as pd
from my_functions import *
import streamlit as st
from sqlalchemy import create_engine, text

schema = "liane_library"
host = "127.0.0.1"
user = "root"
password = "Vihan2014("
port = 3306

connection_string = f'mysql+pymysql://{user}:{password}@{host}:{port}/{schema}'



st.title(":blue[liane Library]")
st.write("📊 Library Dashboard")


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Books", books_count())

with col2:
    st.metric("👥 Friends", friends_count())

with col3:
    st.metric("⏰ Delayed", delayed_books_count())

st.divider()


tab1, tab2, tab3 = st.tabs(
    ["📚 Books", "👥 Friends", "🔄 Loans"]
)





with tab1:
    st.header(':blue[Delayed books]')
    st.dataframe(delayed_books())
    st.divider()






with tab1:
    st.subheader(":blue[Search Book]")

    title = st.text_input("Book Title")

    if title:
        st.dataframe(search_book(title))
    st.divider()


    st.subheader(":blue[Add Book]")

    new_title = st.text_input(
        "Book Title",
        key="add_book_title"
    )

    new_author = st.text_input(
        "Author",
        key="add_book_author"
    )

    new_genre = st.text_input(
        "Genre",
        key="add_book_genre"
    )

    new_year = st.number_input(
        "Published Year",
        min_value=0,
        key="add_book_year"
    )

    new_isbn = st.text_input(
        "ISBN",
        key="add_book_isbn"
    )


    if st.button("Add Book"):

        add_book(
            new_title,
            new_author,
            new_genre,
            new_year,
            new_isbn
        )

        st.success("Book added successfully.")
        st.divider()

    st.subheader(":blue[Delete Book]")

    book_title_delete = st.selectbox(
        "Book Title", 
         all_titles(),
        key="delete_book"
    )


    if st.button("Delete Book"):

        isbn = get_book_id(book_title_delete)

        if isbn is None:
            st.error("Book not found.")

        else:
            delete_book(isbn)
            st.success("Book deleted successfully.")    





with tab2:
    
        st.subheader(":blue[Add Friend]")

        new_friend_name = st.text_input(
        "Friend Name",
        key="new_friend_name"
        )

        new_friend_note = st.text_input(
        "Note",
        key="new_friend_note"
    )

        new_friend_max_loans = st.number_input(
        "Max Loans",
        min_value=1,
        value=3,
        key="new_friend_max_loans"
    )

        if st.button("Add Friend"):

            add_friend(
            new_friend_name,
            new_friend_note,
            new_friend_max_loans
        )

        st.success("Friend added successfully.")
        st.divider()

        st.subheader(":blue[Delete Friend]")

        friend_name_delete = st.selectbox(
        "Friend Name",
        all_friends(),
        key="delete_friend"
    )


        if st.button("Delete Friend"):

            friend_id = get_friend_id(friend_name_delete)

            if friend_id is None:
                st.error("Friend not found.")

            else:
                delete_friend(friend_id)
                st.success("Friend deleted successfully.")






with tab3:
    st.subheader(":blue[Update Loan Status]")

    status = st.selectbox(
        "Loan Status",
        [
            "loaned",
            "returned",
            "delayed",
            "missing"
        ],
        key="loan_states_select"
    )

    friend_name = st.selectbox(
        "Friend Name",
        all_friends(),
        key="friend_name_status"
    )

    book_title = st.selectbox(
        "Book Title",
        all_titles(),
        key="book_title_status"
    )

    if st.button(
        "Update Loan Status",
        key="update_loan_states_button"
    ):
        friend_id = get_friend_id(friend_name)
        book_id = get_book_id(book_title)

        if friend_id is None:
            st.error("Friend not found.")

        elif book_id is None:
            st.error("Book not found.")

        else:
            update_result = update_loan_states(
                friend_id,
                book_id,
                status
            )

            if update_result == "updated":
                st.success("Loan status updated successfully.")

            elif update_result == "not_found":
                st.error(
                    f'"{book_title}" was not borrowed by {friend_name}.'
                )

            elif update_result == "unchanged":
                st.warning(
                    f'The loan already has the status "{status}".'
                )

    st.divider()







with tab3:

    st.subheader(":blue[Update Due Date]")

    due_date = st.date_input(
        'Due Date',
        key="due_date_update"
    )

    ###friend_name_due = st.text_input(
        ###"Friend Name",
        ###key="friend_name_due"
    ###)
    friend_name = st.selectbox("Friend Name", all_friends(), key="friend_name_due")

    ###book_title_due = st.text_input(
       ### "Book Title",
       ### key="book_title_due"
    ###)
    book_title = st.selectbox('book Title', all_titles(), key="book_title_due")
    


    if st.button("Update Due Date"):

        friend_id = get_friend_id(friend_name)
        book_id = get_book_id(book_title)

        if friend_id is None:
            st.error("Friend not found.")

        elif book_id is None:
            st.error("Book not found.")

        else:
            result = update_due_date(
        friend_id,
        book_id,
        due_date
        )

        if result == "updated":
            st.success("Due date updated successfully.")

        elif result == "unchanged":
            st.info("This due date is already set.")

        elif result == "not_found":
            st.error("This friend has not borrowed this book.")

        else:
            st.error("Something went wrong.")

    st.divider()




with tab3:

    st.subheader(":blue[Update Loan Note]")

    loan_note = st.text_area("Loan Note")


    friend_name_note = st.selectbox(
        "Friend Name",
        all_friends(),
        key="friend_note"
    )


    book_title_note = st.selectbox(
        "Book Title",
        all_titles(),
        key="book_note"
    )


    if st.button("Update Loan Note"):

        friend_id = get_friend_id(friend_name_note)
        book_id = get_book_id(book_title_note)

        if friend_id is None:
            st.error("Friend not found.")

        elif book_id is None:
            st.error("Book not found.")

        else:
            result = update_loan_note(
        friend_id,
        book_id,
        loan_note
            )

            if result == "updated":
                st.success("Loan note updated successfully.")

            elif result == "unchanged":
                st.info("This note is already saved.")

            elif result == "not_found":
                st.error("This friend has not borrowed this book.")

            else:
                st.error("Something went wrong.")

    st.divider()
    






with tab3:
    st.subheader(":blue[Create Loan]")

    loan_date = st.date_input(
        "Loan Date",
        key="create_loan_date"
    )

    create_due_date = st.date_input(
        "Due Date",
        key="create_due_date"
    )

    friend_name_create = st.text_input(
        "Friend Name",
        key="create_friend"
    )

    book_title_create = st.text_input(
        "Book Title",
        key="create_book"
    )

    if st.button(
        "Create Loan",
        key="create_loan_button"
    ):

        friend_id = get_friend_id(friend_name_create)
        book_id = get_book_id(book_title_create)

        result = create_loan(
            friend_id,
            book_id,
            loan_date,
            create_due_date
        )

        if result == "created":
            st.success("Loan created successfully.")

        elif result == "already_exists":
            st.warning("This loan already exists.")

        else:
         st.error("Something went wrong.")

    st.divider()







with tab3:
    
    st.subheader(":blue[Delete Loan]")

    friend_name_delete = st.selectbox(
        "Friend Name",
        all_friends(),
        key="delete_loan_friend"
    )

    book_title_delete = st.selectbox(
        "Book Title",
        all_titles(),
        key="delete_loan_book"
    )

    if st.button(
        "Delete Loan",
        key="delete_loan_button"
    ):

        friend_id = get_friend_id(friend_name_delete)
        book_id = get_book_id(book_title_delete)

        result = delete_loan(
            friend_id,
            book_id
        )

        if result == "deleted":
            st.success("Loan deleted successfully.")

        elif result == "not_found":
            st.error("This loan does not exist.")

        else:
            st.error("Something went wrong.")

import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

schema = "liane_library"
host = "127.0.0.1"
user = "root"
password = "password"
port = 3306

connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema}"





def delayed_books_count():
    df = pd.read_sql("""
        SELECT COUNT(*) AS delayed_count
        FROM loans
        WHERE loan_states = 'delayed'
    """, con=connection_string)

    return df.iloc[0]["delayed_count"]






def books_count():
    df = pd.read_sql("""
        SELECT COUNT(*) AS books_count
        FROM books
    """, con=connection_string)

    return df.iloc[0]["books_count"]





def friends_count():
    df = pd.read_sql("""
        SELECT COUNT(*) AS friends_count
        FROM friends
    """, con=connection_string)

    return df.iloc[0]["friends_count"]




def delayed_books():
    df = pd.read_sql('''select books.title, friends.friend_name, loans.book_id, loans.due_date from books
                join loans 
                ON books.isbn = loans.book_id
                join friends
                ON loans.friend_id = friends.friend_id
                where loans.loan_states = "delayed"''', con = connection_string)
    return df





def search_book(title):
    df = pd.read_sql(f"""
        SELECT title, author, genre, published_year, isbn
        FROM books
        WHERE title LIKE '%%{title}%%'
    """, con=connection_string)
    

    return df




def get_book_id(book_title):
    query = """
        SELECT isbn
        FROM books
        WHERE title = %(title)s
    """

    df = pd.read_sql(
        query,
        con=connection_string,
        params={"title": book_title}
    )

    if df.empty:
        return None

    return df.iloc[0]["isbn"]




def all_titles():
    books_title_list = pd.read_sql( """
        SELECT title
        FROM books
    """, con=connection_string)["title"]
    return books_title_list




def add_book(title, author, genre, published_year, isbn):
    engine = create_engine(connection_string)

    query = f"""
        INSERT INTO books (title, author, genre, published_year, isbn)
        VALUES ('{title}', '{author}', '{genre}', {published_year}, '{isbn}');
    """

    with engine.connect() as connection:
        transaction = connection.begin()

        try:
            connection.execute(text(query))
            transaction.commit()

        except:
            transaction.rollback()
            raise






def delete_book(isbn):
    engine = create_engine(connection_string)

    with engine.connect() as connection:
        transaction = connection.begin()

        try:
            # اول loan های مربوط به این کتاب حذف شوند
            connection.execute(
                text(f"DELETE FROM loans WHERE book_id = '{isbn}'")
            )

            # بعد خود کتاب حذف شود
            connection.execute(
                text(f"DELETE FROM books WHERE isbn = '{isbn}'")
            )

            transaction.commit()

        except:
            transaction.rollback()
            raise        




def get_friend_id(friend_name):
    query = """
        SELECT friend_id
        FROM friends
        WHERE friend_name = %(name)s
    """

    df = pd.read_sql(
        query,
        con=connection_string,
        params={"name": friend_name}
    )

    if df.empty:
        return None

    return df.iloc[0]["friend_id"]




def all_friends():
    friends_list = pd.read_sql("""
        SELECT friend_name
        FROM friends
    """, con=connection_string)["friend_name"]

    return friends_list



def add_friend(friend_name, notes, max_loans):
    engine = create_engine(connection_string)

    query = f"""
        INSERT INTO friends (friend_name, notes, max_loans)
        VALUES ('{friend_name}', '{notes}', {max_loans});
    """

    with engine.connect() as connection:
        transaction = connection.begin()
        try:
            connection.execute(text(query))
            transaction.commit()
        except:
            transaction.rollback()
            raise





def delete_friend(friend_id):
    engine = create_engine(connection_string)

    with engine.connect() as connection:
        transaction = connection.begin()

        try:
            connection.execute(
                text(f"DELETE FROM loans WHERE friend_id = {friend_id}")
            )

            connection.execute(
                text(f"DELETE FROM friends WHERE friend_id = {friend_id}")
            )

            transaction.commit()

        except:
            transaction.rollback()
            raise    



def update_loan_states(friend_id, book_id, status):
    engine = create_engine(connection_string)

    check_query = text("""
        SELECT loan_states
        FROM loans
        WHERE friend_id = :friend_id
          AND book_id = :book_id
        LIMIT 1
    """)

    update_query = text("""
        UPDATE loans
        SET loan_states = :status
        WHERE friend_id = :friend_id
          AND book_id = :book_id
    """)

    try:
        with engine.begin() as connection:

            # Prüfen, ob dieses Buch tatsächlich diesem Freund zugeordnet ist
            existing_loan = connection.execute(
                check_query,
                {
                    "friend_id": friend_id,
                    "book_id": book_id
                }
            ).mappings().first()

            if existing_loan is None:
                return "not_found"

            current_status = existing_loan["loan_states"]

            # Kein unnötiges Update, wenn der Status bereits gleich ist
            if current_status == status:
                return "unchanged"

            result = connection.execute(
                update_query,
                {
                    "status": status,
                    "friend_id": friend_id,
                    "book_id": book_id
                }
            )

            if result.rowcount > 0:
                return "updated"

            return "not_found"

    except Exception as error:
        st.error(f"Database error: {error}")
        return "error"








def update_due_date(friend_id, book_id, due_date):
    engine = create_engine(connection_string)

    check_query = text("""
        SELECT due_date
        FROM loans
        WHERE friend_id = :friend_id
          AND book_id = :book_id
        LIMIT 1
    """)

    update_query = text("""
        UPDATE loans
        SET due_date = :due_date
        WHERE friend_id = :friend_id
          AND book_id = :book_id
    """)

    try:
        with engine.begin() as connection:

            # Check whether this loan exists
            existing_loan = connection.execute(
                check_query,
                {
                    "friend_id": friend_id,
                    "book_id": book_id
                }
            ).mappings().first()

            if existing_loan is None:
                return "not_found"

            current_due_date = existing_loan["due_date"]

            # No update if the date is already the same
            if current_due_date == due_date:
                return "unchanged"

            result = connection.execute(
                update_query,
                {
                    "due_date": due_date,
                    "friend_id": friend_id,
                    "book_id": book_id
                }
            )

            if result.rowcount > 0:
                return "updated"

            return "not_found"

    except Exception as error:
        st.error(f"Database error: {error}")
        return "error"

def update_loan_note(friend_id, book_id, note):
    engine = create_engine(connection_string)

    check_query = text("""
        SELECT note
        FROM loans
        WHERE friend_id = :friend_id
          AND book_id = :book_id
        LIMIT 1
    """)

    update_query = text("""
        UPDATE loans
        SET note = :note
        WHERE friend_id = :friend_id
          AND book_id = :book_id
    """)

    try:
        with engine.begin() as connection:

            existing_loan = connection.execute(
                check_query,
                {
                    "friend_id": friend_id,
                    "book_id": book_id
                }
            ).mappings().first()

            if existing_loan is None:
                return "not_found"

            current_note = existing_loan["note"]

            if current_note == note:
                return "unchanged"

            result = connection.execute(
                update_query,
                {
                    "note": note,
                    "friend_id": friend_id,
                    "book_id": book_id
                }
            )

            if result.rowcount > 0:
                return "updated"

            return "not_found"

    except Exception as error:
        st.error(f"Database error: {error}")
        return "error"





def create_loan(friend_id, book_id, loan_date, due_date):
    engine = create_engine(connection_string)

    check_query = text("""
        SELECT *
        FROM loans
        WHERE friend_id = :friend_id
          AND book_id = :book_id
        LIMIT 1
    """)

    insert_query = text("""
        INSERT INTO loans
        (
            friend_id,
            book_id,
            loan_date,
            due_date,
            loan_states
        )
        VALUES
        (
            :friend_id,
            :book_id,
            :loan_date,
            :due_date,
            'loaned'
        )
    """)

    try:
        with engine.begin() as connection:

            existing = connection.execute(
                check_query,
                {
                    "friend_id": friend_id,
                    "book_id": book_id
                }
            ).mappings().first()

            if existing is not None:
                return "already_exists"

            connection.execute(
                insert_query,
                {
                    "friend_id": friend_id,
                    "book_id": book_id,
                    "loan_date": loan_date,
                    "due_date": due_date
                }
            )

            return "created"

    except Exception as error:
        st.error(f"Database error: {error}")
        return "error"




def delete_loan(friend_id, book_id):
    engine = create_engine(connection_string)

    delete_query = text("""
        DELETE FROM loans
        WHERE friend_id = :friend_id
          AND book_id = :book_id
    """)

    try:
        with engine.begin() as connection:

            result = connection.execute(
                delete_query,
                {
                    "friend_id": friend_id,
                    "book_id": book_id
                }
            )

            if result.rowcount > 0:
                return "deleted"

            return "not_found"

    except Exception as error:
        st.error(f"Database error: {error}")
        return "error"





import sqlite3

DB_PATH = './todo.db'

conn = sqlite3.connect(DB_PATH)

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS todo 
            (
                number INT,
                task TEXT,
                deadline DATE,
                state TEXT
            )''')

# c.execute('INSERT INTO todo VALUES (?, ?, ?)', ('study', '2020-06-23', 'not started'))
# def add_task(task):

def main():
    num = 1
    while True:
        print('1) Display list\n2) Add task\n3) Delete task\n4) Exit')
        option = int(input('> '))
        order = 1
        if option == 1:
            if len(c.execute('SELECT * FROM todo ORDER BY deadline').fetchall()) == 0:
                print('Nothing to display!\n')
                continue
            for row in c.execute('SELECT * FROM todo ORDER BY deadline'):
                print(order, row)
                order+=1
        elif option == 2:
            task = input('Enter task: ')
            deadline = input('Enter deadline (YYYY-MM-DD): ')
            c.execute('INSERT INTO todo VALUES (?, ?, ?, ?)', [(num), (task), (deadline), ('Not started')])
            num+=1
            continue
        elif option == 3:
            if len(c.execute('SELECT * FROM todo ORDER BY deadline').fetchall()) == 0:
                print('Nothing to display!\n')
                continue
            for row in c.execute('SELECT * FROM todo ORDER BY deadline'):
                print(row)
            deleteTask()
        else:
            print('Exiting...')
            break
    conn.commit()

def deleteTask():
    delete = input('What task would you like to delete? ')
    c.execute(f'DELETE FROM todo WHERE number = {delete}')

if __name__ == "__main__":
    main()
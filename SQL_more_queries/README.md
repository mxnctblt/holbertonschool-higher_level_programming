# SQL - More queries

## Learning Objectives
```
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION
```

## Requirements
```
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc
```

## Tasks

**0. My privileges!** - Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

**1. Root user** - Write a script that creates the MySQL server user user_0d_1.

**2. Read user** - Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

**3. Always a name** - Write a script that creates the table force_name on your MySQL server.

**4. ID can't be null** - Write a script that creates the table id_not_null on your MySQL server.

**5. Unique ID** - Write a script that creates the table unique_id on your MySQL server.

**6. States table** - Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

**7. Cities table** - Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.

**8. Cities of California** - Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

**9. Cities by States** - Write a script that lists all cities contained in the database hbtn_0d_usa.

**10. Genre ID by show** - Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

**11. Genre ID for all shows** - Write a script that lists all shows contained in the database hbtn_0d_tvshows.

**12. No genre** - Write a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

**13. Number of shows by genre** - Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

**14. My genres** - Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

**15. Only Comedy** - Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.

**16. List shows and genres** - Write a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

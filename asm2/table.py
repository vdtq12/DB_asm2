import sqlite3

conn = sqlite3.connect('data.db', timeout=100)

c = conn.cursor()
conn.execute("PRAGMA foreign_keys = ON")

create_faculties_table = """
    create table if not exists faculties (
        f_name char(40) not null primary key,
        block_name char(40)
    );
"""

create_departments_table = """
    create table if not exists departments (
        d_name char(40) not null primary key,
        f_name char(40) not null,
        foreign key (f_name) references faculties (f_name) on delete cascade
    );
"""

create_lecturers_table = """
    create table if not exists lecturers (
        l_ID integer not null primary key,
        l_name char(40),
        l_phonenum char(40),
        diploma char(40),
        d_name char(40),
        foreign key (d_name) references departments (d_name) on delete cascade
    );
"""

create_students_table = """
    create table if not exists students (
        stu_ID integer not null primary key,
        stu_name char(40),
        stu_address char(200),
        d_name char(40),
        foreign key (d_name) references departments (d_name) on delete cascade
    );
"""

create_subjects_table = """
    create table if not exists subjects (
        s_ID char(40) not null primary key,
        no_credits integer,
        no_hours integer,
        f_name char(40),
        foreign key (f_name) references faculties (f_name) on delete cascade
    );
"""

create_classes_table = """
    create table if not exists classes (
        c_ID char(40) not null,
        semester integer not null,
        time char(40),
        room integer,
        weekday char(40),
        s_ID char(40) not null,
        l_ID integer not null,
        primary key (c_ID, semester)
        foreign key (s_ID) references subjects (s_ID) on delete cascade,
        foreign key (l_ID) references lecturers (l_ID) on delete cascade
    );
"""

create_libraries_table = """
    create table if not exists libraries (
        lib_ID integer not null primary key,
        block char(40),
        no_books integer
    );
"""

create_books_table = """
    create table if not exists books (
        book_ID integer not null primary key,
        book_name char(40),
        status char(40),
        lib_ID char(40),
        foreign key (lib_ID) references libraries (lib_ID) on delete cascade
    );
"""

create_projects_table = """
    create table if not exists projects (
        pro_ID integer not null primary key,
        supporting_cost integer,
        duration_time integer,
        s_ID integer not null,
        foreign key (s_ID) references subjects (s_ID) on delete cascade
    );
"""

create_enroll_in_table = """
    create table if not exists enroll_in (
        c_ID integer not null,
        semester char(40) not null,
        stu_ID integer not null,
        average_score integer,
        foreign key (c_ID, semester) references classes (c_ID, semester) on delete cascade
        foreign key (stu_ID) references students (stu_ID) on delete cascade
    );
"""

create_can_borrow_table = """
    create table if not exists can_borrow (
        book_ID integer not null,
        stu_ID integer not null,
        foreign key (book_ID) references books (book_ID) on delete cascade
        foreign key (stu_ID) references students (stu_ID) on delete cascade
    );
"""

create_participate_in_table = """
    create table if not exists participate_in (
        pro_ID integer not null,
        stu_ID integer not null,
        bonus_score integer,
        foreign key (pro_ID) references projects (pro_ID) on delete cascade
        foreign key (stu_ID) references students (stu_ID) on delete cascade
    );
"""

create_guide_table = """
    create table if not exists guide (
        pro_ID integer not null,
        l_ID integer not null,
        foreign key (l_ID) references lecturers (l_ID) on delete cascade
        foreign key (pro_ID) references projects (pro_ID) on delete cascade
    );
"""

insert_faculties_value = """
    insert into faculties 
    select 'CSandCE' as f_name, 'A3' as block_name
    union all select 'Industrial Management', 'B10'
    union all select 'Mechanical Engineering', 'A1'
    union all select 'Logistic and Supply Chain Management', 'B4'
    union all select 'Chemical Engineering', 'B6'
"""

insert_departments_value = """
    insert into departments 
    select 'Computer Science' as d_name, 'CSandCE' as f_name
    union all select 'Computer Engineering', 'CSandCE'
    union all select 'Marketing', 'Industrial Management'
    union all select 'Manufacturing', 'Industrial Management'
    union all select 'Organic Chemistry', 'Chemical Engineering'
    union all select 'Manufacturing Engineering', 'Mechanical Engineering'
"""

insert_lecturers_value = """
    insert into lecturers 
    select '0003518' as l_ID, 'Thinh Duc Bao' as l_name, '(206) 342-8631' as l_phonenum, 'Professor' as diploma, 'Computer Science' as d_name
    union all select '0003520', 'Vu Tung Linh', '(717) 550-1675', 'Professor', 'Marketing'
    union all select '0003522', 'Cao Vu Minh', '(248) 762-0356', 'Doctor', 'Manufacturing'
    union all select '0003524', 'Mai Duc Toan', '(253) 644-2182', 'Doctor', 'Computer Science'
    union all select '0003525', 'Chester Woods', '(212) 658-3916', 'Professor', 'Organic Chemistry'
    union all select '0003526', 'Alina Wilkerson', '(202) 918-2132', 'Doctor', 'Manufacturing Engineering'
"""

insert_students_value = """
    insert into students 
    select '2052233' as stu_ID, 'Vu Quyen' as stu_name, 'Hiep Binh Chanh, Thu Duc' as stu_address, 'Computer Science' as d_name
    union all select '2052235', 'Ha Tran', 'Nguyen Van Thuong, Binh Thanh', 'Marketing'
    union all select '2052237', 'Hoang Nhat', 'Nguyen Xi, Binh Thanh', 'Computer Engineering'
    union all select '1912239', 'Nhat Truong', 'Bac Hai, District 10', 'Marketing'
    union all select '1822241', 'Huynh Phat', 'To Hien Thanh, Phu Nhuan District', 'Manufacturing'
"""

insert_subjects_value = """
    insert into subjects 
    select 'CO3017' as s_ID, '4' as no_credits, '45' as no_hours, 'Industrial Management' as f_name
    union all select 'CO1003', '3', '55', 'CSandCE'
    union all select 'CO2015', '4', '50', 'CSandCE'
    union all select 'CO2017', '2', '55', 'Mechanical Engineering'
    union all select 'CO3002', '2', '40', 'Chemical Engineering'
"""

insert_classes_value = """
    insert into classes 
    select 'CO3017_1' as c_ID, '221' as semester, '7 a.m' as time, '306' as room, 'Mon' as weekday, 'CO3017' as s_ID, '0003522' as l_ID
    union all select 'CO3017_1', '211', '4 p.m', '512', 'Mon', 'CO3017', '0003520'
    union all select 'CO1003_3', '213', '1 p.m', '112', 'Tue', 'CO1003', '003518'
    union all select 'CO2015_7', '221', '1 p.m', '512', 'Fri', 'CO2015', '0003518'
    union all select 'CO2017_11', '223', '3 p.m', '207', 'Fri', 'CO2017', '0003526'
    union all select 'CO2015_12', '221', '8 a.m', '405', 'Sun', 'CO2015', '0003524'
"""

insert_librries_value = """
    insert into libraries 
    select '1' as lib_ID, 'A2' as block, '2' as no_books
    union all select '2', 'A4', '3'
    union all select '3', 'H6', '1'
"""

insert_books_value = """
    insert into books 
    select '111' as book_ID, 'Fundamental of Database System' as book_name, 'On loan' as status, '1' as lib_ID
    union all select '112', 'Fundamental of Software Architecture', 'On loan', '1'
    union all select '113', 'Clean Architecture', 'On loan', '2'
    union all select '114', 'Rescuing Human Rights', 'Available for loan', '2'
    union all select '115', 'The Science of Learning and Development in Education', 'On loan', '2'
    union all select '116', 'Earthopolis', 'On loan', '3'

"""

insert_projects_value = """
    insert into projects 
    select '1' as pro_ID, '5000000' as supporting_cost, '80' as duration_time, 'CO3017' as s_ID
    union all select '2', '7000000', '50', 'CO3017'
    union all select '3', '10000000', '60', 'CO1003'
    union all select '4', '5200000', '55', 'CO2017'
    union all select '5', '500000', '20', 'CO3002'
"""

insert_enroll_in_value = """
    insert into enroll_in 
    select 'CO3017_1' as c_ID, '221' as semester, '2052233' as stu_ID, '8' as ave_score
    union all select 'CO3017_1', '211', '2052235', '9'
    union all select 'CO1003_3', '213', '2052237', '7'
    union all select 'CO2015_7', '221', '1912239', '6'
    union all select 'CO2017_11', '223', '1822241', '7'
    union all select 'CO2015_12', '221', '2052233', '6'
"""

insert_can_borrow_value = """
    insert into can_borrow 
    select '111' as stu_ID, '2052235' as book_ID
    union all select '112', '1912239'
    union all select '113', '2052237'
    union all select '115', '1822241'
    union all select '116', '2052235'
"""

insert_participate_in_value = """
    insert into participate_in 
    select '1' as pro_ID, '2052233' as stu_ID, '1' as bonus_score
    union all select '2', '2052235', '1'
    union all select '3', '2052237', '2'
    union all select '2', '1912239', '2'
    union all select '4', '1912239', '3'
"""

insert_guide_value = """
    insert into guide 
    select '1' as pro_ID, '0003518' as l_ID
    union all select '2', '0003520'
    union all select '3', '0003520'
    union all select '3', '0003518'
    union all select '4', '0003524'
"""

query1 = """
    select block_name
    from faculties
    inner join departments on faculties.f_name = departments.f_name
    where d_name = 'Manufacturing'
"""

queryt2_1 = """
    create temporary table t1 as 
    select l_ID,count(pro_ID) 
    from guide
    group by l_ID
"""

query2_2 = """
    create temporary table t2 as
    select * from t1 
    where [count(pro_ID)] > 1
"""

query2_3 = """
    select l_name
    from t2
    natural join lecturers
"""

query3_1 = """create temporary table all_stu as
select distinct stu_ID from students;"""

query3_2 = """create temporary table stu_with_proj as
select distinct stu_ID from participate_in;"""

query3_3 = """create temporary table stu_without_proj as
select stu_ID from all_stu 
except select stu_ID from stu_with_proj;"""

query3_4 = """select stu_ID, stu_name from 
stu_without_proj natural join students;"""

update = """update participate_in
set stu_ID = '2052235'
where pro_ID = '1'"""

query4_1 = """create temporary table all_stu_adv as
select distinct stu_ID from students;"""

query4_2 = """create temporary table stu_with_proj_adv as
select distinct stu_ID from participate_in;"""

query4_3 = """create temporary table stu_without_proj_adv as
select stu_ID from all_stu_adv 
except select stu_ID from stu_with_proj_adv;"""

query4_4 = """select stu_ID, stu_name from 
stu_without_proj_adv natural join students;"""

delete = """delete from projects 
where s_ID = 'CO3017'"""

query_projects = """select *from projects"""
query_participate_in = """select *from participate_in"""
query_guide = """select *from guide"""
query_books = """select *from books"""
query_can_borrow = """select *from can_borrow"""
query_classes = """select *from classes"""

drop = """ drop table classes"""

create_trigger_on_books = """ 
create trigger validate_book_status_insert
	before insert on books
begin 
	select  
		case 
			when new.status not in('Available for loan','On loan') then 
				raise(abort, 'Status of book must be "Available for loan" or "On loan"')
		end;
end;"""

insert_book_invalid = """insert into books (book_ID, book_name, status, lib_ID)
values ('117', 'Nineteen Eighty-Four', 'is loaned', 3);""" 

 
insert_book_valid = """insert into books (book_ID, book_name, status, lib_ID)
values ('118', 'A Brief History of Time', 'Available for loan', 3);"""


create_trigger_on_can_borrow = """
create trigger limit_borrow_book_per_student
	before insert on can_borrow
begin
	select case 
		when (select count(*) from can_borrow where stu_ID = new.stu_ID) >= 3 then 
			raise(abort, 'Max number of books student can loan at a time is 3.')
	end;
end;"""

insert_borrow_valid = """insert into can_borrow (book_ID, stu_ID)
values ('114', '2052235');"""

insert_borrow_invalid = """insert into can_borrow (book_ID, stu_ID)
values ('118', '2052235'); """

create_triiger_on_classes = """create trigger assign_class_to_lecturer
	before insert on classes
begin
	select case 
		when (select distinct f_name from faculties 
				natural join subjects
				where s_ID = new.s_ID) != (select distinct f_name from faculties
												natural join departments
												natural join lecturers
												where l_ID = new.l_ID) then 
			raise(abort, 'Lecturer can only be assigned to the subject of the same faculties')
	end;
end;"""

insert_classes_invalid = """insert into classes(c_ID, semester, time, room, weekday, s_ID, l_ID)
values ('CO1003_5', '222', '7 a.m', '206', 'Sat', 'CO1003', '0003525');"""

insert_classes_valid = """insert into classes(c_ID, semester, time, room, weekday, s_ID, l_ID)
values ('CO3002_5', '222', '7 a.m', '206', 'Sat', 'CO3002', '0003525');"""

        #TASK 1,2: DESIGN AND IMPLEMENTING PHYSICAL DATABASE
c.execute(create_faculties_table)
conn.commit()
c.execute(create_departments_table)
conn.commit()
c.execute(create_lecturers_table)
conn.commit()
c.execute(create_students_table)
conn.commit()
c.execute(create_subjects_table)
conn.commit()
c.execute(create_classes_table)
conn.commit()
c.execute(create_libraries_table)
conn.commit()
c.execute(create_books_table)
conn.commit()
c.execute(create_projects_table)
conn.commit()
c.execute(create_enroll_in_table)
conn.commit()
c.execute(create_can_borrow_table)
conn.commit()
c.execute(create_participate_in_table)
conn.commit()
c.execute(create_guide_table)
conn.commit()

        #TASK 3: INSERT DATA FOR ALL TABLE
# c.execute(insert_faculties_value)
# conn.commit()
# c.execute(insert_departments_value)
# conn.commit()
# c.execute(insert_lecturers_value)
# conn.commit()
# c.execute(insert_students_value)
# conn.commit()
# c.execute(insert_subjects_value)
# conn.commit()
# c.execute(insert_classes_value)
# conn.commit()
# c.execute(insert_librries_value)
# conn.commit()
# c.execute(insert_books_value)
# conn.commit()
# c.execute(insert_projects_value)
# conn.commit()
# c.execute(insert_enroll_in_value)
# conn.commit()
# c.execute(insert_can_borrow_value)
# conn.commit()
# c.execute(insert_participate_in_value)
# conn.commit()
# c.execute(insert_guide_value)
# conn.commit()


        #TASK 4: OPERATION PERFORMING AS SELECT, UPDATE, DELETE AND SOME NESTED QUERIES
print("\nRetrieve the block name of department 'Manufaturing':")
# c.execute(query1)
# print(c.fetchall())
print("\nList the name of all lecturers who guide 2 or more projects:")
# c.execute(queryt2_1)
# conn.commit()
# c.execute(query2_2)
# conn.commit()
# c.execute(query2_3)
# print(c.fetchall())
print("\nRetrieve the names and IDs of the students with no bonus score => these student do not participate in any project:")
# c.execute(query3_1)
# conn.commit()
# c.execute(query3_2)
# conn.commit()
# c.execute(query3_3)
# conn.commit()
# c.execute(query3_4)
# print(c.fetchall())
print("\nChange participated student of project 1 to another student who already participated in other project and observe the change:")
# c.execute(update)
# conn.commit()
# print("Data was updated!")
print("\nRetrieve the names and IDs of the students with no bonus score => these student do not participate in any project:")
# c.execute(query4_1)
# conn.commit()
# c.execute(query4_2)
# conn.commit()
# c.execute(query4_3)
# conn.commit()
# c.execute(query4_4)
# print(c.fetchall())
print("\n Show delete on cascade: delete all projects of subjects CO3017, when any project is deleted, the coresponding data from other tables is also being deleted:")
# c.execute(delete)
# conn.commit()
# print("Data was delete!")
print("\nTable projects after deleted:")
# c.execute(query_projects)
# print(c.fetchall())
print("\nTable participate_in after deleted:")
# c.execute(query_participate_in)
# print(c.fetchall())
print("\nTable guide after deleted:")
# c.execute(query_guide)
# print(c.fetchall())

    #TASK5: Write TRIGGER, FUNCTION, STORE PROCEDURE for the queries and constraints
print("\nCreate trigger for: status of books can only be one of these fixed value ( available for loan, on loan)")
# c.execute(create_trigger_on_books)
# conn.commit()
# print("Trigger created!")
print("\nInvalid insert:")
# c.execute(insert_book_invalid)
# conn.commit()
# print(c.fetchall())
print("\nValid insert:")
# c.execute(insert_book_valid)
# conn.commit()
# c.execute(query_books)
# print(c.fetchall())
print("\nCreate trigger for: One student can borrow a limited quantity of books")
# c.execute(create_trigger_on_can_borrow)
# conn.commit()
# print("Trigger created!")
print("\nValid insert:")
# c.execute(insert_borrow_valid)
# conn.commit()
# c.execute(query_can_borrow)
# print(c.fetchall())
print("\nInvalid insert:")
# c.execute(insert_borrow_invalid)
# conn.commit()
print("\nCreate trigger for: Lecturers can only be assigned to a class of subject belonging to the faculty that they are in")
# c.execute(create_triiger_on_classes)
# conn.commit()
# print("Trigger created!")
print("\nInvalid insert:")
# c.execute(insert_classes_invalid)
# conn.commit()
print("\nValid insert:")
# c.execute(insert_classes_valid)
# conn.commit()
# c.execute(query_classes)
# print(c.fetchall())

    #Task6: Building a desktop, web, or mobile application to connect to the database
print("\nFor this task, we use Python, HTML and SQLAlchemy to perform an web aplication.\n Please check in the report or run web.py in the same folder!")

conn.close()
create table faculties (
            f_name char(40) not null primary key,
            block_name char(40)
        );
        create table departments (
            d_name char(40) not null primary key,
            f_name char(40) not null,
            foreign key (f_name) references faculties (f_name) on delete cascade
        );
create table lecturers (
            l_ID integer not null primary key,
            l_name char(40),
            l_phonenum char(40),
            diploma char(40),
            d_name char(40),
            foreign key (d_name) references departments (d_name) on delete cascade
        );

create table students (
            stu_ID integer not null primary key,
            stu_name char(40),
            stu_address char(200),
            d_name char(40),
            foreign key (d_name) references departments (d_name) on delete cascade
        );
        create table subjects (
            s_ID char(40) not null primary key,
            no_credits integer,
            no_hours integer,
            f_name char(40),
            foreign key (f_name) references faculties (f_name) on delete cascade
        );
        create table classes (
            c_ID char(40) not null,
            semester integer not null,
            time char(40),
            room integer,
            weekday char(40),
            s_ID char(40) not null,
            l_ID integer not null,
            primary key (c_ID, semester),
            foreign key (s_ID) references subjects (s_ID) on delete cascade,
            foreign key (l_ID) references lecturers (l_ID) on delete cascade
        );
        create table libraries (
            lib_ID integer not null primary key,
            block char(40),
            no_books integer
        );
        create table books (
            book_ID integer not null primary key,
            book_name char(100),
            status char(40),
            lib_ID integer,
            foreign key (lib_ID) references libraries (lib_ID) on delete cascade
        );
        create table do_projects (
            pro_ID integer not null primary key,
            supporting_cost integer,
            duration_time integer,
            s_ID char(40) not null,
            foreign key (s_ID) references subjects (s_ID) on delete cascade
        );
        create table enroll_in (
            c_ID char(40) not null,
            semester integer not null,
            stu_ID integer not null,
            average_score integer,
            foreign key (c_ID, semester) references classes (c_ID, semester) on delete cascade,
            foreign key (stu_ID) references students (stu_ID) on delete cascade
        );
        create table can_borrow (
            book_ID integer not null,
            stu_ID integer not null,
            foreign key (book_ID) references books (book_ID) on delete cascade,
            foreign key (stu_ID) references students (stu_ID) on delete cascade
        );
        create table participate_in (
            pro_ID integer not null,
            stu_ID integer not null,
            bonus_score integer,
            foreign key (pro_ID) references do_projects (pro_ID) on delete cascade,
            foreign key (stu_ID) references students (stu_ID) on delete cascade
        );
        create table guide (
            pro_ID integer not null,
            l_ID integer not null,
            foreign key (l_ID) references lecturers (l_ID) on delete cascade,
            foreign key (pro_ID) references do_projects (pro_ID) on delete cascade
        );

insert into faculties (f_name, block_name)
        select 'CSandCE', 'A3' from dual
        union all select 'Industrial Management', 'B10' from dual
        union all select 'Mechanical Engineering', 'A1' from dual
        union all select 'Logistic and Supply Chain Management', 'B4' from dual
        union all select 'Chemical Engineering', 'B6' from dual;
        
insert into departments (d_name, f_name)
        select 'Computer Science', 'CSandCE' from dual
        union all select 'Computer Engineering', 'CSandCE' from dual
        union all select 'Marketing', 'Industrial Management' from dual
        union all select 'Manufacturing', 'Industrial Management' from dual
        union all select 'Organic Chemistry', 'Chemical Engineering' from dual
        union all select 'Manufacturing Engineering', 'Mechanical Engineering' from dual;
    
insert into lecturers (l_ID, l_name, l_phonenum, diploma, d_name)
        select '0003518', 'Thinh Duc Bao', '(206) 342-8631', 'Professor', 'Computer Science' from dual
        union all select '0003520', 'Vu Tung Linh', '(717) 550-1675', 'Professor', 'Marketing' from dual
        union all select '0003522', 'Cao Vu Minh', '(248) 762-0356', 'Doctor', 'Manufacturing' from dual
        union all select '0003524', 'Mai Duc Toan', '(253) 644-2182', 'Doctor', 'Computer Science' from dual
        union all select '0003525', 'Chester Woods', '(212) 658-3916', 'Professor', 'Organic Chemistry' from dual
        union all select '0003526', 'Alina Wilkerson', '(202) 918-2132', 'Doctor', 'Manufacturing Engineering' from dual;

insert into students (stu_ID, stu_name, stu_address, d_name)
        select '2052233', 'Vu Quyen', 'Hiep Binh Chanh, Thu Duc', 'Computer Science' from dual
        union all select '2052235', 'Ha Tran', 'Nguyen Van Thuong, Binh Thanh', 'Marketing' from dual
        union all select '2052237', 'Hoang Nhat', 'Nguyen Xi, Binh Thanh', 'Computer Engineering' from dual
        union all select '1912239', 'Nhat Truong', 'Bac Hai, District 10', 'Marketing' from dual
        union all select '1822241', 'Huynh Phat', 'To Hien Thanh, Phu Nhuan District', 'Manufacturing' from dual;

insert into subjects (s_ID, no_credits, no_hours, f_name)
        select 'CO3017', '4', '45', 'Industrial Management' from dual
        union all select 'CO1003', '3', '55', 'CSandCE' from dual
        union all select 'CO2015', '4', '50', 'CSandCE' from dual
        union all select 'CO2017', '2', '55', 'Mechanical Engineering' from dual
        union all select 'CO3002', '2', '40', 'Chemical Engineering' from dual;

insert into classes (c_ID, semester, time, room, weekday, s_ID, l_ID)
        select 'CO3017_1', '221', '7 a.m', '306', 'Mon', 'CO3017', '0003522'  from dual
        union all select 'CO3017_1', '211', '4 p.m', '512', 'Mon', 'CO3017', '0003520' from dual
        union all select 'CO1003_3', '213', '1 p.m', '112', 'Tue', 'CO1003', '003518' from dual
        union all select 'CO2015_7', '221', '1 p.m', '512', 'Fri', 'CO2015', '0003518' from dual
        union all select 'CO2017_11', '223', '3 p.m', '207', 'Fri', 'CO2017', '0003526' from dual
        union all select 'CO2015_12', '221', '8 a.m', '405', 'Sun', 'CO2015', '0003524' from dual;
    
insert into libraries (lib_ID, block, no_books)
        select '1', 'A2', '2'  from dual
        union all select '2', 'A4', '3'  from dual
        union all select '3', 'H6', '1'  from dual;

insert into books (book_ID, book_name, status, lib_ID)
        select '111', 'Fundamental of Database System', 'On loan', '1'  from dual
        union all select '112', 'Fundamental of Software Architecture', 'On loan', '1'  from dual
        union all select '113', 'Clean Architecture', 'On loan', '2'  from dual
        union all select '114', 'Rescuing Human Rights', 'Available for loan', '2'  from dual
        union all select '115', 'The Science of Learning and Development in Education', 'On loan', '2'  from dual
        union all select '116', 'Earthopolis', 'On loan', '3'  from dual;

insert into do_projects (pro_ID, supporting_cost, duration_time, s_ID)
        select '1', '5000000', '80', 'CO3017'  from dual
        union all select '2', '7000000', '50', 'CO3017'  from dual
        union all select '3', '10000000', '60', 'CO1003'  from dual
        union all select '4', '5200000', '55', 'CO2017'  from dual
        union all select '5', '500000', '20', 'CO3002'  from dual;

insert into enroll_in (c_ID, semester, stu_ID, average_score)
        select 'CO3017_1', '221', '2052233', '8'  from dual
        union all select 'CO3017_1', '211', '2052235', '9'  from dual
        union all select 'CO1003_3', '213', '2052237', '7'  from dual
        union all select 'CO2015_7', '221', '1912239', '6'  from dual
        union all select 'CO2017_11', '223', '1822241', '7'  from dual
        union all select 'CO2015_12', '221', '2052233', '6'  from dual;

insert into can_borrow (book_ID, stu_ID)
        select '111', '2052235'  from dual
        union all select '112', '1912239'  from dual
        union all select '113', '2052237'  from dual
        union all select '115', '1822241'  from dual
        union all select '116', '2052235'  from dual;

insert into participate_in (pro_ID, stu_ID, bonus_score)
        select '1', '2052233', '1'  from dual
        union all select '2', '2052235', '1'  from dual
        union all select '3', '2052237', '2'  from dual
        union all select '2', '1912239', '2'  from dual
        union all select '4', '1912239', '3'  from dual;
        
insert into guide (pro_ID, l_ID)
        select '1', '0003518'  from dual
        union all select '2', '0003520'  from dual
        union all select '3', '0003520'  from dual
        union all select '3', '0003518'  from dual
        union all select '4', '0003524'  from dual;
    
select block_name
        from faculties
        inner join departments on faculties.f_name = departments.f_name
        where d_name = 'Manufacturing';
        
create global temporary table t1 
        on commit preserve rows
        as 
        select l_ID, count(pro_ID) as count_pro_ID
        from guide
        group by l_ID;
create global temporary table t2 
        on commit preserve rows
        as
        select * from t1 
        where count_pro_ID > 1;
select l_name
        from t2
        natural join lecturers;
        
create global temporary table all_stu 
    on commit preserve rows
    as
    select stu_ID from students;
create global temporary table stu_with_proj 
    on commit preserve rows
    as
    select distinct stu_ID from participate_in;
create global temporary table stu_without_proj 
    on commit preserve rows
    as
    select stu_ID from all_stu 
    except select stu_ID from stu_with_proj;
select stu_ID, stu_name from 
    stu_without_proj natural join students;


update participate_in
    set stu_ID = '2052235'
    where pro_ID = '1';
    
create global temporary table all_stu_adv
    on commit preserve rows
    as
    select stu_ID from students;
create global temporary table stu_with_proj_adv 
    on commit preserve rows
    as
    select distinct stu_ID from participate_in;
create global temporary table stu_without_proj_adv 
    on commit preserve rows
    as
    select stu_ID from all_stu_adv 
    except select stu_ID from stu_with_proj_adv;
select stu_ID, stu_name from 
    stu_without_proj_adv natural join students;
    
delete from do_projects 
    where s_ID = 'CO3017';
    
--create or replace trigger validate_book_status_insert
--        before insert or update
--        on books 
--        for each row
--    begin 
--        if :new.status not in ('Available for loan', 'On loan')
--        then
--            raise_application_error(-20000, 'Status of book must be "Available for loan" or "On loan"');
--        end if;
--    end;
    
insert into books (book_ID, book_name, status, lib_ID) 
    values ('117', 'Nineteen Eighty-Four', 'is loaned', 3);

delete from books where book_ID = '117';
    
insert into books (book_ID, book_name, status, lib_ID)
    values ('118', 'A Brief History of Time', 'Available for loan', 3);
    
--create or replace trigger limit_borrow_book_per_student
--	before insert on can_borrow for each row
--    declare max_num integer;
--begin
--    select count(*) into max_num from can_borrow where stu_ID = :new.stu_ID;
--    if max_num >= 3 then 
--        raise_application_error(-20101, 'Max number of books student can loan at a time is 3.');
--	end if;
--end;

insert into can_borrow (book_ID, stu_ID)
    values ('114', '2052235');

insert into can_borrow (book_ID, stu_ID)
    values ('118', '2052235'); 
    
--create or replace trigger assign_class_to_lecturer
--        before insert on classes for each row
--        declare 
--            fs_name char(40);
--            fd_name char(40);
--    begin
--        select distinct f_name into fs_name from faculties 
--                    natural join subjects
--                    where s_ID = :new.s_ID;
--        select distinct f_name into fd_name from faculties
--                    natural join departments
--                    natural join lecturers
--                    where l_ID = :new.l_ID;
--        if fs_name <> fd_name then
--                raise_application_error(-20102, 'Lecturer can only be assigned to the subject of the same faculties');
--        end if;
--    end;

insert into classes(c_ID, semester, time, room, weekday, s_ID, l_ID)
    values ('CO1003_5', '222', '7 a.m', '206', 'Sat', 'CO1003', '0003525');
    
insert into classes(c_ID, semester, time, room, weekday, s_ID, l_ID)
    values ('CO3002_5', '222', '7 a.m', '206', 'Sat', 'CO3002', '0003525');



select * from do_projects;
select * from books;
select * from students;
select * from can_borrow;
select * from guide;
select * from participate_in;
select * from t1;
select * from t2;

drop table all_stu_adv;
drop table stu_with_proj_adv;
drop table stu_without_proj_adv;
drop table t1;
drop table t2;
drop table all_stu;
drop table stu_with_proj;
drop table stu_without_proj;

drop trigger validate_book_status_insert;
drop trigger limit_borrow_book_per_student;

drop table enroll_in;
drop table can_borrow;
drop table participate_in;
drop table guide;
drop table do_projects;
drop table books;
drop table libraries;
drop table classes;
drop table subjects;
drop table students;
drop table lecturers;
drop table departments;
drop table faculties;



create role student;
grant select, insert, delete, update on participate_in to student;

create role faculty;
grant create session, create table, create view to faculty;

create user student_a identified by sa;

grant student to student_a;

create user faculty_a identified by fa;

grant faculty to faculty_a;

select * from faculties;
insert into faculties (f_name, block_name) 
    values ('abc', 'def');

-- system 
create role manager;
create role lecturer;
create role student;

grant all privileges to manager;
grant create session, create view to lecturer;
grant select on lecturers to lecturer;
grant select on classes to lecturer;
grant select on students to lecturer;
grant select, update, insert, delete on do_projects to lecturer;
grant select, update, insert, delete on participate_in to lecturer;

grant create session, create view to student;
grant select on participate_in to student;
grant select on enroll_in to student;
grant select on classes to student;
grant select on can_borrow to student;
grant select on books to student;

create user manager_x identified by man;
create user lecturer_x identified by lec;
create user student_x identified by stu;
create user outside_people identified by out;

grant manager to manager_x;
grant lecturer to lecturer_x;
grant student to student_x;


-- login as manager
select * from system.lecturers;

insert into system.lecturers (l_ID, l_name, l_phonenum, diploma, d_name)
    values (0003527, 'Nguyen A', '(123) 772-3453', 'Doctor', 'Computer Science');
    
create table system.new_table (
    a integer,
    b char(40)
);

insert into system.new_table (a, b) values (1, '1b');

select * from system.new_table;

drop table system.new_table;

-- login as lecturer
select * from system.faculties;
select * from system.classes;
select * from system.do_projects;
insert into system.do_projects (pro_ID, supporting_cost, duration_time, s_ID) 
    values (6, 100000, 30, 'CO3017');

create table system.new_table (
    a integer,
    b char(40)
);

-- login as student
select * from system.enroll_in;

insert into system.enroll_in (c_ID, semester, stu_ID, average_score)
    values ('CO2015_12', 221, 1912239, 10);

-- login as other people
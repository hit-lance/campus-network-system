create database cns_test;

use cns_test;

create table department(
    name CHAR(2) NOT NULL,
    building VARCHAR(20) NOT NULL,
    telephone CHAR(8) NOT NULL,
    PRIMARY KEY (name)
);

create table instructor(
    inst_id CHAR(6),
    name VARCHAR(20) NOT NULL,
    sex ENUM('M', 'F') NOT NULL CHECK (sex IN('M', 'F')),
    email VARCHAR(320) NOT NULL,
    title VARCHAR(20) NOT NULL,
    dept CHAR(2) NOT NULL,
    PRIMARY KEY (inst_id),
    FOREIGN KEY (dept) REFERENCES department(name)
);

create table student(
    stud_id CHAR(10),
    name VARCHAR(20) NOT NULL,
    sex ENUM('M', 'F') NOT NULL CHECK (sex IN('M', 'F')),
    email VARCHAR(320) NOT NULL,
    password VARCHAR(16) NOT NULL,
    grade VARCHAR(10) NOT NULL,
    dept CHAR(2) NOT NULL,
    PRIMARY KEY (stud_id),
    FOREIGN KEY (dept) REFERENCES department(name)
);

create table student_family(
    stud_id CHAR(10),
    father_name VARCHAR(20),
    father_job VARCHAR(20),
    mother_name VARCHAR(20),
    mother_job VARCHAR(20),
    PRIMARY KEY (stud_id),
    FOREIGN KEY (stud_id) REFERENCES student(stud_id)
);

create table classroom(
    room_number VARCHAR(4) NOT NULL,
    capacity SMALLINT NOT NULL CHECK(capacity>0),
    PRIMARY KEY (room_number)
);

create table course(
    cno CHAR(7),
    title VARCHAR(20),
    credit TINYINT NOT NULL CHECK(credit>0),
    dept CHAR(2) NOT NULL,
    room_number VARCHAR(4) NOT NULL,
    PRIMARY KEY (cno),
    FOREIGN KEY (dept) REFERENCES department(name),
    FOREIGN KEY (room_number) REFERENCES classroom(room_number)
);

create table instructor_arrangement(
    inst_id CHAR(6),
    cno CHAR(7),
    PRIMARY KEY (inst_id, cno),
    FOREIGN KEY (inst_id) REFERENCES instructor(inst_id),
    FOREIGN KEY (cno) REFERENCES course(cno)
);

create table student_grade(
    stud_id CHAR(10),
    cno CHAR(7),
    semester CHAR(5),
    grade TINYINT CHECK(grade=0 AND grade<=100),
    PRIMARY KEY (stud_id, cno, semester),
    FOREIGN KEY (stud_id) REFERENCES student(stud_id),
    FOREIGN KEY (cno, semester) REFERENCES course(cno, semester)
);

create table project (
    number CHAR(6),
    title VARCHAR(20) NOT NULL,
    start_time DATE NOT NULL,
    end_time DATE NOT NULL,
    PRIMARY KEY (number)
);

create table research (
    inst_id CHAR(6),
    proj_number CHAR(6),
    role VARCHAR(10) NOT NULL,
    PRIMARY KEY (inst_id, proj_number),
    FOREIGN KEY(inst_id) REFERENCES instructor(inst_id),
    FOREIGN KEY(proj_number) REFERENCES project(number)
);

create table friendship (
    user_id CHAR(10),
    friend_id CHAR(10),
    class VARCHAR(20) NOT NULL,
    PRIMARY KEY (user_id, friend_id),
    FOREIGN KEY (user_id) REFERENCES student(stud_id),
    FOREIGN KEY (friend_id) REFERENCES student(stud_id)    
);

create table log (
    log_id CHAR(10),
    author_id CHAR(10) NOT NULL,
    title VARCHAR(20) NOT NULL,
    text MEDIUMBLOB NOT NULL,
    post_time DATE NOT NULL,
    replyable TINYINT DEFAULT 1,
    PRIMARY KEY (log_id),
    FOREIGN KEY (author_id) REFERENCES student(stud_id)
);

create table reply (
    user_id CHAR(10),
    log_id CHAR(10),
    content TEXT NOT NULL,
    time DATE NOT NULL,
    PRIMARY KEY (user_id, log_id),
    FOREIGN KEY (user_id) REFERENCES student(stud_id),
    FOREIGN KEY (log_id) REFERENCES log(log_id)    
);

create view log_list as select author_id,title,post_time from log;
create view student_info as select stud_id,name,sex,email,dept from student;
create view enrollment as (select cno,count(cno) as enroll,capacity from student_grade natural join course natural join classroom group by cno);

select name from instructor_arrangement natural join instructor where cno='CS31001';
select cno, group_concat(name) as instructor,enroll,capacity from instructor_arrangement natural join instructor natural join enrollment group by cno;
insert into department (name,building,telephone) values ('AS','main building','86403166');
delete from department where name='AS';
select * from student_info;
select * from course where credit = (select max(credit) from course);
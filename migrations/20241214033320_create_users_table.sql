drop table if exists users;
create table users (
    id int AUTO_INCREMENT primary key,
    name varchar(255) not null,
    email varchar(255) not null,
    password varchar(255) not null,
    created_at timestamp not null default current_timestamp,
    is_login boolean not null default false
);

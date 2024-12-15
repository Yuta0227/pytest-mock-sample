alter table posts 
add column user_id int,
add constraint fk_user
foreign key (user_id) references users(id);

update posts set user_id = 1 where user_id is null;
update posts set user_id = 3 where id = 1;

alter table posts modify column user_id int not null;
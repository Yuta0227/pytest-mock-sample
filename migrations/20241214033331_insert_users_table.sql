insert into users 
(id, name,email,password,created_at,is_login) 
values 
(1,"user1","user1@test.com","password",CURRENT_TIMESTAMP,false),
(2,"user2","user2@test.com","password",CURRENT_TIMESTAMP,false),
(3,"user3","user3@test.com","password",CURRENT_TIMESTAMP,true);
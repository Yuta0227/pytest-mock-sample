alter table posts add column is_private boolean not null default false;
update posts set is_private = true where id = 2;
create table users (
    id integer primery key,
    username text not null,
    password text not null
);

insert into users (id, username, password) values (1, "willy", "willy");
insert into users (id, username, password) values (2, "kari", "kari");
insert into users (id, username, password) values (3, "agus", "agus");
insert into users (id, username, password) values (4, "joako", "joako");
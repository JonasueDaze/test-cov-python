-- migrate:up
create table people(
	id integer primary key generated always as identity,
	name varchar(255),
	age integer
);

-- migrate:down
drop table people;

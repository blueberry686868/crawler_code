create table history(
	ds datetime not null comment '日期',
	confirm int(11) default null comment '累计确诊',
	confirm_add int(11) default null comment '当日新增确诊',
	suspecct int(11) default null comment '剩余疑似',
	suspecct_add int(11) default null comment '当日新增疑似',
	heal int(11) default null comment '累计治愈',
	heal_add int(11) default null comment '当日新增治愈',
	dead int(11) default null comment '累计死亡',
	dead_add int(11) default null comment '当日新增死亡',
	primary key(ds) using btree
)engine=InnoDB default charset=utf8mb4;


create table details(
	id int(11) not null auto_increment,
	update_time datetime default null comment '数据最后更新时间',
	province varchar(20) default null comment '省',
	city varchar(20) default null comment '市',
	confirm int(11) default null comment '累计确诊',
	confirm_now int(11) default null comment '现有确诊',
	confirm_add int(11) default null comment '新增确诊',
	heal int(11) default null comment '累计治愈',
	dead int(11) default null comment '累计死亡',
	primary key(id)
)engine=InnoDB default charset=utf8mb4;



create table hotsearch(
	id int(11) not null auto_increment,
	dt datetime default null,
	content varchar(255) default null,
	primary key(id)
)engine=InnoDB default charset=utf8mb4;

CREATE TABLE tables_index (
    id                   serial primary key,
    table_name           varchar(50),
    csv_url              varchar(500),
    state                integer,
    columns              text,
    parse_attempts       integer default 0,
    inserted_at          timestamp,
    parsed_at            timestamp,
    succeeded_at         timestamp,
    failed_at            timestamp
);
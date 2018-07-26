CREATE TABLE STOCK (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    STOCK_CODE_NSE TEXT UNIQUE,
    STOCK_CODE_BSE TEXT UNIQUE
);

CREATE TABLE STOCK_DATA (
    STOCK_ID INTEGER NOT NULL,
    TRADE_DATE INTEGER NOT NULL,
    OPEN_PRICE REAL,
    CLOSE_PRICE REAL
);
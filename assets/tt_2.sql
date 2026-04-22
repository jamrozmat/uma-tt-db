
CREATE TABLE IF NOT EXISTS Rivals (
    Rival_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Rival_Nickname VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Classes (
    Class_ID INTEGER PRIMARY KEY,
    Class_Name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Trial_Difficulty (
    Difficulty_ID INTEGER PRIMARY KEY,
    Difficulty_Name TEXT NOT NULL
);

INSERT INTO Classes (Class_ID, Class_Name) VALUES (0, '1'), (1, '2'), (2, '3'), (3, '4'), (4, '5'), (5, '6');
INSERT INTO Trial_Difficulty (Difficulty_ID, Difficulty_Name) VALUES (0, 'easy'), (1, 'medium'), (2, 'hard');

CREATE TABLE IF NOT EXISTS Trials_new (
    Trial_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Trial_Date DATE,
    Trial_Time TIME,
    Points INTEGER,
    is_added SMALLINT DEFAULT 1,
    Rival_ID INTEGER,
    Class_ID INTEGER,
    Difficulty_ID INTEGER,
    FOREIGN KEY (Rival_ID) REFERENCES Rivals(Rival_ID),
    FOREIGN KEY (Class_ID) REFERENCES Classes(Class_ID),
    FOREIGN KEY (Difficulty_ID) REFERENCES Trial_Difficulty(Difficulty_ID)
);

INSERT INTO Trials_new (Trial_ID, Trial_Date, Trial_Time)
SELECT Trial_ID, Trial_Date, Trial_Time FROM Trials;

DROP TABLE Trials;

ALTER TABLE Trials_new RENAME TO Trials;
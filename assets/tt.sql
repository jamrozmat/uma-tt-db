
CREATE TABLE Distances (
    Distance_ID INTEGER PRIMARY KEY,
    Distance_Name VARCHAR(100) NOT NULL
);

CREATE TABLE Trials (
    Trial_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Trial_Date DATE,
    Trial_Time TIME
);

CREATE TABLE Uma (
    Uma_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Uma_Name VARCHAR(100) NOT NULL,
    Uma_Rank INTEGER NOT NULL,
    Distance_ID INTEGER,
    FOREIGN KEY (Distance_ID) REFERENCES Distances(Distance_ID)
);

CREATE TABLE Results (
    Result_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Trial_ID INTEGER,
    Uma_ID INTEGER,
    Position SMALLINT NOT NULL,
    Score INTEGER,
    Distance_ID INTEGER,
    FOREIGN KEY (Uma_ID) REFERENCES Uma(Uma_ID),
    FOREIGN KEY (Trial_ID) REFERENCES Trials(Trial_ID),
    FOREIGN KEY (Distance_ID) REFERENCES Distances(Distance_ID)
);

INSERT INTO Distances (Distance_ID, Distance_Name) VALUES (0, 'Sprint');
INSERT INTO Distances (Distance_ID, Distance_Name) VALUES (1, 'Mile');
INSERT INTO Distances (Distance_ID, Distance_Name) VALUES (2, 'Medium');
INSERT INTO Distances (Distance_ID, Distance_Name) VALUES (3, 'Long');
INSERT INTO Distances (Distance_ID, Distance_Name) VALUES (4, 'Dirt');
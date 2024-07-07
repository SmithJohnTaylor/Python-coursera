SELECT * FROM read_csv('flights.csv',
    header = true,
    columns = {
        'Pass Rider #': 'VARCHAR',
        'Name': 'VARCHAR',
        'Boarding Priority': 'VARCHAR',
        'Flight': 'VARCHAR',
        'Departure Date': 'DATE',
        'Origin/Destination': 'VARCHAR'
    });

CREATE TABLE flightinfo (
    PassRiderNum VARCHAR,
    RiderName VARCHAR,
    BoardingPriority VARCHAR,
    Flight VARCHAR,
    DepartureDate DATE,
    OriginDestination VARCHAR
);
COPY flightsinfo FROM 'flights.csv'
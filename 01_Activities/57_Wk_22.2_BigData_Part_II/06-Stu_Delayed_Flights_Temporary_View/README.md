# Delayed Flight Temporary Views

In this activity, you’ll import a delayed flight dataset, create a temporary table, and then use Spark SQL to run queries on the temporary table.

## Instructions

1. Start a Spark Session, and then import the [Delayed Flight dataset](https://2u-data-curriculum-team.s3.amazonaws.com/dataviz-classroom/v1.2/22-big-data/3/DelayedFlights.csv).

  * **Note:** This dataset may take about 5 minutes to load.

2. Use Spark SQL to answer the following questions:

    * Retrieve the first five airline carriers that arrive at George Bush Intercontinental Airport (IAH) in Houston and what airport the flight originates.

      * **Hint** Pass in the airport code as a string.

    * Get all the origin and destination of all the Southwest (WN) flights.

    * Get the airline carrier, the origin, the destination, and the elapsed time in descending order, and limit the results to 10.

    * Get the total number of diverted flights from each airline carrier, and group the results by airline carrier and order by the total number of diverted flights in descending order.

    * Get the average time for delayed departures and arrivals for each airline carrier, and group the results by the airline carrier.

---

© 2022 edX Boot Camps LLC. Confidential and Proprietary. All Rights Reserved.
